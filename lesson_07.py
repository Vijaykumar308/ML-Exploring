import numpy as np
import matplotlib.pyplot as plt

image = np.zeros((10, 10))
image[2:8, 2:8] = 255

plt.imshow(image, cmap="viridis")
plt.show() 
