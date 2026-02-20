# 📖️ Model formulation: Dynamics of larvae and juveniles
The modeling approach as developed so far seems a concise but effective way of assessing the consequences of Year Class age structure in the Atlantic croaker population.
However, as noted by [](doi:10.1139/cjfas-57-10-2010), the first year of a croaker's life involves a sequence of developmental stages.
These stages (and their defining characteristics) are:
- Egg (EGG): spawning to hatching
- Yolk-Sac larva (YSL): hatching to yolk-sac absorption
- Ocean larva (OL): yolk-sac adsorption to entrance in an estuary
- Estuary larva (EL): entrance in an estuary to arrival at the primary nursury
- Early juvenile (EJ): arrival at the primary nursury to movement to secondary nursery
- Late juvenile (LJ): arrival at secondary nursery to depart estuary  

Croakers at these stages differ in size, physiology, behavior and environment.
Mortality rates are high in all these stages, and but the stages also differ very substantially in mortality rates and in duration (how long a larva spends in each stage).

To improve their predictions of survival in the critical first year, [](doi:10.1139/cjfas-57-10-2010) decided they needed a more detailed submodel of larval and juvenile demography within their age-structured model.
Their solution is a **stage-within-age model**, in which details of larval life are used to calculate **survival through the first year**, $S_1$.
The resulting survival probability is used as a parameter in the age-structured Leslie matrix model for the remaining year classes.

## Estimating Year 1 survival
Considering each of the larval and juvenile stages explicitly, we can say that the probability of surviving the entire first year is the product of survival probabilities in each stage: 
    $$S_{1} = S_{EGG} ~ S_{YSL} ~ S_{OL} ~ S_{EL} ~ S_{EJ} ~ S_{LJ}.$$
Note that, in this equation, the survival terms are *multiplicative*.
That is, a fraction $S_{egg}$ survive from spawning to hatching at the end of the Egg stage.
From that fraction, a subfraction $S_{YSL}$ survive to the end of the Yolk-Sac larva stage.
From *that* fraction, a subfraction $S_{OL}$ survive to the end of the Ocean Larva stage, *etc*.
	
We can be even more explicit in calculating survival probabilities, by noting that the probability of survival in each stage is an exponentially decreasing function of mortality rate and duration of that stage. For example,
    $$S_{EGG} = e^{-\mu_{EGG} T_{EGG}}$$
where $\mu_{EGG}$ is the daily mortality rate during the egg stage and $T_{EGG}$ is the time (in days) an egg requires to develop into the Yolk-Sac Larval stage. Similarly,
    $$S_{YSL} = e^{-\mu_{YSL} T_{YSL}}$$
where $\mu_{YSL}$ is the daily mortality rate during the egg stage and $T_{YSL}$ is the time (in days) a Yolk-Sac Larva requires to develop into the Ocean Larval stage, and so forth for all the larval and juvenile stages.

