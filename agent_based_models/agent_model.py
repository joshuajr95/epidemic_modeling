'''
File: agent_model.py
Author: Joshua Jacobs-Rebhun
Date: April 7, 2022

Implements the agent based modelling 
'''

from agent import Agent
import random
import sqlite3
import json

class AgentModel:

    # stateFile is for saving the agent_model (possibly pickle) and databaseFolder
    # is for storing databases that hold results of simulation.
    # SaveFile is for saving (serializing) the AgentModel object, and the
    # databaseFolder is the path to a folder to store all of the simulation results
    def __init__(self, numAgents, saveFile, databaseFolder):

        # simulation number keeps track of the number of simulations
        # that have been done so far to avoid conflicts between different runs
        # of the simulation overwriting the same database
        self.saveFile = saveFile
        self.simulationNumber = 0

        self.databaseFolder = databaseFolder

        # number of and array containing agents in simulation
        self.numAgents = numAgents
        self.agents = [None] * self.numAgents

        
        self.numSusceptible = numAgents
        self.numInfected = 0
        self.numRecovered = 0
        self.numDead = 0

        # indices of agents that are currently infected
        #self.infected = []
        
        
        # indices of agents that are currently recovered
        self.recovered = []
    
    '''
    def save(self):
        with open(self.saveFile) as sf:
            json.dump(self, sf)
    '''

    def initializeModel(self, initialInfected):

        for i in range(self.numAgents):
            if i < initialInfected:
                self.agents[i] = Agent(i, compartment="infected")
            else:
                self.agents[i] = Agent(i)
        
        self.numInfected = initialInfected
        
    
    '''
    Routine for running the actual simulation. Simultaneously simulates and records
    the aggregate simulation data to a sqlite database file.
    '''
    def simulate(self, infectionRate, recoveryRate, deathRate, reinfectionRate, timestep, numTimeSteps):

        databaseFile = self.databaseFolder + "/simulation_" + str(self.simulationNumber) + ".db"

        databaseConnection = sqlite3.connect(databaseFile)
        cursor = databaseConnection.cursor()
        cursor.execute("CREATE TABLE SIRD (Timestamp INTEGER PRIMARY KEY, Susceptible INTEGER, Infected INTEGER, Recovered INTEGER, Dead INTEGER)")

        for i in range(numTimeSteps):
            for j in range(self.numAgents):
                if self.agents[j].getCompartment() == "susceptible":
                    if random.random() <= infectionRate:
                        self.agents[j].infect()
                        self.numInfected += 1
                        self.numSusceptible -= 1

                elif self.agents[j].getCompartment() == "infected":
                    oneRecovered = False
                    if random.random() <= deathRate:
                        self.agents[j].die()
                        self.numDead += 1
                        self.numInfected -= 1
                        continue

                    elif random.random() <= recoveryRate:
                        self.agents[j].recover()
                        self.numRecovered += 1
                        self.numInfected -= 1

                elif self.agents[j].getCompartment() == "recovered":
                    if random.random() <= reinfectionRate:
                        self.agents[j].infect()
                        self.numInfected += 1
                        self.numRecovered -= 1

                else:
                    pass
            
            insertCommand = "INSERT INTO SIRD VALUES ({}, {}, {}, {}, {})".format(i, self.numSusceptible, self.numInfected, self.numRecovered, self.numDead)
            cursor.execute(insertCommand)
            #self.publish()
        
        self.simulationNumber += 1

        databaseConnection.commit()
        databaseConnection.close()
                
            



