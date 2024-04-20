import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def simulate_market(n, true_value, desired_accuracy=0.05, interaction_factor=0.1, iterations=10):
    """

    Simulate a prediction market with n participants using a heavy-tailed t-distribution for predictions.
    Introduce interaction among participants to reflect influence from the market consensus.

    """

    # fix the parameters
    bias_range = (-0.5, 0.5)    # bias range for normal players
    sd_range = (0.5, 2)         # stdev range for normal players
    
    strategic_bias_range = (-0.1, 0.1)  # bias range for strategic players
    strategic_sd_range = (0.1, 0.5)     # stdev range for strategic players

    degrees_of_freedom = 5      # degrees of freedom for t distribution

    # participant categorization
    strat_players = int(n * 0.1)
    norm_players = n - strat_players

    #strategic player params
    strat_biases = np.random.uniform(strategic_bias_range[0], strategic_bias_range[1], strat_players)
    strat_sds = np.random.uniform(strategic_sd_range[0], strategic_sd_range[1], strat_players)
    strat_predictions = np.random.standard_t(degrees_of_freedom, strat_players) * strat_sds + strat_biases + true_value

    # normal player params
    norm_biases = np.random.uniform(bias_range[0], bias_range[1], norm_players)
    norm_sds = np.random.uniform(sd_range[0], sd_range[1], norm_players)
    norm_predictions = np.random.standard_t(degrees_of_freedom, norm_players) * norm_sds + norm_biases + true_value

    # combine predictions
    predictions = np.concatenate((strat_predictions, norm_predictions))

    # iterate and adjust predictions towards the market consensus
    for i in range(iterations):
        market_consensus = np.median(predictions)
        adjustments = interaction_factor * (market_consensus - predictions)
        predictions += adjustments

    final_consensus = np.median(predictions)

    return abs(final_consensus - true_value) <= desired_accuracy


# number of simulations
num_sims = 1000
true_value = 100    # set a true value for all simulations
results = []

for i in range(num_sims):
    result = simulate_market(100, true_value)
    results.append(result)

# calculate percentage of successsul predictions
success_rate = np.mean(results)
print(f"Accuracy within desired range: {success_rate * 100:.2f}%")

# plot the results
plt.figure(figsize=(10,5))

# convert boolean results to ints
int_results = [int(success) for success in results]

plt.hist(int_results, bins=2, color='blue', alpha=0.7)
plt.title("Simulation Results Distribution")
plt.xlabel("Prediction Accuracy (within desired range)")
plt.ylabel("Frequency")
plt.xticks([0, 1], ["Outside Range", "Within Range"])
plt.show()



