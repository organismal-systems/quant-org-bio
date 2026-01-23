# ️💡️  A discrete-time model of cholera immune period
This page explains key mathematical elements of [Koelle *et al*. (2005)](https://doi.org/10.1038/nature03820) cholera model.
This model has the the following characteristics:
- The model structure is a discrete time [SIR](wiki:Compartmental_models(epidemiology)) model with a time unit of 1 month.
- It assumes the total population in month $t$, $N_t$, is known, so that 

$$
S_t = N_t - I_t - R_t
$$ (sir)

- Koelle *et al*. assume that a cholera infection lasts less than 1 month, so that all the individuals infected at time $t$ are recovered by time $t+1$.
- In Equation {eq}`sir`, the recovered population population is determined by:
  - the historical time series of infections, and by the decrease in the immunity level $\Kappa_i$ with time since the infection as a function of the immune period, $t_{immunity}$.
  The immunity level, $\Kappa_i$, is the fraction of people retaining an acquired immunity to cholera $i$ months after they have recovered.
  
  This is quantified by

$$
R_t = \Sum_i=0^m \Kappa_i I_{t-i}
$$ (rs)

