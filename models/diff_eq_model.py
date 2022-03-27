'''
File: diff_eq_model.py
Author: Joshua Jacobs-Rebhun
Date: March 25, 2022

This file implements an interface for a model that is formulated as a system
of differential equations. The model has certain input variables and certain
output variables, both of which are class members. Both input variables and
output variables must be iterables which can be iterated over. Finally, the
model interface has a number of methods that must be implemented for the model
to work, including run().
'''


class Model:

    def __init__(self):
        pass
    
    def run_simulation(*args, **kwargs):
        pass
    
    def graph():
        pass
    
