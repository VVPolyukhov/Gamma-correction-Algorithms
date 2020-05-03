import matplotlib.pyplot as plt
import cv2
import time
start_time = time.time()

'''

Gamma Correction
Color model - HSV

'''

img = cv2.cvtColor(cv2.imread('img/GammaCorrection/girl.jpg'), cv2.COLOR_BGR2HSV)
shape = img.shape  # Width, height, number of image channels

Y = 1
const = 1

'''
Wrapping (?)

img[:, :, 2] = 255 \
    if (const * img[:, :, 2] ** Y > 255).all() \
    else const * img[:, :, 2] ** Y 
'''

for i in range(0, shape[0]):
    for j in range(0, shape[1]):
        value = const * img[i][j][2] ** Y
        if value > 255:
            img[i][j][2] = 255
        else:
            img[i][j][2] = value

rgb = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)

print("--- %s seconds ---" % (time.time() - start_time))

plt.imshow(rgb)
plt.show()