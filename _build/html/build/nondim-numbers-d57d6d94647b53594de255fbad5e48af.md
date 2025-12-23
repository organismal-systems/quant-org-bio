# 📖 Non-dimensional numbers
The idea that *similarity of proportions generalized to include both geometries and forces* as required for dynamic similarity is most practical to work with using **non-dimensional numbers**.
Dimensions, in this context, refers to measurements in physical units (such as SI units: meters, seconds, kilograms, etc.).
"Non-dimensional numbers" is somewhat strange terminology, because by nature pure numbers are not associated with any physical dimensions.
In this context, though, "non-dimensional" refers to ratios that have no dimensions because the units of the numerator are the same as the units of the denominator.
That is, **non-dimensional numbers are composed of factors with units (lengths, times, masses, etc.) but they are nonetheless non-dimensional because the units of their factors cancel.**

Many non-dimensional numbers have been devised in diverse fields of science.
Some of these are listed, together with their physical interpretations, in [this Wikipedia page](https://en.wikipedia.org/wiki/List_of_dimensionless_quantities).

Non-dimensional numbers are useful in quantitative sciences for two reasons:
1. Many phenomena are governed by non-dimensional combinations of parameters, which is made explicit in the form of non-dimensional numbers. 
By using non-dimensional numbers as "meta" parameters, these phenomena can be understood and predicted using far fewer variables than in the original dimensional form.
2. Non-dimensional numbers in which the denominator and the numerator reflect different mechanisms can be indicators of the relative importance of those mechanisms, across variation in important parameters such as size, speed, duration, etc.

Because non-dimensional numbers are not intuitive the first few times they are encountered, it's worth delving into some further explanation of these ideas.

## Characteristic values

A good starting point for thinking about non-dimensional numbers is to consider the fact that adjectives like big, small, fast, slow, etc. are *relative* descriptions.

That is, nothing is big or small except in comparison to something else.
In our ordinary thinking, that something else is a standard set of units.
For example, the fundamental SI unit for length is the meter.
An object a kilometer long is "big" compared to a meter -- it's equal to 1000 of them.
An object a micron long is "small", because it's only 1/1000th of a meter.

Suppose, instead, we adopt a complementary perspective, in which the basis for comparison comes from the object itself.
This depends on finding what are called **characteristic values**.
Characteristic values could include a length, speed or duration that emerges from the object or its interations with its surroundings.
These characteristic values specify a subset chosen from a set of scale models.

### Characteristic dimensions of an egg
Let's begin with an intentionally simplified example, that we completely understand: 
In the previous page, we considered the surface area, $A$, and volume, $V$, of a spherical egg.
Because spheres have the same shape, all spheres are geometrical scale models of each other.

Across the set of spheres, there is a single parameter, the diameter $d$, to specify a unique sphere.
Knowing $d$, we can calculate the surface area $A$ and volume $V$ using familiar formulas:
- $A = \pi d^2$
- $V = \frac{\pi}{6} d^3$

Let's consider using a non-dimensional ratio to express these formulas, in a more general form with fewer parameters.
We'll start by choosing a characteristic length, $L$.
The geometry of the egg suggests that the most useful choice of characteristic value is the length scale corresponding to the diameter, 
- $L = d$.

From this characteristic length $d$, we can substitute into the formulas for $A$ and $V$:
- $A = \pi L^2$
- $V = \frac{\pi}{6} L^3$

Dividing by $L^2$ and $L^3$ respectively,
- $\frac{A}{L^2} = \pi$
- $\frac{V}{L^3} = \frac{\pi}{6}$

Note that $L^2$ is the area of a square of length $L$ on each side, and $L^3$ is the volume of a cube of length $L$ on each edge.

These expressions show that in terms of the variables $\hat{A} = \frac{A}{L^2}$ and $\hat{V} = \frac{V}{L^3}$, the area and volume are
- $\hat{A} = \pi$
- $\hat{V} = \frac{\pi}{6}$

That is, expressed in these new variables, the area and volume are constant.
We have reduced the number of parameters from one to zero!

#### What did we just do?
In the lines above, we did not create any new formulas or data.
The only thing we did was to change variables, to express the diameter, area and volume in terms of a characteristic length, $L$.

As a result of this change in variables, 
- All the effects of **size** are encapsulated in the length scale, $L$. 
- All the effects of **shape** are encapsulated in the constants $\hat{A}$ and $\hat{V}$.

The shape effects hold for all spheres.
The result that one constant summarizes the surface area or volume of all spheres is a simplification from a list of measured volumes, and even from the formua that specifies it as a function of an infinite spectrum of diameters.

Because this formulation separates the effects of size from those of shape, we can expect that for this principle applies to any shape. 
For example, if the basic shape is an ellipsiod, a dodecahedron, or a lobster, the shape factor will be a new constant, but size effects will obey equations of the same form.

As stated, this example started with an extremely simple calculation, which the analysis made still simpler.
The real utility of non-dimensionalization is found in application to more complex problems, in which there are many independent variables and for which no formulas are available.
In these cases, including examples found in the following chapters of this book, a reduction in the number of parameters and an orderly separation of effects of different elements of the problem can be very useful and insightful.

























