#======== Print Rectangle ===============
# import numpy as np
# import matplotlib.pyplot as plt

# image = np.zeros((10, 10))
# # image[2:8, 2:8] = 255

# # image[2:8, 2:6] = 255
# image[2:6, 2:8] = 255

# plt.imshow(image, cmap="viridis")
# plt.show() 


#======== Print Circle =================

import numpy as np
import matplotlib.pyplot as plt

image = np.zeros((100, 100))

y, x = np.ogrid[:100, :100]

center_x = 50
center_y = 50
radius = 30

circle = (x - center_x)**2 + (y - center_y)**2 <= radius**2

image[circle] = 255

plt.imshow(image, cmap="viridis")
plt.show()