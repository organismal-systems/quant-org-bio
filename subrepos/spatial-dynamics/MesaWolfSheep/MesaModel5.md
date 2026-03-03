# 🛼 Inferences from the Wolf-Sheep-Grass model: Part 2
The second step is in this Activity is to estimate the demographic time scale, $T_{demog}$.

Unlike for the KISS model, in the agent-based model there is no explicit parameter for the intrinsic rate of growth.
Instead, growth and decline of populations is an emergent property of the agent interactions.
Furthermore, the model dynamics are **stochastic**, meaning there is a random component in the outcomes for a given set of parameters. 

For the present purposes, these features have two implications:
1. You must conceive a new metric based on the visual time series of booms and busts of agent populations, and apply it to estimate an approximate demographic time scale that roughly captures the essential model dynamics.
2. You must evaluate your metric in the context of multiple replicates, knowing that very different outcomes are possible, and that some of them may be rare.

## Estimating the demographic time scale, $T_{demog}$
To begin this part of the Activity, it is useful to change some parameters to make the simulations as fast and informative as possible:
1. Exit the simulation window by clicking on the icon at right.
2. Change the parameters in the first code cell:

	```{code} python
	:label: cell1
	:caption: Creating a TensorMesh using SimPEG
	import codes.WSPcomm
	codes.WSPcomm.g_width = 32/2
	codes.WSPcomm.g_height = 32/2
	codes.WSPcomm.g_marker = 50*2
	codes.WSPcomm.psize = 125*2
	#codes.WSPcomm.g_width = 32
	#codes.WSPcomm.g_height = 32
	#codes.WSPcomm.g_marker = 2
	#codes.WSPcomm.psize = 125
	```
	- In this code block:
	    - `g_width` and `g_height` are the grid dimensions
		- `g_marker` and `psize` are the dimensions of the sheep, wolf and grass icons  
	- The icon sizes do not affect model outcomes, but can make the grid plot easier to interpret and more aesthetic.
   - In the example code block,
       - Changed parameters are expressed as multiples of the original parameters
	   - The original parameters are preserved as comments (that is, preceded by `#`)
	   
    Both of these are optional; in some cases, it is easier to keep track of previous work if the parameter sets are recorded in these ways.

3. Run the simulations multiple times, changing the random seed each time before resetting agents in the grid.

    - It may be helpful to adjust the initial sheep and wolf populations in the simulation window.
4. Write down your best estimate of the demographic time scale, $T_{demog}$, along with your rationale for choosing it.  
    It may be useful later to make a screenshot of a typical simulation that illustrates your time scale metric.
5. Calculate and record the critical habitat size, $L_{crit}$, implied by your estimate of $T_{demog}$.
	
	
