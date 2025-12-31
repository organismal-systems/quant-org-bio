# 📖 Cloning in marine invertebrate larvae
In "normal" development (without cloning), a cohort of marine invertebrate larvae always decreases in population due to mortality.
This is because there is no mechanism for adding new larvae to the cohort. 
Assuming there is always a non-zero amount of mortality, the larval population must decrease.

The term [larval duration](wiki:Marine_larval_ecology) refers to the time required for larvae to develop to the a stage and size that makes them capable of metamorphosis.
The ultimate [recruitment](wiki:Recruitment_(biology)) &ndash; that is, the fraction of larvae surviving to  successfully metamorphose and join the post-larval population &ndash; is then determined by the impacts of the larval mortality rate, acting over the larval duration.

Recently, it has become clear that the larvae of a number of marine invertebrates can [clone](wiki:Cloning), either intrinsically or in response to environmental cues such as chemical stressors or predators.[^cln1]
In a cloning species, one larva can divide into two or more genetically identical "daughter" larvae. 
This means that, in cloning larvae, the number of larvae in a cohort can either increase or decrease at any given time during development.

[^cln1]: Some larvae may also shed parts of their bodies, which are not subsequently capable of developing into adults. This is a form of tissue loss, as distinct from the types of cloning that we consider here. 

While cloning produces two larvae out of one, it does not provide any additional tissue or nutritional resources to those larvae. 
This means a larva that clones produces two daughter larvae which are smaller.
In most cases it is not known what the metabolic losses of cloning are, as the daughter larvae divide resources from the original larva.
If cloning itself is not too metabolically costly, then a reasonable baseline approximation is that the resources of two daughters produced by cloning add up approximately to the resources of the original larva.

While cloning has an obvious benefit in terms of larval numbers, it also has costs.
Those costs may include disruptions to key larval functions such as swimming or feeding, as a clone redevelops a complete larval morphology.
For example, if either or both clones are initially formed without a functional stomach, feeding is impossible until one is developed.

Other costs may stem form delays to metamorphosis.
The term [larval duration](wiki:Marine_larval_ecology) refers to the time required for larvae to develop to the a stage and size that makes them capable of metamorphosis.
if the smaller clones must undergo additional growth to reach a threshold size, or the costs of forming a smaller juvenile if the clones metamorphose before growing enough to make up for dividing resources from the original larva.

Because there are relatively few quantitative observations of cloning in marine invertebrate larvae, especially under natural conditions, there is currently little empirical evidence whether or not cloning has important demographic effects on marine invertebrate populations.

## Modes of cloning
Across species, cloning occurs in different forms.
Echinoderms, which represent many of the reported observations of cloning, there are at least two distinct modes of cloning:
1. *The echinoid mode of cloning*

	In the cloning mode most commonly observed in echinoids [sea urchins](wiki:Sea_urchin), larvae simply bifurcate during development, prior to having grown and developed 
dividing their tissue into two parts. Each of these parts can either redifferentiate into a complete, smaller larva, or resume growing to reform the lost body parts. Whether it redifferentiates or regrows lost parts, a clone has to grow back to a size at which it is capable of metamorphosis (or of cloning again). The model neglects this difference in developmental mode of clones: Consistent with using size as a proxy, the model treats all larvae of size $s$ the same. 

The model can simulate characteristics of two distinct modes of cloning, exemplified by cloning typically found in Echinoids and Ophiuroids:

- In the **Echinoid mode** of cloning, larvae grow and develop to a threshold size smaller than the size at metamorphosis. At this threshold size, some fraction of individuals clone to form two smaller daughters. These clones resume growth, and either clone again when they reach the threshold size or proceed to metamorphosis. Clones resume growth, and either clone again when they reach the threshold size or proceed to metamorphosis.

- In the **Ophiuroid mode** of cloning, a fraction of surviving larvae grow past the size at metamorphosis. These larger larvae then divide into two clones, one of which metamorphoses immediately. The other, smaller clone then resumes development, repeating growth and either metamorphosing directly or cloning again to form a metamorph and yet another small clone.



%Like most larval life history models in the literature, **size is assumed in the** `clone_modelND` **model to be a *proxy* for developmental state**. This means that the model does not represent developmental state directly. Instead, it assumes that developmental state is closely coupled to size. For example, a larva is assumed to be competent to settle when it reaches a specific size. This approach means that the model does not exactly describe many details of morphology and life history associated with any given species. However, the more general results of this modeling approach may approximately describe a great many different species.



The `clone_modelND` model is capable of modeling many scenarios, such as fluctuating environments or multiple potential cloning or metamorphosis sizes, that are not implemented through this Jupyter NoteBook interface. These can be accessed by running the model directly from Python.
