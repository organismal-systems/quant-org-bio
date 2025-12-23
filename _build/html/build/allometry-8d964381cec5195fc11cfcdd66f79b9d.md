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
trait = size^p,
$$
where $p$ is an exponent indicating the type of allometry.
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
In the case of bones, for example, the stresses on bones due to an animal's weight may scale isometrically and follow the [square-cube law](wiki:Square-cube_law).
In that case, isometrically scaled bones would sustain increasingly heavy loading as their cross-sections grew in proportion to length squared, while the loads on them grew in proportion to length cubed.
