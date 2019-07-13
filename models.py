# -*- coding: utf-8 -*-
"""
@author: Alessandro
"""

class DiscreteTimeSimulation:    
    
    def __init__(self, initial_population):
        self.population = initial_population       

    def step(self):
        try: 
            self.population = self.population.step()
        except:
            print('Error; simulation step could not be executed.')