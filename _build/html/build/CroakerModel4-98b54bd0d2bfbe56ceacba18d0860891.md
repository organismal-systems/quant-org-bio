# 📖️  Model formulation: The Leslie matrix
We have now recapitulated the key elements of [](doi:10.1139/cjfas-57-10-2010)'s stage-within-age model.
To execute and analyze their model, [](doi:10.1139/cjfas-57-10-2010) borrowed tools for matrix mathematics from linear algebra (see the [overview of matrix methods used in population modeling](../../../content/appendix/MathSum/matrix.md)).
Specifically, the modeling terms itemized above can be written very concisely as a matrix multiplication,
$$
\mathbf{P}(t+1) = \mathbf{A} \mathbf{P}(t)
$$
As above, $\mathbf{P}(t)$ is the vector of the croaker populations in Year Classes 1-8 in year $t$.

The matrix $\mathbf{A}$ contains the terms of the age-structured model that specified how the croaker population transitions from year $t$ to year $t+1$:

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
 
This matrix is in a common form in population modeling, called a [Leslie matrix](wiki:Leslie_matrix), in which non-zero terms appear only in the top row and the subdiagonal[^sbd].

[^sbd]: The *subdiagonal* of a matrix is the set of terms stretching diagonally downwards and to the right, starting from the first entry in the second row.

The interpretations of the non-zero terms are:  
- In the top row, each entry is the **age-specific fecundity**, which is the contribution of a female croaker in a given year class to the number of female eggs in the following year.  
    For example, $\frac{F_2}{EIF}$ is the fecundity of a female croaker in Year Class 2, $\frac{F_3}{EIF}$ is the fecundity of a female croaker in Year Class 3, *etc*.
    
- The subdiagonal terms, $S_{1}$ and $S_{adult}$, are the survival probabilities for each age class.  
    Specifically, $S_{1}$ is the probability an egg will survive its first year to become an adult in Year Class 2. 
	$S_{adult}$ is the probability a fish in Year Class 2 will survive to enter Year Class 3, *etc*.
    
With substitution into $\mathbf{A}$ of the larval life history parameters determining first-year survival, 
$$
S_{1} = e^{-\left( \mu_{EGG} T_{EGG} + \mu_{YSL} T_{YSL} + \mu_{OL} DF T_{OL} + \mu_{EL} T_{EL} + \mu_{EJ} T_{EJ} + \mu_{LJ} T_{LJ}  \right)},
$$
we obtain the stage-within-age model in matrix form, as posed and analyzed by [](doi:10.1139/cjfas-57-10-2010) but with the speculative addition of a potential evolutionary adjustment of egg size.

## Stable age distributions and population growth rates
Leslie matrices have some properties that are extremely useful for applications in population modeling.
Summarizing from the [overview of matrix methods used in population modeling](../../../content/appendix/MathSum/matrix.md):
> 1. The population in a Leslie matrix model always approaches a **stable age distribution**, in which the proportion of the population in each age class remains constant.
> 2. The size of the population in this stable age distribution always **increases or decreases geometrically**, by a constant factor each time increment (in this case, each year).

To understand how [](doi:10.1139/cjfas-57-10-2010) utilized these facts, we need to define some notation:
- $\mathbf{\hat{P}}$ is the stable age distribution approached by the croaker population.
    - If the population is proportional to $\mathbf{\hat{P}}$ in year $t$, it is also proportional to $\mathbf{\hat{P}}$ in year $t+1$.
	- From any starting age distribution, the croaker population will converge to having an age distribution increasingly similar to $\mathbf{\hat{P}}$ over each year-to-year transition.
	- $\mathbf{\hat{P}}$ is typically normalized, to have a unit population size or "vector length".
- $\lambda$ is the rate of geometric increase or decrease of the population, which is the discrete-time equivalent of [](wiki:Exponential_growth).
    - If $\lambda>1$, the population has a positive intrinsic rate of growth (*i.e.*, it is growing).
    - If $\lambda<1$, the population has a negative intrinsic rate of growth (*i.e.*, it is declining).
    - If $\lambda=1$, the population has a zero intrinsic rate of growth (*i.e.*, it is constant).

Putting these facts together, we can say that, in the long run (after initial transients have passed), the croaker age distribution in [](doi:10.1139/cjfas-57-10-2010)'s model will always converge to $\mathbf{\hat{P}}$.
Specifically, 
> - After the initial transients, the population in year $t$ is related to the population in year $t+1$ by
    $$
	\mathbf{P}(t)  = c \mathbf{\hat{P}} \\
	\mathbf{P}(t+1) =  c \lambda \mathbf{\hat{P}}
	$$
	where $c$ is a constant of proportionality specifying the population at time $t$.  
	- Following the same logic for years  $t+1$, $t+2$, *etc*.,
    $$
	\mathbf{P}(t+2) & = & \lambda \mathbf{P}(t+1) & = & c \lambda^2 \mathbf{\hat{P}} \\
	\mathbf{P}(t+3) & = & \lambda \mathbf{P}(t+2) & = & c \lambda^3 \mathbf{\hat{P}} \\
	\mathbf{P}(t+n) & = & \lambda \mathbf{P}(t+n-1) & = & c \lambda^n \mathbf{\hat{P}}
	$$
	where $n$ is the general case of *any* number of years after $t$.

## Elasticities
Because the intrinsic rate of growth, $\lambda$, is such a useful summary of the long-term trajectory of a croaker population in their model, [](doi:10.1139/cjfas-57-10-2010) investigated how changes in various natural and human-influenced factors affected this rate.

Specifically, they calculated a metric called the **elasticity** to quantify the sensitivity of $\lambda$ to various parameters.
Again summarizing from the [overview of matrix methods used in population modeling](../../../content/appendix/MathSum/matrix.md),
the elasticity for a given parameter $m$ is defined as
$$
E_m = \frac{m}{\lambda} \frac{\partial \lambda}{\partial m}
$$
$E_m$ is most commonly applied in cases where the variable parameter $m$ is an element in the transition matrix, $\mathbf{A}$, but it can also be very usefully applied to variables that contribute to those elements.

In our case, [](doi:10.1139/cjfas-57-10-2010) calculated elasticities for the mortality rates and durations of each larval stage, as well as for the adult demographic parameters.
To these, we can add our speculative Egg Investment Factor, $EIF$.
