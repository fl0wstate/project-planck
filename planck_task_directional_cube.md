# Planck task - directional mixed-valence cube

**FINAL ANSWER: 12**

**Subdomain:** Chemistry - Inorganic / coordination chemistry

**Source:** none. The cage, linker, valence rule, and connectivity condition are original idealized constructions. The underlying donor-charge bookkeeping and proper-rotation equivalence are standard coordination chemistry and molecular symmetry.

---

## Prompt

```text
An ideal cubic $M_8L_{12}$ coordination cage has one metal at each cube vertex and one rigid linker on every edge. Each linker is constitutionally directional: one end binds through a neutral pyridyl-N donor and the other through a monoanionic carboxylate-O donor; it has no other orientational state.

Each metal also carries the same neutral facial tridentate cap, leaving three equivalent cis sites for its incident edge linkers. An allowed capped node is either $M^{II}$ with one O and two N edge donors or $M^{III}$ with two O and one N; nodes with zero or three O donors are excluded. Donor orientations and formal valences are frozen, and no linker dissociates.

Retain only cages in which the $M^{III}$ vertices form one edge-connected domain. Count valence-linkage topologies, not conformers. Two topologies are identical exactly when a rigid rotation of the complete cube maps all N/O ends and metal valences; reflection alone is not an equivalence.

How many retained topologies exist? Report one exact integer.
```

---

## Why This Candidate

The earlier cubic $A_2B_2$ bridge-matching prompt collapses immediately into straight and bent perfect matchings. This successor has no equivalent two-class shortcut. It combines four reasoning layers:

1. Orient every linker toward its O donor and infer metal valence from vertex indegree.
2. Apply the global conservation of the twelve O ends.
3. Enforce connectivity of the complete high-valent domain rather than checking vertices independently.
4. Quotient directional cages by the full proper cube-rotation group, including rotations through undecorated face centers.

The last layer targets the observed porphyrin failure: solvers constructed operations around decorated sites and omitted axes through undecorated framework elements. Here all nonidentity fixed-state contributions come from face-centered axes; vertex- and edge-centered rotations contribute zero.

---

## Golden

Direct every edge toward its carboxylate-O end. Its endpoint indegree is then the number of incident O donors. An $M^{II}$ vertex has indegree 1 and an $M^{III}$ vertex has indegree 2.

If $h$ vertices are $M^{III}$, summing indegrees over the twelve directed edges gives

$$
2h+(8-h)=12,
$$

so $h=4$.

The connected four-vertex subsets of a cube and their compatible edge orientations are:

| induced $M^{III}$ domain | embedded subsets | orientations per subset | labeled states |
|---|---:|---:|---:|
| square face $C_4$ | 6 | 4 | 24 |
| corner star $K_{1,3}$ | 8 | 6 | 48 |
| skew path $P_4$ | 24 | 6 | 144 |

Thus the identity fixes $24+48+144=216$ states.

For the 24 proper rotations of the cube, the fixed-state counts are:

| rotation class | operations | fixed states per operation |
|---|---:|---:|
| identity | 1 | 216 |
| $C_4^{\pm1}$ through face centers | 6 | 8 |
| $C_2$ through face centers | 3 | 8 |
| $C_3^{\pm1}$ through opposite vertices | 8 | 0 |
| $C_2$ through opposite edge midpoints | 6 | 0 |

For a face-centered $C_4$, the two opposite face cycles may each circulate in either direction, and all four connecting edges have either common direction: $2\cdot2\cdot2=8$. For a face-centered $C_2$, connectivity again forces the four connecting edges to have one common direction, while each face has two compatible half-turn-invariant orientations, also giving 8.

A vertex-centered $C_3$ forces all three edges at each axial vertex inward or outward, producing forbidden indegree 3 or 0. An edge-centered $C_2$ exchanges the endpoints of an edge on its axis and therefore cannot preserve that linker's N/O direction.

Burnside's lemma gives

$$
\frac{216+6(8)+3(8)}{24}=\boxed{12}.
$$

The twelve proper-rotation orbits independently split into eight of size 24 and four of size 6, accounting for all 216 labeled states.

---

## Wrong Branches

| answer | reasoning error |
|---:|---|
| 4 | Count only the four proper-rotation classes of connected $M^{III}$ vertex domains and ignore N/O linkage orientations. |
| 6 | Include reflections, merging mirror-related directional cages. |
| 9 | Divide $216$ by 24 and assume every topology has a trivial stabilizer. |
| 14 | Omit connectivity and include reflections. |
| 24 | Apply the local valence rule but omit connectivity of the $M^{III}$ domain. |
| 38 | Count labeled connected four-vertex domains but ignore linkage orientations and rotational equivalence. |
| 216 | Enumerate all retained labeled states but never quotient by rotations. |
| 450 | Enforce only local valence and perform no connectivity or symmetry reduction. |

None collides with 12.

---

## Verification

`verify_directional_cube.py` independently:

1. Generates all $2^{12}=4096$ N/O edge orientations.
2. Retains 450 with every vertex indegree in $\{1,2\}$.
3. Retains 216 whose four indegree-2 vertices are connected.
4. Generates the 24 determinant-$+1$ signed coordinate permutations.
5. Obtains eight size-24 orbits and four size-6 orbits.
6. Finds one identity operation fixing 216 states, nine operations fixing 8 states, and fourteen fixing none.
7. Repeats with all 48 spatial operations and obtains 6 orbits.
8. Removes connectivity and obtains 24 proper-rotation orbits or 14 full-spatial orbits.

Actual output ends with `VERIFIED 12`.

---

## Compliance

- One question and one exact integer answer.
- Prompt is comfortably below 2,000 characters.
- Self-contained idealized structure, donor rules, kinetic assumptions, connectivity condition, equivalence relation, and output format.
- At least eight plausible distinct outcomes.
- No external data, post-cutoff fact, named mechanism, or obscure empirical constant is load-bearing.
- Difficulty is the composition of standard coordination, graph, conservation, connectivity, and molecular-symmetry reasoning.

## Probe Status

Three independent no-tool cold solvers all returned 12 by constructing the complete cube rotation group. None described a named "trap." Under the campaign evidence, this makes the candidate valid but lower priority; correct proxy solves do not predict platform success, whereas explicitly naming the hidden mechanism would retire it. Treat this as a secondary platform experiment, not a guaranteed stump.
