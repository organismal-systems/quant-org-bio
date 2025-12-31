# 📖️ Estimating drag forces, Part 2
With the set of organismal and fluid characteristics developed in [Part 1](./RScharact.md), we can now begin to assess the generic effects of size and speed on drag forces acting on organisms.
As a reminder, we are deliberately avoiding references to specific morphologies, behaviors or fluids.
Instead, we are looking for inherent effects of size, velocity and fluid characteristics that generalize across these specifics.
Because we omit specifics, we are aiming here for **order of magnitude estimates**.
The intent is, knowing the order of magnitude of the inherent generic effects, we will then be able to focus in detail about possible "tweaks" due to adaptations in morphology, behavior *etc*.

As our case study, we will think about the organism from [Part 1](./RScharact.md) that is sinking at a steady speed in stationary fluid.
We will consider two types of forces, drawn from the previous pages:
- *Forces due to momentum*

	Momentum forces on an organism moving at a constant velocity stem from the wake momentum, which is increasing as the length of the wake lengthens over time and requires force to maintain.

- *Forces due to viscosity*

    Viscous forces on an organism moving in a fluid stem from the fluid's viscosity, $\mu$, acting on the organism's surface in proportion to the velocity gradient in flow from the organism's surface (where fluid moves with the organism) to the "free stream" far from the organism, where fluid is undisturbed.

The key question we will address is, "*How do we expect forces due to viscosity and wake momentum to increase with organism size and speed?*"
	
## Forces due to wake momentum
[](sph2) is a cartoon of the wake behind the sinking organism.
```{figure} sphere2.png
:label: sph2
:width: 60%
:align: center
:alt: An idealized wake behind a sinking sphere.

Idealized wake behind a sinking particle. The orange lines indicate the wake. For our estimate, we assume the cross section of the wake is equal to $A$, the projected area of the particle. We also assume water within the wake has velocity $U$, and that water outside the wake has negligible velocity.

```
Our estimate of forces on an organism due to wake momentum is based on:
1. The organism's "characteristic" parameters: size, $L$; area, $A = L^2$; and velocity, $U$.
2. The fluid's density, $\rho$.
3. Newton's 2nd Law, which tells us that the force arising from wake momentum, $F_{mom}$, equals

$$
	F_{mom} = \mathit{rate~of~increase~of~wake~momentum} 
$$	

4. The knowledge that the wake momentum is increasing because fluid mass "swept out" by the organism (approximately at rate $A \times U \times \rho$) is accelerated to the organism's velocity ($U$).

Putting these observations together, we can estimate the apparent drag force on the organism due to wake momentum as
$$
	F_{mom} = \rho L^2 U^2
$$	
In sum, $F_{mom}$ is an order of magnitude estimate of the wake momentum force on an organism, which expresses the inherent effects of size $L$, velocity $U$ and fluid density $\rho$, subject to "tweaks" from future consideration of effects from specific details such as the organism's shape.

	
## Forces due to viscosity
[](sph3) is a cartoon of the fluid motion to the side of the sinking organism.
The cartoon illustrates several features that are important to recognize before estimating the drag forces due to viscosity.
```{figure} sphere3.png
:label: sph3
:width: 60%
:align: center
:alt: A cartoon of the viscous boundary layer adjascent to a sinking sphere.

Idealized shear layer on a sinking particle. We assume that the velocity grades from $U$ on the particle's surface to close to zero over a distance approximately the size of the particle, $L$.

```
The orange curve represents a **velocity profile**, which is simply a plot of velocity as a function of distance from the organism's surface.
This velocity profile reflects the fact that, regardless of details about the organism or the fluid, the fluid's velocity at the surface equals the organim's velocity, and the velocity of undisturbed fluid far from the organism is zero.

The velocity profile also illustrates the *velocity gradient* (that is, the rate of change of velocity with distance from the surface).
In the cartoon, the velocity gradient is relatively steep near the organism and becomes more gradual further away, which is typical of profiles observed near objects moving in fluids.
The velocity gradient is important because, as we saw in [Part 1](./RScharact.md), the viscous force on the organism's surface is proportional to this gradient.

To estimate the viscous force, then, we need an estimate of the velocity gradient at the organism's surface.
As before, because we are deferring consideration of specifics like shape and behavior, we will settle for order of magnitude estimates of the velocity gradient and viscous force.
These details can be considered when we better understand the inherent effects of size, velocity and fluid properties.

Our estimate of forces on an organism due to viscosity is based on:
1. The organism's "characteristic" parameters: size, $L$; area, $A = L^2$; and velocity, $U$.
2. The fluid's dynamic viscosity, $\mu$.
3. The knowledge (stemming from the way dynamic viscosity is defined and measured) that the viscous force is equal to the velocity gradient adjacent to the organism's surface, multiplied by the dynamic viscosity and the area over which that viscosity acts.
4. The likelihood that the size of the organism, $L$, is usually a rough indicator of the distance over which it disturbs the surrounding fluid (illustrated by $L$ in [](#sph3) above the velocity profile.

From these facts we can estimate the drag force due to viscosity, $F_v$, as
$$
	F_{v} = \mathit{viscosity} \times \mathit{area} \times \mathit{velocity~gradient} 
$$	
In mathematical terms,
$$
	F_{v} = \mu L^2 \frac{U}{L} = \mu L U
$$	
where the area is estimated as $L^2$ and the velocity gradient is estimated as $\frac{U}{L}$.


