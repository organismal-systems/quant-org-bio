# 📖️ A speculative evolutionary scenario
[](doi:10.1139/cjfas-57-10-2010) carried out a detailed statistical analysis in which they estimated all the key parameters discussed so far.
In addition to reproducing their modeling approach and results, we can add a new dimension to predictions of croaker population trajectories by speculating about evolutionary changes through which croaker life history might adjust to increases or decreases in mortality.
This is of particular interest in the case of addition of significant fishing mortality to populations that evolved without this type of mortality. 

In other fish species, a variety of life history changes have been observed in response to anthropogenic stresses. 
For example, a species in which large adults are heavily fished might evolve towards allocating more resources to reproduction and fewer to growth in small adults. 
Note that this is a different phenomenon than a simple change in the relative frequency of different age or size classes, which might result directly from fishing mortality without any evolutionary changes.
    
An implication from [](doi:10.1139/cjfas-57-10-2010) is that conditions had changed relative to historical patterns at the time of their study, at least in fishing-induced mortality and possibly in many other ways.
Thus, there is reason to speculate that croaker life history parameters might evolve away from current values, if those changes increase reproductive success.

## Evolution of egg size
Here, we will consider changes in only one life history parameter: egg size.
If we assume females have a specific amount of resources to invest in eggs, they face a trade-off between allocating those resources to more, smaller eggs or to fewer, larger eggs.
There is a large literature on the evolution of egg size.
Changes in egg size have consequences for sperm-egg encounter rates, for movement through the water column, for predation rates, for development times, and many other factors in larval life history.
Here, we will focus on one possible effect of a hypothetical change in egg size, which is the development time of early larval stages.

We will assume that an Ocean Larva must reach a critical size before it is able to transition into an Ocean Larva.
To do so, it must feed in the plankton.
This takes time during which it has a high probability of dying.
If a larva starts from a larger egg, it has less growing to do before it can transition.
Hence, its duration in the Ocean Larval stage is shorter, and its probability of surviving commensurately higher.

In this lab, we consider a scenario in which (over evolutionary time) females can adjust their egg size relative to the currently observed size by an Egg Investment Factor, $EIF$. 
If so, constraints on total maternal investment mean that the number of eggs must decrease by a factor of $\frac{1}{EIF}$. 
Then, the population of female eggs in the $t+1$st year will be
$$
p_1(t+1) = \frac{1}{EIF} \sum_{i=1}^8 F_i~p_i(t)
$$
The other side of the egg-size tradeoff is the effect on larval duration, and hence on survival probability.
We will assume that the effect of changed egg size is by changing the duration of the Ocean Larva stage, because this is the first stage at which the larva acquires resources by feeding. We define a Duration Factor, $DF$, by assuming that growth is exponential during the OL stage in Diamond et al.'s model (this is an assumption because they specify only the total duration of each larval stage, not the growth progression within it). Our assumption is unproven, but plausible -- many models assume growth rate is proportional to body size, because larger consumers often encounter more and larger resources. If we accept this assumption, the duration of the OL stage, $T_{OL}$, is changed by a factor
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
