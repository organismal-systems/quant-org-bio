# 📖️  Model formulation: The Leslie matrix
We have now recapitulated the key elements of [](doi:10.1139/cjfas-57-10-2010)'s age-within-stage model.
To execute and analyze their model, [](doi:10.1139/cjfas-57-10-2010) borrowed tools for matrix mathematics from linear algebra (see the [overview of matrix methods used in population modeling](../../../content/appendix/MathSum/matrix.md)).
Specifically, the modeling terms itemized above can be written very concisely as a matrix multiplication,
$$
\mathbf{P}(t+1) = \mathbf{A} \mathbf{P}(t)
$$
As above, $\mathbf{P}(t)$ is the vector of the croaker populations in Year Classes 1-8 in year $t$.
The matrix $\mathbf{A}$ contains the terms of the age-structured model that specified how this population transitions to year $t+1$:

$$
\mathbf{A} = \begin{pmatrix}
\frac{F_1}{EIF} & \frac{F_2}{EIF} & \frac{F_3}{EIF} & \frac{F_4}{EIF} & \frac{F_5}{EIF} & \frac{F_6}{EIF} & \frac{F_7}{EIF} & \frac{F_8}{EIF} \\
S_{1} & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & S_{adult} & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & S_{adult} & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & S_{adult} & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & S_{adult} & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & S_{adult} & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & S_{adult} & 0 \\
\end{pmatrix}
$$
 
This matrix is in a common form in population modeling, called a **Leslie matrix**, in which non-zero terms appear only in the top row and the subdiagonal.

The interpretations of the non-zero terms are:  
- In the top row, each entry is the **age-specific fecundity**, which is the contribution of a female croaker in a given year class to the number of female eggs in the following year.  
    For example, $\frac{F_2}{EIF}$ is the fecundity of a female croaker in Year Class 2, $\frac{F_3}{EIF}$ is the fecundity of a female croaker in Year Class 3, *etc*.
    
- The *subdiagonal* terms, $S_{1}$ and $S_{adult}$, are the survival probabilities for each age class.  
    Specifically, $S_{1}$ is the probability an egg will survive its first year to become an adult in Year Class 2. 
	$S_{adult}$ is the probability a fish in Year Class 2 will survive to enter Year Class 3, *etc*.
    
With substitution into $\mathbf{A}$ of the larval life history parameters determining first-year survival, 
$$
S_{1} = e^{-\left( \mu_{EGG} T_{EGG} + \mu_{YSL} T_{YSL} + \mu_{OL} DF T_{OL} + \mu_{EL} T_{EL} + \mu_{EJ} T_{EJ} + \mu_{LJ} T_{LJ}  \right)},
$$
we obtain the stage-within-age model in matrix form, as posed and analyzed by [](doi:10.1139/cjfas-57-10-2010) but with the speculative addition of a potential evolutionary adjustment of egg size.




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
