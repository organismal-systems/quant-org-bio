# 🛼 Testing hypothetical performance standards: Metrics and rationale
We now consider strategies for assessing the hypothesis that natural selection effectively imposes "standards" for swimming performance in early-stage marine invertebrate larvae.
The tool at hand &ndash; a low Reynolds number simulation of swimming by idealized larval shapes &ndash; lends itself to an exploration of this hypothesis with a systematic mapping of swimming metrics across a range of morphologies.
A map of this type makes clear which sets of morphologies meet a hypothetical standard, and which fall short.

Assessing performance using a model of this sort is challenging primarily because:
- Numerous parameters are needed to specify the external and internal morphologies, material properties, initial conditions, *etc*.
- Ambient flow conditions are highly variable, and it is not clear which conditions are most relevant to selection on larval forms.
- It is not clear which metrics best reflect aspects of swimming performance most important to larval success, especially if testing is done in simplified flow conditions.

Here, we mitigate these problems by using organism-based parameters, further constrained by assumptions that [minimize the number of variables](./ChimeraTest.md) while still giving scope to variability that summarizes key trends, and by removing flow parameters by devising swimming performance metrics that can be measured in still water.
 
## Rationale: Testing a hypothetical performance standard for upwards swimming
A hypothetical performance standard for upwards swimming lends itself to a simple assessment of steady state velocity in simulations of larval swimming.
Specifically, starting from an arbitrary orientation, a freely swimming larva will over time assume its stable orientation after a transient re-orientation period.
For the range of morphologies considered here, the stable orientation is associated with the maximum upwards swimming rate.
That is, any deviation from that orientation will lead to a decrease in upwards swimming, as some or all of the swimming is directed in a horizontal direction.
Simulated still-water upwards swimming velocity in the stable orientation is a convincing metric of limits to swimming capacity associated with larval size and shape, as well as being directly analogous to most observations of larval swimming in experiments.

## Rationale: Testing a hypothetical performance standard for stability
Early stage larvae must be capable of maintaining vertical orientation in the shear and turbulence characteristic of the habitats in which they undergo development.

The key rationale is testing whether a larva coupld sustain upswimming in turbulent eddies, without simulating the eddies.

### Disturbances to larval swimming due to turbulence
For example, an important factor in larval swimming is the type and intensity of disturbances to position and orientation due to movement of the ambient water, especially due to [turbulence](wiki:Turbulence).
Turbulence is chaotic flow that includes energetic [eddies and vortices](wiki:Vortex) and [shear](wiki:Simple_shear) at small scales.
Turbulence arises from [instabilities] in fast-flowing large-scale features such as currents, in which initially small flow disturbances are amplified and become more energetic. 
These instabilities are themselves unstable, so that distubances in the initial instabilities provoke further instabilities at smaller scales. 
This is referred to as the [energy cascade](wiki:Energy_cascade), and it causes some of the energy from large scale flows to be diverted to smaller and smaller eddies, until at very small scales that energy is absorbed by viscosity and converted to heat.

How small are "very small scales"? 
That depends on the strength of the 


In the [larval swimming model](./ChimeraSwim.ipynb), water motion 


More specifically
assumes 
A simple way of conceptualizing variations in early-stage larval morphologies is to survey across a range of key variables, with other parameters held constant.



Parameters to vary:


restrict attention to a subset of geometries and flow conditions:
- Larval morphologies: We will consider a set of [chimeras](./ChimeraSwim.ipynb) created by 




biomechanical requirements 




hypotheses/questions:

> Larval morphologies must provide passive stability in excess of the torques imposed on them by turbulence and shear.

> Is producing fewer large eggs that are more likely to survive, or more small eggs despite their being more susceptible to mortality, a more sucessful strategy?


> How do embryos and other early-stage larvae, accomplish similar swimming performance with almost no apparently specialized swimming morphological features?


> What are the constraints on larval size and shape resulting from the need to swim?

> What are the constraints on swimming imposed by the need to satisfy other requirements and limitations in larval development?

> How do each of these interact with environmental variations, and with the different life histories adopted by different taxa?
