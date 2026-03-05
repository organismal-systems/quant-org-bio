# 🛼 Inferences from the Wolf-Sheep-Grass model: Part 2
The second step is in this Activity is to estimate the demographic time scale, $T_{demog}$.

Unlike for the KISS model, in the agent-based model there is no explicit parameter for the intrinsic rate of growth.
Instead, growth and decline of populations is an emergent property of the agent interactions.
Furthermore, the model dynamics are **stochastic**, meaning there is a random component in the outcomes for a given set of parameters. 

For the present purposes, these features have two implications:
1. You must conceive a metric based on the visual time series of booms and busts of agent populations, and apply it to estimate an approximate demographic time scale that roughly captures the essential model dynamics.
2. You must evaluate your metric in the context of multiple replicates, knowing that very different outcomes are possible, and that some of them may be rare.

## Part 2: Estimating the demographic time scale, $T_{demog}$
To begin this part of the Activity, it is useful to change some parameters to make the simulations as fast and informative as possible:
1. Exit the simulation window by clicking on the icon at right.
2. Change the parameters in the first code cell:

	```{code} python
	:label: cell1
	:caption: Creating a TensorMesh using SimPEG
	import codes.WSPcomm
	codes.WSPcomm.g_width = 16
	codes.WSPcomm.g_height = 16
	codes.WSPcomm.g_marker = 2*50
	codes.WSPcomm.psize = 2*125
	```

	In this code block:
	    - `g_width` and `g_height` are the grid dimensions
		- `g_marker` and `psize` are the dimensions of the sheep, wolf and grass icons
	The icon sizes do not affect model outcomes, but can make the grid plot easier to interpret and more aesthetic.
- The 


