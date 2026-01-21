# 💡️  Notes on Poisson Processes
A [Poisson process](wiki:Poisson_point_process) is a random algorithm that approximates many stochastic events in biology, such as the spatial distributions of organisms or the order and spacing of physiological or demographic events in time.
Often when we think intuitively of "random" distributions, we have in mind something very similar to distributions produced by Poisson processes.

More formally, a Poisson process is one that generates *Possion points*.
Poisson points satisfy the following conditions: 
1. The probability of $n$ individuals being present in a sample from an interval $[t_1,t_2]$ depends only on $n$, $t_1$ and $t_2$ for any $t_1$ and $t_2$.
2. The probabilities of samples $n_i, i = 1,\dots,m$ on $m$ distinct intervals are independent.
3. There is zero probability that a sample on a finite interval is infinite.

These conditions sound somewhat abstract, so it's worth getting a more intuitive explanation of what they mean.
Essentially, conditions 1 and 2 say that events in any interval are *independent*.
That means knowing what happened in the last interval does not give you any insight into what will happen in the next interval.
A familiar example is radioactive decay events &ndash; knowing whether an atom decayed in the last milisecond does not give you any additional predictive power about the next milisecond.
Condition 3 is mostly a invoked to insure that sums and integrals involving Poisson processes are well-defined.
Because no quantity relevant to Oganismal Biology is infinte, this condition is not of much concern to us.

Poisson processes are a pretty good approximation for many biological processes (as well as processes in physics, chemistry and many other fields).
By "pretty good", we mean that Poisson processes describe few biological scenarios *exactly*, but a large number of biological scenarios closely enough so that the results are numerically quite accurate.

## Poisson point facts

The importance of Poisson processes is that many useful analytical results exist for them.
If you cast your model in terms of a Poisson process, you can take advantage of the following facts[^pap]:

%[^pap]:In addition to many online references, *Probability, Random Variables, and Stochastic Processes*, A.  Papoulis, is a very comprehensive reference for Poisson processes and many other statistical tools. An older edition is available for free download.}: 

- If Poisson events occur randomly at a rate $\lambda$, then the expected number of events in a time interval $\Delta t$ is $\rho = \lambda \Delta t$.
  
-  The actual number occurring in a sample is a random variable, $n$.
   The probability that any given sample has the value $k$ is
$$
Pr ( n = k ) = \frac{\rho^k}{k!} e^{-\rho}
$$

- The **variance** of the number of Poisson points in an interval is equal to the **mean**. 
  That is,
$$
\mu_n =  E[n] = \rho
$$
and 
$$
\sigma^2_\mu = E[n^2] - E^2[n] = \rho
$$
where $E[]$ denotes expected value.

  Furthermore, the **mode** is also $\rho$, the **skewness** is $\rho^{-1/2}$, and the **excess kurtosis** is $\rho^{-1}$.

- If $t_i$ are a set of Poisson points with a density $\rho$, and $t_0$ is a fixed point in time, the time from $t_0$ to the $n$th Poisson point is a random variable, $\tau$, with the frequency distribution
$$
f_n(\tau) = \frac{ \rho^n}{(n-1)! } \tau^{n-1} e^{-\rho}
$$

  For example, the time to the *nearest* point is 
$$
f_1(\tau) =  \rho e^{-\rho}
$$
Note that because the numbers of Poisson points in distinct intervals are independent, the past has no predictive value about what will happen. 
For example, if encounters with predators are distributed in time like Poisson points, an encounter is made no more or less likely by the fact that a predator has recently been encountered.  

- If $\rho$ is sufficiently large, the Poisson distribution is closely approximated by a normal distribution with $\mu = \sigma = \rho$.

- The sample mean of an ensemble of estimates $n_1, n_2,\dots$ is an unbiased and efficient estimator of $\rho$.
Nonetheless, if $\rho$ is small the number of samples must be large to accurately estimate $\rho$.[^ran]

[^ran]: That is, is takes many samples to distinguish between $\rho=0.001$ and $\rho=0.0001$ because almost all the samples are 0.

