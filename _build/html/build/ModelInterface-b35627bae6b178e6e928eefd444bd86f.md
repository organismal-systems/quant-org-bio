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
