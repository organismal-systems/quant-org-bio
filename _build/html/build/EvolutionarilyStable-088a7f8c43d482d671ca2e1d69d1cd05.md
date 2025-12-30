# 💡️ Evolutionarily Stable States: Predicting the outcomes of natural selection

An [Evolutionarily Stable State](wiki:Evolutionarily_stable_state), commonly abbreviated as an **ESS**, is description of the outcome of competition among a set of variants with different traits.
ESS's are related to the idea of [competitive exclusion](wiki:Competitive_exclusion_principle), the hypothesis that if two species, or variants of one species compete for the same limiting resource, one will be a better competitor and the other will die off[^better].

An ESS describes the scenario in which, if one variant (or combination of variants) is initially dominant, no other variants introduced in small numbers can grow.
That is, once established, an initial ESS population of variants can exclude "invasion" by a small number of individuals from any other variant.

For example, suppose a set of diatoms varying in size are competing for a limiting nutrient that is supplied at a constant rate.
If the initial variant is a middle-sized diatom, it will draw the nutrients to the lowest concentration that allows it to grow[^litch].
If a few larger cells are then introduced, those cells cannot grow because their nutrient uptake is insufficient at the nutrient level set by the established middle-sized cells.

[^litch]: This expectation is based on the allometric analysis in [Litchman *et al.* (2009)](https://www.pnas.org/doi/epdf/10.1073/pnas.0810891106), and conforms to conventional wisdom about the surface area:volume ratio advantages of smaller cells over larger cells.

However, if a few small cells are introduced, those cells can grow at the nutrient level established by the middle-sized cells.
This is because, typically, smaller diatom can grow at lower nutrient concentrations than middle-sized or large diatoms.
As they grow, the small cells drive the nutrient levels lower, until the middle-sized cells cannot grow and eventually die off. 

In this case, a population of middle-sized cells *is not* an ESS, because a population of middle-sized cells can be invaded by smaller cells.

In contrast, if the initial variant population is small, then those cells drive the nutrient level so low that neither middle-size nor large cells can invade.
In this case, the initial population of small cells *is* an ESS.

## ESS variations
Several variations exist in the idea of an Evolutionarily Stable State.
In some interpretations, the dominant variant in an ESS must resist invasion only by slightly different variants.
This interpretation is based on the idea that viable mutations lead to gradual changes in characteristics.

In other interpretations, the dominant variant in an ESS must resist invasion by *all* other variants.
This interpretation is based on the idea that viable mutations can cause large changes, or that evolution can follow different paths in separated environments that are subsequently connected.
Under this interpretation, more complex scenarios are possible.
For example, two or more very different variants can together form an ESS, excluding all other variants.

## Real-world complications
The simple ESS scenario above has a clear and univesal implication: small diatoms should always exclude middle-sized and large diatoms.
This trend is indeed frequently observed in aquatic environments.
However, middle-sized or large diatoms can persist and even dominate some aquatic habitats.
How can this be if small diatoms are better competitors?

One of the useful outcomes of simple models is that they provide clear expectations, and highlight deviations from these expectations that need to be explained.
Many potentially relevant factors were omitted from the simple ESS scenario above, that may provide advantages to middle-sized and large diatoms.
These include:
- variable environments with fluctuating nutrient concentrations (such that storage or ability to survive low-growth intervals are important) 
- exceptions to the rule about poor growth at low nutrient concentrations
- selective grazing or attacks by pathogens on small diatoms
- competition for multiple limiting nutrients, light or other requirements
- behavioral factors like depth regulation, which may be more effective for larger diatoms

The expectation that small diatoms should dominate is a motivation to investigate these and other factors that may contribute to the size diversity that actually exists in diatoms.

## Evolutionarily Stable States and competition in mixed populations
ESS populations are usually, but not always, the same as the outcome of competition within an initially mixed population. 
Differences can arise due to the key assumption that *the initially dominant population creates the conditions into which other variants must invade*.
If the ESS variants have not had exclusive use of the environment to create the conditions into other variants must invade, different outcomes are possible.

Scenarios are also possible in which multiple ESS's exist.
For example variant A, when established, can exclude all other variants (including variant B).
However, variant B, when established, can also exclude all other variants (including variant A).

[^better]: Note that "better" in this context is defined as the successful competitor. For example, it could be that species A has faster uptake of high-concentration nutrients but species B has faster uptake of low-concentratin nutrients. If the nutrient is limiting, it will be driven down to low concentrations, so species B is "better" in competitive terms, even though under other circumstances species A might have higher growth. For example, under predation, both populations might be reduced so that nutrients are not limiting, and species B might predominate.

