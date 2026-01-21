# 💡️ Ordinary Differential Equations (ODEs)
Differential equations are equations that define functions  in terms of their rates of change -- that is,
their derivatives.
The power of calculus to describe physical and biological dynamics stems from the fact that many "rules" we know about them -- such as conservation laws --  are expressed in terms of differential equations.
For example, conservation of energy does not give us an explicit expression for how heat is distributed in an object.
Instead, it gives us an expression for the *rate of change} of heat in each part of that object, given an initial heat distribution.
Similarly, our understanding of population biology gives us insight into the rates of population change due to reproduction and mortality.
We then need to use the tools of calculus to figure out what the actual values of heat or population are in a given scenario.

Many biological models are expressed as [*Ordinary Differential Equations* (ODEs)](wiki:Ordinary_differential_equation) of the form
```{math}
:label: de1
\frac{d f}{d t} = g(f(t))~.
```
The "ordinary" in ODE means that the function has only one independent variable, in this case $t$, and that the rates of change depend only on the present value of $t$.
If the rate of change depends on previous values of $t$, the equation is of a form called a [*Delay Differential Equation* (DDE)](wiki:Delay_differential_equation) or an [*Integro-differential equation* (IDE)](wiki:Integro-differential_equation).
If there is more than one independent variable, the equation is a [*Partial Differential Equation* (PDE)](wiki:Partial_differential_equation).
PDEs are discussed in another section of these notes.

