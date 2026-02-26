# 🛼 Time scales in the Wolf-Sheep-Grass model
Like many models (and real populations), the Mesa Wolf-Sheep model has a tendency towards boom-bust dynamics.
In these dynamics, one trophic level &ndash; grass, sheep or wolves &ndash; undergoes an outbreak, followed by a crash and the outbreak of a different trophic level.
Particularly in small habitats, these dynamics repeatedly bring populations down to very low levels, from which recovery or extinction is a matter of chance.

An important factor determining the likelihood of extinction is whether or not a population is **synchronized** across the entire habitat.
In a very small habitat, movement ensures that the population cannot be high in one location while being low in another.
That is, booms and busts are **synchronous** in very small habitats, so if extinction risk is high anywhere it's usuallyhigh everywhere.

The situation *may* be different in a very large habitat.
In a large habitat, it may take so long to move from one part of the habitat to another that different locations can become **asynchronous**.
If so, a bust in one location may coincide with a boom in another. 
Then, it may be rare for extinction risk to be high *everywhere*, even if it is almost always high *somewhere*.

## How big is big enough?
To get an indication of whether this might occur, and if so what is the minimum habitat size to make extinction unlikely, we will recapitulate (with modification) some of the analysis from the KISS model.

Specifically, we will conceive of a demography time scale, $T_{demog}$, and a movement time scale, $T_{move}$:
- $T_{demog}$ is the analog of $T_\alpha$ in the KISS mode, with the different notation reflecting that the multi-trophic level agent-based model does not have a parameter corresponding to the intrinsic rate of growth, $\alpha$.
- $T_{move}$ is the analog of $T_D$ in the KISS model, with the different notation reflecting that we need to estimate the effective diffusion rate from individual movement behaviors.

From these time scales, we can hypothesize that the parameter space of the Wolf-Sheep model has two distinct regions:
> - $\frac{T_{demog}}{T_{move}} \gg 1$, in which agents move across the domain quickly but demography happens slowly
> - $\frac{T_{demog}}{T_{move}} \ll 1$, in which demography happens quickly but agents move across the domain slowly

### Estimating the movement time scale
Borrowing results from the KISS model analysis, we can use the knowledge that both time and space steps are 1 in the Wolf-Sheep model:[^mov]
- $\Delta x = 1$
- $\Delta t = 1$

[^mov]: In a real population, we would typically obtain this information from tracking individuals or capture-recapture studies.

From this, we know that 
$$
D = \frac{\Delta x^2}{c \Delta t} = \frac{1}{c}
$$
where $c$ is a constant of order 1.

Depending on which cells are in the "neighborhood" into which wolves and sheep can move, the constant may be at or close to $c=4$.
Accepting this value for the present purposes, the movement time scale is then
$$
T_{move} \approx \frac{L^2}{D} = 4 L^2
$$

Using this result and rearranging, the parameter space regions are defined by
> - $\frac{\sqrt{T_{demog}}}{2} \gg  L$, in which agents move across the domain quickly but demography happens slowly
> - $\frac{\sqrt{T_{demog}}}{2} \ll  L$, in which demography happens quickly but agents move across the domain slowly

It is the latter case in which the hypothesis predicts persistence, so we propose the critical habitat size:
$$
L_{crit} = \frac{\sqrt{T_{demog}}}{2} 
$$
 
It remains, however, to estimate the demographic time scale that we proposed, $T_{demog}$, and to test whether simulation results support or contradict the hypothesis.
