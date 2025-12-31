# 🛼 Evolutionarily Stable States for diatoms in mixed layers: Overview
Identifying and quantifying the constellation of ecological mechanisms that determine the diversity and abundance of species in ecosystems is an on-going challenge.
In aquatic ecosystems, this challenge was termed by G. E. Hutchinson the [Paradox of the Plankton](wiki:Paradox_of_the_plankton) &ndash; the idea that competitive exclusion should lead to a low-diversity community with only one "best" competitor for each of the relatively few limiting resources.
Most communities are much more diverse than this logic would suggest.

One useful tool for understanding how diversity in communities might be promoted or suppressed is the idea of an [Evolutionarily Stable State](./EvolutionarilyStableStates.md), or ESS.
The ESS concept applies to a community of "variants", that could be different species or different strains of a single species.
An ESS is a population of one or more of these variants that, once established, can exclude all other variants.

[Litchman *et al.* (2009)](https://www.pnas.org/doi/epdf/10.1073/pnas.0810891106) developed an ESS analysis of diatom size distributions in [mixed layers](./MixedLayers.md). 
Key aspects of their model were:
- the allometries of growth rate, nutrient uptake rate and nutrient storage across small, middle-sized and large diatoms
- fluctuating nutrient concentrations, including decreases due to nutrient consumption by diatoms and increases due to episodic mixing with nutrient-rich deep water.

Litchman *et al.* sought to understand why diatom size distributions are larger in marine habitats than in freshwater habitats.
They hypothesized that differences between typical marine mixed layers layers and typical freshwater mixed layers underlie the differences in diatom communities. 
They further hypothesized that the key functional traits affected by the marine *vs.* freshwater mixed layer characteristics are the allometries of growth- and nutrient-related traits.


> - Does Evolutionarily Stable States, as inferred from Litchman *et al.*'s model, correspond to relatively large diatom size distributions in marine environments?
> - Do long-term competitive outcomes from initially mixed populations match ESS outcomes?
> - Do diatom communities in mixed layers approach Evolutionarily Stable States or long-term competitive outcomes quickly enough to be observed in nature?



Activities frame with linkages orgs w higher lower levels 


For comparability, we will use a standard set of diatom sizes for the basic model experiments (feel free to explore additional sizes if you want to):
\[ s=[2.5, 3.55, 5.0, 6.25, 7.5, 8.75, 10.0, 11.25] \] and on four mixing intervals, \[ T=[3,14,35,40] \] 
For these parameter combinations:


For 3 different mixing intervals, run simulation to find most successful. That is the candidate ESS variant.


Restart with only that variant, then seed with all and restart the simulation to see if any other variants can invade.



 \textbf{Evolutionary stable strategies:} A key idea in evolutionary analysis is the Evolutionary Stable Strategy (a.k.a. Evolutionar\underline{ily} Stable Strategy), or \textit{ESS}. An \textit{ESS} among a range of variants (in this case, diatoms of different sizes), is a variant that once established cannot be invaded by any other variant. For example, suppose a population of variant $s_1$ is established in the mixed layer. Variant $s_1$ is an \textit{ESS} if an initially small population of any other size variant $s_2$ would decrease (due to competition from $s_1$ diatoms). If at least one variant $s_2$ can increase from an initially small population, then $s_1$ is not an \textit{ESS}.

There may or may not be an \textit{ESS} in any particular trait-based model. In some cases, no single variant is an \textit{ESS} but a combination of two variants might jointly form an \textit{ESS}. That is, $s_1$ and $s_2$ form a joint \textit{ESS} if established coexisting populations of $s_1$ and $s_2$ variants can exclude any distinct $s_3$ variant (more preciesely, if an initially small population of $s_3$ variants decreases over time). 

To investigate competition, coexistence and \textit{ESS}'s across a range of diatom sizes, we will look at dynamics when multiple variants are present simultaneously. \textbf{Set the Number of Phytoplankton Size Classes at the top of the worksheet to 8 (remember to re-execute the evaluation group!).} The worksheet will create a default range of variants in $s$. Examine the outcome of 8-way competition for each of the focal mixing intervals $T$. What sized diatoms appear to be the best competitors under different mixing intervals? Is there an indication of $ESS$ diatom sizes under the assumed fluctuating resources and allometric uptake and storage relationships? Are variants that maximize biomass the same as variants that form \textit{ESS}'s (and if not, which would you expect to see in the plankton)? 


