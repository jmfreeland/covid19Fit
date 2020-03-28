# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 08:33:35 2020

@author: freel
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate, optimize


#ODE for timestep in SIR model
def sir_model(y, x, beta, gamma):
    #initial conditions
    Si = y[0]
    Ii = y[1]
    Ri = y[2]
    #deltas
    S = -beta * Si * Ii
    I = (beta * Ii * Si) - gamma * Ii
    R = gamma * Ii
    return S, I, R

N = 1.0
I0 = .00001
R0 = .001
S0 = N - I0 - R0

#add initial conditions to definition. return integrated ODE for Infected cases
def fit_odeint(initial, x, beta, gamma):
    return integrate.odeint(sir_model, initial, x, args=(beta, gamma))[:,1]

#define function to optimize using global S0, I0, R0
def temp_odeint(x, beta, gamma):
    return fit_odeint((S0, I0, R0), x, beta, gamma)


fitted = temp_odeint(xdata_long, .29,.2)
plt.plot(xdata_long,fitted)
popt
