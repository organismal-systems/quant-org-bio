# 📖️ A speculative evolutionary scenario
[](doi:10.1139/cjfas-57-10-2010) carried out a detailed statistical analysis in which they estimated all the key parameters discussed so far.
In addition to reproducing their modeling approach and results, we can add a new dimension to predictions of croaker population trajectories by speculating about evolutionary changes through which croaker life history might adjust to increases or decreases in mortality.
This is of particular interest in the case of addition of significant fishing mortality to populations that evolved without this type of mortality. 

In other fish species, a variety of life history changes have been observed in response to anthropogenic stresses. 
For example, a species in which large adults are heavily fished might evolve towards allocating more resources to reproduction and fewer to growth in small adults. 
Note that this is a different phenomenon than a simple change in the relative frequency of different age or size classes, which might result directly from fishing mortality without any evolutionary changes.
    
An implication from [](doi:10.1139/cjfas-57-10-2010) is that conditions had changed relative to historical patterns at the time of their study, in fishing-induced mortality and possibly in many other ways.
This is reason to speculate that croaker life history parameters might evolve away from current values, if those changes increase reproductive success.

## Evolution of egg size
Here, we will consider changes in only one life history parameter: egg size.
If we assume that females have a specific amount of resources to invest in eggs, they face a trade-off between allocating those resources to more, smaller eggs or to fewer, larger eggs.
There is a large literature on the evolution of egg size.
Changes in egg size have consequences for sperm-egg encounter rates, for movement through the water column, for predation rates, for development times, and many other factors in larval life history.
Here, we will focus on one possible effect of a hypothetical change in egg size, which is the development time of early larval stages.

> It's important to keep in mind that we do not have data informing us about how development in croaker larvae actually takes place.    
> The discussion of egg size evolution is based on educated guesses, and is therefore highly speculative.

We will assume that an Ocean Larva must reach a critical size before it is able to transition into an Estuary Larva.
To do so, it must feed in the plankton.
This takes time during which it has a high probability of dying.
If a larva starts from a larger egg, it has less growing to do before it can transition.
Hence, its duration in the Ocean Larval stage is shorter, and its probability of surviving commensurately higher.

In this lab, we consider a scenario in which (over evolutionary time) females can adjust their egg size relative to the currently observed size by an **Egg Investment Factor, $EIF$**. 
### Effects on fecundity
If each egg consumes a factor of $EIF$ more resources, constraints on total maternal investment mean that the number of eggs must decrease by a factor of $\frac{1}{EIF}$. 
Then, the population of female eggs in the $t+1$st year will be
$$
p_1(t+1) = \frac{1}{EIF} \sum_{i=1}^8 F_i~p_i(t)
$$
### Effects on survival
The other side of the egg-size tradeoff is the effect on larval duration, and hence on survival probability.
We will assume that the effect of changed egg size is by changing the duration of the Ocean Larva stage, because this is the first stage at which the larva acquires resources by feeding.

We define a Duration Factor, $DF$, by assuming that growth is exponential during the OL stage in [](doi:10.1139/cjfas-57-10-2010)'s model.
This is a speculative assumption because they specify only the total duration of each larval stage, not the growth progression within it.
Our assumption is guesswork, but plausible -- many models assume growth rate is proportional to body size, because it is often observed that growth rates are approximately proportional to size, and that larger consumers consume more and larger resources.

If we accept this assumption, the duration of the OL stage, $T_{OL}$, is changed by a factor
    $$DF = max \left(1-\frac{log(EIF)}{\alpha T_{ol}},0 \right)$$
Here, $\alpha$ is a growth rate, and the "max" function enforces the fact that the OL stage cannot have a negative duration.
The mathematical logic behind this formula for $DF$ is shown in [this derivation](./CroakerEIF.md).

The question is, then,
> Would changes from the observed condition (in which $EIF=1$) be evolutionarily advantageous or disadvantageous (i.e., would they lead to higher or lower reproductive fitness)?
