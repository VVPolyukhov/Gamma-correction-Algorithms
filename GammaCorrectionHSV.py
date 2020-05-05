import matplotlib.pyplot as plt
import cv2
import numpy as np
import time
start_time = time.time()

'''

Gamma Correction
Color model - HSV

'''

img = cv2.cvtColor(cv2.imread('img/GammaCorrection/ball.jpg'), cv2.COLOR_BGR2HSV)

Y = 1
const = 1

# Checking for 'wrapping'
np.putmask(img[:, :, 2], const * img[:, :, 2] ** Y > 255, 255)

img = img.astype('float64')
np.putmask(img[:, :, 2], const * img[:, :, 2] ** Y <= 255, const * img[:, :, 2] ** Y)
img = img.astype('uint8')

rgb = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)

print("--- %s seconds ---" % (time.time() - start_time))

plt.imshow(rgb)
plt.show()