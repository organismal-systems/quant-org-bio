# 📖️ Modeling Croaker demography
In many demographic models of aquatic populations, multiple species are "lumped"  into a single broad biomass category (e.g., phytoplankton, microzooplankton, *etc*.).
In these models, taxonomic resolution is a major concern.
That is, we need to consider whether a model that groups many different species together into one functional unit can decribe the aggregate population dynamics accurately enough to have useful predictive power. 

In the case of the croaker, [Diamond *et al*. (1999)](https://academic.oup.com/tafs/article/128/6/1085/7891472)'s detailed statistical analysis led them to conclude that even one functional category for this species alone is insufficient.
That was because the life history parameters &ndash; survival, mortality and fecundity &ndash; differ so dramatically between year classes, and between larval and juvenile stages within the first year class, that it was not possible to understand the impacts of natural and human factors in population declines without accounting for these categories separately.

To understand the impacts of natural and human-influenced factors on croaker populatons, [](doi:10.1139/cjfas-57-10-2010) devised a type of **structured population model** called a **stage-within-age matrix model**.
This type of model is based on a well-known method for formulating a structured  population model using a type of matrix called a [Leslie matrix](wiki:Leslie_matrix).
An overview of how to work with matrices, and of Leslie matrices in particular, is presented in the [Math appendix](../../../content/appendix/MathSum/matrix.md).

[](doi:10.1139/cjfas-57-10-2010)'s  model accounts for Atlantic croaker demography at two levels: Age and stage.
1. **Age**  
    In their model, the croaker population in any given year is represented by a population vector, in which each element represents the number of fish in a given Year Class.
	In this level of the model, elements of a **transition matrix**  account for the survival from Year 1 to Year 2, Year 2 to Year 3, *etc*., and for the fecundity of the fish in each Year Class.
	The total fecundity of all the year classes determines the number of eggs that are produced, to begin development in the following year.
2. **Stage**  
    The survival of croakers *within their first year* is determined by several distinct stages, each of which has a distinct mortality rate that is determined by conditions in several different aquatic habitats.
	These mortality rates are so high, and affected by so many factors of interest in [](doi:10.1139/cjfas-57-10-2010)'s analysis, that trying to account for them using a single mortality rate for the entire first year is uninformative.
	Therefore, the model accounts for mortality in the first year with a *submodel*, in which the survival of the first year cohort is resolved in detail across each stage using *daily* mortality rates.
	The cumulative stage-specific survival across all the first-year stages constitutes the corresponding element in the year-class Leslie transition matrix.

## Model structure
The starting point of [](doi:10.1139/cjfas-57-10-2010)'s model to use a single variable to represent the number of croakers in each Year Class:  $p_1$, the number of croakers in Year Class 2 as $p_2$, *etc*.
The population of all seven Year Classes in year $t$  can then be summarized by the vector 
$$
\mathbf{P}(t) = \begin{pmatrix}
p_1 \\ p_2 \\ p_3 \\ \vdots \\ p_8
\end{pmatrix}. \label{eq:eqnVEC}
$$
In this vector:
- $p_1$ is the number of eggs
- $p_2$ is the number of juveniles
- $p_i,~i=3,4,\dots$ is the number of adults in Year Class $i$.
%Like many population models, [](doi:10.1139/cjfas-57-10-2010)'s model is essentially a model of the female population.
%The underlying assumption is that there are always enough males to fertilize eggs, so the number of eggs is the limiting demographic factor.

It's important to recognize that Leslie matrix models are **discrete time models**.
That is, time is represented as a discrete variable that increments for each year, $t = 1, 2, 3, \dots$.
This means that $p_i$ represents the number of croakers in the $i^{th}$ Year Class **at a specific time of year**.

In this case, [](doi:10.1139/cjfas-57-10-2010) have assumed that
> $p_i(t)$ represents the croaker population in the $i^{th}$ Year Class  **at the end** of year $t$.

This choice has implications for how we interpret demographic parameters, and for how they are quantified from fisheries and other data (see [Diamond *et al*. (1999)](https://academic.oup.com/tafs/article/128/6/1085/7891472)). 

For example, the age-specific survival rate, 
> $S_i$ is the fraction of croakers in the $i^{th}$ Year Class at the end of year $t$ that survives an entire year to be counted in the $(i+1)^{st}$ Year Class at the end of year $t+1$. 

In reality, fish mortality has been occuring throughout the year, continously but possibly at seasonally varying rates.
The survival metric, $S_i$, "leapfrogs" over that continuous mortality to summarize the total mortality over the entire year.

Likewise, the age-specific fecundity, 
> $F_i$ is the number of eggs produced by fish in the $i^{th}$ Year Class during year $t$ and developing during year $t+1$, normalized by the number of Year Class $i$ croakers at the end of year $t$. 

In reality, croaker spawning occurs over about six months of each year, including times at which their population was not the same as it was at the end of year $t$ or as it will be at the end of year $t+1$.
The fecundity, $F_i$, *implicitly* accounts for this variation by adjusting the per-fish fecundity to factor in fish that died before they had a chance to reproduce, the fish that reproduced but died before the end of the year, *etc*.



