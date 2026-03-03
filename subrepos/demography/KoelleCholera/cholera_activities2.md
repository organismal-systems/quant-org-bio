# 🛼 Alternative approaches to cholera mitigation
For one or more of the following mitigation strategies, design an exploration based on variations of the parameters in [Koelle *et al*.'s (2005)](https://doi.org/10.1038/nature03820) cholera model to gain insights into how effective different interventions might be.
Summarize your analytical rationale, and synthesize your results and conclusions, in a short narrative with graphics.

## Cholera mitigation strategy A: Improve sanitation and provide clean drinking water

Cholera is transmitted largely by exposure to contaminated water.
An obvious strategy to mitigate this is to improve access to uncontaminated water, by a combination of supplying clean water sources and improving handling of sewage to reduce cholera bacteria prevalence in the environment.

However, this is expensive, and may be only partially successful.
Depending on the specific infrastructure project, the resulting benefit may be a reduction of the seasonal increases in transmission, a decrease in sensitivity to climatic fluctuations, or a combination of the two. 

Suppose that (depending on the amount of money available) investments in infrastructure could decrease exposure to contaminated water by 10%, 25%, or 50%.
Suppose also that the projects that would reduce seasonal transmission fluctuations are not the same ones that would reduce transmission increases due to climate fluctuations.

That is, resources could be invested entirely to reduce seasonal effects (parameter $c$), climate effects (parameter $b$), or some of each. 

Which approach would have the biggest impact on reducing cholera cases? 
How does the effect on case load improve with increasing levels of investment?

## Cholera mitigation strategy B: Vaccinate against cholera
Another potential mitigation strategy is vaccination. 

Vaccines, because they don't induce severe disease, sometimes provide a lower level of immunity than actually contracting the disease.
Nonetheless, they typically provide some resistance to getting infected, and especially protection against more severe effects for people who do get infected.

You can model the effects of vaccinating a given fraction of the population with the parameter $f_{vaccinated}$.

Assume vaccination levels of 1%, 10%, 25% and 75%. 
- How does the number of cases depend on the fraction vaccinated? 
 
 That is, must a large fraction of the population be vaccinated before a significant reduction is seen in cholera cases, or is a lower vaccination rate also effective?

## Cholera mitigation strategy C: Improve nutrition and basic health
The duration of immunity after recovery from cholera, $t_{immunity}$, is one of many physiological impacts of nutritional state.

A more general but potentially effective approach would be to invest in improving nutrition for the whole population through improvements in agriculture, transportation and food handling.

Let's assume that, because of regional population pressure, the overall nutritional state is decreasing and so, without intervention, the period of immunity will decrease by 25%.
However, with investment, this decrease could be prevented.
With even more investment, nutrition could actually improve, increasing the period of immunity by 25%.
- How effective might these investments be in reducing cholera caseloads?
