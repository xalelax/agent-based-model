# -*- coding: utf-8 -*-
"""
@author: Alessandro
"""
import numpy as np
import matplotlib.pyplot as plt

class InsuredCustomers:
    
    def __init__ (self,
                  initial_number: int,
                  linear_monthly_growth_rate,
                  accident_probability: float,
                  claims_distribution):
        
        self.number_of_customers = initial_number
        self.growth_rate = linear_monthly_growth_rate
        
        # Initialize customer properties to zero
        self.months_insured  = np.zeros(self.number_of_customers)
        self.damages_claimed = np.zeros(self.number_of_customers)
        self.monthly_claim_rate = np.zeros(self.number_of_customers)
        
        if (0 < accident_probability < 1):
            self.accident_probability = accident_probability
        else:
            raise ValueError("Probability of accidents must be > 0.")
            
        self.claims_distribution = claims_distribution


    def add_users(self, n):
        self.months_insured     = np.append(self.months_insured,
                                            np.zeros(n))
        self.damages_claimed    = np.append(self.damages_claimed,
                                            np.zeros(n))
        self.monthly_claim_rate = np.append(self.monthly_claim_rate,
                                            np.zeros(n))


    def update(self, months):
        """Update the population taking into account accidents 
        and new customers"""
        
        # Update time since underwriting       
        self.months_insured += months
        
        # boolean variable which indicates how many had accidents
        accidents = (np.random.rand(self.number_of_customers) 
                                               > self.accident_probability)
        # Record damage claimed, and recalculate mcr
        for customer in accidents.nonzero():
            self.damages_claimed += self.claims_distribution.sample()
            self.monthly_claim_rate = (self.damages_claimed 
                                        / self.number_of_customers)
            
        self.add_users(round(self.growth_rate/months))
            
        
class ClaimsDistribution:

    def __init__ (self, mean, std):
        self.mean = mean
        self.std = std

    def sample(self):
        # Log claims normally distributed
        claim = np.random.lognormal(mean = self.mean, 
                                    std  = self.std)
        return claim

    