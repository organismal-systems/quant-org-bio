# 🛼 Size-dependence of diatom biomass in mixed layers
Diatoms are a diverse and abundant group that represents a large fraction of [primary production](wiki:Primary_production) and oxygen generation in aquatic habitats worldwide.
Diatoms are major prey species for aquatic grazers, important hosts for aquatic pathogens and important competitors for other primary producers.
The impacts diatom populations have, in these roles and others, is strongly affected  by the [standing stock](wiki:Population_density) of diatoms of different sizes.

[Litchman *et al.* (2009)](https://www.pnas.org/doi/epdf/10.1073/pnas.0810891106) derived a model that uses observed of allometries of growth, nutrient uptake and nutrient storage quotas to test hypotheses about the outcomes of competition and evolution among populations of different-sized diatoms.
This model predicts, among other things, the size-specific standing stocks of diatoms across variation in [mixed layer](./MixedLayers.md) characteristics.

>In this Activity, we assume that the size-specific standing stock of diatoms (expressed as biovolume) is a **proxy** for the effects of mixed layer characteristics on primary production, prey availability to diatom grazers and intensity of competition among primary producers.

In making this assumption, we should be clear that it is a simplification.
The rationale for assuming that standing stock is a plausible proxy for trophic impacts is that prey availability to grazers is roughly proportional to the number of cells in the water, and the payoff per cell is roughly proportional to cell volume.
Litchman *et al.* lend support to this interpretation in their paper, by subsuming losses to higher trophic levels in their density-independent "background" mortality term[^mort].
While there is little discussion of this term in their paper, Litchman *et al.* were well aware of grazing and pathogen impacts on diatoms, and intended the size-independent mortality term to account for it.[^mod]
It is also plausible to assume that competition for light is affected by standing stock biovolume, and that competition for nutrients is largely determined by the standing stock of nutrients.

[^mod]: In fact, their motivation was in part to present an alternative to size-selective grazing in explaining diatom size distributions. The literature contains models that have a more resolved accounting of different classes of grazers, such as small and large zooplankton, with size-specific impacts on diatoms. However, those models do not resolve the specific effects of diatom allometry that Litchman *et al.* hypothesize to determine diatom size distributions in mixed layers.

[^mort]: That term is $\m N_i$, where $N_i$ is the number of cells of size class $i$ and $m$ is the mortality rate. See [this explanation of the model](./Litchman_etal2009.md) and the original paper for details.

## Variations in diatom biovolume
With these limitations in mind, we can use the model to look for broad trends in the population-level impacts of diatoms, across their size distribution and variations in mixed layer characteristics.

### Understanding the model interface
To understand how the model works:
1. Open an executable version of the [notebook](./DiatomSizeESS.ipynb) in Binder.
2. Select **Run all cells** under the **Run** menu. This sets up the graphical interface for the model.
3. Scroll down to the section labeled **Setting up diatom variants and mixed layer characteristics**. 
   The textboxes enable you to change the number and size of diatom classes, and the mixed layer characteristics.
   Leave these as the defaults for now, and **click on the Set up population** button.
4. Scroll down to the section labeled **Seeding the mixed layer with diatom variants**.
   These textboxes enable you to add populations of some or all diatom size classes.
   To seed the cells into the population, **click on the Seed cell population** button.
   
   Seeding cells is *additive*, meaning that if you click the button twice, it will add twice the selected cell populations. 
5. Scroll down to the section labeled **Setting mixing event intervals, and running the simulation**.
   These textboxes enable you to set the number of days betwen mixing events, the number of mixing intervals to run the simulation, and how many times to record data as the cell numbers, nutrient quotas and nutrient concentration change between mixing events. 

### Setting up a model investigation
Your task in this activity is to undertake a "mini-study", in which you use a systematic series of model runs to expose trends, which you then interpret in terms of the motivating questions and model assumptions.

In addressing the questions below, it is helpful to keep these points in mind:
#### The model should be run for many mixing periods.

As in many models, Litchman *et al.*'s model starts with potentially unrealistic initial conditions. 
That is, we do not know ahead of time what a reasonable starting population is for a given size class of diatoms.
	
The model is informative because the long-term model results are independent many aspects of the initial conditions.
For example, whether the initial population of diatoms is 1 or 10, in the long run the initial population is typically "forgotten" as the population settles into a periodic pattern timed by the mixing interval.[^per]

This means you have to run the model for a sufficiently long time to be periodic.
The model interface makes it easy to do this, because you can see from the [period-averaged plots](./averaged.png) whether the long term trend has approach a constant.
If it hasn't, you can simply click the **Run simulation** button.
	
[^per]:This is not always the case. For example, if the starting population of a given size class is 0, it will always be 0.)


### Does the variant with the largest standing stock win in competition?

### Is the standing stock of single variants higher, lower or the same as for multiple variants?

### Which variants, or combinations of variants, are most effective at taking up nutrients?



% &ndash; mediated by their impacts on diatom population dynamics &ndash;


Among the highly diverse characteristics of diatoms is their 
The consequences of diatom size &ndash; in particular, the 

Activities frame with linkages orgs w higher lower levels 



The point of this activity is to assess the average standing stock of diatoms, across different variants (or combinations of variants), mixing fractions and mixing intervals.

If we assume that the constant mortality rate $m$ represents grazing or pathogens, then $m$ times the standing stock represents the strength of that trophic interaction.



Run is long enough when top line is flat and others are decreasing, and results look the same when simulation is restarted.




This activity explores how cell size affects populations of diatoms in mixed layers.
[Litchman *et al.*](https://www.pnas.org/doi/epdf/10.1073/pnas.0810891106) (2009) analyzed the size distributions of diatoms in multiple marine and freshwater habitats.
They concluded that, within a wide range of diversity in all habitats, diatom size distributions were larger in marine than in freshwater habitats.

In looking for explanations for this difference, noted that smaller diatoms have some advantages over larger diatoms in growth and nutrient uptake rates.
Conversely, larger diatoms have some advantages in nutrient storage over smaller diatoms.
Litchman et al.* hypothesized that the different characteristics of mixed layers in marine *cs.* freshwater habitats accentuate the relative advantages of large and small diatoms, causing the differences in size distributions.

To understand the implications of the model Litchman *et al.* devised to explore this hypothesis, this activity leads you through

For comparability, we will use a standard set of diatom sizes for the basic model experiments (feel free to explore additional sizes if you want to):
\[ s=[2.5, 3.55, 5.0, 6.25, 7.5, 8.75, 10.0, 11.25] \] and on four mixing intervals, \[ T=[3,14,35,40] \] 
For these parameter combinations:

## Biomass of single variants

Make sure only one variant is present (i.e., with Number of Phytoplankton Size Classes set to 1 at the top of the worksheet). 
Use different values of $s$ and $T$ to determine:
- \textbf{what are the consequences for total biomass if diatom cells are of small or large sizes?} 
- \textbf{What are the consequences of long vs. short mixing intervals for biovolumes of different-sized diatoms?} 

In your answers, use the information in the time series of quotas and nutrients to help interpret the patterns you observe in biovolume. \textit{Note that different dynamics are best visualized using different Plotting Intervals. For example, Plotting Interval [0,8] might best show initial transients well, [0,100] might best show longer transients, and [98,100] might best show details of long-term population cycles.}
