# 📖 Modes of cloning
Across species, cloning occurs in different forms.
In echinoderms, which represent many of the reported observations of cloning, there are at least two distinct modes of cloning:
1. *The echinoid mode of cloning*
	In the cloning mode most commonly observed in echinoids [sea urchins](wiki:Sea_urchin), larvae bifurcate during development, partway into their larval duration and prior to reaching competence.
	Each of these clones can either redifferentiate into a complete, smaller larva, or resume growth to reform the lost body parts. 
	Whether it redifferentiates or regrows lost parts, each clone has to grow back to a size and developmental stage at which it is competent. 
	

The model can simulate characteristics of two distinct modes of cloning, exemplified by cloning typically found in Echinoids and Ophiuroids:

- In the **Echinoid mode** of cloning, larvae grow and develop to a threshold size smaller than the size at metamorphosis. 
At this threshold size, some fraction of individuals clone to form two smaller daughters. 
These clones resume growth, and have one of three outcomes:
	1. They can remain as larvae until fully grown, and then proceed to metamorphosis.
	2. They proceed to metamorphosis before being fully grown, becoming smaller juveniles.
	3. They can remain as larvae, and clone again when they reach a threshold size.


- In the **Ophiuroid mode** of cloning, larvae grow past the point of competence. 
  These larger larvae then divide into two clones, one of which retains the size and stage needed for competence.
  This clone metamorphoses immediately.
  The other, smaller clone then resumes development, repeating growth and either metamorphosing directly or cloning again to form a metamorph and yet another small clone.

The `clone_modelND` model is a simulation of these two cloning stratagies, implemented as a [Jupyter notebook](LarvalCloningModel.ipynb).
