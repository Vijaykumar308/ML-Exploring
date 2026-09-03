import torch

# Simple single-layer neural network example using PyTorch.
# This creates a linear model with 1 input and 1 output, then prints its parameters.
model = torch.nn.Linear(1, 1)

print(model)

print(model.weight)
print(model.bias)

