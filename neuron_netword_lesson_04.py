import numpy as np

# Input
inputs = np.array([2,3])

# Weights
weights = np.array([1.0, 1.0])

#Bias
bias = 1

# Neuron calculation
neuron = np.sum(inputs * weights) + bias

output = max(0, neuron)

print(output)