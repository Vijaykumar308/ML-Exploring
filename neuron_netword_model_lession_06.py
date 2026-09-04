import torch

X = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y = torch.tensor([[2.0], [4.0], [6.0], [8.0]])


model = torch.nn.Linear(1, 1)

# print(model)
# print(X)
# print(y)

loss_fn = torch.nn.MSELoss()

# print(loss_fn)

prediction = model(X)
loss = loss_fn(prediction, y)

# print("Prediction:", prediction)
# print("Loss:", loss)

optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

loss.backward()
optimizer.step()

# print("Updated weight:", model.weight)
# print("Updated bias:", model.bias)

for epoch in range(1000):
    prediction = model(X)
    loss = loss_fn(prediction, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print("Final weight:", model.weight)
print("Final bias:", model.bias)
print("Final loss:", loss)