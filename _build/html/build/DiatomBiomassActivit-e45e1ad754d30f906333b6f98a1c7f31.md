# 🛼 Size-dependence of diatom biovolume in mixed layers: Mini-study procedure
With the rationales for interpreting standing stocks of diatoms and nutrient in mind, your task in this Activity is to execute a mini-study in which you tabulate model results to address the questions:
> Do primary productivity, availability to grazers and pathogens, and competitive impacts vary with diatom cell size?

> How do effects of diverse populations differ from the effects of single variants?

> Do primary productivity, availability to grazers and pathogens, and competitive impacts vary with mixing layer characteristics?



%> Does the variant with the largest standing stock win in competition?

%> Is the standing stock of single variants higher, lower or the same as for multiple variants?

%> Which variants, or combinations of variants, are most effective at taking up nutrients?

## Variations in diatom biovolume
With these limitations in mind, we can use the model to look for broad trends in the population-level impacts of diatoms, across their size distribution and variations in mixed layer characteristics.
   
### Setting up a model investigation
Your task in this activity is to undertake a "mini-study", in which you use a systematic series of model runs to expose trends, which you then interpret in terms of the motivating questions and model assumptions.



### Does the variant with the largest standing stock win in competition?

### Is the standing stock of single variants higher, lower or the same as for multiple variants?

### Which variants, or combinations of variants, are most effective at taking up nutrients?



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
