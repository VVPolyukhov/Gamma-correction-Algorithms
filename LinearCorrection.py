from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
start_time = time.time()

image = np.array(Image.open('img/LinearCorrection/ball.jpg'))

max_red   = np.max([j[0] for i in image for j in i])
min_red   = np.min([j[0] for i in image for j in i])
max_green = np.max([j[1] for i in image for j in i])
min_green = np.min([j[1] for i in image for j in i])
max_blue  = np.max([j[2] for i in image for j in i])
min_blue  = np.min([j[2] for i in image for j in i])

# Preliminary values (second multiplier)
preliminary_red   = (255 / (max_red - min_red))
preliminary_green = (255 / (max_green - min_green))
preliminary_blue  = (255 / (max_blue - min_blue))

image[:, :, 0] = (image[:, :, 0] - min_red) * preliminary_red
image[:, :, 1] = (image[:, :, 1] - min_green) * preliminary_green
image[:, :, 2] = (image[:, :, 2] - min_blue) * preliminary_blue

print("--- %s seconds ---" % (time.time() - start_time))

plt.imshow(image)
plt.show()