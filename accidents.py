# -*- coding: utf-8 -*-
"""
@author: Alessandro
"""

from models import DiscreteTimeSimulation

import numpy as np

class InsuredCustomers:
    
    def __init__ (self, size):
        self.months_insured  = np.zeros(size)
        self.damages_claimed = np.zeros(size)
        self.monthly_claim_rate = np.zeros(size)


