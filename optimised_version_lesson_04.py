import torch

# 1. Weight
weight = torch.tensor(0.5, requires_grad=True)

# 2. Optimizer
optimizer = torch.optim.SGD([weight], lr=0.01)

# 3. Input and target
x = torch.tensor(3.0)
target = torch.tensor(6.0)

# 4. Prediction
prediction = x * weight

# 5. Lossa
loss = (target - prediction) ** 2

# 6. Calculate gradient
loss.backward()

# 7. Optimizer updates the weight
optimizer.step()

print("New weight:", weight)
print("Gradient:", weight.grad)
