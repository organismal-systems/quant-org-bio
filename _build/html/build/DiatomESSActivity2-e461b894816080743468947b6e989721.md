# 🛼 Evolutionarily Stable States for diatoms in mixed layers: Data collection
Your task in this Activity is to execute a "mini-study" that addresses the [motivating questions](./DiatomESSActivity.md) by tabulating [Evolutionarily Stable States](./EvolutionarilyStableStates.md), outcomes of competition among mixed diatom populations, and the timescales over which these outcomes occur, across several mixing intervals.
You will [interpret those data](./DiatomESSActivity3.md) results in terms of the motivating questions, in the next phase of the mini-study.

## Mini-study rationale
In their published research, Litchman *et al.* surveyed a finely resolved diatom size distribution, with numerous size classes.
They used a computerized loop to assess whether or not each of these size classes was an ESS, for each of a wide range of mixing intervals.
This approach is not practical in a mini-study.

Instead, you will execute your mini-study parts that address elements of the motivating questions:
1. In **Part 1**, you will ask, 
   > Is there a mixing interval at which diatoms of a specific size are an ESS?
   
   As case studies, you will test three sizes: the smallest, largest and middle sizes $i=0,7,15$, corresponding to $s=2.5,7.17,12.5$.
   
   If you find an ESS with a diatom variant larger than the smallest size class, that is evidence that mixing events at the associated interval can favor larger cells than constant habitats would.

2. In **Part 2**, you will ask,
   > Are the outcomes of competition among initially mixed populations of variants the same as the ESS outcomes?

   As case studies, you will assess the long-term outcomes of competition over a serices of mixing intervals.
   You will also assess the time scale over which these outcomes occur, as context for their predictive value for real-world habitats.
   
   If you find that "winners" of competition are also the variants that form EES's, that would support the relevance of the ESS concept as an indicator of trends in natural selection.
   Conversely, if you find that winners of competition in initially mixed populations differ from EES variants, that would suggest the specific assumptions underlying ESS analysis may be less relevant.
   
   If you find that diatom populations quickly approach these ESS or competitive outcomes, that would suggest these dynamics may dominate other factors in determining diatom size distributions. 
   Conversely, if you find that populations arrive at ESS and competitive outcomes only very slowly, that would suggest these dynamics may be overwhelmed by other factors in variable aquatic habitats.
   

## Part 1: Scenario setup
In this mini-study, you will focus on a scenario most relevant to marine diatom communities and  mixed layers.

To get started:
1. Open a spreadsheet, in which to tabulate and plot results.
2. Launch the [model](./DiatomSizeESS.ipynb) on Binder, and generate the user interface with **Run all cells**.
3. In the **Setting up diatom variants and mixed layer characteristics** section, use the following parameter choices:
   - Set the number of size classes to $n_{sizes}=16$, to better reflect potential marine diatom diversity.
   - Set the mixed layer depth to $z_m=100$, to reflect the relatively deep mixed layers in some marine habitats.
4. Initialize a scenario by clinking the **Set up population** button.




Because testing all size classes would take too long, in this part of the Activity we will only test three: the smallest, largest and middle sizes $i=0,7,15$ or $s=2.5,7.17,125.$


Set n_pers=128



3. Initialize a new diatom population using the default parameters, by clicking on the **Set up population** button.
4. Scroll down to the **Seeding...** section.  
   Seed the population with diatoms of the smallest size class, by **setting** $0$ **in the $i$ textbox** (replacing "all"), then clicking the **Seed cell population** button.
   
   Note that, if there are 8 size classes, these are numbered 0 to 7.

5. Click on the **Run simulation** button using the default settings.

6. In the results labelled "Period-averaged statistics: standing stocks", look at the $BV$ column. This contains the biovolume of diatoms in each size class. Because you seeded cells only in the smallest size class ($s=2.5$), only this size class has nonzero biovolume.

