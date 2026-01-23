# 🛼 Assessment of potential cholera mitigation strategies
An important use of epidemiological models is to design effective strategies for using limited resources to obtain the maximum possible benefits.
Preventable diseases cause untold suffering and mortality across many parts of the world, especially developing nations.
Resources to cope with these diseases are almost always insufficient, and more effective choices about resources translate directly into lowered incidence and fewer fatalities.

Donors often contribute to various initiatives to lower incidence of these diseases or mitigate their negative consequences.
However, before they contribute, many donors want a concrete indication that the project they fund will have a significant impact on the ground.
Furthermore, most donors receive many more funding requests than they can accommodate.
So, they need an objective way to assess the relative benefits of alternative intervention strategies.

The activities below use the model of cholera by [Koelle *et al*. (2005)](https://doi.org/10.1038/nature03820) as a tool with which to get some quantitative insights into how much alternative hypothetial intervention strategies might benefit an affected population.

## Sensitivity to parameters
To base an assessment of mitigation strategies on a model, we need to understand the model's basic characteristics.
In particular, we need to know how different parameters affect key statistics like the average number of cholera cases, the average transmission rate, the fraction of a population that is likely to remain susceptible to contracting cholera, *etc*.

[](#pars) is a table of model parameters. 
The middle column has default values; the right column has estimates for these parameters by Koelle *et al*. (2005).

:::{table} Table of parameters for Koelle *et al.'s model
:align: center
:label: pars
| Parameter | Default | Koelle *et al*. (2005) estimate |
| --- | --- | --- |
|Seasonal fluctuation  parameter, $c$ | 0 | 1 |
| Climate fluctuation parameter, $b$ | 1.5 | 10 |
| Noise parameter, $\epsilon$ | 0 | 0.95 |
| Initial fraction infected, $I_{init}$ | 0.0001 |  |
| Asymptomatic ratio, $A$ | 25 | 50 |
| Period of immunity, $t_{immunity}$ | 12 | 120 |
| Fraction vaccinated, $f_{vaccinated}$ | 0 | |
:::
Given possible inaccuracies of data, simplifying assumptions in the model, uncertainties about parameter-fitting procedures, *etc*., Koelle *et al*.'s parameters might be slightly or even wildly erroneous.

Let's get a sense for how sensitive the model is to some parameters. 
- Koelle et al. suggest the seasonal fluctuations correspond to roughly c=1 in the cholera worksheet. How does changing this parameter from the default (c=0) qualitatively change the temporal patterns of infected and susceptible people in the time series plots? How does it affect the average monthly cases and population fraction of susceptible?
- Koelle et al. suggest the climate fluctuations correspond to roughly b=10 in the cholera worksheet. How does changing this parameter from the default (b=1.5) qualitatively change the temporal patterns of infected and susceptible people in the time series plots? How does it affect the average monthly cases and population fraction of susceptible?
- Koelle et al. suggest the immune period is on the order of ten years (120 months). How does this parameter change affect the temporal patterns and summary statistics? 
- Koelle et al. suggest the noise parameter ε is 0.95. How does this parameter change affect the temporal patterns and summary statistics? 

2. (2 pts) Cholera mitigation strategy A: Improve sanitation and provide clean drinking water
Cholera is transmitted by exposure to contaminated water. An obvious strategy to mitigate this is to improve access to uncontaminated water, by a combination of supplying clean water sources and improving handling of sewage to reduce cholera bacteria populations in the environment. However, this is expensive, and may be only partially successful. Depending on the specific infrastructure project, the resulting benefit may be a reduction of the seasonal increases in transmission, a decrease in sensitivity to climatic fluctuations, or a combination of the two. 

Suppose that (depending on the amount of money available) investments in infrastructure could decrease exposure to contaminated water by 10%, 25%, or 50%.  Suppose also that the projects that would reduce seasonal transmission fluctuations are not the same ones that would reduce transmission increases due to climate fluctuations. That is, resources could be invested entirely to reduce seasonal effects (parameter c), climate effects (parameter b), or some of each. Which approach would have the biggest impact on reducing cholera cases? How does the effect on case load improve with increasing levels of investment?

3. (2 pts) Cholera mitigation strategy B: Vaccinate against cholera
Another potential mitigation strategy is vaccination. Vaccines, because they don't induce severe disease, often provide a lower level of immunity. You can model the effects of vaccinating a given fraction of the population with the slider for the parameter fvaccinated. Assume vaccination levels of 1%, 10%, 25% and 75%. How does the number of cases depend on the fraction vaccinated? That is, must a large fraction of the population be vaccinated before a significant reduction is seen in cholera cases, or is a lower vaccination rate also effective?  

4. (2 pts) Cholera mitigation strategy C: Improve nutrition and basic health
The duration of immunity after recovery from cholera is one of many physiological impacts of nutritional state. A more general but potentially effective approach would be to invest in improving nutrition for the whole population through improvements in agriculture, transportation and food handling. Let's assume that, because of regional population pressure, the overall nutritional state is decreasing and so, without intervention, the period of immunity will decrease by 25%. However, with investment, this decrease could be prevented. With even more investment, nutrition could actually improve, increasing the period of immunity by 25%. How effective might these investments be in reducing cholera caseloads?
