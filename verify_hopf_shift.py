"""Independent verification for the update-procedure stability census v2 (answer 39.75).

f(u,v) = 2 - (b+1)u + u^2 v,  g(u,v) = b u - u^2 v,  fixed point P = (2, b/2).
Procedures: A simultaneous explicit (h=0.34), B sequential explicit (h=0.34),
C strict alternation of A and B, D trapezoidal-averaged implicit (h=0.08).
Census grid: b in {3.0, 3.5, 4.0, 4.5, 4.75, 5.2, 5.5}; answer = sum of b over
all (procedure, b) pairs where P is locally asymptotically stable.
"""
import cmath
import itertools
import os

HA = 0.34
HD = 0.08
GRID = [3.0, 3.5, 4.0, 4.5, 4.75, 5.2, 5.5]


def jac(b):
    return (b - 1.0, 4.0, -b, -4.0)  # f_u, f_v, g_u, g_v at P


def mat_A(b, h=HA):
    fu, fv, gu, gv = jac(b)
    return (1 + h * fu, h * fv, h * gu, 1 + h * gv)


def mat_B(b, h=HA):
    fu, fv, gu, gv = jac(b)
    return (1 + h * fu, h * fv,
            h * gu * (1 + h * fu), 1 + h * gv + h * h * gu * fv)


def inv2(m):
    a, bb, c, d = m
    det = a * d - bb * c
    return (d / det, -bb / det, -c / det, a / det)


def mul2(m, n):
    a, bb, c, d = m
    e, f, g, hh = n
    return (a * e + bb * g, a * f + bb * hh, c * e + d * g, c * f + d * hh)


def mat_C(b):
    return mul2(mat_B(b), mat_A(b))  # two-step composite of the alternation


def mat_D(b):
    fu, fv, gu, gv = jac(b)
    h2 = HD / 2.0
    fwd = (1 + h2 * fu, h2 * fv, h2 * gu, 1 + h2 * gv)
    bwd = inv2((1 - h2 * fu, -h2 * fv, -h2 * gu, 1 - h2 * gv))
    return mul2(bwd, fwd)


MATS = {"A": mat_A, "B": mat_B, "C": mat_C, "D": mat_D}


def eigs(m):
    a, bb, c, d = m
    tr, det = a + d, a * d - bb * c
    s = cmath.sqrt(tr * tr - 4 * det)
    return ((tr + s) / 2, (tr - s) / 2)


def rho(m):
    return max(abs(e) for e in eigs(m))


# ---- 1: single stability boundary per procedure + exit mechanism
print("== per-procedure thresholds (scan b in (0,20], step 5e-4; bisection) ==")
THRESH = {}
for name, mat in MATS.items():
    crossings = []
    prev = None
    for i in range(1, 40001):
        b = 20.0 * i / 40000
        s = rho(mat(b)) - 1.0
        if prev is not None and (prev < 0) != (s < 0):
            crossings.append(b)
        prev = s
    assert len(crossings) == 1, (name, crossings)
    lo, hi = crossings[0] - 5e-4, crossings[0]
    for _ in range(80):
        mid = (lo + hi) / 2
        if rho(mat(mid)) - 1.0 < 0:
            lo = mid
        else:
            hi = mid
    t = (lo + hi) / 2
    THRESH[name] = t
    e1, e2 = eigs(mat(t))
    mech = "complex |mu|=1" if abs(e1.imag) > 1e-7 else "real mu=%+.5f" % max((e1, e2), key=abs).real
    print("  %s: threshold b = %.7f  (exit: %s)" % (name, t, mech))
assert abs(THRESH["A"] - 3.64) < 1e-8
assert abs(THRESH["B"] - 1.0624 / 0.2448) < 1e-7      # flip exit: 1+tr+det = 0
assert abs(THRESH["D"] - 5.0) < 1e-8
assert 3.35 < THRESH["C"] < 3.36

# ---- 2: paradox certificate — both factors solidly stable, composite unstable
print("== composition-paradox certificate ==")
ok = False
for bi in range(3400, 3641):
    b = bi / 1000.0
    ra, rb, rc = rho(mat_A(b)), rho(mat_B(b)), rho(mat_C(b))
    if ra <= 0.99 and rb <= 0.99 and rc > 1.0:
        print("  b = %.3f: rho(A) = %.4f, rho(B) = %.4f, rho(B@A) = %.4f  -> paradox"
              % (b, ra, rb, rc))
        ok = True
        break
assert ok, "no paradox window with factor radii <= 0.99"

# ---- 3: census cells — eigenvalue verdicts, margins, and nonlinear simulation
def f(u, v, b):
    return 2.0 - (b + 1) * u + u * u * v


def g(u, v, b):
    return b * u - u * u * v


def step_A(u, v, b):
    return u + HA * f(u, v, b), v + HA * g(u, v, b)


def step_B(u, v, b):
    un = u + HA * f(u, v, b)
    return un, v + HA * g(un, v, b)


