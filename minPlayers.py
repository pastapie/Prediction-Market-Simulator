import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from simulateMarket import simulate_market

def find_minimum_participants(simulate_market_func, true_value, max_participants=5000, 
                             desired_accuracy=0.05, confidence=0.8, trials=1000):
    """
    Find the minimum number of participants needed for the prediction market to achieve the desired accuracy.
    Utilizes a binary search approach for optimization.
    
    :param simulate_market_func: Function to simulate the market, should match signature of `simulate_market`
    :param true_value: The true value participants are trying to predict
    :param max_participants: Maximum number of participants to consider
    :param desired_accuracy: The threshold for considering a prediction successful
    :param confidence: The required proportion of successful trials
    :param trials: Number of trials to run for each participant count
    :return: Minimum number of participants needed for a reliable market prediction
    """
    def is_accurate(n):
        """Run the simulation multiple times and check if it meets the confidence level."""
        successful_trials = sum(simulate_market_func(n, true_value, desired_accuracy) for _ in range(trials))
        return successful_trials / trials >= confidence
    
    # Start with a binary search
    left, right = 1, max_participants
    while left < right:
        mid = (left + right) // 2
        if is_accurate(mid):
            right = mid
        else:
            left = mid + 1
    
    # If we exit the loop without finding an accurate number, return None or max_participants
    if not is_accurate(left):
        return None
    return left

# Example usage:
minimum_participants = find_minimum_participants(simulate_market, true_value=100)
print(f"Minimum participants needed: {minimum_participants}")