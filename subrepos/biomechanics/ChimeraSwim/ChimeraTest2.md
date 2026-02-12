# 🛼 Testing hypothetical performance standards: Metrics and rationale
We now consider strategies for assessing the hypothesis that natural selection effectively imposes "standards" for swimming performance in early-stage marine invertebrate larvae.
The tool at hand &ndash; a low Reynolds number simulation of swimming by idealized larval shapes &ndash; lends itself to an exploration of this hypothesis with a systematic mapping of swimming metrics across a range of morphologies.
A map of this type makes clear which sets of morphologies meet a hypothetical standard, and which fall short.

Assessing performance using a model of this sort is challenging primarily because:
- Numerous parameters are needed to specify the external and internal morphologies, material properties, initial conditions, *etc*.
- Ambient flow conditions are highly variable, and it is not clear which conditions are most relevant to selection on larval forms.
- It is not clear which metrics best reflect aspects of swimming performance most important to larval success, especially if testing is done in simplified flow conditions.

Here, we mitigate these problems by using organism-based parameters, further constrained by assumptions that [minimize the number of variables](./ChimeraTest.md) while still giving scope to variability that summarizes key trends, and by removing flow parameters by devising swimming performance metrics that can be measured in still water.
 
## Rationale: Testing a hypothetical performance standard for upwards swimming
A hypothetical performance standard for upwards swimming lends itself to a simple assessment of steady state velocity in simulations of larval swimming.

Specifically, starting from an arbitrary orientation, a freely swimming larva will over time assume its stable orientation after a transient re-orientation period.
For the range of morphologies considered here, the stable orientation is associated with the maximum upwards swimming rate.
That is, any deviation from that orientation will lead to a decrease in upwards swimming, as some or all of the swimming is directed in a horizontal direction.

Simulated still-water upwards swimming velocity in the stable orientation is therefore an informative metric of limits to swimming capacity associated with larval size and shape, as well as being directly analogous to most observations of larval swimming in experiments.

## Rationale: Testing a hypothetical performance standard for stability
The rationale for assessing a hypothetical performance standard for stability with still-water simulations is a bit more nuanced.

The starting point is the assumption that early-stage larvae must be capable of maintaining vertical orientation in the shear and turbulence characteristic of the habitats in which they undergo development.

### Disturbances to larval swimming due to turbulence
The key factor in larval stability is the type and intensity of disturbances to orientation due to movement of the ambient water, especially due to [turbulence](wiki:Turbulence).
Turbulence is chaotic flow that includes energetic [eddies and vortices](wiki:Vortex) and [shear](wiki:Simple_shear) at small scales.
Turbulence arises from [instabilities](wiki:Kelvin–Helmholtz_instability) in fast-flowing large-scale features such as currents, in which initially small flow disturbances are amplified and become more energetic. 
These instabilities are themselves unstable, so that distubances in the initial instabilities subsequently provoke further instabilities at smaller scales. 
This is referred to as the [energy cascade](wiki:Energy_cascade), and it causes some of the energy from large scale flows to be diverted to smaller and smaller eddies.

At very small scales, that energy is absorbed by viscosity and converted to heat.
At these scales, the flow at any one point is well approximated as being locally "linear" &ndash; that is, it is approximated by constant gradients in velocity expressed as shear in the form of(which, through viscosity, dissipates the energy as heat) and rotation.
That local shear and rotation are the flows implemented in the  [](ChimeraSwim.ipynb) model.

How small are these "very small" scales, and what are the shears and rotations involved? 
That depends on the how energetic the flow is: more energetic flows imply more energy flowing through the cascade that reaches smaller scales.
The most famous and widely used estimates of the length, time and velocity scales of the smallest eddies in a turbulent flow are the [Kolmogorov microscales](wiki:Kolmogorov_microscales).
These scales were defined using dimensional analysis by Kolmogorov as functions of the **turbulent energy dissipation rate**, $\epsilon$, and the **kinematic viscosity**, $\nu$:
- length scale, $l_K=\left( \frac{\nu^3}{\epsilon} \right)^{\frac{1}{4}}$ 
- time scale, $\tau_K=\left( \frac{\nu}{\epsilon} \right)^{\frac{1}{2}}$
- velocity scale, $v_K=\left( \nu \epsilon \right)^{\frac{1}{4}}$

