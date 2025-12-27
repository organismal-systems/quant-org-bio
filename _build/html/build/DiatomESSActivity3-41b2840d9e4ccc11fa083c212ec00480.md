# 🛼 Evolutionarily Stable States for diatoms in mixed layers: Data collection
In this mini-study, you will focus on a scenario most relevant to marine diatom communities and  mixed layers.

To get started:
1. Open a spreadsheet, in which to tabulate and plot results.
   - In a convenient place in the spreadsheet, enter four column heading in a row: "s", "T8", "T12", and "T16".
   
   These represent the cell size, and three mixing layer intervals to test.
   - Under "s", enter three numbers in a column: 2.5, 7.17 and 12.5.
   
   Tese represent the sizes of cells you will test.
2. Launch the [model](./DiatomSizeESS.ipynb) on Binder, and generate the user interface with **Run all cells**.
3. In the **Setting up diatom variants and mixed layer characteristics** section, use the following parameter choices:
   - Set the number of size classes to $n_{sizes}=16$, to better reflect potential marine diatom diversity.
   - Set the mixed layer depth to $z_m=100$, to reflect the relatively deep mixed layers in some marine habitats.
4. Scroll down to the **Seeding...** section.  
   - Set the number of cells to seed to $N_i=0.1$.  
   
   This will be the "small" initial number of cells to test whether a diatom variant can invade.
5. In the **Setting mixing event intervals, and running the simulation** section, 
   - Set the number of intervals to $n_{pers}=128$.

These parameters will apply to all the model runs in this Activity.

## Part 1: Is a diatom variant an ESS?
Because testing all size classes would take too long, in this part of the Activity we will only test three: the smallest, largest and middle sizes $i=0,7,15$ or $s=2.5,7.17,125.$

Starting with the smallest diatom size class:

6. Initialize a new diatom population using the default parameters, by clicking on the **Set up population** button.
7. Scroll down to the **Seeding...** section.  
   Seed the population with diatoms of the smallest size class, by **setting** $0$ **in the $i$ textbox** (replacing "all"), then clicking the **Seed cell population** button.
   
   Note that, if there are 16 size classes, these are numbered 0 to 15.

8. Click on the **Run simulation** button.
   - Check the Period-averaged biovolume plot (middle plot in the first figure) to make sure the period-averaged diatom population and nutrient concentrations have reached constant values.
   - If they are still varying, click **Run simulation** again to restart the simulation.
   
   If they are constant, cells of size class $i=0$ have established the conditions under which you can test whether they are an ESS.
   
9. Return to the **Seeding...** section, replace the size class $0$ with "all". 
   - Click **Seed cell population**
   
   You have now introduced a small population of potentially invading variants.
   
10. Click on the **Run simulation** button again.
   - Check the Period-averaged biovolume plot (middle plot in the first figure) to make sure the period-averaged diatom population and nutrient concentrations have reached constant values.
   - If they are still varying, click **Run simulation** again to restart the simulation.

11. Determine whether any size classes have "invaded":
	- Check the cell numbers column in the top output table ("standing stocks").
	- If *all* of the variants, other than the original ESS candidate, have populations above the number you seeded ($10^{-1}$) then there are no "successful" invaders, and **the original size class is an ESS**.
	
		In the spreadsheet cell representing the original size class and the mixing interval, enter a 1.
	- If *any* of the variants, other than the original ESS candidate, have populations above the number you seeded ($10^{-1}$) then these are "successful" invaders, and **the original size class is *not* an ESS**.
	
		In the spreadsheet cell representing the original size class and the mixing interval, enter a 0.

12. Repeat steps 6 through 11 for each size class $i=0,7,15$ and each mixing interval $T_{mix}=8, 12, 16$.


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


