# 📖️ Assessing past and future life histories of an anadromous fish, the Atlantic croaker
The life history of marine organisms is under evolutionary selection in ways that are often difficult to quantify and understand. 
An opportunity to advance our understanding arises when the evolutionary pressures change. 
That is, the evolutionary response to a changing selective factor can tell us which direction that factor drives life history, and how strongly relative to other factors.

We humans are providing ourselves with lots of opportunities to learn about life histories in this way. 
This is particularly true with respect to mortality rates. 
Mortality rates for pelagic species are usually very difficult to measure directly, and so their roles in life history evolution often remain somewhat speculative. 

However,  due to direct fishing pressure, and to indirect pressures such as by-catch and habitat degradation, humans have imposed major, and often quantifiable, increases in mortality rates in many species. 
It would be surprising if these species did not evolve to have different life histories under such dramatically changed conditions.


```{figure} https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Micropogonias_undulatus_RR_072120_0655_%2850142583921%29.jpg/960px-Micropogonias_undulatus_RR_072120_0655_%2850142583921%29.jpg
:label: acroaker
:alt: Wikipedia image of an Atlantic croaker
:width: 600px
:align: center

Wikipedia image of an Atlantic croaker. 
For additional information on this species see this [Texas Parks and Wildlife page](http://www.tpwd.state.tx.us/huntwild/wild/species/croaker))

Citation :*Micropogonias undulatus* RR 072120 0655 (50142583921).jpg, https://commons.wikimedia.org/w/index.php?title=File:Micropogonias_undulatus_RR_072120_0655_(50142583921).jpg&oldid=950950469 (last visited February 17, 2026). 
```

[](doi:10.1139/cjfas-57-10-2010)  presented  population dynamics analysis for a fish called the [Atlantic croaker](wiki:Atlantic_croaker), *Micropogonias undulatus* ( [](#acroaker)) .
At the time of the study, the croaker had been experiencing significant mortality as [by-catch](wiki:Bycatch) from shrimp trawling. 
Its population was declining (I haven't followed up with the most recent catch data, but there are published suggestions ocean warming is contributing to increases in croaker stocks). 
[](doi:10.1139/cjfas-57-10-2010) sought to establish whether by-catch mortality was a significant factor in causing declining populations of Atlantic croakers.

According to the analysis of demographic parameters in  [Diamond *et al*. (1999)](https://academic.oup.com/tafs/article/128/6/1085/7891472),  Atlantic croakers have a natural lifespan of approximately 7 years.
Over their lives, croakers grow and (as in most fish) increase their [fecundity](wiki:Fecundity) (production of eggs and sperm) as they get bigger. 
Their [natural mortality rate](wiki:Mortality_rate)  is very high when they are [larvae](wiki:Ichthyoplankton) and **juveniles**.
Once they become **adults**, however, mortality is much lower and roughly constant between ages 2 and 7 years. 
As noted, the juveniles and adults are also subject to human-induced mortality from bycatch and targeted fishing.

Aside from changes in fecundity and mortality across year classes, the first year of a croaker's life is distinct because during this year it begins as an egg and develops through a sequence of stages into a juvenile and finally into an adult.
During this interval, croakers grow and develop rapidly,  but also suffer very high mortality rates.
Small changes in mortality rates during larval and juvenile stages can have big impacts on how many croakers survive to become long-lived, reproducing adults.
Hence, variations in the demography of the first year can alter the fate of the entire population.

In many demographic models of aquatic populations,multiple species are "lumped"  into a single broad biomass category (e.g., phytoplankton, microzooplankton, *etc*.).
In these models, taxonomic resolution is a major concern.
That is, we need to consider whether a model that lumps many different species together into one functional unit can decribe the aggregate population dynamics accurately enough to have useful predictive power. 

In the case of the croaker, [Diamond *et al*. (1999)](https://academic.oup.com/tafs/article/128/6/1085/7891472)'s detailed statistical analysis led them to conclude that even one functional category for this species alone is insufficient.
That was because the life history parameters &ndash; survival, mortality and fecundity &ndash; differ so dramatically between year classes, and between larval and juvenile stages within the first year class, that it is not possible to understand the impacts of natural and human factors in population declines without accounting for these categories separately.

To understand the impacts of natural and human-influenced factors on croaker populatons, [](doi:10.1139/cjfas-57-10-2010) devised a so-called **stage-within-age matrix model**.
This type of model is based on a well-known method for formulating a structured  population model using a type of matrix called a [Leslie matrix](wiki:Leslie_matrix).
An overview of how to work with matrices, and of Leslie matrices in particular, is presented in the [Math appendix](../../../content/appendix/MathSum/matrix.md).

[](doi:10.1139/cjfas-57-10-2010)'s  model accounts for Atlantic croaker demography at two levels: Age and stage.
1. **Age**  
    In their model, the croaker population in any given year is represented by a population vector, in which each element represents the number of fish in a given year class.
	In this level of the model, elements of a **transition matrix**  account for the survival from Year 1 to Year 2, Year 2 to Year 3, *etc*., and for the fecundity of the fish in each Year class.
2. **Stage**  
    The survival of croakers *within their first year* is determined by several distinct stages, each of which has a distinct mortality rate that is determined by conditions in several different aquatic habitats.
	These mortality rates are so high, and affected by so many factors of interest in [](doi:10.1139/cjfas-57-10-2010)'s analysis, that resolving population changes over the entire year is uninformative.
	Therefore, the model accounts for mortality in the first year with a *submodel*, in which the survival of the first year cohort is resolved in detail across each stage using *daily* mortality rates.
	The cumulative stage-specific survival across all the first-year stages constitutes the element in the year-class Leslie transition matrix.