- The difference $n_1 - n_2$, where $n_1$ and $n_2$ are independent Poisson variables with expected values $\mu_1$ and $\mu_2$, is  a random variable that has a [Skellam distribution](wiki:Skellam_distribution).
So, the probability that $n_1 - n_2 = k$ is
$$
Pr(k = n_1 - n_2) = e^{-(\mu_1 + \mu_2)} \left( \frac{\mu_1}{\mu_2} \right)^{k/2} I_k(2 \sqrt{\mu_1 \mu_2})
$$
where $I_k$ is the modified Bessel function of the first kind. (This is a "special function" that you can find in libraries like [Numpy](https://numpy.org/)).

This distribution can arise, for example, when an organism is attempting to decide which foraging area has greater resource density by comparing foraging success rates. 
If resources come in rare discrete packages, the difficulty of this estimation problem can place severe constraints on foraging success.

## Population density and probability density functions
The rate at which Poisson events occur do not have to be constant.
As an example, let's consider the spatial positions of one or more individuals.
We assume an individual's position at any given time is a Poisson random variable, in the spatial coordinate $x$.

In general, the probability that a Poisson event (that is, the occurrence of the individual) will occur at a given value of $x$ is given by its [probability density function](wiki:Probability_density_function), often abbreviated as ***pdf***.

For example, if $f(x)$ is the probability density function of a Poisson point, then the probability that it occurs somewhere in the interval $[x_1, x_2]$ is
$$
Pr(point~within~ [x_1, x_2]) = \int_{x_1}^{x_2} f(x) ~dx
$$
This equation actually defines the probability density function -- the *pdf* is the function that makes the above statement true for a given Poisson point process. 

The integral of the *pdf* over the entire range of possible positions is one, because (assuming the point exists) it has to be at exactly one value of $x$.

It is important to understand the distinction between *population density* and *probability density*.
The population density, $p(x)$, is the function that specifies how many individuals are in a given interval:
$$
N([x_1,x_2]) =  \int_{x_1}^{x_2} p(x) ~dx
$$
The integral of the population density over the entire range of possible positions is equal to the total population, $P$. 

It is often assumed that **a population is distributed as Poisson points with equal *pdf*'s**. If that is the case, then 
$$
N([x_1,x_2]) = P \int_{x_1}^{x_2} f(x) ~dx
$$
where $f(x)$ is the *pdf* of each individual in the population.

This is a very useful assumption, because many population statistics are then easy to calculate. 
In particular, this assumption is commonly used to estimate mean rates of reproduction, mortality, encounters with other organisms, etc. in the derivation of differential equations.

However, keep in mind two very important caveats. 
First, the actual biological processes are stochastic. 
The differences between the actual outcome and the expected outcome can in some cases qualitatively change the outcome of biological interactions. 
The [Wolf-Sheep-Grass  simulation](../../../subrepos/spatial-dynamics/MesaWolfSheep/WolfSheepPersist.ipynb) is an example of this: the individual-based stochastic model has completely different dynamics than the ODE or PDE approximations to it.

The difference between the actual outcomes and the expected outcome is sometimes refered to as the [atto-fox](wiki:Lotka–Volterra_equations#Atto-fox) problem.
For example, suppose a model predicts that the local density of foxes is $10^{-18}$.
By any reasonable metric this means the foxes are extinct.
However, in *ODE* models, populations can decrease exponentially but they may never reach zero.
This means that there are always *some* predators around, and an atto-fox can always rebound to a large population given favorable conditions.

Second, many biological applications violate the assumptions of Poisson processes.
In many cases these violations don't matter too much, but in others the errors can be large.

For example, consider a predator-prey interaction.
The likelihood that a prey organism is at a location immediately adjacent to a predator is lowered by the presence of the predator &ndash; either the prey will move to avoid the predator, or the predator will eat it.
That is, the occurrences are not independent, violating the assumption that predators and prey can be described as Poisson points. 

An ODE model's estimate of encounter rates based on the Poisson point assumption might therefore overestimate the actual encounter rate. 
A consequence can be, for example, that the populations in the ODE model will go extinct while in the stochastic model they coexist.

