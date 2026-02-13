# 🛼 Testing hypothetical performance standards: Data collection
To collect data for the Activity exploring hypothesized early-stage larval swimming performance standards, follow these steps:
1. Select fixed values for aspect ratio $\alpha$, relative equator position $\eta$, tissue density $\rho_{tissue}$ and inclusion density $\rho_inclusion$.

2. Select a series of values for tissue volume $V_t$ and excess density $\rho_{excess}$, over which to quantify swimming metrics.  
    - These series should span the range that you think is most relevant, with enough resolution that you can discern key transitions.
    - Keep in mind, though, that you will be constructing morphologies and executing simulations for all or most combinations of $V_t$ and $\rho_{excess}$.
    - The excess density, $\rho_{excess}$, is constrained because the average larval density, $\rho_{excess}+\rho_{seawater}$ to be less than the inclusion density $\rho_{inclusion}$ (its lightest constituent) or more than the tissue density $\rho_{tissue}$ (its heaviest constituent).  
  
3. Prepare a spreadsheet with tables to record two metrics: upswimming velocity and reorientation time.  
  Your spreadsheet may look something like this:
  
```{figure} images/CT3_1.png
:label: ct3_sprd
:alt: Cells with tables in a sample spreadsheet
:width: 400px
:align: center

Cells with tables in a sample spreadsheet for colecting swimming performance data.  

In this example, it's assumed that the inclusion density $\rho_{inclusion} \le 25$ and that the tissue density $\rho_{tissue} \ge 240$.
Outside these ranges, it is not possible to construct a larva with the specified $\rho_{excess}$ out of the specified materials.
```
4. For each combination of $V_t$ and $\rho_{excess}$ in your table:  
    - Create a morphology in [](./ChimeraOrg.ipunb) and save it under an informative name.
	- Load it into [](./ChimeraSwim.ipynb) and run a simulation in still water to determine:  
	  1. equilibrium upswimming velocity
	  2. reorientation timescale
  