def step_D(u, v, b):
    h2 = HD / 2.0
    cu, cv = u + h2 * f(u, v, b), v + h2 * g(u, v, b)
    X, Y = u, v
    for _ in range(60):
        Fx = X - cu - h2 * f(X, Y, b)
        Fy = Y - cv - h2 * g(X, Y, b)
        fu = -(b + 1) + 2 * X * Y
        j = inv2((1 - h2 * fu, -h2 * X * X, -h2 * (b - 2 * X * Y), 1 + h2 * X * X))
        dX, dY = j[0] * Fx + j[1] * Fy, j[2] * Fx + j[3] * Fy
        X, Y = X - dX, Y - dY
        if abs(dX) + abs(dY) < 1e-14:
            break
    return X, Y


def simulate(name, b, n=60000, d0=1e-4):
    u, v = 2.0 + d0, b / 2.0
    d = d0
    for k in range(n):
        if name == "A":
            u, v = step_A(u, v, b)
        elif name == "B":
            u, v = step_B(u, v, b)
        elif name == "C":
            u, v = (step_A if k % 2 == 0 else step_B)(u, v, b)
        else:
            u, v = step_D(u, v, b)
        d = ((u - 2.0) ** 2 + (v - b / 2.0) ** 2) ** 0.5
        if d > 100 * d0 or d < 1e-3 * d0:
            break
    return d / d0


print("== census cells (eigenvalues + nonlinear simulation) ==")
stable_cells = {}
min_margin = 99.0
for name in "ABCD":
    for b in GRID:
        stable = rho(MATS[name](b)) < 1.0
        stable_cells[(name, b)] = stable
        margin = abs(b - THRESH[name])
        min_margin = min(min_margin, margin)
        ratio = simulate(name, b)
        if stable:
            assert ratio < 0.5, (name, b, ratio)
        else:
            assert ratio > 10, (name, b, ratio)
        print("  %s b=%-4s  rho=%.4f  %-8s  sim |x-P|/d0 = %-8.1e  margin to threshold %.3f"
              % (name, b, rho(MATS[name](b)), "STABLE" if stable else "unstable", ratio, margin))
assert min_margin >= 0.14 - 1e-9, min_margin

# report C-column eigenvalues for the golden response
print("== C-column eigenvalues (for the golden) ==")
for b in GRID:
    e1, e2 = eigs(mat_C(b))
    print("  b=%-4s  mu = %.4f%+.4fi, %.4f%+.4fi   rho = %.4f"
          % (b, e1.real, e1.imag, e2.real, e2.imag, rho(mat_C(b))))

# ---- 4: golden total
golden = sum(b for (nm, b), s in stable_cells.items() if s)
expected = {("A", 3.0), ("A", 3.5), ("B", 3.0), ("B", 3.5), ("B", 4.0),
            ("C", 3.0), ("D", 3.0), ("D", 3.5), ("D", 4.0), ("D", 4.5), ("D", 4.75)}
assert {k for k, s in stable_cells.items() if s} == expected
assert abs(golden - 39.75) < 1e-12
print("== golden total = %.2f ==" % golden)

# ---- 5: route cross-product, collision-free
def col_total(name, thr):
    return sum(b for b in GRID if b < thr)


ROUTES = {
    "A": {"correct": THRESH["A"], "flow": 5.0},
    "B": {"correct": THRESH["B"], "as_A": 3.64, "flow": 5.0, "det_slip": 6.229},
    "C": {"correct": THRESH["C"], "fallacy_minAB": 3.64, "as_A": 3.64,
          "average": (3.64 + THRESH["B"]) / 2, "flow": 5.0},
    "D": {"correct": 5.0, "down": 4.68, "up": 5.32},
}
collisions = []
totals = set()
for combo in itertools.product(*(ROUTES[k].items() for k in "ABCD")):
    labels = tuple(lab for lab, _ in combo)
    tot = sum(col_total(nm, thr) for nm, (lab, thr) in zip("ABCD", combo))
    totals.add(round(tot, 2))
    if abs(tot - golden) < 5e-3 and labels != ("correct",) * 4:
        collisions.append((labels, tot))
assert not collisions, collisions
print("== wrong-branch enumeration: %d combinations, %d distinct totals, zero collisions with %.2f =="
      % (2 * 4 * 5 * 3, len(totals), golden))
for lab in ["fallacy only", "flow everywhere", "B as A", "D down", "D up", "B det slip"]:
    pass
print("  fallacy-C only      -> %.2f" % (golden - col_total("C", THRESH["C"]) + col_total("C", 3.64) - 0))
print("  flow everywhere     -> %.2f" % sum(col_total(nm, 5.0) for nm in "ABCD"))
print("  B-as-A only         -> %.2f" % (golden - col_total("B", THRESH["B"]) + col_total("B", 3.64)))
print("  D-down only         -> %.2f" % (golden - col_total("D", 5.0) + col_total("D", 4.68)))
print("  D-up only           -> %.2f" % (golden - col_total("D", 5.0) + col_total("D", 5.32)))
print("  B-det-slip only     -> %.2f" % (golden - col_total("B", THRESH["B"]) + col_total("B", 6.229)))

# ---- 6: prompt length
text = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "planck_task_hopf_shift_census.md")).read()
prompt = text.split("## PROMPT (SUBMIT THIS)")[1].split("## GOLDEN RESPONSE")[0].strip()
print("== prompt length: %d chars (< 2000 required) ==" % len(prompt))
assert len(prompt) < 2000

print("\nALL CHECKS PASSED — FINAL ANSWER 39.75")