7. Choose a part of your spreadsheet in which to tabulate biovolume, and another part to tabulate nutrient concentration. 
   - In the biovolume part of your spreadsheet, enter "s" into a cell, and under it enter the size of diatom you just simulated (2.5). This is the column for diatom size in your biovolume table.  
   Next to the "s", enter "BV8" and below it enter the $BV$ value corresponding to $s=2.5$ in the model output. This is the column for biovolume for each of the size classes you simulate. The "8" in "BV8" is the mixing interval, which is still the default 8 days.

   - In the nutrient concentration part of your spreadsheet, enter "s" into a cell, and under it enter the size of diatom you just simulated (2.5). This is the column for diatom size in your nutrient concentration table.  
   Next to the "s", enter "R8" and below it enter the averaged nutrient concentration value in the model output. This is the column for nutrient concentration  for each of the size classes you simulate. The "8" in "R8" is the mixing interval, which is still the default 8 days.

8. Now, **change the mixing interval, $t_{mix}$** to 16, in the textbox, and click **Run simulation** again.
	
	This restarts the simulation, but uses the new mixing interval of 16 days instead of the default 8 days. 
	When you restart the simulation, it will use the endpoint of the previous simulation as its initial condition.
	Because the simulation is running for many mixing intervals, it will "forget" these initial conditions just as it did in the original run.
	
9. To record this datum, enter "BV16" next to "BV8", and enter the new $BV$ value below it. Also, enter "R16" next to "R8", and enter the new averaged nutrient concentration value below it.

10. Repeat this for mixing intervals $T_{mix}=32$ and  $T_{mix}=64$, recording those results as before to create a row of one size class $s$ and four values of $BV$ or nutrient concentration.

11. Repeat steps 3-10, but this time using the size class $i=3$, corresponding to $s=6.79$. Use the results to fill out the second row of $BV$ and nutrient concentration data in your spreadsheet.

12. Repeat steps 3-10, but this time using the size class $i=7$, corresponding to $s=12.5$. Use the results to fill out the third row of $BV$ and nutrient concentration data in your spreadsheet.  
   **Pay particular attention to the plots in Figure 2, to assess whether the diatom population is periodic. If not, make a note of the results, but do not include it in your table.**

13. When the tables are complete, make X-Y Scatter plots of the data using the spreadsheet's Chart funtion. 
	- The data are in columns, with the first column being the x-axis.
	- The title of the $BV$ plot is "1-spp variation of biovolume". 
	- The title of the nutrient concentration plot is "1-spp variation of nutrient concentration". 
	- The x-axis label is "log10(Diatom size)". 
	- The y-label is "Biovolume".
	- The legend indicates the mixing interval associated with each line.   
	- Because the biovolume and nutrient concentration differences are so extreme, double click on the vertical axes and set the scales to "Logarithmic".
	
This completes the data collection for Part 1 of this Activity.

## Part 2: Consequences of diatom diversity
The second part of this activity is a survey of biovolume and nutrient concentrations across a series of mixing event intervals, for a mixed diatom population that initially includes all the size classes.

1. Choose a part of your spreadsheet for a new table for biovolume and nutrient concentration data, or start a new one.  
   - Start a column labeled "Tmix" and fill out the column underneath by entering the sequence of mixing intervals to assess: $T_{mix} = 8, 16, 32, 64$.  
   - Next to "Tmix", enter a label for biovolume, $BV$, and a label for nutrient concentration, $R$.
2. Execute the three setup button clicks:
   - **Set up population**
   - **Seed cell population**
   - **Run simulation**.
3. Continue the simulation, with repeated clicks on **Run simulation**, until the total biovolume does not change. 
   This means the diatom population is essentially periodic, though there may be remnants of diatom variants at tiny population numbers.  
   Enter the results for averaged biovolume and nutrient concentration under their respective columns, in the row for $T_{mix}=8$.
4. Repeat steps 2-3, changing the mixing interval $T_{mix}$ to 16, 32 and 64, and recording the results in the appropriate rows.
5. Make a chart with $T_{mix}$ on the horizontal axis, and total biovolume on the vertical axis.  
   Make another chart with  $T_{mix}$ on the horizontal axis, and nutrient concentration on the vertical axis.  
	- Label the axes of both plots.
	- The title of the $BV$ plot is "Multi-spp variation of biovolume". 
	- The title of the nutrient concentration plot is "Multi-spp variation of nutrient concentration". 

This completes the data collection for Part 2 of this Activity.


