# 📖️ Transport of organisms by currents and turbulence

Most environmental fluids &ndash; masses of air in weather systems, or the water in lakes, rivers, estuaries, and the open ocean &ndash; are moving at velocities that can vary from almost undetectable to extremely rapid.
We experience these as winds, river flows, tidal fluctuations and large scale ocean currents, among other ways.
Here, we begin to consider the effects of these environmental flows on the movement and distribution of organisms.

## Examples of transport in environmental flows
To get a concrete sense of the relevant phenomena, let's begin with a couple examples:

### Reproductive biology
Most benthic marine invertebrates are [free spawning](wiki:Spawning), meaning that they release their gametes into the water.
Sperm must encounter eggs for [fertilization](wiki:Fertilisation) to happen, but this is more challenging than it might seem.
That's because the surrounding water is almost always moving, due to waves, currents and tides.
Movement of the water into which gametes are released means that in a very short time &ndash; possibly within a few seconds &ndash; these gametes have been moved far from the adults that released them.
Though sperm are motile, their swimming abilities do not enable them to find and fertilize eggs that have been transported over long distances.

This has important consequences for the life histories of many species.
Marine invertebrates typically accumulate metabolic resources to produce gametes for months or even years before spawning. 
Once spawning begins, however, it's essential that multiple individuals precisely synchronize the timing of spawning. 
If an individual is early or late, its eggs will not encounter sperm to fertilize it, or its sperm will not encounter eggs to fertilize.
This risk of reproductive failure leads to behavioral strategies such as formation of large colonies or reproductive aggregations; use of environmental cues such as moon phases; and chemical communication among reproductive adults.

Given synchronized spawning, successful reproduction then depends on maximizing encounters of eggs with approriate concentrations of sperm, sufficient to make fertilization successful but not so dense as to make [polyspermy](wiki:Polyspermy) likely.
The encounter rate of eggs with sperm &ndash; and hence, reproductive success &ndash; is determined in large part by how fast these gametes sink, rise or swim, along with the rates at which they are transported, mixed and diluted by environmental flows.

### Agriculture
Suppose a rice farmer uses a crop-dusting airplane to apply pesticide to a rice paddy under no-wind conditions. 
The crop-duster has nozzles that emit droplets of known size. 
If we know the density of the pesticide mixture, we can calculate the sinking velocity of the liquid pesticide droplets using the calculators in [this worksheet](./rs1.ipynb).
If we know the height at which pesticide particles were released, we can use the sinking rate to estimate how long it takes pesticide particles to arrive at ground level.

Under no-wind conditions, a long descent time means only a delay in arrival at the rice paddy. 
However, suppose rather than no-wind conditions there is a moderate breeze. 
In this scenario, as particles sink vertically they are carried horizontally from the release point by the wind. 
If you have walked downwind of a sprinkler or fountain in a stiff wind you are familiar with this phenomenon.

In the windy scenario, sinking time has a consequence that is potentially much more important than a delayed arrival time at the paddy: a long delay and strong wind might mean the pesticide arrives at ground level far downwind.
It may even miss the rice paddy entirely, landing instead on a different area which may be occupied by people, grazed by livestock or have other sensitive uses.

The ways in which sprayed pesticides, pollen, dust and a great many other anthropogenic and natural particles are transported and ultimately deposited are determined by their settlement rates, and by the environmental flows that transport and spread them.

## Transport by advection
Transport of organisms and other immersed objects or substances by moving fluid is called [advection](wiki:Advection)[^adv].
Environmental flows often *advect* organisms, particles and solutes much faster and in different directions than they would otherwise move.
For example, many organisms move vertically &ndash; they sink or rise under the influence of gravity and buoyancy.
In contrast, the principal direction of wind, currents and many other environmental flows is often horizontal.
In such cases, advection causes movement in directions those organisms would not otherwise move.

[^adv]: The phenomenon of population, mass, momentum, energy or any other *conserved quantity* being carried by moving fluid is called *advection* or *convection*. 
	Different fields in the natural sciences and engineering use these terms slightly differently, but in all cases they imply that moving fluid transports a conserved quantity.

Even when an organism has some horizontal movement, horizontal advective transport can be orders of magnitude faster than swimming movements. 
For example, in many aquatic environments, characteristics such as light, temperature and nutrient availability change over a few meters in the vertical direction but are relatively constant over many kilometers in the horizontal direction.
The slow swimming of organisms such as plankton is often considered fast enough to regulate their access to light, warmth and nutrients by moving up or down in the water column.
However, horizontal swimming at the same rate can have negligble effects, because their environment varies so slowly in the horizontal direction. 
In these cases, only long-range advection by currents can move plankton sufficiently in the horizontal direction to significantly affect ambient conditions.

## Mixing by turbulence
Most environmental flows also have some level of [turbulence](wiki:Turbulence).
If you have been aboard an airplane flying through turbulent air, you have felt first-hand that turbulence is composed of [eddies](wiki:Eddy_(fluid_dynamics)) and other small-scale but energetic fluctuations of fluid velocity. 
Turbulence is also a very effective mechanism for mixing; this is frequently called [turbulent diffusion](wiki:Turbulent_diffusion), because it in some ways mimics the effects of molecular diffusion but is much faster. 

When you stir your coffee to mix cream or sugar, you can see how effective turbulent diffusion is. 
Sometime, when you have a lot of time on your hands, add cream or sugar to coffee and wait for the mixing to occur without stirring. 
This will give you a sense for how much turbulence has sped up the mixing process[^mix].
Turbulent diffusion has similar effects in environmental flows, greatly enhancing the spread and mixing of organisms and other particles.

[^mix]: Even this is an overestimate of mixing without turbulence, because temperature differences as the coffee cools cause some mixing currents!

## Distributions of organisms in environmental flows
We now have three components of velocity to consider when thinking quantitatively about the movement of particles such as microorganisms, pollen or dust immersed in environmental flows:
1. The particles' own velocity relative to the fluid in which they are immersed, such as sinking or rising under the influence of gravity, buoyancy and drag forces.
2. Advection by the directional velocity of the fluid, such as wind or current, often primarily in horizonatal directions.
3. Turbulent eddies, that cause small-scale random movements of individual particles while mixing and spreading a population of particles.

To understand the combined effects of vertical movements with advection and turbulence, it's important to keep in mind the different effects on *population distributions* of advection by currents *vs.* mixing by turbulence. 
- Starting with a group of organisms or a blob of solute, *advection* (with no turbulence) moves the overall average position (in engineering jargon, the center of mass) of that group or blob, such that it  moves with the current over time. 
- Starting with a group of organisms or a blob of solute, *turbulent diffusion* (with no advection) spreads out the group or blob in a similar way to molecular diffusion or random swimming, but much faster except at very small length scales (much smaller than a millimeter).

Keeping in mind that advection and turbulence are distinct forms of transport by fluids, we can anticipate environmental situations in which we have high adection and low turbulence; low advection and high turbulence, high advection and high turbulence, etc.
The [next worksheet](RS2exec.ipynb) gives us tools for quantitatively assessing the consequences of these different scenarios for different types of particles. 

