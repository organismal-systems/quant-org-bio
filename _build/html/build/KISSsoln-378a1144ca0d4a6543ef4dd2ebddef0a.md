# 💡️ Mathematical analysis of the KISS model
The KISS[^kiss] model is expressed as a [Partial Differential Equation (PDE)](../../../content/appendix/MathSum/pdes.md) for the changes of a population with density $p^*(t^*,x^*)$,
$$
\label{kiss1}
	\frac{\partial p^*}{\partial t^*} = D \frac{\partial^2 p^*}{\partial x^{*^2}} + \alpha p^*
$$
for an interval $x^* \in [0,L]$.[^in]

[^in]: The notation $\in[a,b]$ means "within the interval between $a$ and $b$", with [some notational details about whether the endpoints are included](wiki:Interval_(mathematics)). 

In Equation [](#kiss1), $^*$ implies dimensional variables:
- $p^*$ has units of $\frac{individuals}{length}$
- $t^*$ has units of $time$
- $x^*$ has units of $length$

The parameters also have dimensions:
- $\alpha$ has units of $\frac{1}{time}$
- $D$ has units of $\frac{length^2}{time}$
- $L$ has units of $length$

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
\begin{equation}
	\frac{\partial p^*}{\frac{1}{\alpha}\partial t^*} = \alpha \frac{\partial p^*}{\partial t} = D \frac{\partial^2 p^*}{\partial x^{*^2}} + \alpha p^*
\end{equation}
Dividing both sides by $\alpha$,
\begin{equation}
	\frac{\partial p^*}{\partial t} = \frac{D}{\alpha} \frac{\partial^2 p^*}{\partial x^{*^2}} + p^*
\end{equation}
We now define a non-dimensional position, scaled by $\sqrt{\frac{D}{\alpha}}$:
\begin{equation}
	x = \sqrt{\frac{\alpha}{D}} x^*,~ x^* = \sqrt{\frac{D}{\alpha}} x 
\end{equation}	
Substituting this into Equation [](#kiss1) gives
\begin{equation}
	\frac{\partial p^*}{\partial t} = \frac{D}{\alpha} \frac{\partial^2 p^*}{\frac{D}{\alpha} \partial x^{2}} + p^*  = \frac{\partial^2 p^*}{ \partial x^{2}} + p^*
\end{equation}
Population is scaled by a reference:
\begin{equation}
	p = \frac{p^*}{p_0},~ p^* = p~p_0
\end{equation}	
Divide by $p_0$:
\begin{equation}
	\frac{\partial p}{\partial t} = \frac{\partial^2 p}{ \partial x^{2}} + p
\end{equation}
Try a separable solution:
\begin{equation}
	p = s(x) e^{\sigma t}
\end{equation}
Substitution:
\begin{equation}
	\sigma s(x) e^{\sigma t} = \frac{\partial^2 s(x)}{ \partial x^{2}} e^{\sigma t} + s(x) e^{\sigma t}
\end{equation}
Simplify:
\begin{equation}
	0 = \frac{\partial^2 s(x)}{ \partial x^{2}} + (1-\sigma) s(x)
\end{equation}
Try $s(x)=\sin{\frac{\pi n x}{L}},~n=1,2,\dots$, where $L=\sqrt{\frac{\alpha}{D}}~L^*$, to fit boundary conditions; then, $\frac{\partial^2 s(x)}{ \partial x^{2}}=-\left(\frac{\pi n}{L}\right)^2 \sin{\frac{\pi n x}{L}}$:
\begin{equation}
	0 = -\left(\frac{\pi n}{L}\right)^2 \sin{\frac{\pi n x}{L}} + (1-\sigma) \sin{\frac{\pi n x}{L}} = \left(1-\left(\frac{\pi n}{L}\right)^2-\sigma\right) \sin{\frac{\pi n x}{L}}
\end{equation}
Can only be true for $1-\left(\frac{\pi n}{L}\right)^2-\sigma=0$. Rearranging:
\begin{equation}
	\sigma = 1 - \left(\frac{\pi n}{L}\right)^2
\end{equation}
Positive growth only for:
\begin{equation}
	\frac{\pi n}{L} < 1  
\end{equation}
or
\begin{equation}
	\pi n < L  
\end{equation}
Minimum value $n=1$:
\begin{equation}
	L > \pi  
\end{equation}

Dimensional form:
\begin{equation}
	L^* > \pi \sqrt{\frac{D}{\alpha}}   
\end{equation}

















[^kiss]: This model is due to Kierstead, Slobodkin and Skellam:  
Kierstead, H.; Slobodkin, L.B. The Size of Water Masses Containing Plankton Bloom. J. Mar. Res. 1953, 12, 141–147.  
Skellam, J.G. Random Dispersal in theoretical biology. Bull. Math. Biol. 1991, 53, 135–165; Reprinted from Biometrika 1951, 38,
196–218.
