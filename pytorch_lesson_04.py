# import torch

# x = torch.tensor(3.0, requires_grad=True)

# y= x ** 2
# y.backward()

# print(x.grad)

import torch

# 1. Create the weight
weight = torch.tensor(0.5, requires_grad=True)

# 2. Input
x = torch.tensor(3.0)

# 3. Make prediction
prediction = x * weight

# 4. Target value
target = torch.tensor(6.0)

# 5. Calculate loss
loss = (target - prediction) ** 2

# 6. Calculate gradient
loss.backward()

# 7. Print everything
print("Weight:", weight)
print("Prediction:", prediction)
print("Loss:", loss)
print("Gradient:", weight.grad)



#=============
import torch

weight = torch.tensor(0.5, requires_grad=True)

x = torch.tensor(3.0)

prediction = x * weight

target = torch.tensor(6.0)

loss = (target - prediction) ** 2

# Calculate gradient
loss.backward()

# Update weight
learning_rate = 0.01

with torch.no_grad():
    weight -= learning_rate * weight.grad

print("Old weight: 0.5")
print("New weight:", weight)
print("Gradient:", weight.grad)
