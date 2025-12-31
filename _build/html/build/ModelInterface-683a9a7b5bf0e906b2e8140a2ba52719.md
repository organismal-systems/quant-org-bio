# 🛼 Understanding the model interface
The first Activity is getting familiar with how to simulate diatom population dynamics using the model.

## Running the model
To execute a simulation, follow these steps:
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
   These textboxes enable you to set the number of days between mixing events, the number of mixing intervals to run the simulation, and how many times to record data between mixing events.
   
   To run the simulation with the default parameters, **click on the Run simulation** button. 
6. **Examine the textual and graphical output.**
   In particular, look at:
   - The table of **Period-averaged statistics: standing stocks** in the textual output.
   
	   This table summarizes the number $N$, quota $\frac{Q}{Q_{min}}$, and biovolume $BV$ of each diatom size class $i$ over the last simulated mixing interval.
	   Below the table are the total averaged biovolume of all the diatom size classes, and the total averaged nutrient concentration, in the final mixing interval.
   
   - The **Period-Averaged Time Series (Figure 2)** in the graphical output.
	 The plots in this figure show the period-averaged quotas and biovolume for each diatom size class, and the mixed layer nutrient concentration.
	 *Note that the vertical axis in the biovolume plot uses a **log scale**. 
	 That means one major grid tick represents a factor of 10 in cell numbers.*[^num]  
	 
   In the **Period-Averaged Biovolume** plot, it is clear that populations of some size classes are still increasing while others are still decreasing.
   To get a better sense of the ultimate periodic pattern, again **click on the Run simulation** button to restart the simulation from where it left off.
7. Look again at the **Period-Averaged Time Series (Figure 2)**.
   This time, the **Period-Averaged Biovolume** plot shows that cell populations are more nearly constant, when averaged across a mixing interval.
   
   However, the smallest diatoms ($s=2.5$) are still slowly increasing, while the second smallest diatoms ($s=3.93$) are slowly decreasing, such that the dominant strain appears to be changing.
8. For a third time, **click on the Run simulation** button to restart the simulation from where it left off.
   
   This time, it is clear that the smallest diatoms ($s=2.5$) are going to be the dominant variant, and outcompete diatoms in the other size classes.
   This also means that the  **1-Period Time Series (Figure 1)** plots reflect a recurring, periodic pattern.
9. Repeat steps 1-8, but this time change the "all" to "3,5" in the **Size classes ($S_i$) to seed** textbox in the  **Seeding the mixed layer with diatom variants** section.
   When you run the simulation this time, only size classes 3 and 5 are present in the diatom population.
   
[^num]: Note that the coordinates of the cursor are shown at the bottom of the figure, so you can read the actual numbers off data in the plots.

## Setting up a model investigation
Your task in these Activities is to undertake a "mini-study", in which you use a systematic series of model runs to expose trends, which you then interpret in terms of the motivating questions and hypothesis tests.

In addressing the questions prompted by the Activities, it is helpful to keep these points in mind:

### The model should be run for many mixing periods
As in many models, Litchman *et al.*'s model starts with potentially unrealistic initial conditions. 
That is, we do not know ahead of time what a reasonable starting population is for a given size class of diatoms.
	
The model is informative because the long-term model results are independent of many aspects of the initial conditions.
For example, whether the initial population of diatoms is 1 or 10, in the long run the initial population is typically "forgotten" as the population settles into a periodic pattern timed by the mixing interval.[^per]

This means you have to run the model for a sufficiently long time to be periodic.
The model interface makes it easy to do this, because you can see from the [period-averaged plots](./averaged.png) whether the long term trend has approached a "steady state" in which some size class populations are constant and others absent or steadily decreasing.
If it hasn't, you can simply click the **Run simulation** button to continue the simulation as long as necessary.
	
[^per]:This is not always the case. For example, if the starting population of a given size class is 0, it will always be 0.

### Plan a hypothesis test
Model results are most informative when you systematically vary one or two parameters, with a specific motivating question to answer or hypothesis to test. 

For this model, a motivating question can be something like, 
> Does mixed layer depth have an effect on diatom cell numbers?

A series of runs to answer that question might leave all parameters and initial conditions constant, but vary the mixed layer depth parameter $z_m$ over the largest range you think may be relevant to aquatic habitats.
Because you varied only the $z_m$ parameter, any changes in the results must be due to that parameter.
To see whether this result holds true generally, you could try another set of parameters, and hold those constant while you vary $z_m$.

A hypothesis for this model might be something like, 
> Mixing interval determines the size of the dominant diatoms.

An *implication* of this hypothesis is that changing the mixing interval ($T_{mix}$), while holding the other parameters constant, leads to different dominant strains.
A systematic series of simulations, in which you vary only $T_{mix}$ is therefore a test of this hypothesis.

### Envision a plot
While it can be useful to do an initial exploration of parameter space with haphazard changes in parameters, it is usually difficult to detect clear patterns in the results of these changes, and even harder to communicate them to another scientist.
The most effective approach is to envision a hypothetical plot of data that would address a specific hypothesis or question.
As you design your modeling approach, ask yourself:
> What would a plot look like that convinces me this hypothesis is true or false?

With the answer to that question, you can design the systematic series of model runs to generate data for that plot.

We are familiar with this approach for empirical data.
For example, Litchman *et al.* hypothesized that marine diatom size distributions are larger than freshwater diatom size distributions. 
They envisioned a plot of their empirical data (their Figure 1) that would effectively test this hypotheses by showing the size distributions of several examples from each habitat type. 
If the plot showed a systematic difference between the two types of habitat (it did) that would be compelling evidence in support of the hypothesis.
A plot that showed no systematic difference across the two habitat types would contradict their hypothesis.

Though it is less familiar, the same approach is informative with simulation results.
For example, Litchman *et al.* hypothesized that the interval between mixing events affected the stable diatom size distribution so as to favor larger diatoms than expected in mixed layers without mixing events.
To test this hypothesis, Litchman *et al.* envisioned a graph of the sizes of dominant diatom variants, across systematic variation in the interval between mixing events.
The conducted a series of simulations to obtain the data to make this plot, and used it to show support for their hypothesis.
