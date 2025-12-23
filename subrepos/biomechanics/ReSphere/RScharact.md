# 📖️ Estimating drag forces, Part 1
In understanding the ways organisms move through fluids, it's useful to distinguish between effects that are due mostly to an organism's size from those associated with its shape.
We might ask, for example, "How does swimming speed and cost of locomotion differ between a smaller younger fish and that same fish when it is older and larger but substantially the same shape?"
We could also ask, "Is the morphology of this fish streamlined as an adaptation to swimming quickly or for long distances, by comparison to another fish that is equal in size but largely sedentary?"

Here, we focus on understanding the basic effects of size on drag forces acting on organisms moving in fluids.
That is, we will ask, "*What are the inherent effects of being large or being small on drag forces?*"
Likewise, we will ask, "*What are the inherent effects of moving quickly or slowly on drag forces?*"
These questions are posed in generic terms because  we are interested in *inherent* effects &ndash; those that are largely unavoidable consequences of size or speed.

The answers to these questions will provide us with tools to think more concretely about the effects of specific shapes, behaviors, *etc*.
The idea is that factors like size and speed will have strong effects on drag, and that variations in shape, surface properties and other specific traits will be "tweaks" of those strong effects.
If we can factor out the effects of size and speed, more subtle effects (like those of shape) will be easier to understand and quantify.

## Organismal characteristics
[](#sph1) is a cartoon of an organism moving through a fluid (in this case, sinking downwards).
As it moves, it pushes aside fluid in front of itself, illustrated by the blue "streamlines" moving sideways near the underside of the organism.
Immediately adjacent to the organism, fluid is moving with the organism (hence, added mass).
The organism leaves a wake behind itself, of fluid that is moving nearly as fast as it is (hence, wake momentum).

```{figure} Images/sphere1.png
:label: sph1
:width: 30%
:align: center
:alt: A cartoon of flow around a sinking sphere.

A cartoon of a sinking organism. The organism has a linear dimension (diameter) $L$, frontal area $A$, and sinking velocity $U$. The blue lines indicate water flow around the organism, and the wake it leaves behind.

```
In generic terms, we can describe this organism using **characteristic values** (also see the discussion on Scale models and nondimensional numbers in the Overview). 
For example, we can consider a **characteristic length**, ***L***, as a linear metric that expresses an object size.
If the organism is spherical, then an obvious choice for *L* is the diameter.
If the organism is oblong, then there is some ambiguity, but if we choose for *L* some consistent standard such as maximum dimension or average of the dimensions, then the analysis will still reflect the differences between larger and smaller (but similarly shaped) particles.

*L* is the characteristic length.
Analogously, we specify a **characteristic area**, ***A***.
*A* is an indicator of the approximate magnitude of the organism's projected area. 
As with length, the exact specification of *A* is obvious for a sphere, and a little ambiguous for an oblong organism.
In general, choosing a simple standard like the square of the characteristic length, $A = L^2$, will capture essential size effects as long as it is used consistently.

We also specify a **characteristic speed**, ***U***, which in this case is clearly the sinking rate, as indicated by the blue arrow in [](#sph1).

## Fluid characteristics
The drag on a moving organism depends, of course, on the characteristics of the fluid in which it is immersed.
The key fluid properties that affect drag are density and viscosity.
You can open worksheet to calculate these properties for freshwater, saltwater and air on Binder by clicking on

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/organismal-systems/python-fluidprop/HEAD?urlpath=%2Fdoc%2Ftree%2FFluidProp)

The variation of density and viscosity over a range of relevant temperatures for freshwater and saltwater with 35 ppt salinity are shown in [](#props)
```{figure} Images/Jumars_etal1993props.png
:label: props
:width: 80%
:align: center
:alt: Fluid properties of freshwater and saltwater

These plots show the variation of density, dynamic viscosity and kinematic viscosity across a range of temperatures relevant to aquatic organisms. It is a personal communication from Dr. Pete Jumars, and was calculated using formulas in  Jumars, P.A., J.W. Deming, P.S. Hill, L. Karp-Boss, P.L. Yager and W.B. Dade. 1993. Physical constraints on marine osmotrophy in an optimal foraging context. Mar. Microbial Food Webs 7:121-159.
```

### Density
The density of a fluid is simply the mass of the fluid for a given volume. 
In SI units, density is expressed in $\frac{kg}{m^3}$ (that is, kilograms per meter cubed).
Density is a function of temperature, the concentration of solutes such as salt, and pressure.
As an example, the bottom plot of [](#props) shows the variation in density of freshwater (lower line) and 35 ppt saltwater (upper line).
This plot show that density is a slowly decreasing function of temperature. [^1]
[^1]: The curve for freshwater ends at $0\degree C$; that is, at the freezing point of fresh water. The curve for salt water extends to lower temperatures, because its freezing point is lower.

### Viscosity
We intuitively understand the difference between a more viscous fluid like honey or molasses and a less viscous fluid like water.
If we imagine sliding two plates next to each other in a fluid, viscosity expresses how much force is required to keep them moving.
Intuitively, if the fluid is honey, it requires more force than if the fluid is water.
Keeping them moving in air requires even less force.
Therefore, honey is more viscous than water, and air is less viscous than either water or honey.

There is one slightly confusing aspect of viscosity, however: there are two ways in which visosity is commonly measured: dynamic viscosity and kinematic viscosity.

#### Dynamic viscosity
The **dynamic viscosity** relates to forces, such as the *force* required to keep plates sliding past each other.
Dynamic viscosity is often symbolized by the Greek letter $\mu$.
The SI units for dynamic viscosity are $\frac{N s}{m^2}$. 

To understand dynamic viscosity, let's think about two plates immersed in water, separated by a distance $H$.
One of these plates is stationary, and the other is sliding past it at velocity $U \frac{m}{s}$.
The water touching the stationary plate is stationary, and the water touching the moving plate moves with it at velocity $U$[^2].
The dynamic viscosity is the force acting on each unit area of the moving plate required to keep it moving, divided by the separation distance $H$ and the velocity $U$. [^3]

The velocity $U$ divided by the distance $H$ is a quantity called the **velocity gradient**. 
Therefore **the dynamic viscosity is the force acting on each unit area of the moving plate normalized by the velocity gradient.**

[^2]: This is because of the **no-slip condition**, which says that fluid molecules in contact with a surface are moved along with that surface.
[^3]: For "simple" fluids, like water or air, dynamic viscosity does not vary with $H$ or $U$. These are called *Newtonian fluids*. For some complex fluids relevant to Organismal Biology, such as blood or mucus, dynamic viscosity can differ for different values of $H$ and $U$. These are called *non-Newtonian fluids*.

#### Kinematic viscosity 
Kinematic viscosity is simply the dynamic viscosity divided by the density.
Kinematic viscosity is often symbolized by the Greek letter $\nu$.
The SI units for kinematic viscosity are $\frac{m^2}{s}$. 

In some ways, since we typically know both the density and the dynamic viscosity, it seems counter-intuitive to also define the kinematic viscosity. 
The reason it is defined is that dynamic viscosity frequently occurs in formulas divided by the density.
Furthermore, the kinematic viscosity has an intuitive interpretation: it characterizes the diffusion of momentum in the same way the diffusion coefficient characterizes the diffusion of a solute, and conductivity characterizes the diffusion of heat.
This analogy between diffusion of mass, heat and momentum is often helpful in gaining intuition and in quantitative analysis about organism function.

