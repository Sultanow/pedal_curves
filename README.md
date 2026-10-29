# Arithmetic Envelopes on the Circle and Diophantine Imaging

Code, notebooks and data for two papers that place numbers on the circle and join them by chords:

1. [**Arithmetic Envelopes on the Circle: An Introduction**](#part-1-arithmetic-envelopes-on-the-circle) – Preprints.org, 2026
2. [**Diophantine imaging reveals the broken symmetry of sums of integer cubes**](#part-2-diophantine-imaging) – Scientific Reports, 2024

<p align="center">
  <img src="img/image1.png" height="180">
  <img src="img/image2.png" height="180">
  <img src="img/image3.png" height="180">
  <img src="img/primes.png" height="180">
</p>

## Part 1: Arithmetic Envelopes on the Circle

[![Preprint](https://img.shields.io/badge/Preprints.org-202610.2366-orange)](https://www.preprints.org/manuscript/202610.2366)
[![DOI](https://img.shields.io/badge/DOI-10.20944%2Fpreprints202610.2366.v2-blue)](https://doi.org/10.20944/preprints202610.2366.v2)
[![License: CC BY 4.0](https://img.shields.io/badge/Paper-CC%20BY%204.0-lightgrey)](https://creativecommons.org/licenses/by/4.0/)

> **Paper:** E. G. Sultanow, *Arithmetic Envelopes on the Circle: An Introduction*. Preprints (2026), [doi:10.20944/preprints202610.2366.v2](https://doi.org/10.20944/preprints202610.2366.v2).
> **Read it on [Preprints.org](https://www.preprints.org/manuscript/202610.2366).** The code in this repository reproduces the computations and figures of the paper.

Place numbers on a circle and join each label $x$ to the label of $g(x)$. The curve that every chord touches is an *arithmetic envelope*. For $x \mapsto kx \bmod 1$ it is an epicycloid: the cardioid for $k=2$, the nephroid for $k=3$, and, up to similarity, the boundary of the main component of the Multibrot set of $z^k+c$; the times-table cardioid is $-4/3$ times the main cardioid of the Mandelbrot set. Labelling the odd integers by their binary digits identifies them with the Prüfer 2-group. In these coordinates, multiplication by 3 is conjugate to the rotation by $\log_2 3$. The main result of the paper (Theorem 1, *Henkel's convexoid*) shows that the chords $x \to 3x$ leave free a convex region, bounded by the segment $[-\tfrac17, \tfrac15]$ and two epicycloid arcs. The heart-shaped pedal curve of the same chord family lies on the algebraic curves $x = \rho\,T_5(\rho)$ and $x = \rho\,T_7(\rho)$. Lifted into space, envelope and pedal curve lie on one ruled surface; on the number helix $s=\log_2 x$, multiplication by 3 is a screw motion; and in the Klein model the convexoid is hyperbolically convex.

### Paper

**Arithmetic Envelopes on the Circle: An Introduction**
Eldar Gunter Sultanow · Preprints.org, version 2, posted 27 October 2026 (not peer-reviewed)

**[Preprints.org](https://www.preprints.org/manuscript/202610.2366)** · [DOI 10.20944/preprints202610.2366.v2](https://doi.org/10.20944/preprints202610.2366.v2) · [local PDF](doc/Pedal_Curves.pdf)

### Citation

```bibtex
@article{sultanow2026envelopes,
  title   = {Arithmetic Envelopes on the Circle: An Introduction},
  author  = {Sultanow, Eldar Gunter},
  journal = {Preprints},
  year    = {2026},
  month   = oct,
  doi     = {10.20944/preprints202610.2366.v2},
  url     = {https://www.preprints.org/manuscript/202610.2366}
}
```

### Artifacts by section

The figure numbers follow version 2 of the paper; its Table 1 lists the same assignment. Where a notebook contains several variants, choose the multiplier (Figures 1, 2) or the parameter $a$ (Figure A5).

| Section | Topic | Figure | Artifacts |
| --- | --- | --- | --- |
| 2 | Envelopes of chord families, point of contact, numerical drawing | – | [`caustics_simple.ipynb`](python/notebooks/caustics_simple.ipynb) |
| 3 | Caustics of $\times2$, $\times3$, $\times k$: cardioid, nephroid, epicycloids | 1, 2 | [`dupin_cyclide.nb`](mathematica/dupin_cyclide.nb); also drawn in [`caustics_simple.ipynb`](python/notebooks/caustics_simple.ipynb), [`caustics.ipynb`](python/notebooks/caustics.ipynb) |
| 3.1 | Envelopes and Multibrot sets (Proposition 2) | 3 | [`fig_multibrot.py`](python/programs/views/fig_multibrot.py), [`check_views.py`](python/programs/views/check_views.py) |
| 4 | Dyadic labelling and the Prüfer 2-group | 4 | [`circle_numbers.nb`](mathematica/circle_numbers.nb), [`prüfer_group_operator.nb`](mathematica/pr%C3%BCfer_group_operator.nb), [`pruefer_group_p2p3.nb`](mathematica/pruefer_group_p2p3.nb), [`caustics_base2_3.ipynb`](python/notebooks/caustics_base2_3.ipynb) |
| 5 | **Henkel's convexoid** (Theorem 1) | 5 | [`python/programs/convexoid/`](python/programs/convexoid): `fig_convexoid.py`, `heart_vs_convexoid.py`, `convexoid_proof_check.py` |
| 6 | Heart-shaped pedal curve and its polynomials | 6 | [`heartshape_red_blue.nb`](mathematica/heartshape_red_blue.nb), [`heartshape_red_blue_polynomial.nb`](mathematica/heartshape_red_blue_polynomial.nb) |
| 7 | Bungee surface, number helix, Klein and Poincaré disk (Propositions 5, 6, Corollary 2) | 7, 8 | [`python/programs/views/`](python/programs/views): `fig_views3d.py`, `fig_poincare.py`, `check_views.py`; [`caustics_vis.ipynb`](python/notebooks/caustics_vis.ipynb) for further pairs of bases |
| 8.1 | Implicit equations of epicycloids | – | [`cycloid_implicitization.nb`](mathematica/cycloid_implicitization.nb), [`getCartesians.m`](matlab/getCartesians.m) |
| 8.2 | The non-linear map $x \mapsto x^3$ | 9 | [`dupin_analysis.nb`](mathematica/dupin_analysis.nb) |
| A | Tropicalization | A1, A2 | Singular listings in the paper; [`drawtrop.py`](python/programs/tropical/drawtrop.py) (from the course MCS 595, 2013) |
| B | Piecewise linear labelling reproducing the cardioid | A3–A6 | [`pedal_curves_plot.nb`](mathematica/pedal_curves_plot.nb) (A3), [`pedal_parametric_simplified_a.nb`](mathematica/pedal_parametric_simplified_a.nb) (A4, A5), [`pedal_parametric_curves.nb`](mathematica/pedal_parametric_curves.nb) (A6), [`cardioid.nb`](mathematica/cardioid.nb), [`pedal_curves_interactive.nb`](mathematica/pedal_curves_interactive.nb), `pedal_*.nb`, `deriv_*.nb` |
| C | Computer-assisted step of the proof of Theorem 1 | – | [`convexoid_proof_check.py`](python/programs/convexoid/convexoid_proof_check.py) |

The notebooks `dupin_*.nb` keep the working name "Dupin-like" from an earlier draft: `dupin_cyclide.nb` draws the caustics of Figures 1 and 2, `dupin_analysis.nb` the non-linear map of Section 8.2, and the `*_ax.nb` variants treat the maps $x \mapsto ax$.

### Reproducing Theorem 1 and the spatial views

```bash
pip install numpy scipy sympy matplotlib

cd python/programs/convexoid
python fig_convexoid.py          # Figure 5: convexoid and logarithmic labelling
python heart_vs_convexoid.py     # corner C, areas, implicit equations, convexoid vs. heart
python convexoid_proof_check.py  # computer-assisted step of the proof (resultants)

cd ../views
python fig_multibrot.py          # Figure 3: envelopes and Multibrot sets
python fig_views3d.py            # Figure 7: bungee surface and number helix
python fig_poincare.py           # Figure 8: Klein and Poincaré disk
python check_views.py            # numerical checks of Propositions 2, 5 and 6
```

Expected values for Theorem 1: $t_r \approx 1.8291729217$, $t_b \approx 2.4646905931$, $C \approx 0.21545 + 0.42511i$, area $\approx 0.19210$. The proof check reports exactly one intersection of the two arcs and no self-intersection of the second arc.

## Part 2: Diophantine imaging

[![Scientific Reports](https://img.shields.io/badge/Scientific%20Reports-14%2C%2016%20%282024%29-orange)](https://www.nature.com/articles/s41598-023-49960-y)
[![DOI](https://img.shields.io/badge/DOI-10.1038%2Fs41598--023--49960--y-blue)](https://doi.org/10.1038/s41598-023-49960-y)
[![License: CC BY 4.0](https://img.shields.io/badge/Paper-CC%20BY%204.0-lightgrey)](https://creativecommons.org/licenses/by/4.0/)
[![Kaggle](https://img.shields.io/badge/Kaggle-Equal%20Sums%20of%20Powers%20%283%2C1%2C3%29-20BEFF?logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/eldarsultanow/equal-sums-of-powers-313)

> **Paper:** E. Sultanow, M. Henkel, I. J. Aberkane, *Diophantine imaging reveals the broken symmetry of sums of integer cubes*. Scientific Reports 14 (2024), 16, [doi:10.1038/s41598-023-49960-y](https://doi.org/10.1038/s41598-023-49960-y).
> **Read it on [nature.com](https://www.nature.com/articles/s41598-023-49960-y)** (open access). The Mathematica notebooks and datasets in this repository produce the figures of the article.

*Diophantine imaging* places the known solutions $\lbrace a,b,c\rbrace$ of a Diophantine equation on the circle according to the leading digits of $a$, $b$, $c$ in a base $p$ and draws the triangle they span; in base 2 the coordinate system is the labelled Prüfer 2-group of Part 1. The article compares the sums of three cubes $a^3+b^3+c^3=d$ with the cubic quadruples $a^3+b^3+c^3=d^3$ in the bases $2, 3, 7, \pi, \varphi, e$, grouping the triangles by their share of the circle's area. The cubic quadruples spread almost evenly in every base (with a slight asymmetry in base 7), whereas the sums of three cubes show a pronounced, base-dependent structure; base $\varphi$ gives the most even picture.

### Paper

**Diophantine imaging reveals the broken symmetry of sums of integer cubes**
Eldar Sultanow, Max Henkel, Idriss J. Aberkane · Scientific Reports 14, article 16 · received 5 August 2022, accepted 14 December 2023, published 2 January 2024 (open access)

**[nature.com](https://www.nature.com/articles/s41598-023-49960-y)** · [DOI 10.1038/s41598-023-49960-y](https://doi.org/10.1038/s41598-023-49960-y) · [PDF](https://www.nature.com/articles/s41598-023-49960-y.pdf)

Section 4.2 of the preprint in Part 1 corrects some minor slips in the article's description of the group law (cosets of the labels 5 and 7, case distinction, reduction step); the closed formula and the addition table of the article are correct.

### Citation

```bibtex
@article{sultanow2024diophantine,
  title   = {Diophantine imaging reveals the broken symmetry of sums of
             integer cubes},
  author  = {Sultanow, Eldar and Henkel, Max and Aberkane, Idriss J.},
  journal = {Scientific Reports},
  volume  = {14},
  pages   = {16},
  year    = {2024},
  doi     = {10.1038/s41598-023-49960-y},
  url     = {https://www.nature.com/articles/s41598-023-49960-y}
}
```

### Artifacts

| Article | Content | Artifacts |
| --- | --- | --- |
| Methods, Equation (2), Table 1, Listing 1 | Group operation of the labelled Prüfer 2-group | [`prüfer_group_operator.nb`](mathematica/pr%C3%BCfer_group_operator.nb), labelled circle in [`circle_numbers.nb`](mathematica/circle_numbers.nb) |
| Listing 2 | Download and merge of Wroblewski's tables of equal sums of powers (3,1,3) | [`download_prepare_esp.ipynb`](python/notebooks/download_prepare_esp.ipynb), [`datasets/README.md`](mathematica/datasets/README.md) |
| Figures 4–9 | Cubic quadruples in the bases $2, 3, 7, \pi, \varphi, e$ | [`cubic_quadruples_base_2.nb`](mathematica/cubic_quadruples_base_2.nb), [`_3`](mathematica/cubic_quadruples_base_3.nb), [`_7`](mathematica/cubic_quadruples_base_7.nb), [`_pi`](mathematica/cubic_quadruples_base_pi.nb), [`_phi`](mathematica/cubic_quadruples_base_phi.nb), [`_e`](mathematica/cubic_quadruples_base_e.nb) |
| Figures 10–15 | Sums of three cubes in the bases $2, 3, 7, \pi, \varphi, e$ | [`three_cubes_base_2.nb`](mathematica/three_cubes_base_2.nb), [`_3`](mathematica/three_cubes_base_3.nb), [`_7`](mathematica/three_cubes_base_7.nb), [`_pi`](mathematica/three_cubes_base_pi.nb), [`_phi`](mathematica/three_cubes_base_phi.nb), [`_e`](mathematica/three_cubes_base_e.nb); variants [`three_cubes.nb`](mathematica/three_cubes.nb), [`three_cubes_single.nb`](mathematica/three_cubes_single.nb) |

### Data

| Dataset | Content | Source |
| --- | --- | --- |
| [`threecubes_20070419.csv`](mathematica/datasets/threecubes_20070419.csv) | Solutions of $x^3+y^3+z^3=n$ for $n<1000$, neither a cube nor twice a cube (Figures 10–15) | A.-S. Elsenhans and J. Jahnel, formerly at the University of Göttingen; copy in this repository |
| [Equal Sums of Powers (3,1,3)](https://www.kaggle.com/datasets/eldarsultanow/equal-sums-of-powers-313) | Solutions of $a^3+b^3+c^3=d^3$ below 1,000,000 (Figures 4–9) | J. Wroblewski, merged with Listing 2; on Kaggle |

## Repository layout

| Folder | Content |
| --- | --- |
| [`doc/`](doc) | The preprint of Part 1 (PDF) |
| [`python/programs/convexoid/`](python/programs/convexoid) | Theorem 1: figure, corner, area, computer-assisted proof step |
| [`python/programs/views/`](python/programs/views) | Multibrot, bungee surface, number helix, Klein and Poincaré disk |
| [`python/programs/tropical/`](python/programs/tropical) | Drawing tropical curves |
| [`python/notebooks/`](python/notebooks) | Jupyter notebooks for drawing dreamcatchers and envelopes, data preparation for Part 2 |
| [`mathematica/`](mathematica) | Wolfram notebooks: derivations, implicitizations, plots, Diophantine imaging |
| [`mathematica/datasets/`](mathematica/datasets) | Solutions of $x^3+y^3+z^3=n$ and of $a^3+b^3+c^3=d^3$ (see its README) |
| [`matlab/`](matlab) | Symbolic elimination of parametrizations |
| [`img/`](img) | Images used in this README |

## Requirements

- Python 3 with `numpy`, `scipy`, `sympy` and `matplotlib`; Jupyter for the notebooks.
- Wolfram Mathematica for the `.nb` files.
- MATLAB with the Symbolic Math Toolbox for `getCartesians.m`.
- Singular with `tropical.lib` for the listings of Appendix A of the preprint.

## Further experiments

These are exploratory and not part of either paper: [`irrational_rotations.nb`](mathematica/irrational_rotations.nb), [`poincare_collatz.nb`](mathematica/poincare_collatz.nb), [`poincare_collatz_discrete.nb`](mathematica/poincare_collatz_discrete.nb), [`rotateLeft.nb`](mathematica/rotateLeft.nb), [`rotate_left_plot.nb`](mathematica/rotate_left_plot.nb), [`ternary_plot.nb`](mathematica/ternary_plot.nb) and [`negative_pedal_curves.ipynb`](python/notebooks/negative_pedal_curves.ipynb). The prime dreamcatcher in [`caustics.ipynb`](python/notebooks/caustics.ipynb) joins the $i$-th to the $i^2$-th prime and reads the pickled prime list [`primes_179424673.bin`](python/notebooks/primes_179424673.bin).

## Related work

- A. Rahn, E. Sultanow, M. Henkel, S. Ghosh, I. J. Aberkane: *An algorithm for linearizing the Collatz convergence.* Mathematics 9(16), 1898 (2021). [doi:10.3390/math9161898](https://doi.org/10.3390/math9161898)
- M. Henkel: *Visualizing the Collatz Feather as an L-System.* Master's thesis, University of Applied Sciences Schmalkalden (2021). [Code](https://github.com/Sultanow/collatz/tree/master/06%20Collatz%20L-System)
