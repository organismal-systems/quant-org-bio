# ️💡️  A discrete-time model of cholera immune period
[Koelle *et al*. (2005)](https://doi.org/10.1038/nature03820) developed a model in which they tried to simultaneously quantify several epidemiological and environmental factors affecting cholera incidence.
They used monthly data from clinics in a focal site, Matlab, Bangladesh, from 1966 to 2002.
They focused on the predominant biotype, El Tor, but also included data on the Classical and Bengal biotypes as well as several indicators of local weather and regional climate variations.

Koelle *et al*.'s paper was an extensive parameter-fitting exercise, which is quite complicated.
This parameter fitting included physiological factors such as the immune period in a recovered victim of cholera, population factors such as the number of infected and susceptible residents, and environmental factors such as rainfall that affect both the aquatic habitat available to *V. cholera* bacteria and the sanitation breakdown and crowding caused by flooding.

Despite the complex process to estimate parameters, the model used by Koelle *et al*. to simulate cholera outbreaks is relatively simple.
This model is an example of a of so-called [*SIR* model](wiki:Compartmental_models(epidemiology)).
In *SIR* models, the population is classified into three "compartments":
1. $S$, the **susceptible** class
2. $I$, the **infected** class
3. $R$, the **recovered** class

The general structure of an *SIR* model is that 
> Contact between an infected individual and a susceptible individual has some probability of resulting in an infection, in which the susceptible individual becomes an infected individual.







%In these Study Questions, we will use a recreation of their model in the worksheet cholera4.sws to gain insights into the effectiveness of possible cholera mitigation strategies.
