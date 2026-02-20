# 📖️  Model formulation: Year Class demography
To construct a population model, we need formulas that project the population in year $t$, $\mathbf{P}(t)$, forward to year $t+1$.
To understand how [](doi:10.1139/cjfas-57-10-2010) formulated their model, we will go carefully through the three things that happen to the croaker population between the end of year $t$ and the end of year $t+1$:
1. **Individuals age by one year**  
    That is, individuals who are in Year Class $i$ in year $t$ are, if they survive, moved to Year Class $i+1$ in Year $t+1$.
	
2. **Individuals die**  
     [](doi:10.1139/cjfas-57-10-2010) assumed that the probability of an adult dying in a given year is a constant, $\mu_{adult}$, for all age classes older than larvae and juveniles ($i=3, 4, \dots$, 8).
	 
	 Another way to express this is as a survival probability, $S_{adult}$. Because every adult will either die or survive, the probabilities $\mu_{adult}$ and $S_{adult}$ must add up to one, so that
	 $$
	 S_{adult} = 1 - \mu_{adult}.
	 $$
	 
    Combining aging and mortality, we can now say that the croaker population in Year Class $i+1$ in year $t+1$ is equal to the croaker population in Year Class $i$ in year $t$ times the survival rate during that year:
    $$
    p_{i+1}(t+1) = S_{adult} ~ p_i(t), 
    $$
    for all the adult Year Classes, $i = 3, 4, \dots$, 8.

3. **Individuals reproduce**  
In assessing reproduction of fish such as croakers, it's usually assumed that the main limitation is the number of eggs.
That is because sperm are usually available in much greater numbers, most of which never encounter an egg and hence play no part in reproduction.  

    To assess the number of eggs, we must focus on the population of female croakers.
    In some fish species the ratio of males to females is nearly equal (like it is in humans) and we could assume half the adults are female.
    However, in other fish species the sex ratio is strongly biased towards one gender (because of their basic biology, selective harvesting, etc.).
    In this case, it's clearest to model males and females separately, and since the number of males is almost always sufficient to fertilize all the females, we don't even have to worry about the males.
    So, we now make the assumption that we are modeling only females, and adjust populations, fecundity *etc*. accordingly.
    
	Let's assume that a female croaker of age $i$ produces $F_i$ female eggs.
    Accounting for all Year Classes, the population of female eggs ($p_1$) produced at the end of year $t$ to develop during year $t+1$ is then  
    $$
    p_1(t+1) = \sum_{i=1}^8 F_i p_i(t)
    $$
    In words, this equations says that: 
	> The number of eggs in year $t+1$ equals the number of females in Year Class $i$ in year $t$ multiplied by the number of eggs produced per female ($F_i$), summed across all the Year Classes $i=1,2,\dots, 8$.

## Parameters are constant

## There is no density-dependence

