import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from simulateMarket import simulate_market

def find_minimum_participants(true_value, trials=1000, max_participants=5000, desired_accuracy=0.05):
    """
    Find the minimum number of participants needed for the prediction market to achieve the desired accuracy.
    Includes strategic behavior and heavy-tailed prediction distributions.
    """
    for n in range(1, max_participants):
        successful_trials = sum(simulate_market(n, true_value, desired_accuracy) for _ in range(trials))
        if successful_trials / trials >= 0.8:  # 80% of the trials must be successful to be considered reliable
            return n
    return None

minimum_participants = find_minimum_participants(true_value=100, 
                                                 max_participants=1000)
print(f"Minimum participants needed: {minimum_participants}")

minimum_participants = find_minimum_participants(true_value=100, 
                                                 max_participants=1000, 
                                                 desired_accuracy=0.10)
print(f"Minimum participants needed: {minimum_participants}")

minimum_participants = find_minimum_participants(true_value=100, 
                                                 max_participants=10000, 
                                                 desired_accuracy=0.10)
print(f"Minimum participants needed: {minimum_participants}")

minimum_participants = find_minimum_participants(true_value=100, 
                                                 max_participants=50000, 
                                                 desired_accuracy=0.10)
print(f"Minimum participants needed: {minimum_participants}")