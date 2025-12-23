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
In a [previous page](example.ipynb), we considered the surface area, $A$, and volume, $V$, of a spherical egg.
We could expect that $A$ and $V$ have signicance for an egg's biology. 
For example, we might expect its mass to be roughly proportional to its volume; that mass may have functional consequences for respiratory demands, development time, sinking or rising rates, etc.
Likewise, we might expect its surface area to be related to gas exchange rates, encounter probability with sperm or pathogens, and other factors.
In this simplified example, these serve as a biological motivation for understanding how surface area and volume vary with size.

Because spheres have the same shape, all spheres are geometrical scale models of each other.
Across the set of spheres, there is a single parameter, the diameter $d$, that specifies a unique sphere.
Knowing $d$, we can calculate the surface area $A$ and volume $V$ using familiar formulas:
- $A = \pi d^2$
- $V = \frac{\pi}{6} d^3$

Anticipating more complicated and realistic applications in Organismal Biology, let's suppose we did not know these formulas.
In that case, we would expect to conduct a series of observations in which we **measure** the surface area and volume of a series of spheres of various sizes.
We could then use interpolation or curve-fitting to estimate the surface area and volume of spheres within the range of our measurements.

Instead, lt's consider using nondimensional ratios to express the formulas for $A$ and $V$, in a more general form with fewer parameters.
We'll start by choosing a characteristic length, $L$.
The geometry of the egg suggests that the most useful choice of characteristic value is the length scale corresponding to the diameter, 
- $L = d$.
From their units ($m^3$ for $A$, $m^3$ for $V$) we can anticipate that surface areas of shapes generally scale isometrically with the length scale squared, $L^2$, while the volume scales with the length scale cubed, $L^3$.
We know this because there is no other way to construct a quantity with the units of area and volume using the only available characteristic dimension, $L$.

Knowing that $A \propto L^2$ and  $V \propto L^3$, we can set about measuring the constants of proportionality.
Doing so for a conveniently sized sphere, we find that
- $c_{A_{sphere}} = \frac{A}{L^2} = \pi$
- $c_{V_{sphere}} = \frac{V}{L^3} = \frac{\pi}{6}$

That is, our measurements tell us that the constant of proportionality $c_{A_{sphere}}$ of surface area to $L^2$ is $\pi$, and the constant of proportionality $c_{V_{sphere}}$ of volume to $L^3$ is $\frac{\pi}{6}$.

Having measured one sphere, we are done.
That is, knowing $c_{A_{sphere}}$ and $c_{V_{sphere}}$, we can write down $A$ and $V$ for spheres with *any* $L$ (even those too large or small to measure).
That beats making new measurements for tens or hundreds of different-sized spheres!

In words, the constants $c_{A_{sphere}}$ and $c_{V_{sphere}}$ are *shape factors*, that together with basic geometrical scaling tell us the surface area and volume of all spheres.

### What did we just do?
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

























