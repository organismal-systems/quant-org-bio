# 💡️ "Look-up tables" for drag forces on moving particles

A key benefit of the Reynolds number is that it dramatically shrinks the number of experimental observations or numerical computations we need to characterize particle movement in fluids.
That is because it enables us to make and interpret scale models.
If we observe or compute one example of drag forces on an organism moving in fluid, the Reynolds number tells us how to translate that result to any geometrically similar organism in any fluid, as long as it has the same Reynolds number.

As an example, let's consider the general problem of drag forces on spherical organisms moving through a variety of fluids (air, water of different salinities, blood, mucus, etc.).
As with many biomechanics models, assuming an organism is spherical applies to a few organisms exactly, but to a great many organsims approximately. 
Our goal is to create a [lookup table](wiki:Lookup_table) that tabulates the drag forces on these organisms, to understandhow fast they rise or sink, as biomechanical consequences of size, habitat etc. 

To cover relevant biological applications, we have at least four parameters to vary:
- organism *size*, $L$
- organism *velocity*, $U$
- fluid *viscosity* $\mu$ 
- fluid *density*, $\rho$

If we need 20 values of each parameter to fully characterize the parameter space for our lookup table, we need to make $20^4  = 160000$ observations.
Furthermore, some of these observations are difficult or impossible, such as measuring the forces on bacterium-sized organisms.

The Reynolds number rescues us from this difficult situation. 
We know that all geometrically similar organisms with the same $\mathcal{Re}$ are scale models of each other (that is, they are *dynamically similar*).
This means we need only make one observation for each value of $\mathcal{Re}$; from this observation, we can calculate all the specific instances of organisms, fluids etc. with the same Reynolds number.

For example, we can choose one convenient organism size ($L$), and a convenient fluid (with a given visosity, $\mu$, and density, $\rho$).
We can then measure drag forces across a range of velocity, $U$, giving us the complete range of $\mathcal{Re}$ we need to span the biologically interesting applications.
This gives us a lookup table that covers the whole range of organisms by measuring only 20 different values of $\mathcal{Re}$!

To use this concise approach, we need a formula for converting the drag forces on one organism to another organism that is dynamically similar.
That formula has been provided by engineers and fluid mechanicists, and is called the [Coefficient of Drag](wiki:Drag_coefficient)[^cd], $C_d$ (also called the ***Drag Coefficient***).
The formula for $C_d$ is
$$
C_d  = \frac{F}{\frac{1}{2} \rho L^2 U^2}
$$
The Coefficient of Drag has been measured or calculated for many shapes, as for example for [spheres](CdSphere.ipynb).

[^cd]: Also called the *Drag Coefficient*.
