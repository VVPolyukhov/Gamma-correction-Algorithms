import matplotlib.pyplot as plt
import numpy as np
import cv2
import time
start_time = time.time()

'''

Gamma Correction
Color model - YCrCb

'''

img = cv2.cvtColor(cv2.imread('img/GammaCorrection/ball.jpg'), cv2.COLOR_BGR2YCrCb)

Y = 1
const = 1

# Checking for 'wrapping'
np.putmask(img[:, :, 0], const * img[:, :, 0] ** Y > 255, 255)

<<<<<<< HEAD
img = img.astype('float64')
np.putmask(img[:, :, 0], const * img[:, :, 0] ** Y <= 255, const * img[:, :, 0] ** Y)
img = img.astype('uint8')
=======
img[:, :, 0] = 255 \
    if (const * img[:, :, 0] ** Y > 255).all() \
    else const * img[:, :, 0] ** Y 
'''
>>>>>>> 7b888bbc1312a4374a158b9456845c80495b3ee8


rgb = cv2.cvtColor(img, cv2.COLOR_YCrCb2RGB)

print("--- %s seconds ---" % (time.time() - start_time))

plt.imshow(rgb)
plt.show()
