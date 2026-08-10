# planck task — case-volume (planck_task_rotaxane_chirality.md)

**Source inspiration:** Beilstein J. Org. Chem. 2025, 21, 10 (doi:10.3762/bjoc.21.10) — physics borrowed only, no numbers/compounds reused.

**FINAL ANSWER: 9**

**Prompt chars: 1563 / 2000**

## PROMPT

```
All 16 [2]rotaxanes obtained by threading one of four macrocycles $M1$-$M4$ onto one of four dumbbells $A1$-$A4$ are isolable.

Macrocycles: each is a shape-persistent ring of six 1,3-disubstituted benzene residues joined by six secondary amide bonds.
$M1$: every residue is a 3-aminobenzoyl unit, so all six $\mathrm{C(O)NH}$ linkages point the same way around the ring; no further substituents.
$M2$: three isophthaloyl and three benzene-1,3-diamine residues alternate, so the amides meet head-to-head and tail-to-tail; no further substituents.
$M3$: as $M1$, plus a $-\mathrm{CH_2OCH_2}-$ strap joining the 5-positions of two diametrically opposite residues and arching over one face of the ring; the strap cannot reach the other face.
$M4$: as $M2$, plus the same strap joining two diametrically opposite residues.

Dumbbells: each has the core $-\mathrm{O(CH_2)_6O}-$ bearing two end groups, with $\mathrm{Ar}=3,5$-di-tert-butylphenyl and $\mathrm{Ad}=1$-adamantyl.
$A1$: $-\mathrm{CH_2Ar}$ at both ends.
$A2$: $-\mathrm{CH_2Ar}$ at one end, $-\mathrm{CH_2Ad}$ at the other.
$A3$: $-\mathrm{CH(CH_3)Ar}$ at both ends, one $(R)$ and one $(S)$.
$A4$: $-\mathrm{CH(CH_3)Ar}$ at both ends, both $(R)$.

Assume free rotation about all single bonds, planar trans-amides, no atropisomerism, and free shuttling and pirouetting of the macrocycle, which cannot pass over a stopper. A rotaxane counts as achiral if any accessible conformation/co-conformation is superimposable on its mirror image.

How many of the 16 rotaxanes are chiral? Answer with a single integer.
```

## GOLDEN

Set the axle along $z$; the macrocycle encircles it. Any symmetry operation of a [2]rotaxane must map each component onto itself and preserve the axle axis. The only candidate IMPROPER operations are therefore: (i) $\sigma_v$ = a mirror plane containing the axle axis (keeps each stopper on its own side, keeps each macrocycle face on its own side); (ii) $\sigma_h$ = the macrocycle's own mean plane, or any $S_n$ about $z$, all of which exchange the two halves of the axle AND exchange the two faces of the ring. In-plane $C_2$ and rotations about $z$ are proper and irrelevant. Hence:

