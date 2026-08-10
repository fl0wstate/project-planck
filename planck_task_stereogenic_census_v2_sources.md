# Sources — stereogenic-element census v2 (answer 16)

## 1. Seed paper

Akimoto, N.; Takaya, K.; Kasashima, Y.; Watanabe, K.; Yoshida, Y.; Mino, T.
"Pd-Catalyzed asymmetric allylic amination with isatin using a P,olefin-type chiral ligand with C–N bond axial chirality."
*Beilstein J. Org. Chem.* **2025**, *21*, 1018–1023. doi:10.3762/bjoc.21.83
Published **23 May 2025**. Open access, CC BY 4.0. Full text freely verifiable.

**What was taken:** one concept — that a C(aryl)–N(amide) bond can carry a configurationally stable stereogenic axis, and that its stability is set by ortho substitution.

**What was NOT taken:** no compound, structure, yield, ee value, ligand, reaction or measured barrier from the paper appears in the prompt or the golden solution. The paper's actual subject — Pd-catalysed asymmetric allylic amination of isatin with a P,olefin ligand — is entirely absent. All seven compounds in the prompt are chosen for this problem.

**Cutoff status:** 23 May 2025, comfortably before 2025-07-31. (Deliberately preferred over bjoc.21.119, which is dated exactly 31 July 2025 and carries no margin.)

## 2. The ground truth does not depend on any citation

Worth stating plainly, because it is what makes this task QC-robust: the answer is *derived*, not looked up.

- The both-ends-dissymmetric requirement is proved in Step 6 of the golden from first principles — if either end of the axis carries two identical substituents, a 180° rotation maps the molecule onto itself, so the two putative rotamers are one compound. No barrier height can change this, and no literature source is needed to establish it.
- The timescale gate is computed from the Eyring equation (Section 4 below), not asserted.

The references in Section 3 therefore serve one purpose only: to establish that C–N axial chirality is *standard* chemistry, so that adversarial QC cannot dismiss the omitted inventory member as obscure trivia.

## 3. Concept grounding

**(a) C–N axial chirality in anilides and imides.** Curran and co-workers established in 1994 that sufficiently large ortho substituents adjacent to a C–N axis raise the rotational barrier enough to prevent racemisation at room temperature, working on axially twisted **amides and imides** — the two motifs used as D1–D5 here. Later work in the same programme: Curran, D. P.; Chen, C. H.-T.; Geib, S. J.; Lapierre, A. J. B. "Synthesis of Enantioenriched Axially Chiral Anilides from Atropisomerically Enriched Tartarate Ortho-Anilides." *J. Am. Chem. Soc.* **2001**, doi:10.1021/ja010467p.

Openly accessible secondary sources covering the same ground:
- "Atropisomers beyond the C–C axial chirality: Advances in catalytic asymmetric synthesis." *Chem* **2022**, *8*, 1855. (open PDF)
- "Stereoselective construction of atropisomers featuring a C–N chiral axis." *Green Synthesis and Catalysis* (ScienceDirect, open access).
- "Asymmetric Synthesis of Axially Chiral C–N Atropisomers." *Chem. Eur. J.* **2022**, doi:10.1002/chem.202104442.

*Verification note:* the 1994 JACS paper (doi:10.1021/ja00086a056, "Atroposelective Thermal Reactions of Axially Twisted Amides and Imides") is behind an ACS paywall and returned HTTP 403, so its title and DOI were confirmed from indexing rather than from the article itself. The open-access reviews above cover the same claim and can be checked directly.

**(b) Rotation barriers in tertiary aromatic amides.** Clayden and co-workers measured barriers for 40 tertiary aromatic amides by variable-temperature NMR and atropisomer interconversion, giving empirical guidelines for when an amide axis is configurationally stable: "Barriers to rotation about the chiral axis of tertiary aromatic amides," *Tetrahedron* **1998**. (Note this concerns the Ar–C(O) axis; the anilide work in (a) concerns the C(aryl)–N axis used here. The two should not be conflated.)

**(c) Meso relationships; the both-ends-dissymmetric criterion for axial chirality.** Standard stereochemistry: Eliel, E. L.; Wilen, S. H. *Stereochemistry of Organic Compounds*; Wiley: New York, 1994.

**(d) Tetra-ortho-substituted biphenyls are rotationally locked.** Long-established; this is why D6's hindrance is not arguable and the achirality must be decided on symmetry grounds.

## 4. The timescale gate, computed

Eyring at 298.15 K, k_B·T/h = 6.212 × 10^12 s^-1:

| ΔG‡ (kcal/mol) | half-life at 25 °C |
|---|---|
| 15 | 0.011 s |
| 18 | 1.7 s |
| 20 | 51 s |
| 21 | 4.6 min |
| 22 | 25 min |
| 23 | 2.2 h |
| 25 | 2.7 d |
| 26 | 14.8 d |

A half-life of one hour corresponds to ΔG‡ = 22.5 kcal/mol; six hours to 23.6; one day to 24.4.

This gives clean separation with no borderline case:
- **Amide/imide C(O)–N rotation** (≈15–21 kcal/mol) → half-lives from milliseconds to minutes → **excluded** by the stated "hours".
- **Anilide C(aryl)–N atropisomerism** with 2,6-disubstitution (≈25 kcal/mol and above) → half-lives of days → **counted**.

The gap between the two regimes is roughly 4 kcal/mol, a factor of several hundred in lifetime, so the prompt's "hours" stipulation partitions them unambiguously.

**Cross-check against the seed paper.** It reports ΔG‡_rac = 25.0 kcal/mol with a racemisation half-life of about 1.3 days. Eyring at 25.0 kcal/mol gives a *rotation* half-life of 2.73 days. The factor of two is expected and correct: racemisation approaches equilibrium between two enantiomers, so k_rac = 2·k_rot, giving t½(rac) = 1.37 days — matching the paper. This confirms both the arithmetic here and the paper's reported value, and it is the reason the prompt's own compounds sit safely inside the "isolable" regime.

## 5. Originality

The problem is original: not taken from, adapted from, or paraphrased from any published problem set, examination, or textbook exercise. The seed paper supplied one structural concept. The specific question — a stereoisomer census over seven named compounds in which three contain a rotationally locked but achiral axis, each failing for a different reason — does not appear in the literature. The answer 16 was derived here and verified by parametrised enumeration over the four independent judgments (`scratchpad/stereo2.py`).
