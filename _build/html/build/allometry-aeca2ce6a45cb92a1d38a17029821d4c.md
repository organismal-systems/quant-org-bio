# 🏞️ Allometry: How organismal characteristics vary with size

One area in which Organismal Biologists use these ideas is in the study of [allometry](wiki:Allometry).
Allometry is the study of how organismal traits vary systematically with body length or similar metrics of size.
Allometric relationships have been found or hypothesized for many traits, including mass, morphology of limbs and other structures, locomotion and other behaviors, and physiological characteristics such as respiration and nutrient uptake.

A well-known example of an allometric relationshop is [Kleiber's law](wiki:Kleiber's_law), which posits that the basal metabolic rate of animals varies approximately as the animal's mass raised to the $\frac{3}{4}$ power:

```{figure} https://upload.wikimedia.org/wikipedia/commons/6/60/Kleiber1947.svg
:label: Kleiber
:alt: Kleiber's law graphic from Wikipedia
:width: 500px
:align: center

A plot of Kleiber's law, relating the metabolic rates of organisms to their sizes across a large range of sizes. See the Wikipedia article on [Kleiber's law](wiki:Kleiber's_law) for details.
```

Allometric relationships within taxonomic groups are usually determined by statistical analysis of observations across a range of organism sizes within the group.
These observations are most commonly plotted on log-log plots, and statistically analyzed to detect trends.
A line on a log-log plot represents a power law relationship, which can be expressed mathematically as 
$$
:label: K1
trait = c size^p,
$$
where $c$ is a constant, and $p$ is an exponent indicating the type of allometry.
Taking the log of both sides of [#K1] gives
$$
\log{trait} = \log{c} + p \times \log{ size}.
$$

For example, in [](kleiber), the trait is [Basal Metabolic Rate](wiki:Basal_metabolic_rate) in watts, $BMR$, the size metric is mass, $M$,and the hypothesized exponent is $p=\frac{3}{4}$, *i.e.*,
$$
BMR = 70~ M^\frac{3}{4}
$$
It is useful to distinguish two types of allometry, *isometric scaling* and *allometric scaling*.

## Isometric scaling
Isometric scaling is also known as *geometrical similarity*.
In isometric scaling, all linear proportions are held constant as overall size increases or decreases.
The spherical egg model in [the previous notebook](example.ipynb) is an example of isometric scaling.
In general, a series of isometrically scaled objects follow the so-called [square-cube law](wiki:Square-cube_law), stating that surface area is proportional to the length squared, and volume is proportional to length cubed.

## Allometric scaling
In allometric scaling, different organismal traits scale differently with metrics of size. 
For example, larger animals often have more robust bones than would be predicted by isometric scaling from smaller animals.
In a given organism, different traits may reflect either direct or indirect effects of isometric and allometric scaling.

For example, if a set of animals scaled isometrically, their weight might be expected to increase in proportion to the cube of their length.
However, following the [square-cube law](wiki:Square-cube_law), the cross-sectional area of their bones would increase only in proportion to the square of their length.
This is likely to result in much higher loading and risk of breakage in larger animals.

In this case, some traits of these animals might deviate from isometric scaling, and instead follow an allometric scaling.
For example, bones might increase in thickness faster than isometrically, or mass might increase slower than isometrically.
Either form of allometric scaling would tend to equalize the loading on bones, relative to isometric scaling.

