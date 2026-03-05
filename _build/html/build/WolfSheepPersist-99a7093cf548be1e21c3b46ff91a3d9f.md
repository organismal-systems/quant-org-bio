# 📖 Habitat size and persistence: Insights from scaling analysis



This Unit develops insights into spatial population dynamics using scaling analysis &ndash; in mathematical jargon, dimensional analysis.
The basic ideas underlying scaling analysis were described in sections of the Introduction discussing [allometry](../../../content/overview/allometry.md) and [non-dimensional numbers](../../../content/overview/nondim-numbers.md).
Applications to understanding movement of organsims in fluids were presented in the [Biomechanics section](../../../content/biomechanics/README.md).
Here, we use similar analytical approaches to get a "big picture" understanding of how the demography of a population is affected by the size of its habitat.

Specifically, we address the question:
> - How do the movement behaviors and reproductive characteristics of a population interact with habitat structure to determine whether it will persist or go extinct?

The goal of the analysis is to obtain order of magnitude estimates of thresholds for persistence.
Functionally, what size habitat is "big enough" and what size is "too small"?

We will look at two very different models: 
- the so-called KISS model[^kiss], a [Partial Differential Equation (PDE)](../../../content/appendix/MathSum/pdes.md) model that is deterministic and continuous in time, space and population
- an [agent-based model](wiki:Agent-based_model) that is stochastic and discrete in time, space and popultion

Both of these models are highly simplified compared to real-world populations.
Nonetheless, they illustrate how population dynamics are affected by scaling rules that are common not only to these very different models but also to organisms in nature.

The first part of this Unit uses scaling analysis to derive a "back-of-the-envelope" estimate for the minimum habitat size that can support a viable population in the KISS model.
Because the KISS model can be solved analytically, its exact solution is compared to the generic predictions from scaling analysis.
For those interested in understanding how models of this type are solved, a brief derivation of the solution is shown [here](./KISSsoln.md).

The second part of the Unit is an Activity, in which you will analyze demography from an agent-based model implemented in [Mesa](https://mesa.readthedocs.io/latest/) as if it were a real-world population.
Like the analysis of a small population in the wild, you will have to use some judgement to estimate "characteristic" values for some parameters from simulations in small habitats.
From those parameters, you will estimate the habitat size necessary to maintain stable populations.
Unlike the real world, you can easily test you predictions by running simulations on larger domains.

[^kiss]: This model is due to Kierstead, Slobodkin and Skellam:  
Kierstead, H.; Slobodkin, L.B. The Size of Water Masses Containing Plankton Bloom. J. Mar. Res. 1953, 12, 141–147.  
Skellam, J.G. Random Dispersal in theoretical biology. Bull. Math. Biol. 1991, 53, 135–165; Reprinted from Biometrika 1951, 38,
196–218.
