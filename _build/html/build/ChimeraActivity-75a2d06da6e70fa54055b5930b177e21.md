# 🛼 Morphologies that meet the challenges of early larval swimming
The [preceding discussion](./SizeSwim.md) outlined the hypothesis that, to survive through development and successfully metamorphose into juveniles, many or most early stage marine invertebrate larvae must satisfy functional requirements for swimming performance.
Specifically, two hypothetical "performance standards" were proposed:
- **Swimming speed**
  
  The upward swimming speed of early stage larvae in still water must meet or exceed a minimum speed, $V_{min}$.
  The observations and analysis of [](doi:10.1093/icb/icq090) suggested that the minimum speed performance requirement is in the vicinity of $300-400 \frac{\mu m}{s}$.

- **Stability**
  
  Passive stability must be sufficient to maintain vertical orientation enabling upwards swimming under conditions of turbulence and shear prevailing in the habitat in which development occurs.

The benefits and costs of swimming are complex, poorly understood and probably variable across taxa, over time and within different environments.
This makes it difficult to critically assess the life history tradeoffs implied by the hypothesis.

However, with a model, it is possible to quantify the biomechanical consequences of alternative early-stage larval morphologies, and to explore what (if any) constraints hypothetical swimming standards would impose on variations in size and shape.
A systematic exploration of parameter space could delineate larval morphologies that meet or fail to meet the standards.
A testable prediction would then be that extant larval morphologies fall mostly or entirely within the hypothesized constraints.

This Activity uses a biomechanical model to ask, across a range of larval sizes:
> - For a given amount of larval biomass, how are morphological variations constrained by hypothetical swimming requirements?  
> - Do swimming performance requirements for swimming speed and stability impose similar constraints, or are they different or even contradictory?

The goal of the Activity is to produce plots of larval swimming performance across systematic series of variations in morphological parameters, which can be assessed against hypothesized performance standards to specify implied morphological constraints. 
A further analysis (*e.g.* based on data from [](doi:10.1093/icb/icq090) and other sources) could then survey extant larval morphologies to assess whether there is evidence of selection to meet these constraints.

## Model characteristics
The [model](./ChimeraSwim.ipynb) adopts a number of simplifications to make computations tractable and facilitate exploration of morphological parameters:
- The model assumes [low Reynolds number flow](../ReSphere/RSscaling.md), in which inertial effects are negligible and fluid forces are determined by the Stokes equations.
- The model implements early-stage larvae with external shapes constructed as [chimeras](./ChimeraDesign.ipynb) of two semi-spheroids, joined at a common equator.
- The model implements internal structure in the form of an inclusion, also constructed as a chimera of two semi-spheroids.
- The model assumes that the embryonic tissue fills the volume inside the external surface but external to the inclusion; the inclusion contains a different material with a different excess density.
- The model approximates ciiary propulsion using a so-called "envelope model", in which a ciliated surface is approximated by a smooth, continuous surface that moves tangentially at roughly the velocity of cilia tips during the power stroke.
- The model approximates the localized effects of turbulence and other water motion with constant levels of shear or rotation.
- The model is executed in two stages:  
  - **Specification of larval morphology**  
      There are two alternative methods to specify a larval morphology:
    
	- The Jupyter notebook [](./ChimeraDesign.ipynb) provides an interface for approximating a general early-stage larval with a chimera of two semi-spheroids, specified with geometrical parameters such as diameter, length, *etc*.. 
	- The Jupyter notebook [](./ChimeraOrg.ipynb) provides an interface for approximating a subset of early-stage larval morphologies, specified with organism-based parameters such as tissue volume, aspect ratio, excess density, *etc*.. 
	
	Body forces and fluid dynamical characteristics are calculated and saved in a "morphology" file, in these notebooks.
  - **Simulation of larval swimming**
    - Movement of the larva from an initial position and orientation is simulated within a specified ambient flow, in the Jupyter notebook [](ChimeraSwim.ipynb).