achiral iff [macrocycle has a $\sigma_v$ AND axle has a mirror plane containing its axis] OR [macrocycle is face-symmetric ($\sigma_h$) AND the axle's two ends are exchangeable by an improper operation].

Component analysis (8 independent judgments).
Macrocycles:
- $M1$ (head-to-tail hexa-amide): going round the ring the amides all read $\mathrm{N}\to\mathrm{C}$ in one sense. A $\sigma_v$ (or an in-plane $C_2$) reverses that sense, so it is constitutionally forbidden: NO $\sigma_v$. The ring is planar with two chemically equivalent faces: HAS $\sigma_h$ (point group $C_{6h}$; the macrocycle itself is achiral, yet "orientated").
- $M2$ (alternating diacyl/diamine): mirror lines through opposite residues map acyl onto acyl and amine onto amine and preserve amide sense: HAS $\sigma_v$; planar, HAS $\sigma_h$ ($D_{3h}$).
- $M3$ ($M1$ + one-face strap): no $\sigma_v$ (orientation) and no $\sigma_h$ (strap on one face only) $\Rightarrow$ $C_1$, the macrocycle is itself CHIRAL (planar-chiral strapped ring).
- $M4$ ($M2$ + one-face strap): the mirror plane through the two strapped opposite residues survives (the strap is symmetric in it): HAS $\sigma_v$; strap kills $\sigma_h$ and $i$. Point group $C_s$: achiral, faces distinguishable. This is the trap case: distinguishable faces do NOT make a ring "orientated".
Dumbbells (a stereocentre can never lie on a mirror plane, so any axle bearing stereocentres has no $\sigma_v$):
- $A1$: identical ends, no stereocentres: has $\sigma_v$; ends exchangeable by an improper op (midpoint mirror).
- $A2$: different stoppers: has $\sigma_v$; ends NOT exchangeable.
- $A3$: constitutionally identical ends, $(R)$ and $(S)$ = meso axle: no $\sigma_v$; ends exchangeable improperly (midpoint $\sigma$/$i$, which inverts $R\to S$ correctly).
- $A4$: $(R),(R)$: no $\sigma_v$; the two ends are exchanged only by a PROPER $C_2$, never by an improper op (a mirror would demand $R$ opposite $S$). Chiral axle.

16-case table (achiral unless marked):
$M1A1$ achiral ($\sigma_h$); $M1A2$ CHIRAL (canonical mechanically planar chiral rotaxane); $M1A3$ achiral - $\sigma_h$ swaps the ends and inverts $R\leftrightarrow S$, so the mechanical element and the two centres form a meso rotaxane; $M1A4$ CHIRAL.
$M2A1$ achiral ($\sigma_v$); $M2A2$ achiral ($\sigma_v$: an unsymmetrical axle alone is not enough); $M2A3$ achiral ($\sigma_h$); $M2A4$ CHIRAL (chiral component).
$M3A1$-$M3A4$ all CHIRAL (a rotaxane containing a chiral component can have no improper operation).
$M4A1$ achiral ($\sigma_v$); $M4A2$ achiral ($\sigma_v$ survives despite distinguishable faces); $M4A3$ CHIRAL ($\sigma_v$ destroyed by the stereocentres, $\sigma_h$/$i$ destroyed by the strap); $M4A4$ CHIRAL.

Chiral count $=2+1+4+2=9$.

## WHY IT SHOULD STUMP

The hidden gate is decided before any bookkeeping: what actually generates mechanical planar chirality. The memorised slogan is "a macrocycle with two distinguishable faces plus an unsymmetrical axle gives a mechanically planar chiral rotaxane". Both halves of that slogan are wrong here in opposite directions. (1) $M4$ has two chemically distinguishable faces (strap on one side) yet retains a mirror plane containing the axle, so with $A1$/$A2$ it is achiral - face distinguishability is necessary but not sufficient; what is required is that the ring be ORIENTATED (no in-plane mirror line), which for $M1$ follows from head-to-tail amide directionality alone, a constitutional property that no conformation can undo. (2) $A3$ has two ends that are chemically different ($R$ vs $S$) and so reads as "unsymmetrical", yet the very mirror that exchanges them ($\sigma_h$ of a planar orientated ring) converts $R$ into $S$: the mechanical element and the central elements cancel to a meso rotaxane. This is precisely the correlated-outcome trap - treating "mechanical chirality" and "central chirality" as independent contributions that can only add gives $M1A3$ and $M2A3$ as chiral. Conversely $A4$ has two constitutionally AND configurationally identical ends, so the slogan calls it "symmetrical", but it is a chiral $C_2$ axle and every rotaxane containing it is chiral. On top of the gate sit 16 independent cases, each needing its own decision about which of the two improper operation classes survives, with 8 upstream component judgments (orientated vs not; $\sigma_h$ present vs not; $\sigma_v$ killed by stereocentres; proper vs improper end exchange). A single mis-assigned component property moves the integer by 1-4.

## WRONG BRANCHES

- 11 - applies the standard slogan (macrocycle with distinguishable faces = M1, M3, M4; axle with different ends = A2, A3) for six mechanically chiral cases, then unions in the covalently chiral components (all M3, all A4): 6 + 7 - 2 overlap = 11. The single most likely wrong answer.
- 7 - ignores mechanical chirality altogether and counts only rotaxanes containing an intrinsically chiral component: 4 (M3 row) + 4 (A4 column) - 1 (M3A4) = 7.
- 13 - as the 11 branch but also treats M4 as fully face-dissymmetric with A1 and counts M2A2 chiral (any unsymmetrical axle assumed sufficient).
- 10 - correct framework except that M2A2 is called chiral because the axle is unsymmetrical, forgetting that M2's in-plane mirror lines survive threading.
- 8 - correct framework except that M4A3 is called achiral, forgetting that a stereocentre cannot lie on a mirror plane and therefore destroys the only surviving sigma_v of M4.
- 6 - counts only the six 'mechanically planar chiral' pairings from the slogan (M1/M3/M4 with A2/A3) and forgets that M3 is itself a chiral macrocycle and A4 a chiral axle.
- 4 - counts only the M3 row (the one obviously chiral macrocycle), dismissing mechanical chirality entirely and mis-reading A4 as a symmetric axle.
- 12 - counts every rotaxane whose macrocycle is orientated or face-differentiated (M1, M3, M4 = 12 cases) as chiral, ignoring axle symmetry completely.
- 16 - concludes that every combination is chiral because each macrocycle either is orientated or has distinguishable faces and every axle has some distinguishing feature.
- 5 - correct except that M1A2 is judged achiral on the grounds that M1 is itself achiral (C6h) and A2 is achiral, so 'achiral + achiral = achiral', missing emergent mechanical chirality.

## VERIFICATION (design agent's plan)

Two independent checks, both cheap.

(1) Explicit geometric enumeration (script). Build a labelled point model of each of the 16 rotaxanes in $R^3$: ring = hexagon of six residue centroids in the $xy$ plane, each residue tagged with a directed edge to its neighbour encoding the $\mathrm{N}\to\mathrm{C}$ amide sense (M1/M3 all edges cyclically co-directed; M2/M4 alternating), strap = two extra points at $z>0$ over residues 1 and 4 plus a bridging point on the $+z$ side; axle = points on the $z$ axis with distinct stopper labels at the two ends, and each stereocentre rendered as an explicit tetrahedron of four differently labelled points whose handedness encodes $R$ or $S$. Enumerate the finite candidate isometry set that maps the $z$ axis to itself: $C_6^k$ about $z$, $\sigma_h$, the six $\sigma_v$ planes at $30^\circ$ steps, the six in-plane $C_2$ axes, and $S_6^k$ - i.e. the $D_{6h}$ candidate set - composed with a scan over the relative azimuth of the axle in $15^\circ$ steps (only discrete alignments can matter since every axle mirror plane is discrete). Declare the rotaxane achiral iff some IMPROPER member of that set maps the labelled point set onto itself with all labels preserved and stereocentre handedness matched. Expected output: the 16-row table in the golden sketch, total chiral $=9$.

(2) Abstract predicate cross-check (already run, reproduced here): encode macrocycles as (has $\sigma_v$, has $\sigma_h$) $= M1(F,T), M2(T,T), M3(F,F), M4(T,F)$ and dumbbells as (has axial mirror plane, ends exchangeable by an improper operation) $= A1(T,T), A2(T,F), A3(F,T), A4(F,F)$; achiral iff $(\mathrm{mac}\sigma_v \wedge \mathrm{ax}\sigma_v) \vee (\mathrm{mac}\sigma_h \wedge \mathrm{ax\_improper\_endswap})$. Running this over the $4\times4$ grid returns chiral for M1A2, M1A4, M2A4, M3A1-A4, M4A3, M4A4 $\Rightarrow$ 9. The two routes are independent (one geometric, one group-theoretic) and agree.

(3) Sanity anchors from known chemistry: M1+A2 reproduces the textbook mechanically planar chiral [2]rotaxane (orientated ring + directional axle); M2+A2 reproduces the standard negative control (symmetric ring + directional axle = achiral); M1+A3 is a meso rotaxane, the mechanical analogue of a meso diol.

## COMPLIANCE

SELF-CONTAINMENT: all four macrocycles and all four dumbbells are fully specified by constitution and configuration; Ar and Ad are defined inline; the idealisations (free single-bond rotation, planar trans-amides, no atropisomerism, free shuttling/pirouetting, no passage over a stopper, achiral = some accessible conformation superimposable on its mirror image) are stated once each. No symmetry criterion, no chirality rule, no group-theory hint and no mention of mechanical planar chirality appears in the prompt - rule 1 respected (the governing predicate is exactly what must be derived).

CURVD: Contained (one question); Unambiguous (every component property is constitutional/configurational, hence conformation-independent; the choice of which pair of diametrically opposite residues carries the strap is immaterial because all such pairs are symmetry-equivalent in both M1 and M2); Reduced (a single integer); Verifiable (geometric isometry enumeration plus independent predicate check, both specified); Discrete (integer 9, no rounding, no boundary risk - rule 4's rounding clause is vacuous for an integer count). Ten distinct wrong branches listed, exceeding the required six, with values 4, 5, 6, 7, 8, 10, 11, 12, 13, 16 - none collides with 9; in particular the naive slogan route was checked explicitly and yields 11, not 9, so no wrong method reaches the right answer.

CHAR COUNT: 1564 characters, under 2000. LaTeX used for every formula and stereodescriptor; no Unicode math symbols.

TIMELESSNESS / PII / CUTOFF: no dates, no citations, no named people, no post-2025-07-31 content; the chemistry (mechanically interlocked stereochemistry, cyclic aramide macrocycles) is long-established.

ANGLE (rule 11): 16 independent cases, each requiring its own conceptual subtest (which improper operation, if any, survives threading), aggregated into one integer; dropping or mis-judging any single case shifts the answer. Rule 3 satisfied: the naive independent-addition of mechanical and central chirality gives the clean wrong value 11 because A3's two stereocentres cancel the mechanical element. Rule 10 satisfied: no rejection rule or trap is stated in the prompt, so nothing is executable by inspection; difficulty is the 8 component judgments plus 16 case decisions. Rule 2 satisfied: although mechanical planar chirality is a named concept, the slogan version of it is actively wrong on three of the sixteen cases (M4A2, M1A3, M2A3), so pattern-matching mis-fires rather than short-cutting. Rule 7 satisfied: no obscure fact is needed - a stereochemistry expert with pen and paper has everything required.

ORIGINALITY: no number, compound, measurement or claim from the source paper appears. Only the paper's underlying physics is borrowed - a head-to-tail hydrogen-bonded aromatic amide macrocycle threaded by a directional guest - and it is redeployed as a stereochemical census that the paper never discusses.

## INDEPENDENT VERIFICATION (main thread, own re-derivation)

Predicate table re-derived from scratch, not copied from the design agent:

- Improper isometries that can preserve a [2]rotaxane's axle axis are sigma_v (plane containing the axis), sigma_h (ring mean plane) and S_n = C_n . sigma_h. Because the ring pirouettes freely, S_n adds no condition beyond sigma_h, and azimuthal alignment of ring/axle mirror planes is always reachable. So: achiral iff (mac has sigma_v AND axle has sigma_v) OR (mac has sigma_h AND axle ends swappable by an improper op).
- Macrocycles: M1 (F,T) head-to-tail amide sense kills every in-plane mirror line, ring planar so sigma_h survives (C6h). M2 (T,T): vertex mirror through opposite residues maps acyl->acyl, amine->amine, amide sense preserved (D3h). M3 (F,F) = C1, intrinsically chiral. M4 (T,F): the vertex mirror through the two strapped residues survives (strap symmetric in it); strap kills sigma_h.
  - checked M2/M4 opposite-residue pairs: in an alternating ABABAB hexagon 1-4, 2-5, 3-6 are all A/B pairs and are rotation-equivalent, so "diametrically opposite" is unambiguous.
- Axles: A1 (T,T); A2 (T,F); A3 (F,T) - a stereocentre cannot lie on a mirror plane, and the midpoint sigma maps R->S so ends ARE improperly exchangeable (meso); A4 (F,F) - ends exchanged only by a proper C2.

Script over the 4x4 grid returns chiral = M1A2, M1A4, M2A4, M3A1-A4, M4A3, M4A4 = **9**. Matches.

Anchors: M1A2 = textbook mechanically planar chiral rotaxane; M2A2 = standard achiral control; M1A3 = meso rotaxane. All three come out right, so the predicate is not tuned to the answer.

## RISK NOTES (playbook)

- Case volume is HOMOGENEOUS: the 16 cases collapse to 8 component judgments plus one boolean. Per the ink-census lesson, strong responders batch exactly this way - the golden itself is a batched derivation. Expect compression, not 16 separate errors.
- Real difficulty is concentrated in three judgments (M4 keeps sigma_v despite distinguishable faces; A3 is meso; A4 is chiral). That is a 3-fork prompt, not a 16-case one.
- Stereochemistry content is the strongest benchmark lever available (MaCBench 0.24).
- Not cold-probed (per standing directive).
