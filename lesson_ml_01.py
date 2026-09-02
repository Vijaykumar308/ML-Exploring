# Clasifications in Supervised Learning  

from sklearn.tree import DecisionTreeClassifier
X = [
    [10, 10, 1],
    [20, 10, 0],
    [16, 16, 1],
    [30, 10, 0],
    [8, 8, 1],
    [25, 10, 0],
    [10, 11, 0],
]

y = [
    "square",
    "rectangle",
    "square",
    "rectangle",
    "square",
    "rectangle",
    "rectangle",
]

model = DecisionTreeClassifier()

model.fit(X, y)

prediction = model.predict([[22, 22, 0]])

print(prediction)
print(model.tree_.threshold)

# prediction = model.predict([[12, 12]])
# print(prediction)

# prediction = model.predict([[50, 50]])
# print(prediction)

# print(model.predict([[17, 17]]))
# print(model.predict([[18, 18]]))