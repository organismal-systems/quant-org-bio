# 📖 Minimum habitat size in the KISS model: Back-of-the-envelope estimates

The premise of the KISS[^kiss] model is that an isolated patch of good habitat lies surrounded by an infinite expanse of hostile non-habitat.
The habitat patch supports survival and reproduction for a resident population.
Individuals in this population move randomly, which is reflected at the population level as a diffusion (analgous to how randomly moving molucules are reflected in mass diffusion, heat conduction, *etc*.).
However, any individuals that encounter the edge of the habitat and drift into non-habitat die immediately and are lost to the population.

The KISS model is usually implemented as a 1-dimensional spatial distribution of a population. 
This is because, while 2- and 3-dimensional versions can be implemented, their mathematical solution is more involved and the conclusions are substantially the same.

If a habitat is tiny ($L$ is very small) then a randomly-moving individual quickly encounters the boundary of non-habitat and die.
If this typically happens before the individual reproduces, then deaths exceed births and the population will go extinct.

On the other hand, if the habitat is huge ($L$ is very large) then an individual will typically move randomly for a long time before encountering non-habitat. 
This gives it plenty of time to reproduce, so the population can grow.

Between these extremes is a critical threshold for habitat size, above which a population grows and below which it goes extinct.
The purpose of the KISS model is to quantify that critical habitat size, and to understand how it is affected by organism-level characteristics.

## Scaling analysis of the KISS model
[](#Table1) shows the three parameters in the KISS model:
```{csv-table} **Parameters in the KISS model.**
:label: Table1
:header: "Variable", "Units", "Description"
"$\alpha$", $\frac{1}{s}$, "intrinsic rate of growth within the habitat"
"$D$", $\frac{m^2}{s}$, "population-level diffusion rate"
"$L$", $m$, "habitat size"
```
It's useful to emphasize the units of these parameters:
1. The growth rate, $\alpha$, has units of $time^{-1}$ because all rates have "per unit time"
2. The diffusion constant, $D$, has units of $\frac{length^2}{time}$, reflecting the units of all diffusivities.
    The logic underlying this is outlined below.
3. The habitat size, $L$, has units of meters because it is a length

### Individual movement and population diffusion
To understand diffusion in the context of populations, let's consider a highly simplified model of individual movement behavior.
More complex behaviors require more complex derivations, but give similar conclusions.
The simplified model is this:
- Individuals take positions at discrete locations along a line, $x_1 = \Delta x,~ x_2 = 2 \Delta x,~ x_3 = 3 \Delta x$, *etc*., for all positive and negative integers $i$.
- At discrete time intervals $\Delta t$, each individual moves a distance $\Delta x$ to the left or to the right with equal probability.

If the entirety of a large population is initially placed at a given location (say, $x_0$), then it can be shown the distribution of that population over successive time intervals $\Delta t$ is a Poisson process that is approximately described by a normal distribution. 






[^kiss]: This model is due to Kierstead, Slobodkin and Skellam:  
Kierstead, H.; Slobodkin, L.B. The Size of Water Masses Containing Plankton Bloom. J. Mar. Res. 1953, 12, 141–147.  
Skellam, J.G. Random Dispersal in theoretical biology. Bull. Math. Biol. 1991, 53, 135–165; Reprinted from Biometrika 1951, 38,
196–218.
