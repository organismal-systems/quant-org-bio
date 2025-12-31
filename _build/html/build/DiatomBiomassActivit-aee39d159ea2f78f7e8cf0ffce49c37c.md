# 🛼 Size-dependence of diatom biovolume in mixed layers: Mini-study rationale

[Litchman *et al.* (2009)](https://www.pnas.org/doi/epdf/10.1073/pnas.0810891106)'s model used allometries of growth, nutrient uptake and nutrient storage quotas to predict the size-specific standing stocks of diatoms (expressed as biovolume) across variation in [mixed layer](./MixedLayers.md) characteristics.

In this Activity, we assume that that
> - The size-specific standing stock of diatoms is a **proxy** for primary production and availability to grazers and pathogens.
> - The mixed layer nutrient is a **proxy** for the intensity of competition among primary producers.

By "proxy", we mean that standing stocks and nutrient concentration is in some way an indicator, for example by being proportional or indicating increasing or decreasing trends.
In making this assumption, we should be clear that using proxies in this way is a simplification, but that the results may notetheless be informative.

## Grazers and pathogens
The rationale for assuming that standing stock is a plausible proxy for trophic impacts is that:
- prey availability to grazers is roughly proportional to the number of cells in the water; and,
- the payoff per cell (nutritional gain for grazers, or replicates for pathogens) is roughly proportional to cell volume.

Therefore the product of cell number and cell volume &ndash; that is, the biovolume &ndash; is roughly proportional to the "payoff" for a grazer or pathogen. 


Litchman *et al.* lend support to this interpretation in their paper, by subsuming losses to higher trophic levels in their density-independent "background" mortality term[^mort].
While there is little discussion of this term in their paper, Litchman *et al.* were well aware of grazing and pathogen impacts on diatoms, and intended the size-independent mortality term to account for it.[^mod]
It is also plausible to assume that competition for light is affected by standing stock biovolume, and that competition for nutrients is largely determined by the standing stock of nutrients.

[^mod]: In fact, their motivation was in part to present an alternative to size-selective grazing in explaining diatom size distributions. The literature contains models that have a more resolved accounting of different classes of grazers, such as small and large zooplankton, with size-specific impacts on diatoms. However, those models do not resolve the specific effects of diatom allometry that Litchman *et al.* hypothesize to determine diatom size distributions in mixed layers.

[^mort]: That term is $\m N_i$, where $N_i$ is the number of cells of size class $i$ and $m$ is the mortality rate. See [this explanation of the model](./Litchman_etal2009.md) and the original paper for details.

## Primary production
The rationale for assuming that standing stock is a plausible proxy for primary production is that:
- primary production is roughly proportional to the number of cells in the water; and,
- a large diatom cell likely has faster primary production than a small diatom cell; since the model does not have a more detailed calculation for this size dependence, cell volume is the best available metric.

Therefore the product of cell number and cell volume &ndash; that is, the biovolume &ndash; is roughly proportional to the size-specific diatom primary production. 

## Competition for light and nutrients
Diatoms compete with other primary producers for light and nutrients.

The rationale for assuming that standing stock is a plausible proxy for competition for light is that:
- shading is roughly proportional to the number of cells in the water; and,
- a large diatom cell likely has stronger shading effects than a small diatom cell; since the model does not have a more detailed calculation for this size dependence, cell volume is the best available metric.

Therefore the product of cell number and cell volume &ndash; that is, the biovolume &ndash; is roughly proportional to the size-specific competitive impacts of diatom cells due to shading.

The rationale for assuming that standing stock is a plausible proxy for light is that:
- the model directly calculates the availability of nutrient (nitrate) in the mixed layer; and,
- it is assumed that the mixed-layer nutrient concentration is the limiting resource for diatom growth, so it is plausible that is also limiting for other primary producers.

Therefore the mixed-layer nutrient concentration, $R$, is a plausible metric for size-specific competitive impacts of diatom cells due to nutrient limitation.
