# 🛼 Evolutionarily Stable States for diatoms in mixed layers: Data collection
In this mini-study, you will examine the outcomes of competition among diatom variants in mixed layers, and the [Evolutionarily Stable States](./EvolutionarilyStableStates.md) that arise in them.

To get started:
1. Open a spreadsheet, in which to tabulate and plot results.
   
   Prepare a table, by entering a row with the headings: "Tmix", "i_win", "s_win", and "ESS".
   
   - The "Tmix" column will contain a column of mixing intervals.  
   Enter 1.5, 8, 18. 32 into this column.
   - The "i_win" and "s_win" columns will contain the size class and size of the dominant diatom variant (the "winner" of the competition).
   - The "days" column will contain your assessment of how long it took for the winner to become dominant.  
   A rough estimate, based on how many times you ran the simulation (multiplied by the number of mixing intervals, 128, and by the number of days in each mixing period).
   - The ESS column will contain whether or not the winning size class is also an ESS.  
   You will fill this column in Part 2.

2. Launch the [model](./DiatomSizeESS.ipynb) on Binder, and generate the user interface with **Run all cells**.
3. In the **Setting up diatom variants and mixed layer characteristics** section, use the following parameter choices:
   - Set the number of size classes to $n_{sizes}=16$, to reflect a spectrum of  potential marine diatom diversity.
   - Set the mixed layer depth to $z_m=100$, to reflect the relatively deep mixed layers in many marine habitats.
4. Scroll down to the **Seeding...** section.  
   - Set the size classes, $i$, to "all".  
   - Set the number of cells to seed to $N_i=0.1$.  
   
   This will be the "small" initial number of cells to test whether a diatom variant can invade.
5. In the **Setting mixing event intervals, and running the simulation** section, 
   - Set the number of intervals to $n_{pers}=128$.  
   
   This relatively large number of mixing intervals will be helpful in determining the **steady state** outcomes of diatom population dynamics.

These parameters will apply to all the simulation runs in this Activity.

## Part 1: Which variants win competition among mixed diatom populations?
The first part of this Activity is a survey of competitive outcomes across a series of mixing event intervals.

For each of the mixing intervals, $T_{mix} = 1.5, 8, 18 32$, complete the following set of steps:
1. Initialize a new diatom population, by clicking on the **Set up population** button.
2. In the **Seeding...** section, seed the population with diatoms of all size classes, by clicking the **Seed cell population** button.
3. Click on the **Run simulation** button.
4. Take note of which size class has the largest number of cells (under the "N" column in the tabular model output).
5. Click on the **Run simulation** button, again, repeating as necessary, **keeping track of how many times you run the simulation**, until one variant is clearly excluding the other variants.
6. When you judge the outcome is close to a steady state, record the winner's size class $i$, its size $s$ and the approximate number of days it took to arrive at a steady state.

This completes the data collection for Part 1 of this Activity.

## Part 2: Are dominant competitors ESS's?
The second part of this Activity is testing whether the dominant variants from Part 1 meet the criterion for being an ESS.

For each of the mixing intervals, $T_{mix} = 1.5, 8, 18 32$, complete the following set of steps:
1. Initialize a new diatom population, by clicking on the **Set up population** button.
2. In the **Seeding...** section, seed the population with diatoms of the dominant size class, setting $i$ to "i_win", then clicking the **Seed cell population** button.
3. Click on the **Run simulation** button.
4. Confirm in the Period-Averaged Time Series plots that the diatom population of this variant has reached steady state.
5. In the **Seeding...** section, seed the population with diatoms of all size classes, by setting $i$ to "all", then clicking the **Seed cell population** button.
6. Click on the **Run simulation** button.
7. After the transients from seeding new cells have passed, take note of which size class have more cells than you seeded (0.1).  
   In close cases, you may need to run the simulation two or more times.



8. If *all* of the variants, other than the original ESS candidate, have populations below the number you seeded ($10^{-1}$) then there are no "successful" invaders, and **the original size class is an ESS**.  
   In this case, enter a "y" in the ESS column corresponding to the mixing interval.
8. If *any* of the variants, other than the original ESS candidate, have populations above the number you seeded ($10^{-1}$) then these are "successful" invaders, and **the original size class is *not* an ESS**.  
   In this case, enter a "n" in the ESS column corresponding to the mixing interval.

This completes the data collection for Part 2 of this Activity.

