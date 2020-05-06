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

image = image.astype('float64')

for i in range(3):
    division[i] = right_color[i] / wrong_color[i]
    # Checking for 'wrapping'
    np.putmask(image[:, :, i], image[:, :, i] * division[i] > 255, 255)
    # Major changes
    np.putmask(image[:, :, i], image[:, :, i] * division[i] <= 255, image[:, :, i] * division[i])

image = image.astype('uint8')

print("--- %s seconds ---" % (time.time() - start_time))

plt.imshow(image)
plt.show()
