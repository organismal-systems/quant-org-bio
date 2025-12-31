"""
Class definitions for a model of inter-strain competition among variants of 
the marine worm Spirorbis borealis on multiple substrates, as described by
Mackay & Doyle (1978). 
"""
import matplotlib.pyplot as plt
#import numpy as np
import numpy as np
import copy

class SpirorbisStrain:
    """
    Parameters container for Spirorbis competition simulations, for a single Spirorbis strain
    (i.e., a give set of settlement preferences)
    """
    def __init__(self,label='',color='',fecundity = 10**5,select_fucus=1,select_asco=1,
                 initial_larvae=10**9,initial_adults_fucus=0.,initial_adults_asco=0.):
        self.fecundity = fecundity
        self.select_fucus = select_fucus
        self.select_asco = select_asco
        self.initial_adults_fucus = initial_adults_fucus
        self.initial_adults_asco = initial_adults_asco
        self.initial_larvae = initial_larvae
        self.label = label
        self.color = color

class Site:
    """
    Parameters container for Spirorbis competition simulations, for a single site (habitat type).
    """
    def __init__(self,mortality_larvae = 0.1,
                 mortality_fucus = 0.01,mortality_asco = 0.1,
                 carrying_cap = 10**5,strains=[],f = 0.8,cat = 0.,
                 encounter_prob = 0.001,label=''):
        self.label = label
        self.mortality_larvae = mortality_larvae    # Mortality rate in the plankton
        self.mortality_fucus = mortality_fucus      # Mortality rate on Fucus
        self.mortality_asco = mortality_asco        # Mortality rate on Ascophyllum
        self.carrying_cap = carrying_cap            # Total carrying capacity of site
        self.f = f # Fraction carrying capacity covered by fucus substrate
        self.carrying_cap_fucus = carrying_cap * f   # Carrying capaicty on Fucus
        self.carrying_cap_asco = carrying_cap * (1-f) # Carrying capacity on Ascophyllum
        self.cat = cat                               # Probability of catastrophes
        self.encounter_prob = encounter_prob         # Index of larval encounter rate with substrate
        # List of strain objects; need separate dynamics in each site so make explicit copies
        self.strains = [copy.copy(strain) for strain in strains]


class SimParams:
    """
    Parameters container for Spirorbis competition simulations, for a single site (habitat type).
    """
    def __init__(self,exchange = 0.,timesteps = 4 * 10**2,plot_interval = 20,sites=[]):
        # Sites to be simulated
        self.sites = sites
        # Rates of exchange of water between environments (fraction of sites' water mixed per day)
        self.exchange = exchange
        self.timesteps = timesteps # Number of time units for the simulation to run
        self.plot_interval = plot_interval     #   Intervals at which to plot data

        
