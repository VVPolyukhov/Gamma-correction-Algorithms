from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
start_time = time.time()

source_image = np.array(Image.open('img/StatisticalColorGrading/ImageS.jpg'))
target_image = np.array(Image.open('img/StatisticalColorGrading/ImageT.jpg'))

shape_s = source_image.shape
shape_t = target_image.shape

# number of image pixels
n_s = shape_s[0] * shape_s[1]
n_t = shape_t[0] * shape_t[1]

                                        ## First image (color source) ##

# Expectation #
E_red_s = np.sum([j[0] for i in source_image for j in i]) // n_s
E_green_s = np.sum([j[1] for i in source_image for j in i]) // n_s
E_blue_s = np.sum([j[2] for i in source_image for j in i]) // n_s

# Dispersion #
D_red_s = int((np.sum([(j[0] - E_red_s) ** 2 for i in source_image for j in i]) // n_s) ** .5)
D_green_s = int((np.sum([(j[1] - E_green_s) ** 2 for i in source_image for j in i]) // n_s) ** .5)
D_blue_s = int((np.sum([(j[2] - E_blue_s) ** 2 for i in source_image for j in i]) // n_s) ** .5)

                                                ## Second image ##

# Expectation #
E_red_t = np.sum([j[0] for i in target_image for j in i]) // n_t
E_green_t = np.sum([j[1] for i in target_image for j in i]) // n_t
E_blue_t = np.sum([j[2] for i in target_image for j in i]) // n_t

# Dispersion #
D_red_t = int((np.sum([(j[0] - E_red_t) ** 2 for i in target_image for j in i]) // n_t) ** .5)
D_green_t = int((np.sum([(j[1] - E_green_t) ** 2 for i in target_image for j in i]) // n_t) ** .5)
D_blue_t = int((np.sum([(j[2] - E_blue_t) ** 2 for i in target_image for j in i]) // n_t) ** .5)

mas = []

for i in range(0, shape_t[0]):
    for j in range(0, shape_t[1]):
        R = E_red_s + (target_image[i][j][0] - E_red_t) * (D_red_s // D_red_t)
        # Checking for 'wrapping'
        if R >= 0 and R <= 255:
            target_image[i][j][0] = R
        elif R < 0:
            target_image[i][j][0] = 0
        else:
            target_image[i][j][0] = 255

        G = E_green_s + (target_image[i][j][1] - E_green_t) * (D_green_s // D_green_t)
        if G >= 0 and G <= 255:
            target_image[i][j][1] = G
        elif G < 0:
            target_image[i][j][1] = 0
        else:
            target_image[i][j][1] = 255

        B = E_blue_s + (target_image[i][j][2] - E_blue_t) * (D_blue_s // D_blue_t)
        if B >= 0 and B <= 255:
            target_image[i][j][2] = B
        elif B < 0:
            target_image[i][j][2] = 0
        else:
            target_image[i][j][2] = 255

print("--- %s seconds ---" % (time.time() - start_time))

plt.imshow(target_image)
plt.show()
