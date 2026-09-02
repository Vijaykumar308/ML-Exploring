import random
import pandas as pd

data = []

# Generate 10,000 examples
for _ in range(10000):

    # Randomly choose square or rectangle
    shape = random.choice(["square", "rectangle"])

    if shape == "square":
        side = random.randint(1, 100)
        length = side
        width = side

    else:
        length = random.randint(1, 100)
        width = random.randint(1, 100)

        # Make sure it is actually a rectangle, not a square
        while length == width:
            width = random.randint(1, 100)

    data.append([length, width, shape])

# Create DataFrame
df = pd.DataFrame(
    data,
    columns=["length", "width", "shape"]
)

# Save dataset
df.to_csv("shape_dataset.csv", index=False)

#print(df.head(10))
#print("\nDataset size:", len(df))


# ====== ML Task ================================

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X = df[["length", "width"]]
y = df["shape"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,  random_state=42)
model = DecisionTreeClassifier();

prediction = model.fit(X_train, y_train)

print(model.predict([[50, 80]]))

# from sklearn.metrics import accuracy_score

# accuracy = accuracy_score(y_test, predictions)

# print("Accuracy:", accuracy * 100)
