# 🛼 Scaling insights into a 3 trophic level agent-based model
The first part of this Unit demonstrated how scaling analysis can be applied to the KISS model, in which a population distributed in space either grows or contracts over time according to a Partial Differential Equation, or PDE.
The scaling analysis was carrried out using the equation for that model, without the model solution being required. 
This is important, because although the KISS model can be solved analytically, most PDE population models cannot.
Therefore the ability to characterize the demographic outcomes of PDE models from the equation alone greatly extends our understanding of population dynamics

This activity extends our capabilities still further, by carrying out a scaling analysis of an [agent-based model](https://en.wikipedia.org/wiki/Agent-based_model) -- for which there is no equation at all.
In an agent-based model, individual "agents" move and interact with each other on a grid of "patches".
The dynamics of the model are specified in the form of rules for movement, for births of new agents and deaths of existing ones, impacts on their patch, *etc*.

In contrast to the PDE model, in an agent-based model the population-level dynamics are **emergent properties**, determined by numerous stochastic interactions among agents.
Agent-based model have the flexibility to simulate some aspects of individual-level behavior that are difficult to implement in PDEs.
However, extracting a "big-picture" understanding of their implications can be difficult because each simulation gives different results, and any generalities must be synthesized from a set of numerical results.

An additional challenge, and one on which this Activity focuses, is that simulating very large numbers of agents on very large grids is computationally very demanding.
On top of this, many dynamics that occur relatively slowly in small grids take much longer to develop in large grids.
These constraints can make it difficult to assess the outcomes of large populations over long time periods.

In the model, as in the real world, populations in tiny habitats quickly go extinct.
Some [opulations in larger habitats are more sustainable.
However, is that true for any given population?
If it is, how large is large enough?

The challenge in this Activity is to develop a scaling analysis that predicts the outcomes of large populations in large habitats over long times, using only outcomes of small populations in small habitats over short times.
This challenge has obvious relevance to the study and management of real-world populations, in which practical limitations usually constrain the scope of observations to a small number of individuals in a few locations at a few times.

Specifically, you will ask the question,
> - How does persistence in a 3 trophic level community depend on habitat size?

To answer this question, you will use a scaling analysis, similar in concept but different in execution to the scaling analysis for the KISS model.
As in that analysis, the goal here is to obtain an order of magnitude estimate for key thresholds determining "big-picture" outcomes, using the minimum possible amount of demographic data.
