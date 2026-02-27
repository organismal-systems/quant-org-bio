# 🛼 Inferences from the Wolf-Sheep-Grass model: Part 3
The third step in this Activity is to test whether simulation results support or contradict the hypothesized critical habitat size.

Specifically,
> - Does one or more components of the Wolf-Sheep-Grass community typically go extinct in habitats smaller than the critical size, $L_{crit}$?
> - Do all components of the Wolf-Sheep-Grass community typically go persist in habitats smaller than the critical size, $L_{crit}$?

To assess this:
1. Design a mini-study using a series of simulations to observe the frequency of extinctions.

	Among the design criteria you should consider and note are:
   - What sequence of habitat sizes should you run (and why)?
   - How long do simulations need to run (and why)?
   - How many replicates do you need to run (and why)?
   
   In designing this mini-study, keep in mind that:
   - *The hypothesis reflects orders of magnitude.*  
   Therefore, your habitat sizes should span several orders of magnitude.
   Increasing parameters by factors of 2 is freqently a good way to balance quick progress through parameter space without missing important features.
   
   - *Simulations in large habitats can take a long time*.  
   
     In many simulations, most of the computer time is spent in updating graphics. 
	 To speed up run times in slow runs, you can change the `Render Interval (steps)` parameter to be significantly larger (5-15) to greatly reduce computer time spent redrawing marginally different results.

	- Keeping some graphical results (*e.g*., in the form of screenshots) can be useful for explaining the outcomes you observed and articulating your conclusions.
	 
2. Tabulate and plot your results.
Write a few sentences summarizing (and illustrating with graphics) your synthesis addressing the question,
> Do your results support or contradict the hypothesized critical habitat size?

   