Illustrative values of these scaes are shown in [](#kol1).
The values of $\epsilon$ near the top of this table represent the more energetic oceanic conditions (*e.g.*, near-surface) and those near the bottom represent more quiescent conditions (*e.g.*, the deep sea).

:::{table} Table of Kolmogorov microscales. Data are from [Yamazaki *et al*. (2002)](https://www.researchgate.net/publication/237600620_Chapter_3_COUPLING_SMALL-SCALE_PHYSICAL_PROCESSES_WITH_BIOLOGY)
:align: center
:label: kol1
| $\epsilon \left(\frac{W}{kg}\right)$ | $l_K (m)$ | $\tau_K (s)$ | $v_K (\frac{m}{s})$ |
| --- | --- | --- | --- |
| $10^{-4}$ | $3.16 \times 10^{-4}$ | $1. \times 10^{-1}$ | $3.16 \times 10^{-3}$ |
| $10^{-5}$ | $5.62 \times 10^{-4}$ | $3.16 \times 10^{-1}$ | $1.78 \times 10^{-3}$ |
| $10^{-6}$ | $1.0 \times 10^{-3}$ | $1.0$ | $1. \times 10^{-3}$ |
| $10^{-7}$ | $1.78 \times 10^{-3}$ | $3.16$ | $5.62 \times 10^{-4}$ |
| $10^{-8}$ | $3.16 \times 10^{-3}$ | $10.0$ | $3.16 \times 10^{-4}$ |
| $10^{-9}$ | $5.62 \times 10^{-3}$ | $31.6$ | $1.78 \times 10^{-4}$ |
| $10^{-10}$ | $1.0 \times 10^{-2}$ | $100.$ | $1. \times 10^{-4}$ |
:::

Keep in mind that the Kolmogorov microscales are only rough indicators of the length, time and velocity scales that larvae experience in these environments.
They are probably quantitatively accurate in most cases to an order of magnitude, if that.
Nonetheless, they provide a basis for relating habitats to *in situ* flows impacting larvae, particularly with respect to trends in these scales transitioning from quiescent to energetic environments.
In particular, they suggest that:
- Marine invertebrate larvae, particularly in their early stages, are typically smaller than the length scales of the smallest eddies.
That is, they see essentially "linearized" flow as assumed in the model.
- The estimated velocity scales of the smallest eddies are on the same order of magnitude as typical early-stage larval swimming speeds.
Because transport by these eddies is intermittent and in random directions, steady upswimming by larvae would likely lead to significant upwards movement through eddies at these scales over time.
- Because shear has units of $s^{-1}$, Kolmogorov's analysis suggests that the intensity of shear in the smallest eddies should scale approximately as the inverse of the time scale, $\frac{1}{\tau_K}$.
That ranges from $10 s^{-1}$ at the highest dissipation rates in [](#kol1), to $0.01 s^{-1}$ at the lowest.


### The timescale of larval reorientation
The simplest approach to using the Kolmogorov microscales to assess larval stability is to define a larval orientation time scale, 
> $\tau_{orient}$ is the timescale over which a larva, that is initially far from its stable orientation, turns so that its upwards velocity is effectively restored.  

With $\tau_{orient}$ as the time scale over which a larva can re-right itself, the hypothesis based on dimensional analysis is:
- $\tau_{orient} \ll \tau_K$ implies larvae remain oriented
- $\tau_{orient} \gg \tau_K$ implies larvae cannot maintain orientation. 

This relationship provides a rationale for a simple assessment of larval stability in still water:
> Measuring the reorientation time scale in still water provides a basis for estimating the levels of turbulence within which larvae can or cannot maintain the stable orientation necessary for effective swimming.



%Complications include that different taxa inhabit different aquatic habitats, that individual larvae likely transit multiple types of habitats, and that aquatic habitats in general are highly variable and poorly characterized.
%Therefore, is it difficult or impossible to select an intensity of turbulence or shear that can characterize convincingly whether a larva can or cannot maintain stability.

%A further complication is that the model does not simulated natural flow fields, but only a "linearized" flow in which fluid velocityincreases in proportion to distance from the origin.[^emb] 
%This means that, as larvae move further away from the origin, their swimming will in the long run always be overwhelmed by the ambient flow.

[^emb]: A version of the model has been implemented in which swimming larvae are effectively enbedded in turbulent flow, but that is outside the scope of this Activity.


%hypotheses/questions:

%> Larval morphologies must provide passive stability in excess of the torques imposed on them by turbulence and shear.

%> Is producing fewer large eggs that are more likely to survive, or more small eggs despite their being more susceptible to mortality, a more sucessful strategy?


%> How do embryos and other early-stage larvae, accomplish similar swimming performance with almost no apparently specialized swimming morphological features?


%> What are the constraints on larval size and shape resulting from the need to swim?

%> What are the constraints on swimming imposed by the need to satisfy other requirements and limitations in larval development?

%> How do each of these interact with environmental variations, and with the different life histories adopted by different taxa?
