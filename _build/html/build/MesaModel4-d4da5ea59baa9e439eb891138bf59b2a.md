# 🛼 Inferences from the Wolf-Sheep-Grass model: Part 1
In this Activity, you will form an estimate of the demographic time scale, $T_{demog}$, for the agent-based model in the [](./WolfSheepPersist.ipynb) notebook.
From this time scale, you will compute a [critical habitat size](./MesaModel3.md),
$$
L_{crit} = \frac{\sqrt{T_{demog}}}{2} 
$$
that is hypothesized to delineate persistence *vs*. extinction in the 3-level trophic system. 
Then, you will run the model at a variety of habitat sizes to observe population dynamics, and assess whether the results do or do not provide support for the hypothesized critical habitat size.

## Part 1: Model usage
The first step in this Activity is to familiarize yourself with the model:
1. Launch the WolfSheepPersist model on Binder or your own computer.
2. Run the model with the default parameters:
    - **Set up the model**: Click on the `>>` icon at the top of the notebook, to *restart the kernel and run all cells*.  
	It will save time later to check the `Do not ask again` box.
	- **Expand the simulation window**: When the blue bar appears, click on the box icon on the right hand side.
    - **Initialize the agents** by clicking `Reset`
	- **Run the simulation** by clicking the right arrow, ${\blue \blacktriangleright}$  
    Note that clicking the ${\blue \shortparallel}$ button will pause the simulation; then, ${\blue \blacktriangleright}$ will restart it,
3. Examine the output
    - In the visualization of the grid at left, you can follow individual sheep or wolf agents, track an individual grass patch as it grows and gets eaten, and get an overall sense for any spatial patterns that might arise.
	- In the population time series at right, you can get a quantitative sense for population levels and trends.
 
     What are the main features you observe in each of these graphics?

4. Execute a new replicate of the simulation: 
    - **Change the random seed**: Type a new number into the line labeled `Random Seed`  

    <span style="color:red">It's important to understand that running the simulation multiple times with the same random seed will give exactly the same results.
To have a replicate run of the simulation, you must change the random seed.</span>

    What is similar or different about results from different replicates?
