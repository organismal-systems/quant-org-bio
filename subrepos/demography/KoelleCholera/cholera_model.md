# ️💡️  A discrete-time model of cholera immune period
This page explains key mathematical elements of [Koelle *et al*. (2005)](https://doi.org/10.1038/nature03820) cholera model.
This model has the the following characteristics:
- The model structure is a discrete time [SIR](wiki:Compartmental_models(epidemiology)) model with a time unit of 1 month.
- It assumes the total population in month $t$, $N_t$, is known[^k2], so that 

$$
S_t = N_t - I_t - R_t
$$ (sir)

- Koelle *et al*. assume that a cholera infection lasts less than 1 month, so that all the individuals infected at time $t$ are recovered by time $t+1$.

- In Equation {eq}`sir`, the recovered population population is determined by:
  - the historical time series of infections
  - the decrease in the immunity level $\Kappa_i$ with time since the infection.

- The immunity level, $\Kappa_i$, is the fraction of people retaining an acquired immunity to cholera $i$ months after they have recovered.
  - The immunity level at $t=0$ is $A$, the number of asymptomatic (or otherwise unreported) cholera infections for each reported infection.
  - The timescale over which the immunity level declines from $A$ to 0 is the immune period, $t_{immunity}$.

- The recovered and susceptible populations are therefore[^k1]

$$
R_t = \sum_{i=0}^m \Kappa_i I_{t-i} \\
S_t = N_t - I_t - \sum_{i=0}^m \Kappa_i I_{t-i}
$$ (rs)

- The number of infected individuals in month $t+1$ is

$$
I_{t+1} = \beta_t I_t^\alpha \left(\frac{S_t}{N_t}\right)^\gamma \epsilon_t
$$ (inf)
  In Equation {eq}`inf`,
  - $\beta_t$ is the transmission rate in month $t$
  - $\epsilon_t$ is a "noise" factor in month $t$
  - $\alpha$ and $\gamma$ are "clustering" exponents, intended to account for the fact that populations are not freely mixing &ndash; infected individuals are on average more likely to interact with other infected individuals than would be expected if interactions were completely random.[^k3]

- The transmission rate for month $t$ is $\beta_t = \beta_{season} \beta_{climate}$, where
  - $\beta_{season}$ is the seasonal transmission component, defined over the 12 months of a year[^k5]
  - $\beta_{climate}$ is the climate transmission component, defined over an extended period of several years[^k4]

  In this implementation, seasonal fluctuations are modulated by the parameter $c$ and climate fluctuations are modulated by the parameter $b$.


[^k1]: Koelle *et al*. include cross-immunity from infection by the Classical biotype; this implementation addresses only the predominant El Tor biotype.
[^k2]: The implementation of this model in this Unit assumes a constant population.
[^k3]: In their implementation, Koelle *et al*. assume that $\gamma=1$, and use statistical optimization to estimate $\alpha$.
[^k4]: In this implementation, $\beta_{climate}$ linearly increases from the start of a simulation to its midpoint, after which it linearly decreases back to its starting level.
[^k5]: In this implementation, $\beta_{season}$ is a periodic function that is vaguely reminiscent of the seasonal pattern determined by Koelle *et al*. but mostly chosen for convenience.
