# 💡️ Calculus
The basic tool of calculus is the [derivative](wiki:Derivative), which represents the *rate of change* or *slope* of a function at a particular point. 
```{figure} ./images/sketch3.png
:label: sk3
:alt: Two points on the function $f(t)$
:align: center
:width: 400
Two points on the function $f(t)$ indicating "rise over run" over an interval in $t$.
```
As you can see from a sketch ([](#sk3)), you can obtain this slope by drawing a line through two points on the curve -- the point at which the derivative is to be taken, and another nearby point -- and sliding the second point closer and closer to the first point (without actually reaching it). 
The derivative is defined in the same way, using mathematical notation instead of the sketch.

For example, to find the derivative at $t_0$ of the function $f(t)$, we would calculate the function's value at $f(t_0)$ and $f(t_0 + \Delta t)$ (the first and second points, respectively). 
The slope of the line between them is the ``rise over run'',
```{math}
:label: eq1
\frac{f(t_0 + \Delta t) - f(t_0)}{\Delta t}
```
Sliding the second point towards the first amounts to taking the *limit* $\Delta t \rightarrow 0$.
This means having $\Delta t$ get closer and closer to 0, without actually substituting $\Delta t = 0$ (because that would be dividing by zero and wouldn't give a meaningful result).

Using the limit, the derivative ( = the slope) of $f$ at $t_0$ is 
```{math}
:label: eq2
\frac{d f}{d t} \equiv \lim_{\Delta t \to 0}\frac{f(t_0 + \Delta t) - f(t_0) }{ \Delta t } ~~.
```
The $\equiv$ symbol implies a definition, rather than an equality. So, the statement above reads
> We define $\frac{d f }{ d t}$ as $\dots$ 

### Additional notation
Sometimes derivatives are written as 
> $\frac{d }{ d t} f$, $f'$, or $\dot{f}$,

all of which are equivalent (depending on the context) to $\frac{d f }{ d t}$.

A well-written narrative will make it explicitly clear how to interpret notation for derivatives and all other applications.


## Useful facts
### Higher derivatives
- The derivative of the derivative is the second derivative, written 
$$
\frac{d^2 f }{ dt^2}.
$$
   This represents the rate of change of the rate of change, which is the curvature of the function $f(t)$.  

- The *n*th derivative is written  
$$
\frac{d^n f }{ dt^n},
$$
	and is the result of sequential differentiation *n* times.
	
An intuitive example is position as a function of time, $x(t)$:
- The first deriviative of position, $\frac{d x}{dt}$, is *velocity*; this makes sense because velocity is the rate of change of position.
- The second deriviative of position, $\frac{d^2 x}{dt^2}$, is *acceleration*; this makes sense because acceleration is the rate of change of velocity, *i.e.*, the rate of change of the rate of change of position.

### The Chain Rule
The *chain rule* applies in a case like $f(g(t))$, *i.e.*, when $f$ is a function of $g$ and $g$ is a function of $t$.
- The derivative of $f(g(t))$ with respect to $t$ is just the product of two simple derivatives,
$$
\frac{d f }{ d t} = \frac{d f}{d g}.
$$
This situation arises surprisingly often in mathematical biology, so the Chain Rule is a handy thing to remember.

### Sums and differences
The derivative of a *sum* (or *difference*) of two functions is the sum (or difference) of the derivatives,
$$
\frac{d (f+g) }{ d t} = \frac{d f }{ d t} + \frac{d g }{ d t}
$$
$$
\frac{d (f-g) }{ d t} = \frac{d f }{ d t} - \frac{d g }{ d t}
$$
### Products
The derivative of a *product* of two functions is 
$$
\frac{d (f g) }{ d t} = g \frac{d f }{ d t} + f \frac{d g }{ d t}
$$
### Reciprocals
The derivative of the *reciprocal* of a function is 
$$
\frac{d  }{ d t} \left(\frac{1 }{ g} \right) = \frac{d (g^{-1}) }{ d t} = - g^{-2}  \frac{d g }{ d t} = ~-~
\frac{~\frac{d g
}{ d t}~ }{ g^2} 
$$
### Quotients
The derivative of a *quotient* of two functions is 
$$
\frac{d (f / g) }{ d t} = \frac{d (f g^{-1}) }{ d t} = g^{-1} \frac{d f }{ d t} + f \frac{d (g^{-1}) }{ d t}
$$

## Some functions and their derivatives
### Constants
If $c$ is a constant,
$$
\frac{d c }{ d t} = 0.
$$

### Polynomials
The derivative of $t^n$ where $n$ is any number \underline{other than zero} is
$$
\frac{d t^n }{ d t} = n t^{n-1}~,~n \ne 0
$$
*Note*: $t^0 = 1$ (a constant) so its derivative is zero.

### Natural logarithms
The derivative of $\log(f(t))$ or $\ln(f(t))$  is
$$
\frac{d \log(f(t)) }{ d t} = \frac{1 }{ f(t)}~~.
$$

> Note that $\log(f(t))$ or $\ln(f(t))$ are both ways to write the ``natural log'', which is the log base $e$.

Unlike what we're used to in some other contexts, in mathematics it is always assumed that **log** is the natural log, unless it is explicitly stated otherwise.  

Log base $x$ is generally written $log_{x}$, as in $log_{10}(f(t))$ for base 10, $log_{2}(f(t))$ for base 2, *etc*.

### Exponentials
The derivative of $\exp(t) = e^{t}$ is easy to remember:
$$
\frac{d }{ d t} ~ e^{t} =  e^{t} ~~.
$$
If you remember that, you can show using the chain rule that the derivative of $\exp(f(t)) = e^{f(t)}$ is
$$
\frac{d }{ d t} ~ e^{f(t)} = \frac{d f }{ dt }~ e^{f(t)} ~~.
$$

## Integrals
There are two basic ways to think about [integrals](wiki:Integral).
The intuitive way is that integrals represent *areas under a curve*.
For example, the area, $A$, under the curve $f(t)$ between $t_0$ and $t_1$ is
$$
A = \int_{t_0}^{t_1} f(t) dt
$$
The more mathematical way is to think about integrals is as *anti-derivatives*, so
that if
$$
F(t) = \int f(t) dt
$$
then
$$
f(t) = {d F }{ d t }~~.
$$
A key practical fact is that we can get expressions for the derivatives of many functions.
However, there are many functions whose integrals we cannot express analytically.  

For many of those, we can get a *numerical solution* on a computer, although there are cases where that is also difficult.

Note that the first of the above examples is a **definite integral**, meaning that it has a specific range over which the integration is to be applied (in this case, between $t_0$ and $t_1$).

The second example is an **indefinite integral**, meaning that the range is not specified.

A key distinction between definite and indefinite integrals is that (assuming other parameters are specified) *the definite integral has a specific numerical value, while the indefinite integral is a function* (of the lower and upper limits). 

If you remember that the integral means the area under the curve, then this distinction makes sense and is easy to remember &ndash; the area under a curve does not have a specific value until you specify starting and ending values.

## Taylor Series
In many applications it is useful to approximate the values of a function in the neighborhood of a point as polynomials using the derivatives at that point.
This approximation is called a [Taylor Series](wiki:Taylor_series), and is written
```{math}
:label: tay
f(t_1) = f(t_0) + f'(t_0) (t_1 - t_0) + \frac{f''(t_0) }{ 2!} (t_1 - t_0)^2 + \frac{f'''(t_0) }{ 3!} (t_1 - t_0)^3 + \dots
```
In Equation [](#tay), the $'$ implies a derivative with respect to $t$, and the $!$ implies the [factorial](wiki:Factorial) (e.g. $4! = 1 \times 2 \times 3 \times 4$).

The $\dots$ implies that this is an infinite series, but in most applications only the first few terms are used.








