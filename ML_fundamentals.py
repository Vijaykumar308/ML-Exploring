import numpy as np

image = np.zeros([5,5])

for i in range(1, 4):
    for j in range(1, 4):
        image[i][j] = 255


print(image)