# Prediction Market Simulator

This repository contains a Python-based simulation for prediction markets, focusing on collective decision-making and the "wisdom of the crowd." It includes mechanisms for player interaction and market accuracy thresholds.

## Description

The project has two main components:

### `simulate_market.py`

This module contains the `simulate_market` function, which simulates the behavior of a prediction market. Players in the market make predictions about a true value based on a heavy-tailed t-distribution, reflecting the unpredictability of real-world events. Strategic participants have access to better information, reflected by lower variance in their predictions.

#### Key Parameters:

- `n`: Number of participants in the market.
- `true_value`: The actual value that participants are trying to predict.
- `desired_accuracy`: Acceptable deviation range from the true value for a prediction to be considered accurate.
- `interaction_factor`: Degree of influence the current market consensus has on individual participant predictions.
- `iterations`: Number of iterations for the market predictions to converge.

### `find_minimum_participants.py`

This script hosts the `find_minimum_participants` function, which utilizes the `simulate_market` function to determine the minimum number of participants required for the prediction market to reach a specified level of accuracy and reliability.

#### Key Parameters:

- `simulate_market_func`: The simulation function imported from `simulate_market.py`.
- `true_value`: The true value participants are trying to predict.
- `max_participants`: Upper bound for the number of participants to consider.
- `desired_accuracy`: The threshold for considering a prediction successful.
- `confidence`: The required confidence level that determines market reliability.
- `trials`: The number of trials to run for each number of participants.

## Usage

To simulate a prediction market and find the minimum number of participants needed, run the `find_minimum_participants` function with the desired parameters. The output will provide insight into the group size needed for effective prediction aggregation.
