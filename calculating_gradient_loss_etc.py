x = 3
target = 6

weight = 0.5
learning_rate = 0.01

for step in range(30):

    # 1. Make prediction
    prediction = x * weight

    # 2. Calculate loss
    loss = (target - prediction) ** 2

    # 3. Calculate gradient
    gradient = 2 * (prediction - target) * x

    # 4. Update weight
    weight = weight - learning_rate * gradient

    print(
        "Step:", step,
        "Weight:", weight,
        "Prediction:", prediction,
        "Loss:", loss
    )
