# 🏞️ Allometry and size-selection in diatoms

To gain a quantitative perspective on the effects of [mixed layer dynamics](MixedLayers.md) on diatoms, Litchman *et al.* (2009) assumed that many diatom characteristics have allometries of the form of [power laws](./allometry.md),
```{math}
:label: L0
log_{10} X = log_{10}~a + (b \times s)
```
where $X$ is the trait of interest, and $a$ and $b$ are allometric constants.
The metric of size is $$
s = \log_{10}(\mathrm{cell~volume}),
$$
where cell volume is in $\mu m^3$.


Taking the power of 10 of both sides,
```{math}
:label: L0a
X = a \times 10^{b \times s}
```
Litchman et al. analyzed data from the literature to obtain values of the allometric constants $a$ and $b$ for traits involved in growth, mortality and uptake and storage of nitrogen and phosphorus.
The separately analyzed diatoms from marine and freshwater environments.
Their results are summarized in their [supplemental materials](https://www.pnas.org/doi/suppl/10.1073/pnas.0810891106/suppl_file/0810891106si.pdf).

## Model formulation
Litchman *et al.* formulated a model that tracks the increase and decrease of diatom populations in a [mixed layer](./MixedLayers.md).
At intervals, a mixing event such as a storm occurs.
A mixing event replaces a fraction of the water in the mixed layer with an equal amount of water from below the mixed layer.
The diatoms in the displaced mixed layer water are lost, decreasing the cell populations in the mixed layer.
However, the deep water entering the mixed layer brings new nutrient, which can fuel enhanced diatom growth.

Between mixing events, diatoms grow while competing for the diminishing amount of nutrient.
If nutrient concentrations get too low, some or all of the diatoms may be unable to grow, and these populations decrease due to mortality.
Causes of mortality include "background" mortality, which may be due to predators, pathogens, UV damage or other causes, and losses due to [sinking out of the mixed layer](../../../subrepos/biomechanics/ReSphere/RS1.ipynb).

Litchman *et al.*'s model computed the population trajectories of a series of diatom variants, ranging from small to large cells.
For each diatom population, the model acounts for both the **number of cells** and the **nutrient quota**.
The quota is the amount of nutrient cells have in storage, compared to their minimum requirement to sustain growth, and to their maximum storage capacity.
Cells with a large quota can grow at or near their maximum rates, because they are not limited by nutrients.
Cells with a small quota grow slowly or not at all, and may be physiologically stressed, because they are severely nutrient-limited.

A key feature of this model is that growth is determined by stored nutrients, not by the amount of nutrient in the water.
Therefore, when a mixing event provides an instantaneous increase in nutrients, cells must first take up nutrients into storage before they can grow.
According to Litchman *et al.*'s analysis (and consistent with many other observations), small cells take up nutrients faster and can grow at lower quotas, so they have a faster growth response to new nutrients provided by mixing events.

Conversely, Litchman *et al.* concluded that larger diatom cells have disproportionately higher nutrient storage capacity compared to smaller diatom cells. 
This means that scenarios potentially exist in which large diatoms utilize stored nutrients to maintain growth when smaller cells have used up their quotas and stopped growing.


## Allometric power laws in diatoms
The allometric constants that Litchman *et al.* reported for nitrogen-limited diatoms are shown in [](#Table1).
```{csv-table} **Allometric constants for nutrient uptake and growth in diatoms.** The constants $a$ and $b$ are substituted into Equation [](#L0a) to obtain the statistically derived allometry for the corresponding variable.
:label: Table1
:header: "Variable", "a", "b", "Description"
"$V^{hi}_{max.i}$", -7.8, 0.67, "Maximum nutrient uptake rate"
"$K_N$", -0.49, 0.17, "Half-saturation constant for nutrient uptake"
"$Q_{min}$", -8.59, 0.56, "Minimum quota for growth"
"$Q_{max}$", -8.39, 0.81, "Maximum quota (full storage)"
"$\mu_\infty$", 0.74, -0.14, "Maximum growth rate (unlimited nutrient)"
```
In [](#Table1), $b<0$ means that the quantity is decreasing with larger cell size, $s$.
$b>0$ means that the quantity is increasing with larger cell size.

Some key points about these allometric relationships are:
1. Because $b$ is negative, the maximum growth rate, $\mu_{\infty}$, is slower for larger diatoms than for smaller diatoms
2. The minimum quota to support growth, $Q_{min}$, is larger for larger cells ($b=0.56$).
3. The maximum nutrient uptake rate, $V^{hi}_{max.i}$, increases with diatom size ($b=0.67$) but the amount of nutrient required to attain maximum quota increases even faster ($b=0.81$).
4. Both the minimum quota, $Q_{min}$, and the maximum quota, $Q_{max}$, increase with diatom size.
However, $Q_{max}$ grows faster ($b=0.81$) with cell size than $Q_{min}$  ($b=0.56$).

Point 1 means that, with abundant nutrients, small cells can out-grow large cells.
Point 2 means that small cells can continue growth at low quotas when large cells cannot.
Point 3 means that larger cells take longer to fill their quotas than smaller cells.
All these points suggest advantages for small diatom cells. 

However, Point 4 means that nutrient storage capacity, which is the difference between the minimum and maximum quotas, is larger in larger cells.

Litchman *et al.*'s hypothesis is that the pulsed nature of nutrients in  mixed layers &ndash; episodic injections of nutrients duriing mixing events such as storms, followed by long intervals of depleted nutrients &ndash; amplify the storage advantages of large diatoms and enable them to compete successfully with small diatoms.

The model they devised to test their hypothesis about the effects of storage allometry and mixed layer dynamics is implemented in [this notebook](./DiatomSizeESS.ipynb).
Explanation of the formulation of this model is in [this context page](Litchman_etal2009.md).
