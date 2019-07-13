# -*- coding: utf-8 -*-
"""
@author: Alessandro
"""

class DiscreteTimeSimulation:    
    
    def __init__(self, initial_population, 
                 evolution_function = lambda x: x):
        self.population = initial_population
        self.evolution_function = evolution_function
        

    def step(self):
        try: 
            self.population = self.evolution_function(self.population)
        except:
            print('Error; step could not be executed.')