Differential equations are formulas for the rates of change of [conserved quantities](wiki:Conserved_quantity).
**A conserved quantity is anything that is measurable and that does not appear or disappear unaccountably.**
Energy, mass, momentum, and population are commonly studied conserved quantities in organismal biology, together with many others.
Equation [](#de1) is an *ODE* stating that the rate of change of the conserved quantity, $f(t)$, changes in $t$ according to the function $g(f)$.

A typical modeling strategy in Organismal Biology is to put the time derivative on the left of the equal sign (as in Equation [](#de1) above), and to list all the mechanisms that might lead to changes in $f$ on the right.
For example, if $f(t)$ represents population as a function of time, the ODE might be
```{math}
:label: de2
\frac{d f}{d t} = I(t) - E(t) + R(t) f(t) - \mu(t) f(t)~.
```
where $I(t)$ represents immigration, $E(t)$ represents emigration, $R(t)$ represents a specific growth rate, and $\mu(t)$ represents a mortality rate.
In Equation [](#de2), each of these rates is written as a function of $t$, implying that rates potentially change over time (e.g., according to time of day, across seasons, etc.).
Each of the rates also typically changes as a function of $f$ itself.
For example, the reproduction rate might have a form like
$$
R(t) = \alpha(t) f(t).
$$
This expression can be interpreted as saying that the reproduction rate is proportional to the current population, each individual of which has a time-varying reproduction rate of $\alpha(t)$.
You can imagine many other examples of *ODE*s relevant to your own work.

Another, more general form of ODE is
```{math}
:label: de3
g \left(\frac{d f}{d t},f(t) \right) = 0~.	 \label{eq:eqnODE2}
```
Some equations of the form in [](#de3) arise that cannnot be written in the form in [](#de1).
However, most biological models can be written in the form [](#de1) and are easier to work with in that form, so  [](#de1) is the form you are most likely to read in the literature and use in your own work.

## *ODE* Facts

Here are several key facts you should know about ODE's:
### The **order** of an *ODE*  

An equation is of order 1 (or "first order") if the highest derivative is the first derivative, $\frac{d f}{d t}$. 
Equations [](#de1) and  [](#de2) are examples.  
	
This equation for the rate of change of $x(t)$,
```{math}
:label: de5
m \frac{d^2 x}{d t^2} + c \frac{d x}{d t} = F(t), 
```
is **second order** because it has a second derivative.

This particular example is for the position, $x(t)$, of an organism of mass $m$ swimming with thrust force $F(t)$ and with drag coefficient $c$.
It is really a form of Newton's Law, $f = ma$, where $a = \frac{d^2 x}{d t^2}$ is the acceleration and $f = F(t) - c \frac{d x}{d t}$ is the net force.

### Coupled *ODE*s  
*ODE*s in which the conserved quantities affect each others' rates are said to be "coupled".

For example, the populations of a predator and its prey are typically coupled, because the number of predators affects the prey's population dynamics.
The converse is also true &ndash; the number of prey affects the predator's population dynamics &ndash; but the *ODE*s are coupled even if the influence goes in only one direction.

A combination of two coupled first order equations are equivalent to a second order system.
An example is
```{math}
:label: de4
\frac{d f}{d t} = f(t) + g(t)~,  \\	 
\frac{d g}{d t} = g(t) - f(t)~.
```
That's not an obvious fact, until you take the derivative of one of the equations (in this case, the second one):
$$
\frac{d^2 g}{d t^2} = \frac{d g}{d t} - \frac{d f}{d t},
$$
and use it to substitute for $\frac{d f}{d t}$ in the first equation.  After simplifying, the result is
$$
\frac{d^2 g}{d t^2} - 2 \frac{d g}{d t} + 2 g = 0,
$$
which is a second order equation.

This logic applies to higher order systems: 
- three first order equations are equivalent to a third order equation; 
- four first-order equations are equivalent to a fourth-order equation;
and so on. 

### Initial Conditions and Boundary Conditions
*ODE*s describe the rates of change, for example of a population over time.
Reasonably enough, to know what the population is in the future, it is not enough to know just the *ODE*.
You also have to know what the population is now, or was at some specific time in the past.
Depending on the context, this is called an **initial condition** or a **boundary condition**.

The important thing to know is that:
> To specify a solution to an ODE, you need *a number of initial conditions equal to the order* of the equation.

In a coupled ODE system, the number of conditions needed is the total of the orders of all the equations.

For example, if you have one population that changes in time according to , you need to know only the starting population, $f(0)$ &ndash; that is, *one* initial condition.
On the other hand, if you are considering two interacting populations, in a coupled system like [](#de4) or its alternative form as a single second order *ODE*, you need to know both starting populations, $f(0)$ and $g(0)$ &ndash; that is, *two* initial conditions.

These ideas are sometimes expressed in somewhat obscure mathematical jargon.  If you think about the physical situation that the equations represent (e.g., what would you set up an analogous experiment), your intuition will usually steer you in the right direction.

As another example to illustrate this intuition, consider Equation [](#de5).
*To calculate the position $x(t)$, you must know **both** the initial position, $x$, **and** and initial velocity, $\frac{d x}{dt}$.*
Both are required to calculate the acceleration, $\frac{d^2 x}{dt^2}$, from which the time course of velocity and position can be deduced.

### Linear and Nonlinear equations
An ODE is [linear](wiki:Linear_differential_equation) if the conserved quantity and its derivatives do not appear as products of each other, or in other "nonlinear" functions such as powers other than 1, exponents, trigonometric functions, *etc*.
For example, Equation [](#de5) is linear, because all the terms are proportional only to $x(t)$ and its derivatives.

In contrast, the following are *nonlinear*: 
$$
\frac{d f}{d t} = f^2(t)~,  \\	 
\left( \frac{d g}{d t} \right) ^2 = g(t)~,  \\
\frac{d h}{d t} = \sqrt{h(t)}~,  	 
$$
This equation is linear in $g(t)$ but nonlinear in $f(t)$:
$$
\frac{d f}{d t}  f(t) = g(t) + \frac{d g}{d t}
$$
That is, if you know $f(t)$ and solve for $g(t)$, you have a linear equation to solve, but if you know $g(t)$ and solve for $f(t)$, you have a nonlinear equation to solve.

> The distinction between linear and nonlinear is is important because most linear ODEs can be at least partly solved analytically. In contrast,  very few nonlinear ODEs can be solved analytically.  

Both types can usually be solved *numerically*, with a computer program that uses successive calculations of derivatives to closely approximate the solutions to *ODE*s. 
If an equation can be solved analytically (usually true only of linear equations, but there are exceptions) chances are good that symbolic manipulators like [Maxima](wiki:Maxima_(software)), Sage, Maple and Mathematica can quickly provide solutions for them.

### Equilibrium solutions to ordinary differential equations
Ordinary differential equations describe "instantaneous" rates of change -- given the current *state*, what is the *rate* of change?
For example, in a population that is limited by a resource like food, a very small population might enjoy a positive rate of change but an overcrowded population might decline.

Between those extremes is typically a population level that is exactly balanced &ndash; that is, for which the rate of change is zero.
That population level is called an *equilibrium*, a *steady-state solution*, or (if you are speaking with a mathematician) a *fixed point*. From our perspective, these terms mean the same thing and are pretty much interchangeable.

Suppose we are interested in a population that is governed by the (non-dimensional) logistic equation,
```{math}
:label: de6
\frac{d n}{d t}  = n (1 - n^2)
```
An equilibrium population is a choice of $n$ for which $\frac{d n}{d t} = 0$. 

Often equilibrium solutions are given some notation to distinguish them, such as $\bar{n}$. 
For this equation, there are three values of $n$ that result in zero rate of change:
1. $\bar{n} = 0$, i.e., when the population starts at zero it remains at zero;
2. $\bar{n} = 1$, i.e., when the population starts at 1 it remains at 1;
3. $\bar{n} = -1$, i.e., if the population could take on a value of -1 it would remain at -1. 

Note that while the third equilibrium is a valid mathematical solution, it is not a physically meaningful one -- populations cannot be negative.

**Be aware when you are manipulating mathematical models that there may be additional constraints (such as positivity for populations) that may not be expressed explicitly in the formulas, and that may make some apparent solutions biologically irrelevant.**[^lim]

[^lim]: In a properly presented model, constraints such as the valid range of variables (e.g., populations, lengths, masses, energy contents and many other quantities cannot take on negative values).

### Approximate solutions to nonlinear equations
Though nonlinear ODEs usually cannot be solved analytically in their complete forms, there are still useful analytical results that can be gotten from nonlinear ODEs.
Many of  those methods involve *linearization*, which means approximating a non-linear equation with a linear equation over a limited range.
With linearization, we can learn a lot about the dynamics of a physical or biological situation even when we cannot solve the original equation exactly. 

An important example involves the *stability* of equilibria.
Stability in this case concerns whether a system that starts *close to* but not *on* an equilibrium will move closer to the equilibrium or further from it. 
If it moves closer to the equilibrium, it is said to be **stable**.
If it moves further from the equilibrium, it is said to be **unstable**.

An intuitive example of a stable equilibrium is a pendulum hanging vertically downwards.
If this pendulum is pushed slightly off vertical, it will tend to return towards vertical; therefore the equilibrium of the pendulum hanging vertically downwards is stable.

Consider now a pencil balancing on its tip.
As long as it is perfectly vertical, it stays vertical &ndash;it is in equilibrium.
However, if it is the slightest bit off vertical, it will continue to fall over.
In reality, it is impossible to get a pencil perfectly vertical, and in any case there are constant disturbances from air movement, sound, *etc*.
So, the balancing pencil is a theoretical equilibrium solution but, because it is unstable, it cannot be realized in the real world.

Analogous situations apply to many organismal characteristics, for example populations.
If a population that is close to, but not exactly on, an equilibrium moves towards the equilibrium, that equilibrium is a *stable* equilibrium. 
If the population moves away from the equilibrium, it is an *unstable* equilibrium. 
FOr populations, as for pendulums and pencils, this distinction is critical because an unstable equilibrium can almost never be actually realized: 
Even if a population starts at exactly the equilibrium value, the slightest perturbation will move it permanently off. 
In contrast, a stable equilibrium "attracts" populations back after they have been perturbed.

#### Stability analysis for *ODE*s
Suppose we take the nondimensional logistic equation, [](#de6) as an example.
This is a non-linear equation that has two (biologically meaningful) equilibria: $\bar{n} = 0$ and $\bar{n} = 1$.  
We can use *linearization* to determine whether these equilibria are stable or unstable.

There are a few key steps in linearization:
1. First, we define 
$$
\hat{n} \equiv n(t) - \bar{n},
$$
so that $\hat{n}$ is the *perturbation* from the equilibrium $\bar{n}$.
It follows that
$$
n(t) = \bar{n} + \hat{n}.
$$
This does not limit us in any way, because no matter what $n(t)$ and $\bar{n}$ are, we can always find a $\hat{n}$ to make these equations true.

2. Next, we change notation by substituting $\bar{n} + \hat{n}$ for $n(t)$ in [](#de6):
$$
\frac{d \hat{n}}{d t}  =  (\bar{n} + \hat{n}) \left(1 - (\bar{n} + \hat{n}\right)^2) 
$$
which expands to
```{math}
:label: de7a
\frac{d \hat{n}}{d t}  =    \left( \bar{n}-\bar{n}^3 +(-3 \bar{n}^2+1) \hat{n} -3 \bar{n} \hat{n}^2 -\hat{n}^3  \right).
```
3. To determine whether or not the equilibrium $\bar{n}$ is stable, we can assume that the perturbation is very small
$$
\hat{n} \ll 1
$$
	In that case, $\hat{n}^2 \ll \hat{n}$ and so forth for higher powers.

	If powers of $\hat{n}$ are sufficiently small, we can *neglect* them (assume they're close enough to 0 that we can drop them from our equation).
	This give us the *linearized* equation, 

$$
\frac{d \hat{n}}{d t}  \approx    \left( \bar{n}-\bar{n}^3 +(-3 \bar{n}^2+1) \hat{n}   \right)
$$ (de8)

4. Equation  {eq}`de8` is a linear equation in $\hat{n}$, which we can solve by considering each of the equilibria, $\bar{n}$, in turn.
-  If we look at the equilibrium $\bar{n} = 0$, then
$$
\frac{d \hat{n}}{d t} \approx \hat{n}.
$$
Since we know that $\hat{n}>0$ (because populations cannot be negative), this equation shows that $\hat{n}$ will grow exponentially and so the equilibrium t $\bar{n}=0$ is unstable.[^apr]
In biological terms, this means that 
> An initially small population will always grow away from the zero-population equilibrium &ndash; that is, the species will persist.

[^apr]: The $\approx$ notation means "approximately equals", a reminder that we dropped terms in a way that is justifiable only when deviations from the equilibrium are very small.

- On the other hand, if we look at the equilibrium $\bar{n} = 1$, then
$$
\frac{d \hat{n}}{d t}  \approx    -2 \hat{n}.
$$
This equation shows that, when perturbed from the $\bar{n} = 1$ equilibrium, $\hat{n}$ will shrink exponentially and so that equilibrium is stable. In biological terms, this means that
> The population will rebound from perturbations, and tend to return to the $\bar{n} = 1$ equilibrium.

In summary, linearization, in which we examine the result of small perturbations from equilibria by approximating a nonlinear *ODE* with a linear one, has given us a summary of the overall dynamics:
- A small population will grow away from the near-zero equilibrium.
- A population near the $\bar{n}=1$ equilibrium will approach that equilibrium and return to it after small perturbations.

This example demonstrates how we can often get a fairly complete understanding of the dynamics of a system of nonlinear *ODE*s through linearization, even without obtaining a formula for the solution (which is possible in this case, but is often impossible).
