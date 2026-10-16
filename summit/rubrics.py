"""AI-assisted criteria derived from the existing solutions, for permitted workflows."""

INTERMEDIATE_CRITERIA = {
    "adiabatic_regime": [
        r"Identifies the equilibrium temperature as the boiling point, $351.44\,\mathrm{K}$.",
        r"Obtains $K(351.44\,\mathrm{K})\approx3.4925$.",
    ],
    "annulene_quadrant": [
        r"Classifies entry 8, with $360^\circ$ twist, as having Hückel topology.",
        r"Excludes entry 10 from macrocyclic ring-current counting because its $\mathrm{sp}^3$ centre breaks the conjugated circuit.",
    ],
    "battery_cycle": [
        r"Obtains total operating time $3Q$ hours per cycle when $Q$ is the numerical discharge capacity in $\mathrm{mAh\,cm^{-2}}$.",
        r"Obtains initial zinc capacity $Z_0\approx5.9194\,\mathrm{mAh\,cm^{-2}}$.",
    ],
    "battery_v3": [
        r"Obtains total operating time $6Q$ hours per cycle when $Q$ is the numerical discharge capacity in $\mathrm{mAh\,cm^{-2}}$.",
        r"Obtains $Q_{\mathrm{cat}}(n)=1.200[1-0.0080(n-1)]\,\mathrm{mAh\,cm^{-2}}$.",
    ],
    "belt_census": [
        r"Classifies B12 as diatropic with $16$ circuit electrons in its triplet state.",
        r"Excludes B16 because its $\mathrm{sp}^3$ centre severs the cyclic conjugated circuit.",
    ],
    "coordination_census": [
        r"Obtains $12$ distinct stereoisomers for H3, counting enantiomers separately.",
        r"Obtains $2$ distinct arrangements for H4 from the inequivalent N and O chelate donors.",
    ],
    "debye_screening": [
        r"Obtains ionic strength $I=0.095\,\mathrm{mol\,L^{-1}}$.",
        r"Obtains Debye length $\kappa^{-1}\approx0.9863\,\mathrm{nm}$.",
    ],
    "directional_cube": [
        r"Derives that exactly $4$ vertices have formal valence $M^{III}$ from $2h+(8-h)=12$.",
        r"Obtains $216$ labelled admissible states before quotienting by rotations.",
    ],
    "homoaromatic_sum": [
        r"Assigns species C a diatropic homoaromatic circuit contributing $6$ electrons.",
        r"Assigns species B a diatropic circuit contributing $14$ electrons.",
    ],
    "hopf_shift_census": [
        r"Obtains the stability threshold $b<3.64$ for procedure A on the specified grid.",
        r"Classifies procedure C at $b=3.5$ as unstable from the composite update, despite both individual updates being stable there.",
    ],
    "ink_census": [
        r"Derives the flow-and-plug criterion $1/\sqrt{2}\leq\tau_y/\tau_w<1$.",
        r"Obtains the corrosion conversion $\Delta m\approx117.7v\,\mathrm{mg\,cm^{-2}}$ for the numerical hydrogen flux $v$ in the question's units.",
    ],
    "mixed_stereo_census": [
        r"Obtains $2$ stereoisomers for F1 from cis/trans geometry despite the absence of stereocentres.",
        r"Obtains $3$ stereoisomers for F3 after identifying its mixed configurations as one meso form.",
    ],
    "oligoester_census": [
        r"Classifies E1 as achiral through an $S_4$ operation.",
        r"Classifies E5 as chiral because no cyclic shift maps every descriptor to its opposite.",
    ],
    "oligoester_census_v2": [
        r"Classifies G5 as chiral because sequence reversal is not an allowed equivalence of the directional ester ring.",
        r"Classifies G7 as chiral because its residue-preserving shifts are only $0,2,4$, none of which inverts every descriptor.",
    ],
    "organic_v3": [
        r"Assigns acetoxonium participation to the trans-$(1S,2S)$ feed through its trans-diaxial conformation.",
        r"Assigns equal capture probabilities $1/2$ to C1 and C2 of the acetoxonium intermediate.",
    ],
    "osmotic_polymersome": [
        r"Uses number-average molar mass $M_n=2.00\,\mathrm{kg\,mol^{-1}}$ for the polymer's osmotic contribution.",
        r"Obtains total external osmolarity $3.782\,\mathrm{mOsm\,L^{-1}}$.",
    ],
    "pentalene_census": [
        r"Identifies $\{1,3\}$ and $\{2,6\}$ as exactly the two non-Kekulé substitution classes.",
        r"Finds zero-mode nullity $2$ for the $\{2,6\}$ isomer, excluding it as open-shell.",
    ],
    "porphyrin_census": [
        r"Obtains $10$ stereoisomers for Q2 using its face-inverting pyrrole-axis rotation.",
        r"Obtains $8$ stereoisomers for Q5 using its face-inverting meso-axis rotation.",
    ],
    "rotaxane_chirality": [
        r"Identifies M1 as lacking $\sigma_v$ but possessing $\sigma_h$.",
        r"Identifies M4 as possessing $\sigma_v$ despite its distinguishable faces.",
    ],
    "rotaxane_chirality_v2": [
        r"Identifies M1 as lacking a mirror plane containing the axle axis.",
        r"Identifies the face-exchanging achirality route as requiring a macrocycle $\sigma_h$ or $S_n$ together with an improper operation exchanging the dumbbell ends.",
    ],
    "speciation_optionalfork": [
        r"Obtains the Nernst free-ion ratio $x/y\approx0.677587$.",
        r"Includes $10^9h\ell$ in $\alpha_{III}$ to account for the protonated ligand complex.",
    ],
    "stereogenic_census": [
        r"Obtains $2$ stereoisomers for C1 because its identical ortho substituents prevent axial stereogenicity.",
        r"Obtains $3$ stereoisomers for C4 after identifying the mixed axial configurations as one meso form.",
    ],
    "stereogenic_census_v2": [
        r"Obtains $1$ stereoisomer for D4 because the imide nitrogen's two carbonyl substituents are equivalent.",
        r"Obtains $3$ stereoisomers for D5 after identifying its mixed axial configurations as one meso form.",
    ],
    "tetraradical_gap": [
        r"Obtains bridge coupling $J_b=+4.80\,\mathrm{kcal\,mol^{-1}}$ under $\hat H=\sum J_{ij}\hat{\mathbf S}_i\cdot\hat{\mathbf S}_j$, or the equivalent physical coupling under another explicitly stated convention.",
        r"Obtains quintet energy $E_Q=-2.40\,\mathrm{kcal\,mol^{-1}}$ with the solution's energy zero.",
    ],
    "tetraradical_v2": [
        r"Rejects result (ii) as an adiabatic gap unsuitable for the specified fixed-geometry couplings.",
        r"Sets $J_{14}=0$ because result (iv) is below the stated convergence threshold.",
    ],
    "twistane_final": [
        r"Obtains $N_A=12$ distinct carbon signals for A.",
        r"Obtains $N_B=6$ distinct carbon signals for B.",
    ],
}


def rubric_for(slug, answer):
    first, second = INTERMEDIATE_CRITERIA[slug]
    return {
        "criteria": [
            {"id": "c1", "description": f"Gives {answer} as the final answer in the units and precision requested by the question.", "points": 5, "isFinalAnswer": True},
            {"id": "c2", "description": first, "points": 3, "isFinalAnswer": False},
            {"id": "c3", "description": second, "points": 2, "isFinalAnswer": False},
        ],
        "commonWrongAnswers": [],
    }
