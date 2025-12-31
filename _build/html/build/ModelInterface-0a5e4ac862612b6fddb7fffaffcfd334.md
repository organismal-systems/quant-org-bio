# 🛼 Understanding the model interface
To understand how the model works:
1. Open an executable version of the [notebook](./DiatomSizeESS.ipynb) in Binder.
2. Select **Run all cells** under the **Run** menu. This sets up the graphical interface for the model.
3. Scroll down to the section labeled **Setting up diatom variants and mixed layer characteristics**. 
   The textboxes enable you to change the number and size of diatom classes, and the mixed layer characteristics.
   Leave these as the defaults for now, and **click on the Set up population** button.
4. Scroll down to the section labeled **Seeding the mixed layer with diatom variants**.
   These textboxes enable you to add populations of some or all diatom size classes.
   To seed the cells into the population using the default parameters, **click on the Seed cell population** button.
   
   Seeding cells is *additive*, meaning that if you click the button twice, it will add twice the selected cell populations. 
5. Scroll down to the section labeled **Setting mixing event intervals, and running the simulation**.
   These textboxes enable you to set the number of days betwen mixing events, the number of mixing intervals to run the simulation, and how many times to record data as the cell numbers, nutrient quotas and nutrient concentration change between mixing events
   To run the simulation with the default parameters, **click on the Run simulation** button. 
6. **Examine the textual and graphical output.**
   In particular, look at the **Period-Averaged Time Series (Figure 2)**.
   In the **Period-Averaged Biovolume** plot[^num], it is clear that populations of some size classes are still increasing while others are still decreasing.
   To get a better sense of the ultimate periodic pattern, again **click on the Run simulation** button to restart the simulation from where it left off.
7. Look again at the **Period-Averaged Time Series (Figure 2)**.
   This time, the **Period-Averaged Biovolume** plot shows that cell populations are more nearly constant, when averaged across a mixing interval.
   This also means the  **1-Period Time Series (Figure 1)** plots reflect a recurring, periodic pattern.
8. Repeat steps 1-7, but this time change the "all" to "3,5" in the **Size classes ($S_i$) to seed** textbox in the  **Seeding the mixed layer with diatom variants** section.
   When you run the simulation this time, only size classes 3 and 5 are present in the diatom population.
   
[^num]: Note that the coordinates of the cursor are shown at the bottom of the figure, so you can read the actual numbers off data in the plots.

## Setting up a model investigation
Your task in these Activities is to undertake a "mini-study", in which you use a systematic series of model runs to expose trends, which you then interpret in terms of the motivating questions and model assumptions.

In addressing the questions prompted by the Activities, it is helpful to keep these points in mind:

### The model should be run for many mixing periods.
As in many models, Litchman *et al.*'s model starts with potentially unrealistic initial conditions. 
That is, we do not know ahead of time what a reasonable starting population is for a given size class of diatoms.
	
The model is informative because the long-term model results are independent many aspects of the initial conditions.
For example, whether the initial population of diatoms is 1 or 10, in the long run the initial population is typically "forgotten" as the population settles into a periodic pattern timed by the mixing interval.[^per]

This means you have to run the model for a sufficiently long time to be periodic.
The model interface makes it easy to do this, because you can see from the [period-averaged plots](./averaged.png) whether the long term trend has approach a constant.
If it hasn't, you can simply click the **Run simulation** button to continue the simulation as long as necessary.
	
[^per]:This is not always the case. For example, if the starting population of a given size class is 0, it will always be 0.)

### Model results are most informative in the context of systematic variation of one or two parameters, motivated by a test of a specific hypothesis.
While it can be useful to do an initial exploration of parameter space with haphazard changes in parameters, it is usually difficult to detect clear patterns in the results of these changes, and even harder to communicate them to another scientist.
The most effective and time-efficient approach is to envision a hypothetical plot of data that would address a specific hypothesis or question.
This study design using a model, analogously to how an experimentalist would design observations in an empirical study.

For example, Litchman *et al.* stated a hypothesis that marine diatom size distributions are larger than freshwater diatom size distributions. 
They envisioned a plot of their empirical data (their Figure 1) that would effectively test this hypotheses by showing the size distributions of several examples from each habitat type. 
If the plot showed a systematic difference between the two types of habitat (it did) that would be compelling evidence in support of the hypothesis.
A plot that showed no systematic difference across the two habitat types would contradict their hypothesis.

Litchman *et al.* used the same approach with their numerical results. 
They posed the hypothesis that the interval between mixing events affected the stable diatom size distribution so as to favor larger diatoms than expected in mixed layers without mixing events.
To test this hypothesis, Litchman *et al.* envisioned a graph of the sizes of dominant diatom variants, across systematic variation in the interval between mixing events.
A plot that 



### Inferences from models are most easily discerned and communicated with plots of tabulated results.
