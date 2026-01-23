# ️📖️   A model of cholera immune period
[Koelle *et al*. (2005)](https://doi.org/10.1038/nature03820) developed a model in which they tried to simultaneously quantify several epidemiological and environmental factors affecting cholera incidence.
They used monthly data from clinics in a focal site, Matlab, Bangladesh, from 1966 to 2002.
They focused on the predominant biotype, El Tor, but also included data on the Classical and Bengal biotypes as well as several indicators of local weather and regional climate variations.

Koelle *et al*.'s paper was an extensive parameter-fitting exercise, which is quite complicated.
This parameter fitting included physiological factors such as the immune period in a recovered victim of cholera, population factors such as the number of infected and susceptible residents, and environmental factors such as rainfall that affect both the aquatic habitat available to *V. cholera* bacteria and the sanitation breakdown and crowding caused by flooding.

## Model rationale
Despite the complex process to estimate parameters, the model used by Koelle *et al*. to simulate cholera outbreaks is relatively simple.
This model is an example of a of so-called [*SIR* model](wiki:Compartmental_models(epidemiology)).
In *SIR* models, the population is classified into three "compartments":
1. $S$, the **susceptible** class
2. $I$, the **infected** class
3. $R$, the **recovered** class

The general structure of an *SIR* model is that:
- Contact between an infected individual and a susceptible individual has some probability of resulting in an infection, in which the susceptible individual becomes an infected individual (moving from $S$ to $I$).
  
  Infected individuals often have distinct traits, such as a higher mortality rate than susceptible individuals.

- An infected individual has some probability per unit time of recovering from infection (moving from $I$ to $R$).

  A recovered individual may have different characteristics from a susceptible individual. 
  For example, a recovered individual may have an acquired immunity to the disease, or a distinct mortality or reproduction rate.

- A recovered individual may revert to a susceptible individual, after the distinct immunological or demographic characteristics of a recovered individual have subsided.
  
Transitions between $S \rightarrow I \rightarrow R \rightarrow S$ form a cycle, so (in general) an individual can undergo repeated infection and recovery cycles.

Characteristics of this general model must be adapted for application to any given disease.
For example, some diseases are invariably fatal, or do not result in acquired immunity, so there may be no recovered class.
Some diseases have distinctive effects on demographic rates, while others do not.

When the population *N* is known, *SIR* models simplify to two independent population classes, $S$ and $I$, where $R = N - S - I$ implicitly specifies the recovered class.

## Koelle *et al*.'s SIR model
Koelle *et al*.'s model quantifies several characteristics of cholera infections that are poorly understood. 

### Immune period
Koelle *et al*. estimated the period over which an individual who has recovered from a cholera infection is resistant to being re-infected.
In cholera, as in most diseases, this acquired immunity decays over time, and the duration of immunity has strong effects on disease dynamics.

In Koelle *et al*.'s model, immunity has the following form:
```{figure} images/immunity.png
:label: imm
:alt: Immune period
:width: 400px
:align: center

A plot of $\kappa_i$, the immune function from Koelle *et al*.'s cholera model, with immunity period $t_{immunity}=12$ and asymptomatic ratio $A=25$.
```
The graph of immunity level, $\kappa_i$, in [](#imm) reflects two parameters emerging from Koelle *et al.*'s fitting analysis:
1. The **immune period**, $t_{immunity}$, which is the timescale over which immunity decreases from its initial full protection to entirely absent.
2. The **asymptomatic ratio**, $A$, which is the number of cholera infections that are asymptomatic or otherwise not reported in the data from local clinics.
  $A$, is the intercept of the $\kappa_i$ curve at 0 months.

It's important to understand that 
> The $\kappa_i$ curve represents the **actual** number of individual with acquired immunity for each **reported** cholera infection. 

The ratio of actual to reported infections ($A$) is unknown, and must be estimated as part of the analysis. 
This distinction between actual and reported cases explains the apparent paradox that each infection results in 25 individuals with acquired immunity.

### Variability in transmission rate
Factors like flooding have strong but complicated and potentially contradictory effects on transmission cholera rates.
Weather-related factors like flooding are, in turn, affected both by seasonal fluctuations such as monsoons and dry seasons, and by longer term climatic variation such as El Niño. 

Koelle *et al.*'s analysis separated variations in transmission rate into two multiplicative factors:

#### Seasonal variation in transmission rate, $\beta_{season}$
```{figure} images/seasonality.png
:label: sea
:alt: Seasonal transmission effects
:width: 400px
:align: center

Seasonal effects on transimssion rate in Koelle *et al*.'s cholera model.
```
In our implementation of the model, seasonal variability is approximated by a sinusoidal function with a linearly decreasing amplitude ([](#sea)). 

The strength of seasonal variations is determined by the **seasonal fluctuation parameter**, $c$.

#### Climatic variation in transmission rate, $\beta_{season}$
```{figure} images/climate.png
:label: cli
:alt: Climate transmission effects
:width: 400px
:align: center

Climate effects on transimssion rate in Koelle *et al*.'s cholera model.
```
In our implementation of the model, climatic variation is approximated by a linear increase to the midpoint of the simulation, followed by a linear decrease ([](#cli)).

The strength of climate variations is determined by the **climate fluctuation parameter**, $b$.

#### Transmission rate variability, $\beta_t$
```{figure} images/transmission.png
:label: tra
:alt: Climate transmission effects
:width: 400px
:align: center

Transmission rate variability in Koelle *et al*.'s cholera model.
```
The resulting transmission rate used in this implementation of Koelle *et al*.'s model is the product of the seasonal and climate variabilities ([](#tra)).