def SimSites(sim_params):
    """
    A function to parameterize and execute simulations of competition between strains of Spirorbis
    on multiple sites (habitat types).
    """

    sites = sim_params.sites
    exchange = sim_params.exchange
    timesteps = sim_params.exchange
    timesteps = sim_params.timesteps # Number of time units for the simulation to run
    plot_interval = sim_params.plot_interval     #   Intervals at which to plot data    
    #
    N_sites = len(sites) #Number strains
    #Population dynamics
    # Initialize arrays to save the population timeseries
    times = np.zeros(timesteps)
    for site in sites:
        for strain in site.strains:
            strain.Pseries_fucus = np.full(timesteps,np.nan)
            strain.Pseries_asco = np.full(timesteps,np.nan)
            strain.Pseries_larvae = np.full(timesteps,np.nan)
            strain.Pseries_fucus[0] = strain.initial_adults_fucus
            strain.Pseries_asco[0] = strain.initial_adults_asco
            strain.Pseries_larvae[0] = strain.initial_larvae
        
    #Main loop: (calculate populations at timestep+1 from populations at timestep
    for timestep in range(timesteps-1):
        #print(f'timestep = {timestep}')
        #print(i)
        times[timestep+1] = timestep + 1
        for site in sites:
            for strain in site.strains:
                # Calculate site-, stage- and substrate-specific mortality: first, remove individuals that
                # died during timestep, then copy that number into timestep+1 before reproduction, settlement etc.
                # This somewhat clunky sequencing is so that Pseries arrays reflect surviving adults rather than new settlement
                strain.Pseries_fucus[timestep] *= (1 - site.mortality_fucus)
                strain.Pseries_asco[timestep] *= (1 - site.mortality_asco)
                strain.Pseries_larvae[timestep] *= (1 - site.mortality_larvae)
                strain.Pseries_fucus[timestep+1] = strain.Pseries_fucus[timestep]
                strain.Pseries_asco[timestep+1] = strain.Pseries_asco[timestep]
                strain.Pseries_larvae[timestep+1] = strain.Pseries_larvae[timestep]
            #Check if a catastrophe occured.  If so, adults on all substrates die...
            if np.random.rand(1) < site.cat:
                for strain in site.strains:
                    strain.Pseries_fucus[timestep+1] = 0
                    strain.Pseries_asco[timestep+1] = 0
            # Calculate production and release of larvae by adults present at timestep+1
            for strain in site.strains:
                strain.larval_production = strain.fecundity * (strain.Pseries_fucus[timestep+1]+strain.Pseries_asco[timestep+1])
            #Calculate substrate available for settlement (in units of allowed settlers) and number of larvae vying for settlement
            site.avail_fucus = max(0,site.carrying_cap_fucus - sum([strain.Pseries_fucus[timestep+1] for strain in site.strains]))
            site.avail_asco = max(0,site.carrying_cap_asco - sum([strain.Pseries_asco[timestep+1] for strain in site.strains]))
            # Total number of larvae in water at site
            site.total_larvae = sum([strain.Pseries_larvae[timestep+1] for strain in site.strains])
            # Total number of larvae vying for Fucus and Ascophyllum substrate (weighted by selection probability)
            for strain in site.strains:
                strain.fucus_weighted_larvae = site.encounter_prob*strain.select_fucus*strain.Pseries_larvae[timestep+1]
                strain.asco_weighted_larvae = site.encounter_prob*strain.select_asco*strain.Pseries_larvae[timestep+1]
            site.total_fucus_weighted_larvae = sum([strain.fucus_weighted_larvae for strain in site.strains])
            site.total_asco_weighted_larvae = sum([strain.asco_weighted_larvae for strain in site.strains])
            # Add settlers to substrate, in proportion to their weighted abundance, removing them from the larval pool
            for strain in site.strains:
                # Use proportionality, but do not settle more larvae than are present...
                strain.number_settled_fucus = strain.fucus_weighted_larvae*\
                                              min(1.,site.avail_fucus/site.total_fucus_weighted_larvae )
                strain.number_settled_asco = strain.asco_weighted_larvae *\
                                              min(1.,site.avail_asco/site.total_asco_weighted_larvae )
                strain.Pseries_fucus[timestep+1] += strain.number_settled_fucus
                strain.Pseries_asco[timestep+1] += strain.number_settled_asco
                strain.Pseries_larvae[timestep+1] -= strain.number_settled_fucus + strain.number_settled_asco
            # Add larvae produced at timestep+1
            for strain in site.strains:
                strain.Pseries_larvae[timestep+1] += strain.larval_production

            # Exchange larvae among sites, parameterized in units of carrying capacity. It's assumed that:
            #  1) the strains have distinct labels, so that a dictionary based on strain labels correctly assigns larvae
            #  2) larvae from all sites are mixed into a common pool, from which they are reallocated to the sites
            #  3) the fraction of larvae from a given site going into the pool is exchange/carrying_cap; that is,
            #     if larvae occupy water volume proportional to carrying capacity then volume equal to exchange is
            #     mixed into and then drawn from the pool.
            count = 0
            # initialize a dictionary; the loop is usually not necessary to is done in case sites have initially
            # different larval strains
            pool = {}
            for site in sites:
                for strain in site.strains:
                    pool[strain.label] = 0.
            # Put larvae from the site into the pool
            for site in sites:
                for strain in site.strains:
                    transfer_larvae = exchange/site.carrying_cap * strain.Pseries_larvae[timestep]
                    pool[strain.label] += transfer_larvae
                    strain.Pseries_larvae[timestep] -= transfer_larvae
            # Put larvae from the pool back into the site; equal fractions of the pool go to each site
            # because equal amount of water are exchanged
            for site in sites:
                for strain in site.strains:
                    strain.Pseries_larvae[timestep] += 1./N_sites * pool[strain.label]

    # Update the final adult population records by imposing mortality
    for site in sites:
        for strain in site.strains:
            strain.Pseries_fucus[-1] *= (1 - site.mortality_fucus)
            strain.Pseries_asco[-1] *= (1 - site.mortality_asco)
    # Graphs of final results
    linetypes = ['-','--','-.',':']
    fig, axs = plt.subplots(N_sites, 1)
    for i,site in enumerate(sites):
        if N_sites > 1:
            axs_ = axs[i]
        else:
            axs_ = axs
        for j,strain in enumerate(site.strains):
            axs_.semilogy(times,strain.Pseries_fucus+strain.Pseries_asco,strain.color+linetypes[0],label=strain.label)
            axs_.semilogy(times,strain.Pseries_fucus,strain.color+linetypes[1])
            axs_.semilogy(times,strain.Pseries_asco,strain.color+linetypes[2])
        axs_.axhline(y=site.carrying_cap, color='gray', linestyle='-')
        axs_.set_ylabel(f'Site {site.label}')
        axs_.grid(True)
        axs_.legend()
        axs_.set_ylim(0.001*site.carrying_cap,1.2*site.carrying_cap)

        #total_fucus_adults = np.zeros(timesteps)
        #total_asco_adults = np.zeros(timesteps)
        #for strain in site.strains:
        #    total_fucus_adults += strain.Pseries_fucus
        #    total_asco_adults += strain.Pseries_asco
        #axs_.semilogy(timesteps, total_fucus_adultsstrain1_site1_1+strain1_site1_2,'k',
        #        times, strain2_site1_1+strain2_site1_2,'b',
        #        times, strain3_site1_1+strain3_site1_2,'g')

        #axs[0].set_xlim(0, 2)
        #axs[0].set_xlabel('time')

    # Print out summary statistics on final states
    for i,site in enumerate(sites):
        print(f'\nSite {site.label};')
        print(f'\tAvailable Fucus (previous step,): {site.avail_fucus}')
        print(f'\tAvailable Asco (previous step): {site.avail_asco}\n')
        for j,strain in enumerate(site.strains):
            print(f'\tStrain {strain.label} populations (after mortality):')
            print(f'\t\tAdult population: {strain.Pseries_fucus[-1]+strain.Pseries_asco[-1]:.2e}')
            print(f'\t\tFucus population: {strain.Pseries_fucus[-1]:.2e}')
            print(f'\t\tAsco population: {strain.Pseries_asco[-1]:.2e}')
            #print(f'\tStrain {strain.label} populations (after mortality):')
            #print(f'\t\tAdult population: {(1-site.mortality_fucus)*strain.Pseries_fucus[-1]+
            #                               (1-site.mortality_asco)*strain.Pseries_asco[-1]:.2e}')
            #print(f'\t\tFucus population: {(1-site.mortality_fucus)*strain.Pseries_fucus[-1]:.2e}')
            #print(f'\t\tAsco population: {(1-site.mortality_asco)*strain.Pseries_asco[-1]:.2e}')
            print(f'\t\tLarval population: {strain.Pseries_larvae[-1]:.2e}')
            print(f'\t\tNumber settled on Fucus (previous step): {strain.number_settled_fucus:.2e}')
            print(f'\t\tNumber settled on Asco (previous step): {strain.number_settled_asco:.2e}')

            
