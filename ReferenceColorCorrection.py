from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
start_time = time.time()

image = np.array(Image.open('img/ReferenceColorCorrection/ice.jpg'))
shape = image.shape

''' Wrong pixel color (choose any one) '''
wrong_color = image[200][300]  # ice.jpg
#  wrong_color = image[350][600]  # nature.jpg
# wrong_color = image[50][250]  # people.jpg
''' Correct pixel color '''
right_color = [255, 255, 255]  # ice.jpg (white color RedGreenBlue)
#  right_color = [60, 170, 60]  # nature.jpg (green)
#  right_color = [170, 152, 169]  # people.jpg (grey)

division = [0, 0, 0]
division[0] = right_color[0] / wrong_color[0]
division[1] = right_color[1] / wrong_color[1]
division[2] = right_color[2] / wrong_color[2]

for i in range(0, shape[0]):
    for j in range(0, shape[1]):
        R = image[i][j][0] * (division[0])
        # Checking for 'wrapping'
        if R >= 0 and R <= 255:
            image[i][j][0] = R
        else:
            image[i][j][0] = 255

        G = image[i][j][1] * (division[1])
        if G >= 0 and G <= 255:
            image[i][j][1] = G
        else:
            image[i][j][1] = 255

        B = image[i][j][2] * (division[2])
        if B >= 0 and B <= 255:
            image[i][j][2] = B
        else:
            image[i][j][2] = 255

print("--- %s seconds ---" % (time.time() - start_time))

plt.imshow(image)
plt.show()
