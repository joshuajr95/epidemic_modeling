'''
File: simple_sir.py
Author: Joshua Jacobs-Rebhun
Date: March 25, 2022

This file implements a number of compartmental models for disease spread.
Compartmental models are simple models like SIR, SIRD, SISD, etc. that model
disease spread as simple transitions between disease states.
'''

import numpy as np
from matplotlib import pyplot as plt
import pickle


class SimulationResults:

    def __init__(self, S, I, R):
        self.S = S
        self.I = I
        self.R = R


class SIR_Model():

    def __init__(self):
        self.type = "SIR"
        self.num_vars = 3

    '''
    Birth rate and death rate are in percentage of population per time step
    '''
    def run_simulation(self, initial_infected, numTimeSteps, P, delta_t=0.1, beta=0.1, alpha=0.1, birth_rate=0.001, death_rate=0.001):

        # initialize simulation arrays to zeros 
        S = np.zeros(numTimeSteps)
        I = np.zeros(numTimeSteps)
        R = np.zeros(numTimeSteps)
        
        # set initial conditions
        S[0] = P - initial_infected
        I[0] = initial_infected
        R[0] = 0
        

        for t in range(1, numTimeSteps):

            delta_s = (birth_rate - death_rate)*S[t-1] - beta*I[t-1]*S[t-1]/P
            delta_i = beta*I[t-1]*S[t-1]/P - alpha*I[t-1] - death_rate*I[t-1]
            delta_r = alpha*I[t-1] - death_rate*R[t-1]

            S[t] = S[t-1] + delta_s
            I[t] = I[t-1] + delta_i
            R[t] = R[t-1] + delta_r

            #print(f"S[{t}] = {S[t]},\t I[{t}] = {I[t]},\t R[{t}] = {R[t]}")
        

        return SimulationResults(S, I, R)
    

    def graph(self, S, I, R):
        t = np.arange(len(S))

        plt.plot(t, S, color='darkslategray', label="Susceptible")
        plt.plot(t, I, color='lightskyblue', label="Infected")
        plt.plot(t, R, color='darkblue', label="Recovered")
        plt.legend()
        plt.xlabel("Time")
        plt.ylabel("S-I-R")
        plt.title("SIR Model")
        plt.show()
    
    def save(simulation_results, filename):
        pickle.dump(simulation_results, filename)


        