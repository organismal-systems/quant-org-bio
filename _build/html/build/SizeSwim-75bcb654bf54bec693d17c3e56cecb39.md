# 📖️️ Morphologies that meet the challenge of early larval swimming
While there is good evidence that swimming is important in early-stage marine invertebrate larvae, there is much less clarity on exactly *why* it is important, *how* swimming confers benfits, and what are the *minimal requirements for swimming performance* to achieve those benefits.
A study by [](doi:10.1093/icb/icq090) asked whether there is evidence, in the swimming of extant early-stage larvae, of a minimum threshold or *standard* for swimming performance.

The hypothesized swimming performance standard is based on the idea that, across a reasonable diversity of taxa and their habitats, the benefits of swimming acrue only if it typically results in modulating environments, avoids predators or accomplishes other movement-related tasks to a meaningful extent within a meaningful time frame.
This idea is vague and difficult to assess in terms of swimming costs and benefits.
However, because the morphological traits that enable swimming are likely to impinge on other selective pressures on larval form, optimizing swimming performance likely has costs.
If so, it would suggest that morphological traits promoting swimming would be shaped to the point that meets the standard requirement, but does not exceed it.

Consistent with this idea, [](doi:10.1093/icb/icq090) found that, among the early-stage larvae of 13 diverse taxa, most (though not all) performed upwards swimming at rates around $300-400 \frac{\mu m}{s}$.

## Swimming allometries
[](doi:10.1093/icb/icq090)'s finding is interesting, because it is not a result that follows inevitably from simple allometries of swimming by ciliated spheroids. 

In particular, the expectation for ciliary propulsion is that the propulsive force, $F_{cilia}$, should increase roughly in proportion to the surface area of a ciliated spheroid, 
$$
F_{cilia} \propto L^2
$$
where $L$ is the "characteristic" length scale of the larvae (e.g. the cube root of its volume).
Reynolds number analysis shows that the fluid dynamical [drag force](../ReSphere/RSlookup.md) also scales as $L^2$.

In constrast, the force of gravity, $F_{gravity}$, is proportional to mass.
Assuming *isometric size changes* and *constant material properties*, the gravity force that must be overcome by ciliary propulsion increases in proportion to volume,
$$
F_{gravity} \propto L^3
$$
The buoyancy force, $F_{buoy}$, has the same scaling, so that the net body force, 
$$F_{body} = F_{gravity}-F_{buoy}$$
that must be overcome by ciliary propulsion increases in proportion to $L^3$.

Clearly, as the length scale $L$ increases, the body forces (gravity and buoyancy) will exceed the surface force (ciliary propulsion), so that increasingly large larvae will be unable to swim.
Even before this limit is reached, the allometries of surface and body forces suggest that swimming speed should vary strongly with larval size.
However, [](doi:10.1093/icb/icq090)'s observations show that this expectation is not reflected in the actual swimming performance of early stage larvae.

Why?

## Size-dependent changes in excess mass
The amount by which the density of a material exceeds the density of the fluid in which it is immersed is called **excess mass**, $\rho_{excess}$.
The net body force on an object is equal to the volume of the object, $V = L^3$, multiplied by its excess density.
$$
F_{body} = \rho_{excess} L^3
$$
[](doi:10.1093/icb/icq090) found that **larval swimming speed did not decrease as suggested by the allometries of ciliary propulsion and larval volume because the excess mass decreased with larval size.**
These changes were not subtle: the largest larvae measured had roughly $\frac{1}{10}$ the excess density of the smallest.
[](doi:10.1093/icb/icq090) hypothesized that this extreme decrease in excess density with increases in larval size were a specific adaptation to enable meeting a "standard" requirement for swimming performance.

How can excess density vary to this extent, if material properties stay approximately constant (or, at least, vary by nowhere near a factor of 10)?
The answer lies at least partly in the internal morphologies of early stage larvae.
As illustrated in [](#comp-blastulae), early stage marine invertebrate larvae have internal structures such as [blastocoels](wili:Blastulation), that contain materials differing in excess density from ordinary embryonic tissue.

Those materials, which may include fluid of unknown composition, lipids, calcium carbonate, have several distinct effects on swimming biomechanics.

First, they change the overall *average* excess density of a larva, which is the excess density that determines the overall body forces on an immersed object. 
For example, if a larva contains a given amount of tissue, its average excess mass is reduced if that tissue encloses a volume of fluid or lipid if relatively low density.
For isometric size increases, that decrease in excess mass is accompanied by an increase in external surface area to accommodate the increased internal volume.
If this additional surface area is ciliated, then the total ciliary force increases in rough proportion.

The resulting shift in the ratio of body to surface forces result in upwards swimming performance that varies little across a wide range of early-stage larval sizes.

## Stability and orientation in swimming larvae

are non-uniformly distributed within the developing embryo.








