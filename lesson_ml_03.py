from sklearn.linear_model import LinearRegression

X = [
    [500],
    [1000],
    [1500],
    [2000],
]

y = [
    100000,
    200000,
    300000,
    400000,
]


model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[1200]])

print(prediction)