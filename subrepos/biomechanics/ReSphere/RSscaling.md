#  💡 Scaling of fluid forces: the Reynolds Number
A deep insight by fluid mechanicists George Stokes and Osborne Reynolds in the mid-19th century is that *the relative magnitude of the inertial and viscous forces* tells us a lot about a flow. 
That led to the definition of the [Reynolds number](wiki:Reynolds_number), abbreviated as $\mathcal{Re}$:
```{math}
:label: eqnRe1
\mathcal{Re} = \frac{\mathrm{momentum~forces}}{\mathrm{viscous~forces}}
```
Substituting our order-of-magnitude [estimates of drag forces](./RScharact2.md) for these forces, 
```{math}
:label: eqnRe2
\mathcal{Re} = \frac{\rho U^2 L^2}{\mu L U}, 
```
or, after simplification,
```{math}
:label: eqnRe3
\mathcal{Re} = \frac{\rho U L}{\mu}.
```
In words: **The Reynolds number, Equation [](#eqnRe3), states the relative strengths of momentum effects and viscous forces, as inferred from the inherent effects of size, velocity and fluid characteristics.**

Using the Reynolds number, we can list these inherent effects:
- Larger size, $L$, increases the relative strength of momentum effects compared to viscous forces; smaller size increases the relative strength of viscous forces
- Faster velocity, $U$, increases the relative strength of momentum effects compared to viscous forces; slower velocity increases the relative strength of viscous forces
- Higher fluid density, $\rho$, increases the relative strength of momentum effects compared to viscous forces; lower density increases the relative strength of viscous forces
- Higher fluid viscosity, $\mu$, decreases the relative strength of momentum effects compared to viscous forces; lower viscisity decreases the relative strength of viscous forces

It's important to understand that these statements do not imply that increasing $L$ results in smaller viscous forces. 
Instead, the statements are saying that, as $L$ gets larger, momentum effects and viscous forces both increase, but momentum effects increase *faster* than viscous forces.
That can be seen from Equation [](#eqnRe2), which shows that momentum effects increase in proportion with $L^2$, while viscous forces increase in proportion with $L$.


## Scale models and dynamic similarity
The Reynolds number gives us an important insight because it tells us that, for any two similarly shaped organisms moving in any Newtonian fluids, the relative magnitudes of inertial and viscous forces are equal if they have equal $\mathcal{Re}$. 
That is, any two organisms that are similar in shape but that may differ in size, speed and fluid type, are [dynamically similar](wiki:Similiture).
Dynamic similarity means those organisms (or replicas of organisms) are [scale models](wiki:Scale_model) of each other: measuring the forces, flows and other features of one is equivalent, after appropriate scaling, to measuring those features on the other.

### An application of dynamic similarity
As an example, let's consider a tiny organism: a bacterium swimming in water.
It is very difficult to measure the fluid forces on a bacterium.
Suppose, instead, that we create a tennis ball-sized replica of the bacterium. 
Instead of water, we immerse the replica in Karo Syrup, which has a much larger kinematic viscosity, $\nu$.
Since $\nu$ is so much larger, we can make $L$ much larger and (with an appropriate choice of velocity, $U$) we can still make the replica's Reynolds number match the bacterium's. 
We can take then take advantage  of the replicas large size to measure fluid forces, and rescale them to correspond to forces on the bacterium.

## Reynolds number as an analytical tool
The mathematical formulas describing flow of fluids around organisms are called the [Navier-Stokes equations](wiki:Navier–Stokes_equations).
These equations calculate the combined effects of momentum, viscosity and pressure on each part of a moving fluid.
Solving the Navier-Stokes equations is often technically difficult, computationally expensive or simply not possible.
The Reynolds number provides a route to simplifying the Navier-Stokes equations in many biological applications, to obtain approximations that are usefully accurate and much easier to implement.

### The low Reynolds number flow regime: $\mathcal{Re} \ll 1$
A microorganism swimming in water, or a spore or pollen grain drifting in a breeze, is very small and typically moves very slowly.
That is, its characteristic length, $L$, and characteristic velocity, $U$, are both small.
From Equation [](#eqnRe3), we know this implies its Reynolds number is very small. In mathematical terms:
```{math}
:label: eqnRe5
\mathcal{Re} \ll 1
```
We can interpret Equation [](#eqnRe5) to say that momentum effects are much smaller than viscous effects.
If we look for an intuitive comparison for $\mathcal{Re} \ll 1$, we can imagine a human (with much larger $L$ and $U$) swimming in a fluid with very large $\mu$, such as honey or tar.

Equation [](#eqnRe5) suggests that we can approximate the Navier-Stokes equations by neglecting momentum effects, and for very small slow organisms we won't lose much accuracy.
It turns out that this simplification results in fluid flow equations  that are much more tractable than the Navier-Stokes equations.
These are called the Stokes equations, and the flow they describe with $\mathcal{Re} \ll 1$ is called [Stokes flow](wiki:Stokes_flow).
Almost all fluid dynamical analysis of microorganisms is done using the Stokes equations.
The model of swimming larvae later in this unit is an example.

As a reminder, the conclusion that flows around small, slow organisms is dominated by viscous forces arose from a very general consideration of the inherent effects of size and velocity.
They are not changed by specific morphological or behavioral adaptations.
  
### The high Reynolds number flow regime: $\mathcal{Re} \gg 1$
At the other end of the spectrum, high Reynolds number flows are ones in which momentum effects are much larger than viscous forces.
```{math}
:label: eqnRe6
\mathcal{Re} \gg 1
```
There are some complications, because adjacent to a surface viscous forces can have large effects even in high Reynolds number flows.
High Reynolds number flows are also subject to [turbulence](wiki:Turbulence).
Nonetheless, neglecting viscous terms in the Navier-Stokes equations results in simplified equations that are much more tractable.
These equations are very useful approximations that have been widely used not only in biomechanical analysis of large, fast organisms but also in engineering. 


## Reversible and irreversible flows
Viscous forces are directly proportional to the velocity gradient. 
In mathematical terms, they are *linear*.
This results in an interesting and important feature of flows that are dominated by viscous forces &ndash; that is, for flows in which $\mathcal{Re} \ll 1$: they are *reversible*.

If we think about the sliding plates in our [estimates of drag forces](./RScharact.md), it seems intuitive that moving the plate at a speed $v$ to the left would produce an equal and opposite fluid motion compared to moving it to the right.
Furthermore, moving it at half the speed would produce half as much force, but if it acts for twice as long the final positions of the plate and the fluid will be the same.

This is what is meant by reversibility of low  $\mathcal{Re}$ flow.
A classic video by G. I. Taylor shows a [demonstration of reversible flow](https://www.youtube.com/watch?v=QcBpDVzBPMk).
In this video, dye is placed in a viscous fluid between rotating cylinders.
The cyclinders are rotated until the dye is greatly stretched; then reversed back into their original positions to restore the originam dye blob. 

Reversibility has important consequences for microorganism swimming.
In particular, waving a fin back and forth is a  propulsive motion that works well for many fish and other high Reynolds number swimmers.
However, at low Reynolds number, this reciprocating motion would have no net propulsive effect.
Instead, microorganisms must propel themselves with motions that are non-reversible.
For example, the [bacterial flagellum](wiki:Flagellum#Bacterial_flagella) is a helical filament that rotates in a propeller-like way in only one direction.

## Final points
A couple additional points to note:

$\mathcal{Re}$ is a [non-dimensional number](wiki:Dimensionless_quantity) &ndash; because the denominator and the numerator both have units of force, the result has no units.
    So, whichever system of units you use to calculate $\mathcal{Re}$, as long as you use it consistently you will get the same answer.
	
The Reynolds number also be written using the kinematic viscosity, 
```{math}
:label: eqnRe4
\mathcal{Re} = \frac{U L}{\nu}.
```
This is one of many instances that kinematic viscosity, $\nu$, appears in biomechanics and fluid dynamics applications, which is why it is often tabulated in addition to dynamic viscosity, $\mu$.
