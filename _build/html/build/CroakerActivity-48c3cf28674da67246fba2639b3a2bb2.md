# 🛼 Exploring demography and evolution in the Atlantic croaker
This Activity revolves around using the stage-within-age population model developed by Diamond *et al*. (1999, 2000) to gain quantitative insights into demographic and evolutionary dynamics in the Atlantic croaker.
Diamond *et al*.'s primary motivation for developing this model was to assess the impacts of by-catch mortality on juvenile croakers due to the shrimp fishery in the Gulf of Mexico.
They concluded that "Contrary to our expectation, bycatch mortality on late juveniles was not the most important factor affecting either population of Atlantic croaker".

Using this implementation of Diamond *et al*.'s model, you can critically assess their conclusions to better understand the ways in which the model results do or do not provide support.
Furthermore, their model also provides opportunities to better understand structured population models in general; to assess how a variety of natural and human-induced demographic factors affect croaker populations in the past, present and future; and, to consider how models of demography might be applied to evolutionary dymamics.

To begin:
1. Launch the [Croaker model notebook](./Croaker.ipynb) on [Binder](https://mybinder.org/) or on your own computer.
2. Change one or more parameters, making sure to press `<cr>` to visualize the population dynamics using the updated demography.
3. Experiment with the model to familiarize yourself with how to change the simulation, demographic and evolutionary parameters, and how to interpret the output.

Once you have some intuition about how various parameters affect larval survivorship, Year Class structure and long-term population trends, use the notebook to address the questions in some or all of the following topic areas.

## Gaining insights into croaker population structure
Diamond *et al*. (1999, 2000) undertook extensive analysis of fisheries data to estimate parameters for their age-structured Leslie matrix model.
They based their conclusions on a [stable age distribution analysis](./CroakerModel4.md) of this model.
This notebook implements *both* a stable age distribution analysis *and* a full simulation of the underlying demographic formulas.
This gives you an opportunity to understand some of the strengths and limitations of stable age distributions as tools for characterizing demographic mechanisms.

### 1. Initial transients
From [matrix analysis](../../../content/appendix/MathSum/matrix.md), we know that the croaker population in the full simulation should converge, over time, to the stable age distribution.
However, in the short run, differences can be substantial. 
In what ways is the stable age distribution informative or uninformative?

- Explore the initial transients in the population structure by setting the number of years the simulation runs ($N_{years}$) to $1, 2, \dots$
> - Under what circumstances is the analytical steady state age structure a good approximation for the full model?  
> - For how many years do initial conditions have significant impacts on age structure?
> - In the event of a catastrophe (e.g., an oil spill), how long do you expect age structure impacts to last?

Consider more moderate but continual environmental variations (which are not considered explicitly in this model).
> - What kinds of variations (e.g., annual, decadal, etc.) would you expect to have significant effects on croaker age structure?

### 2. Population time series
The stable age distribution corresponds to a total population that always changes geometrically in time (*i.e*., in a linear trajectory on a semi-log plot).
The full model does not necessarily follow this type of trajectory.
The two time series always begin with the same normalized total population; however, that population is initially allocated very differently among Year Classes.

> - What are the similarities and differences between the time series for total population in the full model and the time series for the stable age distribution (derived from eigenvalue analysis)?
> - How are the two time series informative (or uninformative) about short-term *vs*. long-term trends in the croaker population?

### 3. Larval demography
Diamond *et al*.'s model is an exceptionally well-characterized demographc progression through sequential developmental stages, transitions between habitats, and changes in exposure to human impacts.
> What do probabilities of larval survival across stages suggest about vunerabilities during early development?
> On average, how many eggs must a female lay to produce one offspring that survives its first year?
> What stages account for the most significant mortality? Which larval characteristics (e.g., size, sensory capabilities, swimming abilities, habitat, *etc*.) do you hypothesize might be most responsible for these differences?
> In what ways would demographic parameters differ in a fish species that gives live birth to a few, more-developed larvae? 
> If you were sampling the plankton to assess croaker reproduction, how would estimates of larval survival inform your sampling design?

### Elasticities
What do elasticities for key parameters suggest about the croaker population's sensitivity to demographic parameters?

Some parameters are inter-related. For example, in feeding larval stages, behaviors that enhance feeding rates often incur added risk of predation. Hence, a change in foraging behavior that increases feeding might both&nbsp;shorten duration of a larval stage ($T$) and increase mortality rates ($\mu$). 

What determines whether this is a beneficial or harmful change?


### Population structure




Explore how the parameters affect the trajectory of the population, the age structure across years, and the stage structure within the larval period.

What relationships exist between the elasticities, the cumulative larval survival probabilities, and the age distribution?


## Exploration of the stage-within-age model: Study Questions

***What are the key Year Classes?***

Given the relative abundance of fish of different ages, which size classes would be most impacted by targeted fishing or by-catch? Factoring in the age-dependent fecundity parameters, which size classes contribute most to reproduction?


### Responses to climate change
Consider one of the many factors predicted to change in future oceans (temperature, pH, mixed layer depth, nutrient levels, alien invasions, pollution, human exploitation, *etc*.).

Speculate how this factor might affect parameters like larval duration and mortality rates. Use insights from the model to predict the impacts (or lack of impacts) on future croaker population dynamics.

## Predicting evolutionary directions for the Atlantic croaker
Exploring the potential effects of natural selection on croaker life history parameters requires understanding both the costs and benefits of prospective changes.
This typically involves additional analysis to assess how these changes are reflected in elements of the Leslie matrix.
Often, multiple elements will be affected, reflecting tradeoffs between effects that enhance and effects that degrade population growth.
For example, more aggressive feeding behavior during a larval stage may enhance growth, thereby reducing the duration of that stage and potentially reducing mortality.
However, more aggressive feeding likely increases risk of encountering predators, potentially increasing mortality.
Qunatitative analysis is needed to determine the effects of such a behavior change on Leslie matrix elements, after which the model can provide insight into whether or not the benefits outweigh the costs of changing foraging behavior.

### Evolution of egg size


To use this model to study life history evolution, I have added a new component: the possibility to change egg size.
There are two parameters through which you can manipulate life history to examine consequences for population increase or decrease.

The first is simple: The parameter \verb"egg_investment_factor" is just a multiplier by which each female will increase or decrease the reproductive resources expended on each egg (with the commensurate constraints on the number of eggs procuded given the limitation on reproductive resources).

For example, \verb"egg_investment_factor" \verb"="  \verb"2" implies that females make eggs with twice the resources, and consequently make half as many of them.

The second parameter is $\alpha$, which is the  exponential rate of growth during the larval phase. If egg size is larger, then presumably so is the larva. It then has a shorter development time, because it has less to grow, and the time by which development time is shorter is a function of $\alpha$. Large $\alpha$ implies fast growth, and small $\alpha$ implies slow growth.



Keep in mind that the egg-size model implemented here is oversimplified in important ways.
Nonetheless, it may suffice to suggest whether, under the fishing pressure and demographic regime modeled by Diamond et al., different egg sizes might evolve and, if so, whether eggs are likely to become bigger or smaller.

What are the long-term consequences of changes in egg size?

Consider what magnitude of change might be relatively "easy" -- that is, not require major reorganization of egg structure or larval development mechanisms (clearly a speculative threshold...).
Within a spectrum of such changes, would you expect to see evolutionary changes in croaker egg size?



Using the exponential rate of increase as a proxy for fitness, in which directions would you expect egg size (and possibly other life history parameters) to evolve as a result of human-induced mortality? 
Is this an appropriate proxy for fitness, or can you think of better ones? 
Does your analysis apply to other marine organisms as well?




%<p style="margin-left: 30px;">The key parameters of the model are expressed in the Leslie matrix, <strong>B</strong>. Using results from linear algebra, is can be shown that populations with this form of matrix always approach a stable age distribution. That is, if you run them long enough, the population distribution will approach a steady state (blue). Note that this does not mean the total population is constant, only that the fraction of population in a given Year Class is constant. The steady state is a convenient benchmark for population analysis, because it is easy to calculate using mathematical tools from linear algebra, and it is a characteristic only of the Leslie matrix, not involving simulation-specific parameters like initial population structure and number of years simulated.</p>

