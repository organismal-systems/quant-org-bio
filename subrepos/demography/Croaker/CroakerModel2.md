# 📖️ Model formulation: Dynamics of larvae and juveniles
The modeling approach as developed so far seems a concise but effective way of assessing the consequences of Year Class age structure in the Atlantic croaker population.
However, as noted by [](doi:10.1139/cjfas-57-10-2010), the first year of a croaker's life involves a complicated sequence of developmental stages.
These stages (and their durations) are:
- Egg (EGG): spawning through hatching
- Yolk-Sac Larva (YSL): hatching through yolk-sac absorption
- Ocean Larva (OL): yolk-sac adsorption through entrance in an estuary
- Estuary Larva (EL): entrance in an estuary through arrival at the primary nursury
- Early Juvenile (EJ): arrival at the primary nursury through movement to secondary nursery
- Late Juvenile (LJ): arrival at secondary nursery through depart estuary  

Croakers at these stages differ in size, physiology, behavior and environment.
Mortality rates are high in all these stages, and but the stages also differ very substantially in the mechanisms causing that mortality and in duration.

To improve their predictions of survival in the critical first year, [](doi:10.1139/cjfas-57-10-2010) decided they needed a more detailed submodel of larval and juvenile demography within their age-structured model.
Their solution is a **stage-within-age model**, in which details of larval life are used to calculate **survival through the first year**, $S_1$.
The resulting survival probability &ndash; *cumulative* over all the larval stages &ndash; is used as a parameter in the age-structured Leslie matrix model for the remaining year classes.

## Estimating Year 1 survival
Considering each of the larval and juvenile stages explicitly, we can say that the probability of surviving the entire first year is the product of survival probabilities in each stage: 
    $$S_{1} = S_{EGG} ~ S_{YSL} ~ S_{OL} ~ S_{EL} ~ S_{EJ} ~ S_{LJ}.$$
Note that, in this equation, the survival terms are *multiplicative*.
That is, a fraction $S_{egg}$ survive from spawning to hatching at the end of the Egg stage.
From that fraction, a subfraction $S_{YSL}$ survive to the end of the Yolk-Sac larva stage.
From *that* fraction, a subfraction $S_{OL}$ survive to the end of the Ocean Larva stage, *etc*.
	
We can be even more explicit in calculating survival probabilities, by noting that the probability of survival in each stage is an exponentially decreasing function of mortality rate and duration of that stage.
This is a consequence of the assumption that death occurs at a constant probability per day, and that therefore mortality is a [Poisson process](../../../content/appendix/MathSum/poisson.md).

For example,
    $$S_{EGG} = e^{-\mu_{EGG} T_{EGG}}$$
where $\mu_{EGG}$ is the daily mortality rate during the egg stage and $T_{EGG}$ is the time (in days) an egg requires to hatch into the Yolk-Sac Larva stage.
Similarly,
    $$S_{YSL} = e^{-\mu_{YSL} T_{YSL}}$$
where $\mu_{YSL}$ is the daily mortality rate during the Yolk-Sac Larva stage and $T_{YSL}$ is the time (in days) a Yolk-Sac Larva requires to develop into the Ocean Larva stage (and so forth for all the larval and juvenile stages).

