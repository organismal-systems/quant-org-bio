# 🛼  Sensitivity to parameters
To base an assessment of mitigation strategies on a model, we need to understand the model's basic characteristics.
In particular, we need to know how different parameters affect key statistics like the average number of cholera cases, the average transmission rate, the fraction of a population that is likely to remain susceptible to contracting cholera, *etc*.

[](#pars) is a table of model parameters. 
The middle column has default values; the right column has estimates for these parameters by Koelle *et al*. (2005).

:::{table} Table of parameters for Koelle *et al*.'s model
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

Let's get a sense for how sensitive the model is to some parameters:
1. Koelle *et al*. suggest the seasonal fluctuations correspond to roughly $c=1$ in the cholera worksheet.
  - How does changing this parameter from the default ($c=0$) qualitatively change the temporal patterns of infected and susceptible people in the time series plots? 
  - How does it affect the average monthly cases and population fraction of susceptible?
  - At what values of $c$ do these effects begin to be quantitatively significant?

2. Koelle *et al*. suggest the climate fluctuations correspond to roughly $b=10$ in the cholera worksheet.
  - How does changing this parameter from the default ($b=1.5$) qualitatively change the temporal patterns of infected and susceptible people in the time series plots? 
  - How does it affect the average monthly cases and population fraction of susceptibles?
  - At what values of $b$ do these effects begin to be quantitatively significant?

3. Koelle *et al*. suggest the immune period is on the order of ten years ($t_{immunity} = 120$ months).
  - How do variations in this parameter change affect the temporal patterns and summary statistics? 
  
4. Koelle *et al*. suggest the noise parameter $\epsilon = 0.95$.
  - How does this parameter change affect the temporal patterns and summary statistics? 
  - What consequences do large $\epsilon$ values have on collecting and interpretating data on the need for interventions, and their effectiveness in reducing cholera impacts?

