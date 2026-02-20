# 📖️ Modeling Croaker demography
In many demographic models of aquatic populations, multiple species are "lumped"  into a single broad biomass category (e.g., phytoplankton, microzooplankton, *etc*.).
In these models, taxonomic resolution is a major concern.
That is, we need to consider whether a model that groups many different species together into one functional unit can decribe the aggregate population dynamics accurately enough to have useful predictive power. 

In the case of the croaker, [Diamond *et al*. (1999)](https://academic.oup.com/tafs/article/128/6/1085/7891472)'s detailed statistical analysis led them to conclude that even one functional category for this species alone is insufficient.
That was because the life history parameters &ndash; survival, mortality and fecundity &ndash; differ so dramatically between year classes, and between larval and juvenile stages within the first year class, that it was not possible to understand the impacts of natural and human factors in population declines without accounting for these categories separately.

To understand the impacts of natural and human-influenced factors on croaker populatons, [](doi:10.1139/cjfas-57-10-2010) devised a type of **structured population model** called a **stage-within-age matrix model**.
This type of model is based on a well-known method for formulating a structured  population model using a type of matrix called a [Leslie matrix](wiki:Leslie_matrix).
An overview of how to work with matrices, and of Leslie matrices in particular, is presented in the [Math appendix](../../../content/appendix/MathSum/matrix.md).

[](doi:10.1139/cjfas-57-10-2010)'s  model accounts for Atlantic croaker demography at two levels: Age and stage.
1. **Age**  
    In their model, the croaker population in any given year is represented by a population vector, in which each element represents the number of fish in a given year class.
	In this level of the model, elements of a **transition matrix**  account for the survival from Year 1 to Year 2, Year 2 to Year 3, *etc*., and for the fecundity of the fish in each Year class.
	The total fecundity of all the year classes determines the number of eggs that are produced, to begin development in the following year.
2. **Stage**  
    The survival of croakers *within their first year* is determined by several distinct stages, each of which has a distinct mortality rate that is determined by conditions in several different aquatic habitats.
	These mortality rates are so high, and affected by so many factors of interest in [](doi:10.1139/cjfas-57-10-2010)'s analysis, that trying to account for them using a single mortality rate for the entire first year is uninformative.
	Therefore, the model accounts for mortality in the first year with a *submodel*, in which the survival of the first year cohort is resolved in detail across each stage using *daily* mortality rates.
	The cumulative stage-specific survival across all the first-year stages constitutes the corresponding element in the year-class Leslie transition matrix.

## Model structure
The starting point of [](doi:10.1139/cjfas-57-10-2010)'s model to use a single variable to represent the number of croakers in each Year Class:  $p_1$, the number of croakers in Year Class 2 as $p_2$, *etc*.
The population of all seven Year Classes in year $t$  can then be summarized by the vector 
$$
\mathbf{P}_t = \begin{pmatrix}
p_1 \\ p_2 \\ p_3 \\ \vdots \\ p_7
\end{pmatrix}. \label{eq:eqnVEC}
$$
Like many population models, [](doi:10.1139/cjfas-57-10-2010)'s model is essentially a model of the female population.
The underlying assumption is that there are always enough males to fertilize eggs, so the number of eggs is the limiting demographic factor.

It's important to recognize that Leslie matrix models are **discrete time models**.
That is, time is represented as a discrete variable that increments for each year, $t = 1, 2, 3, \dots$.
This means that $p_i$ represents the number of croakers in the $i^{th}$ Year Class **at a specific time of year**.
In this case, [](doi:10.1139/cjfas-57-10-2010) have assumed that
> $p_i$ represents the croaker population in the $i^{th}$ Year Class  **at the end** of the year.

This choice has implications for how we interpret demographic parameters, and for how they are quantified from fisheries and other data (see [Diamond *et al*. (1999)](https://academic.oup.com/tafs/article/128/6/1085/7891472)). 

For example, the age-specific survival rate, 
> $S_i$, is the fraction of croakers in the $i^{th}$ Year class in year $t$ that survives an entire year to be counted in the $(i+1)^{st}$ Year class at the end of year $t+1$. 

In reality, fish mortality has been occuring throughout the year, continously but possibly at varying rates.
The survival metric, $S_I$, "leapfrogs" over that continuous mortality to summarize the total mortality over the entire year.

Likewise, the age-specific fecundity, 
> $F_i$, is the number of eggs produced by $i^{th}$ in year $t$ and developing during year $t+1$, normalized by the number of Year class $i$ croakers at the end of year $t$. 

In reality, croaker spawning may occur at different times of year at which their population was not the same as it was at the end of year $t$ or as it will be at the end of year $t+1$.
The fecundity, $F_i$ *implicitly* accounts for this variation by discounting the per-fish fecundity to factor in fish that died before they had a chance to reproduce (and also discounting males, because the model is of females only).

## Model formulation
To have a population model, we need formulas that project the population $\mathbf{P}_t$ forward to Year $t+1$.
To understand how [](doi:10.1139/cjfas-57-10-2010) constructed their model, we will go carefully through the three things that happen to the croaker population in the transition between the end of year $t$ and the end of year $t+1$:
1. **Individuals age by one year**  
    That is, individuals who are in Year Class $i$ in year $t$ are, if they survive, moved to Year Class $i+1$ in Year $t+1$.
	
2. **Individuals die**  
     [](doi:10.1139/cjfas-57-10-2010) assumed that the probability of an adult dying in a given year is a constant, $\mu_{adult}$, for all age classes older than larvae and juveniles ($i=2, 3, \dots$.
	 
	 Another way to express this is as a survival probability, $S_{adult}$. Because every adult will either die or survive, $\mu_{adult}$ and $S_{adult}$ add up to one, so that
	 $$
	 S_{adult} = 1 - \mu_{adult}.
	 $$
	 
Combining aging and mortality, we can now say that the croaker population in Year Class $i+1$ in year $t+1$ is equal to the croaker population in Year Class $i$ in year $t$ times the survival rate during that year:
$$
p_{j+1}(i+1) = S_{adult} ~ p_j(i)
$$
3. **Individuals reproduce**  
    In assessing reproduction of fish such as croakers, it's usually assumed that the main limitation is the number of eggs. That is because sperm are usually available in much greater numbers, most of which never encounter an egg and hence play no part in reproduction. To assess the number of eggs, we must focus on the population of female croakers. In some fish species the ratio of males to females is nearly equal (like it is in humans) and we could assume half the adults are female. However, in other fish species the sex ratio is strongly biased towards one gender (because of their basic biology, selective harvesting, etc.). In this case, it's clearest to model males and females separately, and since the number of males is almost always sufficient to fertilize all the females, we don't even have to worry about the males.</p>
<p style="margin-left: 30px;">So, we make the assumption now that we are modeling only females, and adjust populations, fecundity etc. accordingly (for example, if half the eggs are of each gender, the effective fecundity in the female-only model is 50% of the total observed fecundity). Let's assume that a female croaker of age $i$ produces $F_i$ female eggs. Accounting for all Year Classes, the population of female eggs ($p_{eggs}$) produced in the $i+1$st year is then 
    $$p_{eggs}(i+1) = F_1 p_1(i) + F_2 p_2(i) + F_3 p_3(i) + F_4 p_4(i) + F_5 p_5(i) + F_6 p_6(i) + F_7 p_7(i)$$
</p>


<p><span style="font-size: medium;"><strong>2. Larval development and survival</strong></span></p>
<p>The modeling approach as developed so far seems a concise but effective way of assessing the consequences of Year Class age structure in the Atlantic croaker population. However, as noted, the first year of a croaker's life involves a sequence of developmental stages: Egg (EGG),&nbsp; Yolk-Sac larva (YSL), Ocean larva (OL), Estuary larva (EL), Early juvenile (EJ) and Late juvenile (LJ). Croakers at these stages differ in size, physiology, behavior and environment. Mortality rates are high in all these stages, and but the stages also differ very substantially in mortality rates and in duration (how long a larva spends in each stage).</p>
<p>To improve their predictions of survival in the critical first year, Diamond et al. decided they needed a more detailed submodel within their age-structured model. Their solution is a <strong>stage-within-age model</strong>, in which details of larval life are used to calculate <strong>survival through the first year</strong>, $S_{Y1}$. The resulting survival probability is used as a parameter in the age-structured model for the remaining year classes.&nbsp;</p>
<p>Considering each of the larval and juvenile stages explicitly, we can say that the probability of surviving the entire first year is the product of survival probabilities in each stage: 
    $$S_{Y1} = S_{EGG} ~ S_{YSL} ~ S_{OL} ~ S_{EL} ~ S_{EJ} ~ S_{LJ}.$$ 
We can be even more explicit in calculating survival probabilities, by noting that the probability of survival in each stage is an exponentially decreasing function of mortality rate and duration of that stage. For example,
    $$S_{EGG} = e^{-\mu_{EGG} T_{EGG}},$$
where $\mu_{EGG}$ is the mortality rate during the egg stage and $T_{EGG}$ is the time an egg requires to develop into the Yolk-Sac Larval stage. Similarly,
    $$S_{YSL} = e^{-\mu_{YSL} T_{YSL}},$$
where $\mu_{YSL}$ is the mortality rate during the egg stage and $T_{YSL}$ is the time a Yolk-Sac Larva requires to develop into the Ocean Larval stage, and so forth for all the larval stages.</p>

<p><span style="font-size: medium;"><strong>3. A speculative evolutionary scenario<br /></strong></span></p>
<p>Diamond et al. carried out a detailed statistical analysis in which they estimated all the key parameters discussed so far. In addition to reproducing their modeling approach and results, we can add a new dimension to predictions of croaker population trajectories by speculating about evolutionary changes through which croaker life history might adjust to increases or decreases in mortality (in particular, addition of significant fishing mortality to populations that evolved without this type of mortality). In other fish species, a variety of life history changes have been observed in response to anthropogenic stresses. For example, a species in which large adults are heavily fished might evolve towards allocating more resources to reproduction and fewer to growth in small adults. 
    
An implication of Diamond et al. is that conditions had changed relative to historical patterns at the time of their study, at least in fishing-induced mortality and possibly in many other ways. Thus, there is reason to speculate that croaker life history parameters might evolve away from current values, if those changes increase reproductive success.</p>

<p>Here, we will consider changes in only one life history parameter: egg size. If we assume females have a specific amount of resources to invest in eggs, they face a trade-off between allocating those resources to more, smaller eggs or to fewer, larger eggs. There is a large literature on the evolution of egg size. Changes in egg size have consequences for sperm-egg encounter rates, for movement through the water column, for predation rates, for development times, and many other factors in larval life history. Here, we will focus on one possible effect of a hypothetical change in egg size, which is the development time in early larval stages.</p>

<p>We will assume that a Yolk-Sac Larva must reach a critical size before it is able to transition into an Ocean Larva. To do so, it must feed in the plankton, and this takes time during which it has a high probability of dying. If a larva starts from a larger egg, it has less growing to do before it can transition. Hence, its duration in the Yolk-Sac Larval stage is shorter, and its probability of surviving commensurately higher.</p>

<p>In this lab, we consider a scenario in which (over evolutionary time) females can adjust their egg size relative to the currently observed size by an Egg Investment Factor, $EIF$. If so, constraints on total maternal investment mean that the number of eggs must decrease by a factor of $\frac{1}{EIF}$. Then, the population of female eggs in the $i+1$st year will be
    $$p_{eggs}(i+1) = \frac{1}{EIF} \left(F_1 p_1(i) + F_2 p_2(i) + F_3 p_3(i) + F_4 p_4(i) + F_5 p_5(i) + F_6 p_6(i) + F_7 p_7(i) \right)$$
The other side of the egg-size tradeoff is the effect on larval duration, and hence on survival probability. We will assume that the effect of changed egg size is by changing the duration of the Ocean Larva stage, because this is the first stage at which the larva acquires resources by feeding. We define a Duration Factor, $DF$, by assuming that growth is exponential during the OL stage in Diamond et al.'s model (this is an assumption because they specify only the total duration of each larval stage, not the growth progression within it). Our assumption is unproven, but plausible -- many models assume growth rate is proportional to body size, because larger consumers often encounter more and larger resources. If we accept this assumption, the duration of the OL stage, $T_{OL}$, is changed by a factor
    $$DF = max \left(1-\frac{log(EIF)}{\alpha T_{ol}},0 \right)$$
Here, the "max" function enforces the fact that the OL stage cannot have a negative duration.
    
The question, then, is would changes from the observed condition (in which $EIF=1$) be evolutionarily advantageous or disadvantageous (i.e., would they lead to higher or lower reproductive fitness)?</p>

<p><span style="font-size: medium;"><strong>4. Modeling mechanics<br /></strong></span></p>
<p>We have now recapitulated the key elements of Diamond et al.'s age-within-stage model. To execute and analyze their model, Diamond et al. borrowed tools for matrix mathematics from linear algebra. Specifically, the modeling terms itemized above can be written very concisely as a matrix multiplication,
$$\mathbf{P}(i+1) = \mathbf{A} \mathbf{P}(i).$$
As above, $\mathbf{P}(i)$ is the vector of population in Year Classes 1-7 in year $i$. The matrix $\mathbf{A}$ contains the terms of the original age-structured model involved in advancing this population to year $i+1$:
$$
\mathbf{A} = \begin{pmatrix}
\frac{F_1}{EIF} & \frac{F_2}{EIF} & \frac{F_3}{EIF} & \frac{F_4}{EIF} & \frac{F_5}{EIF} & \frac{F_6}{EIF} & \frac{F_7}{EIF} \\
S_{Y1} & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & S_{adult} & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & S_{adult} & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & S_{adult} & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & S_{adult} & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & S_{adult} & 0 \\
\end{pmatrix}
$$
 
This matrix is in a common form in population modeling, called a <strong>Leslie matrix</strong>, in which non-zero terms appear only in the top row and the subdiagonal. The interpretations of the non-zero terms are:
    
- In the top row, each entry is the <strong>age-specific fecundity</strong>, which is the contribution of a female croaker in a given year class to the number of female eggs in the following year. For example, $\frac{F_2}{EIF}$ is the fecundity of a 2 year old female croaker, $\frac{F_3}{EIF}$ is the fecundity of a 3 year old female croaker, etc.
    
- The subdiagonal terms, $S_{Y1}$ and $S_{adult}$, are the survival probabilities for each age class. Specifically, $S_{Y1}$ is the probability an egg will survive its first year to become an Age-2 fish. $S_{adult}$ is the probability an Age-2 fish will survive to become an Age-3 fish, that an Age-3 fish will survive to become an Age-4 fish, etc.
    
With substitution into $\mathbf{A}$ of the larval life history parameters determining first-year survival, 
    $$S_{Y1} = e^{-\left( \mu_{EGG} T_{EGG} + \mu_{YSL} T_{YSL} + \mu_{OL} DF T_{OL} + \mu_{EL} T_{EL} + \mu_{EJ} T_{EJ} + \mu_{LJ} T_{LJ}  \right)},$$
we obtain the stage-within-age model in matrix form, as posed and solved by Diamond et al..</p>




## Stable age distributions and population sizes


\subsection{The model}
Diamond et al.'s model provides us with a way of gaining insight into these questions. They used a stage-within-age structured model. This means they used a matrix model, in which each year class of fish (females only) has an age-specific fecundity and mortality rate. To estimate the fecundity and mortality within the first year, they developed a more detailed model of duration and mortality within key stages of larval development: egg (EGG), yolk-sac larva (YSL), ocean larva (OL), estuary larva (EL), early juvenile (EJ), and late juvenile( LJ). They made careful estimates of parameters relevant to each of these parameters, in each of two regions (the Gulf of Mexico and the South and Mid-Atlantic Bights). These estimates were calculated with some modeling assumptions. There may be some inaccuracies associated with these estimates. Nonetheless, for present purposes we will assume the Diamond et al. estimates  to be true reflections of current conditions. That is, these parameters apply to today's short-term demographic dynamics, but are not representative of the long-term evolutionary dynamics under which croaker life history evolved.

The m-file \verb"croaker2.m"  runs the Diamond et al. model. In this code, you can choose between parameters corresponding to either the Gulf or the Atlantic scenario. 
\begin{figure}[t]
\begin{center}
\scalebox{.6}{\includegraphics{croaker.eps}}
\caption[]{\label{fig1} Output of the croaker model. }
\end{center}
\end{figure}
That will bring up the results of the croaker matrix model (Fig. \ref{fig1}). There are four components to this plot. The top left plot shows the age distribution, present both as an analytical estimate (in red) and as a numerical result (in blue). The top right plot shows how the total population changes in time (again, red for analytical estimate, blue for numerical result). In the title, the long-term rate of population increase is shown (i.e., the leading eigenvalue of the population matrix).  The bottom left plot shows the cumulative survival probability through all the larval stages. It is labeled such that you can see how mortality affects the probability of surviving each of the stages. The bottom right plot shows the \textit{elasticities}, which are measures of the relative effects of different parameters on the rates of population increase.

Some caveats: First, the matrix model assumes no density dependence. That may be an appropriate assumption for low densities; it is sometimes but not always, and is rarely appropriate for very large populations (but see the next example!). Second, all analytical estimates are for long-term stable age distributions, where all the demographic parameters remain constant for many generations. Third, there is no stochasticity built into the model -- all conditions are deterministic and constant. As usual, these assumptions are wrong, but it is appropriate for you to consider \textit{how wrong are they}?


\subsection{Study Questions}
To use this model to study life history evolution, I have added a new component: the possibility to change egg size. There are two parameters through which you can manipulate life history to examine consequences for population increase or decrease. The first is simple: The parameter \verb"egg_investment_factor" is just a multiplier by which each female will increase or decrease the reproductive resources expended on each egg. For example, \verb"egg_investment_factor" \verb"="  \verb"2" implies that females make eggs with twice the resources, and consequently make half as many of them.

The second parameter is $\alpha$, which is the  exponential rate of growth during the larval phase. If egg size is larger, then presumably so is the larva. It then has a shorter development time, because it has less to grow, and the time by which development time is shorter is a function of $\alpha$. Large $\alpha$ implies fast growth, and small $\alpha$ implies slow growth.

Additional details are given in the original paper, which is in the \verb"Matrix_model" directory along with the matlab code.
Your tasks are to run the model for awhile to familiarize yourself with how it works, and then:
\begin{enumerate}
  \item Explore the initial transients in the population structure by setting the number of years the simulation runs (\verb"Nyears") to a small number. 
  \item Explore how the parameters affect the trajectory of the population, the age structure across years, and the stage structure within the larval period. What relationships exist between the elasticities, the cumulative larval survival probabilities, and the age distribution?
  \item Using the exponential rate of increase as a proxy for fitness, in which directions would you expect egg size (and possibly other life history parameters) to evolve as a result of human-induced mortality? Is this an appropriate proxy for fitness, or can you think of better ones? Does your analysis apply to other marine organisms as well?
\end{enumerate}
