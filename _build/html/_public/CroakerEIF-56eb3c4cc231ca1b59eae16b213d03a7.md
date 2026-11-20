# 💡️ Effects of changes in egg size in the croaker model
The speculative addition of egg size evolution to [](doi:10.1139/cjfas-57-10-2010)'s Atlantic croaker population model assumes that the allocation to each egg is under evolutionary control, and that increases or decreases in egg size are reflected in different amounts of time spent in the ocean larva stage. 
The effect of changes in egg size are implemented in three inter-related parameters:
- the Egg Investment Factor, $EIF$, which is the factor of increase or decrease of resources invested in each egg, relative to the current investment.
- the Duration Factor, $DF$, which is the factor of increase or decrease of the duration of the Ocean Larva stage during the first year of croaker development .
- The growth rate, $\alpha$, during the Ocean Larva stage.

## Growth model rationale
Let's assume that an Ocean Larva increases in mass exponentially during this stage of feeding and development.
Also, we assume that it starts out with mass $M_0$, and progresses to the Estuary Larva stage when it reaches $M_{mat}$.
Then,

$$
M_{mat} = M_0 ~ e^{\alpha ~t_0},
$$ (eqnM0)

where $\alpha$ is the growth rate and $t_0$ is the observed duration of the OL stage.

We can solve for the duration,
```{math}
\label{eqnM0a}
t_0 = \frac{1}{\alpha} ~\ln{\frac{M_{mat}}{M_0}} ,
```


In our model, croaker moms can increase allocation to each egg by the Egg investment factor, $EIF$.
In this case, the OL duration is set by 
```{math}
\label{eqnM1}
M_{mat} = EIF~M_0 ~ e^{\alpha ~t_1},
```
where the initial size is now $EIF~ M_0$ and the OL duration is 
```{math}
\label{eqnM1a}
t_1 = \frac{1}{\alpha} ~\ln{\frac{M_{mat}}{EIF~ M_0}} .
```
We can now calculate the fraction by which the change in investment per egg has changed the duration:
```{math}
\label{eqnM2}
	DF = \frac{t_1}{t_0} = \frac{ \frac{1}{\alpha} ~\ln{\frac{M_{mat}}{EIF~ M_0}} }{\frac{1}{\alpha} ~\ln{\frac{M_{mat}}{M_0}} }
```
where $DF$ is the Duration Factor.

After canceling the $\alpha$ terms and using 
$$
	\ln{\frac{M_{mat}}{EIF~ M_0}} = \ln{\frac{M_{mat}}{M_0}} - \ln{EIF}
$$
we get
```{math}
\label{eqnDF}
DF = 1 - \frac{\ln{EIF}}{ \ln{\frac{M_{mat}}{M_0}} }
```

This is a nice expression for the duration of the modified larvae, but there is a problem -- we don't have any information about the sizes at the beginning or end of the OL stage.

To make progress we need to go back to Equation [](#eqnM0a), from which we can get
```{math}
\label{eqnM0b}
\ln{\frac{M_{mat}}{M_0}}  = \alpha t_0.
```
Substituting the right hand side of Equation [](#eqnM0b) into Equation [](#eqnDF),
```{math}
\label{eqnDF2}
DF = 1 - \frac{\ln{EIF}}{ \alpha t_0 }
```
Equation [](#eqnDF2) expresses the proportional reduction in development time during the Ocean Larva stage, in terms of the focal parameter, $EIF$, and the growth rate, $\alpha$.

## Larval growth rates
The final step in this analysis is to gain perspective on plausible ranges for the growth rate parameter, $\alpha$.

To best reflect constraints on maternal resources available for reproduction, we have used mass as our currency of larval size.
We do not currently have measured rates of increase for larval mass during the Ocean Larva stage.

However, [Diamond *et al*. (1999)](https://academic.oup.com/tafs/article/128/6/1085/7891472)) calculated growth rates for these larvae for the Atlantic and Gulf populations, expressed in terms of average length increase per day.
- Atlantic: $0.2136 \frac{mm}{day}$.
- Gulf: $0.1316 \frac{mm}{day}$.  

If we assume that larvae grow approximately isometrically, we can use their estimates for various parameters to calculate the corresponding growth factor estimates in terms of mass.
These values are shown in [](#parsD).

:::{table} Table of growth rates during the Ocean Larva stage, quoted (or inferred) [Diamond *et al*. (1999)](https://academic.oup.com/tafs/article/128/6/1085/7891472)).
:align: center
:label: parsD
| Region | Duration | Init. Length | Final Length | Inferred Mass Incr., $\frac{M_{mat}}{M_0}$ | Inferred Growth Rate, $\alpha$ |
| --- | --- | --- | --- | --- | --- |
| Atlantic | 39.8 days | $2~mm$ | $11.0 ~mm$ | 166.4 | 0.128 |
| Gulf | 45 days | $2.~mm$ | $7.9~mm$ | 61.6 | 0.0916 |
:::

With these estimates, we can proceed on the (speculative) assumption that growth rates on the order of $\alpha = 0.1~day^{-1}$ are within the realm of plausibility for croaker larvae in the Ocean Larva stage. 



