# 💡️ Mathematical analysis of the KISS model
The KISS[^kiss] model is expressed as a [Partial Differential Equation (PDE)](../../../content/appendix/MathSum/pdes.md) for the changes of a population with density $p^*(t^*,x^*)$,
$$
\label{kiss1}
	\frac{\partial p^*}{\partial t^*} = D \frac{\partial^2 p^*}{\partial x^{*^2}} + \alpha p^*
$$
for an interval $x^* \in [0,L^*]$.[^in]

[^in]: The notation $\in[a,b]$ means "within the interval between $a$ and $b$", with [some notational details about whether the endpoints are included](wiki:Interval_(mathematics)). 

In Equation [](#kiss1), $^*$ implies dimensional variables:
- $p^*$ has units of $\frac{individuals}{length}$
- $t^*$ has units of $time$
- $x^*$ has units of $length$

The parameters also have dimensions:
- $\alpha$ has units of $\frac{1}{time}$
- $D$ has units of $\frac{length^2}{time}$
- $L^*$ has units of $length$

The KISS model assumes that a population is initially present in a 1-dimensional habitat of size $L$.
The key question addressed by the KISS model is, 
> - How large does habitat size $L$ have to be for the population to persist?

This page develops two aspects of the KISS model.
The first is *non-dimensionalizing* the KISS mode. 
This analysis will show that all KISS models are **scale models** of each other.
That is, a KISS model with any choices of $\alpha$ and $D$ are rescaled versions of the "non-dimensional" KISS model with $\alpha = D = 1$.
The second is an exact analytical solution for the KISS model. 

## Non-dimensionalizing the KISS model
To derive the non-dimensional KISS model, we begin by defining a non-dimensional time, scaled by $\frac{1}{\alpha}$:
\begin{equation}
	t = \alpha t^*,~ t^* = \frac{1}{\alpha} t 
\end{equation}	
Substitution into Equation [](#kiss1) gives
$$
	\frac{\partial p^*}{\frac{1}{\alpha}\partial t^*} = \alpha \frac{\partial p^*}{\partial t} = D \frac{\partial^2 p^*}{\partial x^{*^2}} + \alpha p^*
$$
Dividing both sides by $\alpha$,
$$
\label{kiss4}
	\frac{\partial p^*}{\partial t} = \frac{D}{\alpha} \frac{\partial^2 p^*}{\partial x^{*^2}} + p^*
$$
We now define a non-dimensional position, scaled by $\sqrt{\frac{D}{\alpha}}$:
\begin{equation}
	x = \sqrt{\frac{\alpha}{D}} x^*,~ x^* = \sqrt{\frac{D}{\alpha}} x 
\end{equation}	
Substituting this into Equation [](#kiss4) gives
\begin{equation}
	\frac{\partial p^*}{\partial t} = \frac{D}{\alpha} \frac{\partial^2 p^*}{\frac{D}{\alpha} \partial x^{2}} + p^*  = \frac{\partial^2 p^*}{ \partial x^{2}} + p^*
\end{equation}
Population is scaled by a reference population density, $p_0 = \frac{N_0}{L}$:
\begin{equation}
	p = \frac{p^*}{p_0},~ p^* = p~p_0
\end{equation}	
Substituting and dividing by $p_0$,
$$
\label{kiss8}
	\frac{\partial p}{\partial t} = \frac{\partial^2 p}{ \partial x^{2}} + p
$$
Equation [](#kiss8) is the non-dimensional form of the KISS model, for a population constrained to a habitat of non-dimensional size $L=\sqrt{\frac{D}{\alpha }} L^*$, which was the goal of the analysis.

## Solution of the non-dimensional KISS model
To obtain an exact analytical solution for Equation [](#kiss8), we can use an approach called [Separation of Variables](wiki:Separation_of_variables).
This technique boils down to trying whether an equation involving two independent variables (in this case, $t$ and $x$) can be solved as a product of a function of $t$ alone with a function of $x$ alone.
This succeeds for only some types of PDEs; the KISS model is one of them.

To obtain a separable solution, we assume a solution of the form:
\begin{equation}
	p = s(x) e^{\sigma t}
\end{equation}
Substitution into Equation [](#kiss8) gives
\begin{equation}
	\sigma s(x) e^{\sigma t} = \frac{\partial^2 s(x)}{ \partial x^{2}} e^{\sigma t} + s(x) e^{\sigma t}
\end{equation}
This simplifies to an Ordinary Differential Equation in $x$,
$$
\label{kiss11}
	0 = \frac{\partial^2 s(x)}{ \partial x^{2}} + (1-\sigma) s(x),
$$
that is well-known to have solutions in the form of sines and cosines.

Knowing this, we can infer that the solution will look like
$$
\label{kiss12}
s(x)=\sin{\frac{\pi n x}{L}},~n=1,2,\dots
$$
This is because only this set of sine functions satisfy the boundary conditions of zero population at the habitat edges, $p(t,0)=p(t,L)=0$.

From Equation [](#kiss12),
$$
\frac{\partial^2 s(x)}{ \partial x^{2}}=-\left(\frac{\pi n}{L}\right)^2 \sin{\frac{\pi n x}{L}}
$$
After substituting these expression in Equation [](#kiss11) and simplifying,
$$
\label{kiss13}
	0 = \left(1-\left(\frac{\pi n}{L}\right)^2-\sigma\right) \sin{\frac{\pi n x}{L}}
$$

Because $ \sin{\frac{\pi n x}{L}}$ is not zero within the habitat, Equation [](#kiss13) can be true only if
$$
1-\left(\frac{\pi n}{L}\right)^2-\sigma=0
$$

Rearranging, we obtain the growth rate of a population with a distribution like Equation [](#kiss11):
$$
\label{kiss15}
	\sigma = 1 - \left(\frac{\pi n}{L}\right)^2
$$
This completes the analytical solution of the non-dimensional KISS model

#### Persitence *vs*. extinction
From Equation [](#kiss15), we can see that the population growth rate $\sigma$ is positive only when
\begin{equation}
	\frac{\pi n}{L} < 1  
\end{equation}
or
\begin{equation}
	\pi n < L  
\end{equation}
The minimum value of $L$ occurs when $n=1$, in which case
\begin{equation}
	L > \pi  
\end{equation}
This is the critical non-dimensional habitat size, which is the minimum that can support a growing population.
All smaller habitats lead to extinction.

In dimensional form, the critical habitat size is
\begin{equation}
	L^* > \pi \sqrt{\frac{D}{\alpha}}   
\end{equation}

















[^kiss]: This model is due to Kierstead, Slobodkin and Skellam:  
Kierstead, H.; Slobodkin, L.B. The Size of Water Masses Containing Plankton Bloom. J. Mar. Res. 1953, 12, 141–147.  
Skellam, J.G. Random Dispersal in theoretical biology. Bull. Math. Biol. 1991, 53, 135–165; Reprinted from Biometrika 1951, 38,
196–218.
