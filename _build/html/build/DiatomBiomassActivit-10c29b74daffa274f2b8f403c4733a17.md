# 🛼 Size-dependence of diatom biovolume in mixed layers: Mini-study procedure
Your task in this Activity is to execute a mini-study in which you tabulate model results to address the questions:
> Do primary productivity, availability to grazers and pathogens, and competitive impacts vary with diatom cell size?

> How do effects of diverse populations differ from the effects of single variants?

> Do primary productivity, availability to grazers and pathogens, and competitive impacts vary with mixing layer characteristics?

The [rationales for interpreting standing stocks](./DiatomBiomassActivity2.md) of diatoms and nutrient suggest that usful insight can be gained (keeping limitations in mind) from calculations of standing stocks. 

## Setting up a model investigation
The procedure for this mini-study is to calculate the standing stocks of diatoms and nutrient across several cell sizes and several mixing intervals, and to interpret these results in terms of the motivating questions. 

The primary tool in your "mini-study", aside from the model, is a spreadsheet in which you tabulate and plot model results.

To get started:
1. Open a spreadsheet, in which to tabulate and plot results.
2. Launch the [model](./DiatomSizeESS.ipynb) on Binder, and generate the user interface with **Run all cells**.
3. Initialize a new diatom population using the default parameters, by clicking on the **Set up population** button.
4. Scroll down to the **Seeding...** section; seed the population with diatoms of the smallest size class, by **setting** $i=0$ in the textbox (replacing "all"), then clicking the **Seed cell population** button.
   
   Note that, if there are 8 size classes, these are numbered 0 to 7.
5. Scroll down to the **Setting mixing events...* section, and click on the **Run simulation** button ising the default settings.
6. In the results labelled "Period-averaged statistics: standing stocks", look at the **BV** column. This contains the biovolume of diatoms in each size class. Because you seeded cells only in the smallest size class ($s=2.5$), only this size class has nonzero biovolume.
7. In the spreadsheet, enter "s" into a cell, and under it enter the size of diatom you just simulated (2.5). This is the column for diatom size in your table.
   
   Next to the "s", enter "BV8" and below it enter the BV value corresponding to $s=2.5$ in the model output. This is the column for biovolume for each of the size classes you simulate. The "8" in "BV8" is the mixing interval, which is still the default 8 days.
   
8.Now, **change the mixing interval, $t_{mix}$** to 16, in the textbox, and click **Run simulation** again.
	
	This restarts the simulation, but uses the new mixing interval of 16 days instead of the default 8 days. 
	When you restart the simulation, it will use the endpoint of the previous simulation as its initial condition.
	Because the simulation is running for many mixing intervals, it will "forget" these initial conditions just as it did in the original run.
	
