'''A partial implementation of the allometric quota model from Litchman et al. (2009)
   for the evolution of diatom size in fluctuating environments. This model implements
   only the model for nitrogen limitation. The different alometries for phosphorus
   limitation are not implemented.
'''
# Load modules and set graphics environment
from math import *
from tabulate import tabulate
import numpy as np
from scipy.integrate import solve_ivp
from matplotlib import pyplot as plt
plt.ion();

class diatoms:
    '''A class to facilitate simulation of the diatom size-quota model from Litchman et al. (2009).
    '''
    def __init__(self,n_sizes=8,size_range=[2.5,2.5+1.25*8],qinit=0.1,m=0.08,
                 setup=True,
                 static_v=False,v_const=0.0,z_m=10,a=0.3,Rdeep=40,use_log10=True):
        self.n_sizes = n_sizes
        self.size_range = size_range
        self.use_log10 = use_log10
        self.qinit = qinit    # initial quota, as a fraction between qmax and qmin
        self.Rdeep = Rdeep
        #
        self.m = m
        self.static_v = static_v
        self.v_const = v_const
        self.z_m = z_m
        self.a = a
        #  Allometric parameters for nitrogen, from Litchman et al. (2009)
        self.a_V_hi_max=-7.8
        self.b_V_hi_max=0.67
        self.a_K_n=-0.49
        self.b_K_n=0.17
        self.a_Qmin=-8.59
        self.b_Qmin=0.56
        self.a_Qmax=-8.39
        self.b_Qmax=0.81
        self.a_mu_inf=0.74
        self.b_mu_inf=-0.14
        #
        if setup:
            self.setup()

    def setup(self,size_range=None,n_sizes=None,use_log10=None,qinit=None,
              Rdeep=None):
        '''Set up an ODE system to be solved. The initial diatom populations
           are set to zero; use the seed method to initialize the populations.
           use_log10 determines whether parameters are interpreted as log10
           or ln values.
        '''
        if n_sizes:
            self.n_sizes = n_sizes
        if use_log10:
            self.use_log10 = use_log10
        if size_range:
            self.size_range = size_range
        if qinit:
            self.qinit = qinit
        if Rdeep:
            self.Rdeep = Rdeep
        # Set up arrays for diatom size classes
        self.sizes = np.linspace(self.size_range[0],self.size_range[1],self.n_sizes)
        self.Ns = np.zeros(self.n_sizes)
        #self.Ns = np.zeros([self.n_sizes,1])
        if self.static_v:  # constant sinking velocity
            self.vels = self.v_const * np.ones(self.n_sizes)
        else: # size-dependent sinking velocity
            self.vels = 0.43 * self.sizes - 0.77
            # Sinking velocity must be non-negative
            self.vels[np.where(self.vels<0.)] = 0.
        # Set up rate parameters for uptake, mortality, etc.
        if use_log10: # intepret parameters as log base 10
            ex_ = 10
        else:   # intrepret parameters as natural logs
            ex = np.e
        self.V_hi_max = (ex**(self.a_V_hi_max+self.b_V_hi_max*self.sizes))
        self.K = ex**(self.a_K_n+self.b_K_n*self.sizes)
        self.mu_inf = ex**(self.a_mu_inf+self.b_mu_inf*self.sizes)
        # Set up initial quotas, using fractional initial value qinit
        self.Qmin = ex**(self.a_Qmin+self.b_Qmin*self.sizes)
        self.Qmax = ex**(self.a_Qmax+self.b_Qmax*self.sizes)
        self.Qs = self.qinit*(self.Qmax-self.Qmin) + self.Qmin
        self.V_lo_max = self.mu_inf*(self.Qmax-self.Qmin)

    def mix(self):
        '''Execute a "mixing event" in which deep water is exchanged with water
           from the mixed layer. This is assumed to remove diatom population
           in proportion to the fraction of mixed layer replaced, and add
           nutrients in proportion to the fraction of mixed layer replaced
           and the concentration of nutrient in deep water.
        '''
        #print('Mixing!')
        # Remove cells in water lost to below the mixed layer
        self.QNR[self.n_sizes:2*self.n_sizes] *= 1-self.a
        # Add nutrient in water brought up from below the mxed layer
        self.QNR[-1] = (1-self.a) * self.QNR[-1] + self.a*self.Rdeep

    def seed(self,reset=False,N=10,sizes=[],qinit=None):
        '''Add to the existing diatom populations. If reset is True, then the
           population is replaced, rather than augmented, by the supplied values.
           If the list "sizes" is supplied, only listed sizes are augmented.
           Otherwise, all size classes are augmented.
        '''
        # Calculate provisional initial conditions; then do a sanity check
        # to make sure values are physical before implementing changes
        Ns = self.Ns.copy()
        if reset:  # zero out populations before seeding
            Ns *= 0.
        if isinstance(sizes,list):  # a list is provided of size classes to seed
            #print(f'seeding size classes {sizes} using list mode')
            for i in sizes:
                Ns[i] += N
        elif isinstance(sizes,int):  # a list is provided of size classes to seed
            #print(f'seeding size classes {sizes} using list mode')
            Ns[sizes] += N
        elif sizes=='all':      # seed all size classes
            #print('seeding all size classes using "all" mode')
            Ns += N
        else:
            print('Invalid size selection! Skipping...')
            print(sizes)
            return
        # Initialize total initial nutrient (resource), R, which
        # must be non-negative
        R = self.a*self.Rdeep - (Ns*self.Qs).sum()
        if R >= 0.:    # sanity check passed; implement changes
            self.R = R * np.ones(1)
            #self.R = R * np.ones([1,1])
            self.Ns = Ns
        else:          # sanity check failed; return without implementing
            print('***ERROR: values not changed!***')
            print('Parameters are invalid because cells contain more than the total amount of nutrient')
            print('Please reduce the number of cells or their initial quotas and try again')
            return False

    def ODEsys(self,t,QNRs):
        '''Define the system of ODEs including, in order, the instantaneous rates of change of cell quotas,
           cell numbers, and resource concentration. To satisfy the ODE solver, these are passed as a
           single concatenated array and split inside the method.
        '''
        # Parse the state array into its quota, number and nutrient components
        Qs = QNRs[0:self.n_sizes]
        Ns = QNRs[self.n_sizes:2*self.n_sizes]
        R = QNRs[-1]
        # Define rates of change of quotas, number and resource
        dQdts = (self.V_hi_max-(self.V_hi_max-self.V_lo_max)*(Qs-self.Qmin)/(self.Qmax-self.Qmin)) * \
                 R/(R+self.K) - self.mu_inf*(1-self.Qmin/Qs)*Qs
        dNdts = self.mu_inf * (1-self.Qmin/Qs) * Ns - self.m * Ns - self.vels/self.z_m * Ns
        dRdt = -((self.V_hi_max-(self.V_hi_max-self.V_lo_max) * \
                  (Qs-self.Qmin)/(self.Qmax-self.Qmin))*R/(R+self.K)*Ns).sum()
        # Reassemble rates into a concatenated array; retain its value for debugging and analysis
        self.dQNRdts = np.hstack([dQdts,dNdts,dRdt])
        return self.dQNRdts

    def solveODEs(self,n_pers=None,t_mix=None,n_record=None,mix_first=True):
        '''Execute the simulation and display output.
        '''
        self.t_mix = t_mix      # interval of mixing events, in days
        self.n_pers = n_pers    # end time of simulation, in mixing periods
        self.n_record = n_record # number of data recorded for plotting, per mixing day
        # Set up initial conditions for time, quotas, numbers and resource as a concatenated array
        self.QNR = np.hstack([self.Qs,self.Ns,self.R])
        # initialize arrays for results
        self.t_data = np.linspace(0,self.t_mix,self.n_pers*self.n_record+1) # time points to record data
        self.QNR_avg = np.full([self.n_pers,2*self.n_sizes+1],np.nan) # period-averaged system states
        # Main loop, stopping at intervals to execute a mixing event
        for i in range(self.n_pers):  # loop over mixing periods
            # Mix at the start of the period 
            self.mix()
            # set time range of next integration
            t_step = [0.,self.t_mix]
            # execute the integration
            self.solve_ivp = solve_ivp(self.ODEsys,t_step,self.QNR,t_eval=self.t_data)
            # Append results to data arrays (actually replaces the arrays...)
            self.QNR_data = self.solve_ivp.y.transpose()
            self.QNR_avg[i,:] = np.mean(self.QNR_data,axis=0,keepdims=True)
            # Update the QNR array, as the initial condition for the next period
            self.QNR = self.QNR_data[-1,:]
        # Parse the quotas, numbers and resource back into separate arrays, for restart if desired
        self.Qs = self.QNR_data[-1,:self.n_sizes]
        self.Ns = self.QNR_data[-1,self.n_sizes:2*self.n_sizes]
        self.R = self.QNR_data[-1,-1]
        # Display some statistics
        self.stats()
        # Plot
        self.plot()

    def stats(self):
        '''Report statistics of resource (nutrient), and quota and number for each size class.
        '''
        # Parse 1-period time series (QNR_data) into quota, number and resouce arrays
        Qs = self.QNR_data[:,0:self.n_sizes]
        Ns = self.QNR_data[:,self.n_sizes:2*self.n_sizes]
        R = self.QNR_data[:,-1]
        # Parse period average time series (QNR_avg) into quota, number and resouce arrays
        Qavgs = self.QNR_avg[:,0:self.n_sizes]
        Navgs = self.QNR_avg[:,self.n_sizes:2*self.n_sizes]
        Ravg = self.QNR_avg[:,-1]
        t_avg = [(0.5+n)*self.t_mix for n in range(self.n_pers)]
        # Period-averaged standing stock
        print('\n***Period-averaged statistics: standing stocks (also in standingstocks.txt)***\n')
        tabhdr = ['i','s','10^s','N','Q/Qmin','BV']
        tabdata = []
        BVtotal = 0.
        for i,s in enumerate(self.sizes):
            w = [i,s,10**s,Navgs[-1][i],Qavgs[-1][i]/self.Qmin[i],Navgs[-1][i]*10**self.sizes[i]]
            tabdata.append(w)
            BVtotal += Navgs[-1][i]*10**self.sizes[i]
        print(tabulate(tabdata,tabhdr,floatfmt=".3g"))
        with open('standingstocks.txt','w') as sfile:
            sfile.write('i,s,10^s,N,Q/Qmin,BV\n')
            for i,s in enumerate(self.sizes):
                sfile.write(f'{i},{s:.3g},{10**s:.3g},{Navgs[-1][i]:.3g},{Qavgs[-1][i]/self.Qmin[i]:.3g},{Navgs[-1][i]*10**self.sizes[i]:.3g}\n')
        print(f'\nTotal biovolume = {BVtotal:.3g}')
        print(f'Total averaged nutrient = {Ravg[-1]:.3g}\n')
        
        # Period-averaged losses
        print('\n\n***Period-averaged statistics: biovolume losses per day to mortality (M), sinking (S) and mixing (L) (also in losses.txt)***\n')
        tabhdr = ['i','s','10^s','M','S','L']
        tabdata = []
        Mtotal = 0.
        Stotal = 0.
        Ltotal = 0.
        for i,s in enumerate(self.sizes):
            BVavg_i = Navgs[-1][i]*10**self.sizes[i]   # period-averaged biovolume for the ith size class
            M = self.m * BVavg_i                       # "background" mortality for the ith size class, in BV/day units 
            S = self.vels[i]/self.z_m * BVavg_i        # sinking mortality for the ith size class, in BV/day units 
            BVstart_i = Ns[0][i]*10**self.sizes[i]
            BVend_i = Ns[-1][i]*10**self.sizes[i]
            # these two should agree, if population is periodic:
            L = self.a * BVend_i/self.t_mix         # mixing loss mortality for the ith size class, in BV/day units
            #L = (BVend_i-BVstart_i)/self.t_mix         # mixing loss mortality for the ith size class, in BV/day units
            w = [i,s,10**s,M,S,L]
            tabdata.append(w)
            Mtotal += M
            Stotal += S
            Ltotal += L
        print(tabulate(tabdata,tabhdr,floatfmt=".3g"))
        print(f'\nTotal background mortality = {Mtotal:.3g}')
        print(f'Total sinking mortality = {Stotal:.3g}')
        print(f'Total mixing mortality = {Ltotal:.3g}')
        with open('losses.txt','w') as sfile:
            sfile.write('i,s,10^s,M,S,L\n')
            for i,s in enumerate(self.sizes):
                BVavg_i = Navgs[-1][i]*10**self.sizes[i]   # period-averaged biovolume for the ith size class
                M = self.m * BVavg_i                       # "background" mortality for the ith size class, in BV/day units 
                S = self.vels[i]/self.z_m * BVavg_i        # sinking mortality for the ith size class, in BV/day units 
                BVstart_i = Ns[0][i]*10**self.sizes[i]
                BVend_i = Ns[-1][i]*10**self.sizes[i]
                # these two should agree, if population is periodic:
                #L = (BVend_i-BVstart_i)/self.t_mix         # mixing loss mortality for the ith size class, in BV/day units
                L = self.a * BVend_i/self.t_mix         # mixing loss mortality for the ith size class, in BV/day units
                sfile.write(f'{i},{s:.3g},{10**s:.3g},{M:.3g},{S:.3g},{L:.3g}\n')

    def plot(self,w=8,h=12):
        '''Plot time series data for resource (nutrient), and quota and number for
           each size class.
        '''
        print('\nPlotting...')
        # Parse 1-period time series (QNR_data) into quota, number and resouce arrays
        Qs = self.QNR_data[:,0:self.n_sizes]
        Ns = self.QNR_data[:,self.n_sizes:2*self.n_sizes]
        R = self.QNR_data[:,-1]
        # Parse period average time series (QNR_avg) into quota, number and resouce arrays
        Qavgs = self.QNR_avg[:,0:self.n_sizes]
        Navgs = self.QNR_avg[:,self.n_sizes:2*self.n_sizes]
        Ravg = self.QNR_avg[:,-1]
        t_avg = [(0.5+n)*self.t_mix for n in range(self.n_pers)]
        #----------------------------------------
        # Plot quotas
        self.fig1=plt.figure(figsize=(w,h))
        Qax = self.fig1.add_subplot(311)
        for i in range(self.n_sizes):
            legend_lab=f"s = {self.sizes[i]:4.2f}"
            Qplot = Qax.plot(self.t_data,Qs[:,i]/self.Qmin[i],label=legend_lab)
        Qax.set_ylabel('Fractional quotas')
        Qax.set_xlabel('Time (days)')
        Qax.legend()
        Qax.set_ylim(bottom=1)
        # Plot number/biovolume
        Nax = self.fig1.add_subplot(312)
        for i in range(self.n_sizes):
            legend_lab=f"s = {self.sizes[i]:4.2f}"
            Nplot = Nax.semilogy(self.t_data,Ns[:,i]*10**self.sizes[i],label=legend_lab)
        Nax.set_ylabel('Biovolume')
        Nax.set_xlabel('Time (days)')
        #Nax.legend()
        Nax.set_ylim(bottom=0.1)
        # Plot resource (nutrient)
        Rax = self.fig1.add_subplot(313)
        Rplot = Rax.plot(self.t_data,R)
        Rax.set_ylabel('Resource (nutrient)')
        Rax.set_xlabel('Time (days)')
        Rax.set_ylim(bottom=0)
        self.fig1.suptitle(f'Mixing every {self.t_mix} days: 1-Period Time Series')
        self.fig1.tight_layout()
        #----------------------------------------
        # Plot period averages across all time
        self.fig2=plt.figure(figsize=(w,h))
        Q2ax = self.fig2.add_subplot(311)
        for i in range(self.n_sizes):
            legend_lab=f"s = {self.sizes[i]:4.2f}"
            Q2plot = Q2ax.plot(t_avg,Qavgs[:,i]/self.Qmin[i],label=legend_lab)
        Q2ax.set_ylabel('Period-averaged fractional quotas')
        Q2ax.set_xlabel('Time (days)')
        Q2ax.legend()
        Q2ax.set_ylim(bottom=1)
        # Plot number/biovolume
        N2ax = self.fig2.add_subplot(312)
        for i in range(self.n_sizes):
            legend_lab=f"s = {self.sizes[i]:4.2f}"
            N2plot = N2ax.semilogy(t_avg,Navgs[:,i]*10**self.sizes[i],label=legend_lab)
        N2ax.set_ylabel('Period-averaged biovolume')
        N2ax.set_xlabel('Time (days)')
        #N2ax.legend()
        N2ax.set_ylim(bottom=0.1)
        # Plot resource (nutrient)
        R2ax = self.fig2.add_subplot(313)
        R2plot = R2ax.plot(t_avg,Ravg)
        R2ax.set_ylabel('Period-averaged resource (nutrient)')
        R2ax.set_xlabel('Time (days)')
        R2ax.set_ylim(bottom=0)
        self.fig2.suptitle(f'Mixing every {self.t_mix} days: Period-Averaged Time Series')
        self.fig2.tight_layout()
        


