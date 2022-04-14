'''
File: agent.py
Author: Joshua Jacobs-Rebhun
Date: April 7, 2022

This file implements the agent class for agent-based models.
'''


class Agent:

    # initialize the agent with the given compartment (SIR, etc.) and
    # optionally the x and y position
    def __init__(self, idNumber, compartment="susceptible", xPosition=None, yPosition=None):
        self.compartment = compartment
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.idNumber = idNumber
    

    '''
    Methods for setting compartment state variables.
    '''

    def infect(self):
        self.compartment = "infected"
    
    def recover(self):
        self.compartment = "recovered"
    
    def die(self):
        self.compartment = "dead"
    

    '''
    Getters for compartment state variables
    '''

    def isInfected(self):
        return self.compartment == "infected"
    
    def isRecovered(self):
        return self.compartment == "recovered"
    
    def isDead(self):
        return self.compartment == "dead"
    
    def isSusceptible(self):
        return self.compartment == "susceptible"
    
    def getCompartment(self):
        return self.compartment


    '''
    Move the agent
    '''
    def move(self, newX, newY):
        pass
