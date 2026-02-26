# 📖 Minimum habitat size in the KISS model: Back-of-the-envelope estimates

The premise of the KISS[^kiss] model is that an isolated patch of good habitat lies surrounded by an infinite expanse of hostile non-habitat.
The habitat patch supports survival and reproduction for a resident population.
Individuals in this population move randomly, which is reflected at the population level as a diffusion (analgous to how randomly moving molecules are reflected in mass diffusion, heat conduction, *etc*.).
However, any individuals that encounter the edge of the habitat and drift into non-habitat die immediately and are lost to the population.

The KISS model is usually implemented as a 1-dimensional spatial distribution of a population. 
This is because, while 2- and 3-dimensional versions can be implemented, their mathematical solution is more involved and the conclusions are substantially the same.

If a habitat is tiny ($L$ is very small) then a randomly-moving individual quickly encounters the boundary of non-habitat and dies.
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
"$\alpha$", $\frac{1}{s}$, "[intrinsic rate of growth](wiki:Population_ecology) within the habitat"
"$D$", $\frac{m^2}{s}$, "population-level diffusion rate"
"$L$", $m$, "habitat size"
```
It's useful to emphasize the units of these parameters:
1. The intrinsic growth rate, $\alpha$, has units of $time^{-1}$ because all rates are "per unit time".
2. The diffusion constant, $D$, has units of $\frac{length^2}{time}$, reflecting the units of all diffusivities.
    The logic underlying this is outlined below.
3. The habitat size, $L$, has units of $length$.

### Individual movement and population diffusion
To understand diffusion in the context of populations, let's consider a highly simplified model of individual movement behavior.
More complex behaviors require more complex derivations, but give similar conclusions.
The simplified model is this:
- Individuals take positions at discrete locations along a line, $x_1 = \Delta x,~ x_2 = 2 \Delta x,~ x_3 = 3 \Delta x$, *etc*., for all positive and negative integers $i$.
- At discrete time intervals $\Delta t$, each individual moves a distance $\Delta x$, either to the left or to the right with equal probability.

Let's assume the entirety of a large population is initially placed at a given location (say, $x_0$).
Then, it can be shown (see [](wiki:Normal_distribution) and [](wiki:Central_limit_theorem)) the distribution of that population over successive time intervals $t_n = n \Delta t,~ n = 1, 2, \dots$ is a Poisson process that is approximately described by a normal distribution
$$
p(t_n,x_i) = \frac{1}{2\left(\pi D t_n\right)^\frac{1}{2}}~e^{-\frac{x_i^2}{4 D t_n}}
$$
where the rate of spreading is determined by the diffusion coefficient,
$$
D = \frac{\Delta x^2}{2 \Delta t}
$$
This analysis[^akira] generalizes to many variants of the simple random movement behavior, in 1-, 2- or 3-dimensions as
$$
D = \frac{\Delta x^2}{c \Delta t}
$$
where $c$ is a constant of order of magnitude 1.

These expressions for $D$ illustrates why the diffusion coefficient has units $\frac{m^2}{s}$.

### Characteristic time scales for the KISS model
A scaling analysis typically involves two or more characteristic values expressed in a common unit, used as quotients to form **nondimensional indices** that indicate the relative importance of different mechanisms.
For example, in fluid mechanics, the [Reynolds number](../../biomechanics/ReSphere/RSscaling.md) reflects the relative importance of forces due to momentum compared to forces due to viscosity.

We can summarize the outcomes of the KISS model as stemming from two characteristic time scales:
1. $T_\alpha$, the time scale of reproduction
2. $T_D$, the time scale of movement

Both of these time scales are conceived as order of magnitude estimates.
In some case, exact values are available.
However, a rough approximation is usually all that is required, and that can often be obtained with a very simple analysis.

$T_\alpha$ is how long it takes for "significant" reproduction to occur.
The intrinsic rate of growth of the population in the KISS model is $\alpha$.
Because $\alpha$ has units of inverse time, we can take 
$$
T_{\alpha} = \frac{1}{\alpha}
$$
as the characteristic reproductive time scale.
In the absence of mortality from movement out of the habitat, the population would increase by a factor of $e$ over a time $T_\alpha$.[^grw]

[^grw]: This follows from the definition of the intrinsic rate of growth, which is the value for which a population $p(t)$ grows according to 
    $$p(t) = p(0)~e^{\alpha t}$$
    where $p(0)$ is the population at time $t=0$.

$T_D$ is how long it takes for a population to diffuse over a significant distance.
This is somewhat vague, but we are helped by observing that in the problem definition there is only one length by which to define a "significant" distance: the habitat size, $L$.

We are also helped by observing that the definition of $D$ suggests that, over long times and large distance,
$$
D \approx \frac{L^2}{T_D}
$$
where we neglect a constant of order of magnitude 1 (related to but not necessarily equal to $c$).
This property is implied by the units of $D$:
There is no other way to construct a diffusion coefficient from the parameters $L$ and $T_D$.

Rearranging, we therefore take
$$
T_D \approx \frac{L^2}{D}
$$

### Persistence *vs*. extinction
From the logic underlying the KISS model, we can then define two parts of parameter space:
> - $\frac{T_\alpha}{T_D} \gg 1$ : reproduction takes much longer than movement out of the habitat
> - $\frac{T_\alpha}{T_D} \ll 1$ : reproduction takes much shorter than movement out of the habitat

These two cases clearly delineate parameter spaces in which individuals typically die before reproducing ($\frac{T_\alpha}{T_D} \gg 1$) leading to extinction, from parameter spaces in which individuals typically reproduce before dying ($\frac{T_\alpha}{T_D} \ll 1$), leading to persistence. 

Between these extremes is a critical threshold,
$$
\frac{T_\alpha}{T_D} = 1.
$$
Substituting our estimated time scales at the critical threshold,
$$
\frac{D}{\alpha~L^2} = 1.
$$

At this stage, it is useful to critically assess this conclusion:
1. Are the units consistent?  
    Yes &ndash; the units of $D$, $\alpha$ and $L^2$ on the left side cancel to match the dimensionless constant 1 on the right.
2. Does it make intuitive sense?  
    Yes &ndash; it is intuitively reasonable that:
	
	- increasing growth rate ($\alpha$) favors population persistence, because reproduction is faster
	- increasing habitat size ($L$) favors population persistence, because death due to encountering non-habitat is slower[^len]
	- increasing movement ($D$) favors population extinction, because death due to encountering non-habitat is faster

[^len]: It's worth noting that, if individuals always moved in the same direction, the time to encounter non-habitat would increase in proportion to $L$.
    Because individuals move in random directions, the time to encounter non-habitat must increase faster than the same-direction case.
	$L^2$ is the next higher power of $L$, so this too is plausible.

Rearranging, we can define an estimated critical habitat size $L_{crit}$, based only on scaling arguments, as
$$
L_{crit} = \left(\frac{D}{\alpha} \right)^{\frac{1}{2}}
$$
We interpret $L_{crit}$ as an approximate threshold, and make the predictions that in habitats significantly larger than $L_{crit}$ the population persists, while in habitats significantly smaller than $L_{crit}$ the population goes extinct.


$$
L_{crit} = \left(\frac{D}{\alpha} \right)^{\frac{1}{2}}
$$

For context, the [exact solution to the KISS model](./KISSsoln.md) gives
$$
L_{crit} = \pi \left(\frac{D}{\alpha} \right)^{\frac{1}{2}}
$$
showing that the scaling analysis gives the correct order of magnitude.


[^kiss]: This model is due to Kierstead, Slobodkin and Skellam:  
Kierstead, H.; Slobodkin, L.B. The Size of Water Masses Containing Plankton Bloom. J. Mar. Res. 1953, 12, 141–147.  
Skellam, J.G. Random Dispersal in theoretical biology. Bull. Math. Biol. 1991, 53, 135–165; Reprinted from Biometrika 1951, 38,
196–218.

[^akira]: A readable and comprehensive discussion of biological random walks and population-level diffusion can be found in Okubo, A. and Levin, S.A. (2001) Diffusion and Ecological Problems: Modern Perspectives. Springer, New York. 


