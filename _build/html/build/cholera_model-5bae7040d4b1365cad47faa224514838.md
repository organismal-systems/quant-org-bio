# ️💡️  A discrete-time model of cholera immune period
This page explains key mathematical elements of [Koelle *et al*. (2005)](https://doi.org/10.1038/nature03820) cholera model.
This model has the the following characteristics:
- The model structure is a discrete time [SIR](wiki:Compartmental_models(epidemiology)) model with a time unit of 1 month.
- It assumes the total population in month $t$, $N_t$, is known, so that 

$$
S_t = N_t - I_t - R_t
$$ (sir)

- Koelle *et al*. assume that a cholera infection lasts less than 1 month, so that all the individuals infected at time $t$ are rcovered by time $t+1$.
- In Equation {eq}`sir`, the recovered population population is determined by the historical time series of infections, and by the decrease in the immunity level $\Kappa_i$ with time since the infection as a function of the immune period, $t_{immunity}$.



