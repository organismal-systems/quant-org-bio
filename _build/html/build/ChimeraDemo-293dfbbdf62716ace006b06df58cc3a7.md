# 🛼 Demonstration: Modeling sand dollar larval swimming
To gain familiarity with the [ChimeraSwim](./ChimeraSwim.ipynb) model, we will start by working through the entire process of creating a larval morphology using parameters inspired by observations early-stage larvae, and quantifying its swimming performance.
The parameter values in this demonstration are illustrative, based loosely on data in two primary references[^ref1][^ref2].

Many of these values are poorly constrained, having been measured infrequently or not at all.
For example, while it is fairly straightforward to measure a larva's average excess density, it is difficult to separately measure the densities of its component tissue and inclusion.
For poorly constrained parameters like these, we will make educated guesses at reasonable parameter choices for this demonstration.

## Creating and saving a larval morphoplogy
The larval morphology will be defined, and its characteristics calculated, in the Jupyter notebook [](./ChimeraOrg.ipynb).

1. Open this notebook on Binder or on your own computer.
2. Run all cells to initialize the textboxes and Python classes.
3. Enter organism-based morphological parameters:  
:::{table} Table of parameter values for the [ChimeraSwim model](ChimeraSwim.ipynb) demonstration.
:align: center
:label: parsF
| Parameter | Symbol | Relevant range |
| --- | --- | --- |
| Tissue volume | $V_t$ | $5.12 \times 10^{-13}$ |
| Aspect ratio | $\alpha$ | $1$ |
| Relative equator position | $\eta$ | $0.45$ |
| Relative inclusion position | $\sigma$ | $0.99$ |
| Tissue density | $\rho_{tissue}$ | $1130$  |
| Inclusion density | $\rho_{inclusion}$ | $1030$ |
| Average excess density | $\rho_{excess}$ | $40$ |
:::
4. Press the **Visualize the shape** button to generate a 3-dimensional representation of this morphology.
  - You can **enlarge** the plot by dragging the triangle at the bottom right.
  - You can **reorient** the larva by dragging your mouse while holding the left button down.
  - You can **restore** the original orientation by clicking on the house icon.
  - You can **save** the graphic by clicking on the floppy disk icon.
5. If the morphology is correct, press the **Calculate flow** button to start calculations of body and fluid forces.  

    The calculation takes a few seconds; it's complete when "Done calculating inverse." is printed in the textual output.
6. Press the **Select** button to choose a filename under which to save this morphology.
  
    Enter an informative name, such as "demo_re40.pickle', then click **Select** to choose it.
    This name is informative because:
	- The first part of the name, "demo", labels an associated series of observations.
	- The second part of the name, "re40", specifies a key parameter ($\rho_{excess}$) and its value in this morphology (40).
	- The suffix, "pickle", identifies the file type as a Python pickle.

> In the ideal case:
    - you can infer an informative data file name the series of observations it came from and the value of key parameters, and infer


## Creating and saving a larval morphoplogy
Conceptually, this use of the [ChimeraSwim](./ChimeraSwim.ipynb) model amounts to exploring unknown parameter space, to gain perspective on what values unconstrained parameters might plausibly take on.
However, the immediate purpose is to demonstrate how to use and extract meaningful results from the model, and to gain an initial intuition about parameter space.

of a specific taxon, the sand dollar *Dendraster excentricus*.

:::{table} Table of fixed parameters. The relevant ranges shown are only indicative; some interesting examples may lie outside these ranges.
:align: center
:label: parsF
| Parameter | Symbol | Relevant range |
| --- | --- | --- |
| Aspect ratio | $\alpha$ | 0.5-2 |
| Relative equator position | $\eta$ | 0.2-0.8 |
| Relative inclusion position | $\sigma$ | 0.75-0.99 |
| Tissue density | $\rho_{tissue}$ | 1070-1300 $\frac{kg}{m^3}$ |
| Inclusion density | $\rho_{inclusion}$ | 900-2669 $\frac{kg}{m^3}$ |
|Tissue volume | $V_t$ | $10^{-14}-10^{-11} ~m^3$ |
| Average excess density | $\rho_{excess}$ | $20-300 \frac{kg}{m^3}$ |
:::



[^ref1]: Reference 1: [](doi:10.1093/icb/icq090)
[^ref2]: Reference 2 [](https://doi.org/10.1242/jeb.060541)
