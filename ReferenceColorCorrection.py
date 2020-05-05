from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
start_time = time.time()

image = np.array(Image.open('img/ReferenceColorCorrection/ice.jpg'))

''' Wrong pixel color (choose any one) '''
wrong_color = image[200][300]  # ice.jpg
# wrong_color = image[50][250]  # people.jpg

''' Correct pixel color '''
right_color = [255, 255, 255]  # ice.jpg (white color RedGreenBlue)
#  right_color = [170, 152, 169]  # people.jpg (grey)

division = [0, 0, 0]
division[0] = right_color[0] / wrong_color[0]
division[1] = right_color[1] / wrong_color[1]
division[2] = right_color[2] / wrong_color[2]

# Checking for 'wrapping'
np.putmask(image[:, :, 0], image[:, :, 0] * division[0] > 255, 255)
np.putmask(image[:, :, 1], image[:, :, 1] * division[1] > 255, 255)
np.putmask(image[:, :, 2], image[:, :, 2] * division[2] > 255, 255)

image = image.astype('float64')
np.putmask(image[:, :, 0], image[:, :, 0] * division[0] <= 255, image[:, :, 0] * division[0])
np.putmask(image[:, :, 1], image[:, :, 1] * division[1] <= 255, image[:, :, 1] * division[1])
np.putmask(image[:, :, 2], image[:, :, 2] * division[2] <= 255, image[:, :, 2] * division[2])
image = image.astype('uint8')

print("--- %s seconds ---" % (time.time() - start_time))

plt.imshow(image)
plt.show()
