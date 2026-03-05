# 🛼 The Wolf-Sheep-Grass model in Mesa
The [notebook for this Activity](./WolfSheepPersist.ipynb) implements a modified version of an agent-based model, developed in the Python package [Mesa](https://mesa.readthedocs.io/latest/), called the [Wolf-Sheep Predation Model](https://mesa.readthedocs.io/latest/examples/advanced/wolf_sheep.html).
This model is based on an earlier, similar model implemented in the agent-based modeling platform [NetLogo](https://www.netlogo.org/).
Both these models are intentionally simplistic, and, even aside from lacking species-specific characteristics of wolves and sheep, have rules that do not correspond to nature.

Nonetheless, these models illustrate important aspects of population dynamics involving three trophic levels.
In particular, they highlight the importance of stochasticity &ndash; random occurences &ndash; that are "assumed out" of most PDE models.
In this respect, even more detailed PDE models can give results that are more misleading and difficult to interpret than even simplistic agent-based models.

## Key attributes of the agent-based model
The most important attributes of the Wolf-Sheep model for the purpose of this Activity are:
1. The agents inhabit a so-called  "torus", where if they move off the right boundary of the grid they reappear on the left boundary, and *vice versa*.
    Likewise, if they move off the upper boundary they reappear on the bottom boundary, and *vice versa*.
2. All events happen at discrete time steps, normalized to 1 time unit.
3. The model has three types of agents, that follow these rules:
    - Grass, which grows by itself at a rate set by the user and is consumed by a sheep if it is on the grass patch.
	- Sheep, which gain energy from eating grass, consume energy while moving in random directions, and are eaten if encountered by wolves.
	Sheep reproduce with a constant user-set probability each time step.
	- Wolves, which gain energy from eating sheep, consume energy while moving in random directions, and reproduce with a constant user-set probability each time step.
	- Both sheep and wolves die if they run out of energy.
4. Results are presented in two ways:
    - A visualization of the grid, with grown grass as green, eaten grass as brown, sheep as white and wolves as black.
	- A plot of grass, sheep and wolf populations over time.
5. The behavior of sheep and wolves has been simplified here, to speed execution of the simulation. 
    In the original, sheep avoid moving into patches with wolves, and wolves preferentially move into patches with sheep. 
	In this implementation, both sheep and wolves move randomly into any one of the neighboring patches, without requiring computation time to check for occupancy.
