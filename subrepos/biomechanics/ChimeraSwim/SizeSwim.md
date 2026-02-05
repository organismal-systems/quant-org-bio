# 📖️️ Allometries in early larval swimming
While there is good evidence that swimming is important in early-stage marine invertebrate larvae, there is much less clarity on exactly *why* it is important, *how* swimming confers benfits, and what are the *minimal requirements for swimming performance* to achieve those benefits.
A study by [](doi:10.1093/icb/icq090) asked whether there is evidence, in the swimming of extant early-stage larvae, of a minimum threshold or *standard* for upward swimming performance.

The hypothesized swimming performance standard is based on the idea that, across a diversity of taxa and their habitats, the benefits of swimming acrue only if it typically results in modulating environments, avoids predators or accomplishes other movement-related tasks to a meaningful extent within a meaningful time frame.
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

$$
F_{body} = F_{gravity}-F_{buoy}
$$ (fbod)

that must be overcome by ciliary propulsion increases in proportion to $L^3$.

Clearly, as the length scale $L$ increases, the body forces (gravity and buoyancy) will exceed the surface force (ciliary propulsion), so that increasingly large larvae will at some point be unable to swim.
Even before this limit is reached, the allometries of surface and body forces suggest that swimming speed should vary strongly with larval size.
However, [](doi:10.1093/icb/icq090)'s observations show that this expectation is not reflected in the actual swimming performance of early stage larvae.

Why?

