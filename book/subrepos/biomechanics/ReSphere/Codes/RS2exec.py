# Import modules:
from math import *
import numpy as np
from scipy.interpolate import CubicSpline, interp1d
from scipy.optimize import root, bisect
import matplotlib.pyplot as plt
plt.ion()
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

# Set up textbox inputs
xmax=widgets.FloatText(value=40.,width=20,description = r"Range of plot, $X_{max}$ ($m$)")
n=widgets.FloatText(value=1.,description = r"Particle release rate, $n$ ($\#/s$)")
H=widgets.FloatText(value=10.,description = r"Release height, $h$ ($m$)")
W_s=widgets.FloatText(value=0.5,description = r"Particle sinking speed, $U_{s}$ ($m/s$)")
u_bar=widgets.FloatText(value=1.,description = r"Wind speed, $W$ (m/s)")
A=widgets.FloatText(value=0.5,description = r"Turbulent mixing intensity, $K$ ($m**2/s$)")
ui1f = widgets.VBox([xmax,n,H])
ui2f = widgets.VBox([W_s,u_bar,A])
ui3f = widgets.HBox([ui1f, ui2f])

def Sh7(xmax,n,H,W_s,u_bar,A):
    # A function to calculate and display a Gaussian plume.
    # This uses a combination of results from Okubo & Levin (1989) and Chapt 3, p. 67 from Okubo & Levin (2001).
    #
    # Note that this has somewhat confusing notation. The coded variable have symbols consistent with the 
    # literature from which they were cited. The text box labels have notation consistent with the
    # rest of the worksheet, and with intutive symbols (like W for wind instead of u_bar).
    n=1.     # The rate of particle release -- leave 1 to have normalized deposition.
    nbins=200
    xs=np.linspace(0.5,xmax,nbins)
    # Calculate Cross-Wind Integrated Deposition (CWID)
    sigma_z=np.sqrt(2*A*xs/u_bar);
    CWID=n*W_s/(sqrt(2*pi)*u_bar*sigma_z)*np.exp(-(H - W_s*xs/u_bar)**2./(2*sigma_z**2))
    #  Create a plot of CWID
    fig3, ax3 = plt.subplots()
    fig3.set_figwidth(10)
    CWIDpts=[[xs[i],CWID[i]] for i in range(len(xs))]
    ax3.plot(xs,CWID,'-',color='red',label='CWID')
    ax3.set_xlabel(r'Distance from source, $x$')
    ax3.set_ylabel(r'Particle deposition rate, $CWID$')
    # Create a contour plot of the underlying Gaussian plume (log scale for conc.):
    fig4, ax4 = plt.subplots()
    fig4.set_figwidth(12.5)
    S = lambda n_,u_,K_,x_,z_,w_s_,H_: n_*np.sqrt(u_/(float(pi)*K_*x_))*np.exp(-((z_-H_)+w_s_*x_/u_)**2/(4*K_*x_/u_))   
    x = np.arange(xs[0],xmax,(xmax-xs[0])/nbins)
    z = np.arange(0.,1.5*H,H/32.)
    X,Z=np.meshgrid(x,z)
    s=S(n,u_bar,A,X,Z,W_s,H)
    s_log10=np.log10(S(n,u_bar,A,X,Z,W_s,H))
    levels=[-6.,-5.,-4.,-3.,-2.,-1.,0.]
    CS2 = ax4.contourf(X, Z, s_log10,levels)
    cbar = plt.colorbar(CS2)
    plt.title('Gaussian plume model: $log_{10}$ scale')
    plt.xlabel("Distance from source, $x$")
    plt.ylabel("Height, $z$")        
    # Create a contour plot of the underlying Gaussian plume (log scale for conc.):
    fig5, ax5 = plt.subplots()
    fig5.set_figwidth(12.5)
    CS = ax5.contourf(X, Z, s)
    cbar = plt.colorbar(CS)
    plt.title('Gaussian plume model: linear scale')
    plt.xlabel("Distance from source, $x$")
    plt.ylabel("Height, $z$")        
    
out8 = widgets.interactive_output(Sh7,{'xmax':xmax,'n':n,'H':H,'u_bar':u_bar,'A':A,'W_s':W_s})
display(ui3f,out8)

