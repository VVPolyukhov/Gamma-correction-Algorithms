from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
start_time = time.time()

source_image = np.array(Image.open('img/StatisticalColorGrading/imageS.jpg'))
target_image = np.array(Image.open('img/StatisticalColorGrading/imageT.jpg'))

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

                                                ## Finally ##

division_of_disp_red = D_red_s // D_red_t
division_of_disp_green = D_green_s // D_green_t
division_of_disp_blue = D_blue_s // D_blue_t

# Checking for 'wrapping'
np.putmask(target_image[:, :, 0], E_red_s + (target_image[:, :, 0] - E_red_t) * (division_of_disp_red) > 255, 255)
np.putmask(target_image[:, :, 1], E_green_s + (target_image[:, :, 1] - E_green_t) * (division_of_disp_green) > 255, 255)
np.putmask(target_image[:, :, 2], E_blue_s + (target_image[:, :, 2] - E_blue_t) * (division_of_disp_blue) > 255, 255)

target_image = target_image.astype('float64')
np.putmask(target_image[:, :, 0],
           E_red_s + (target_image[:, :, 0] - E_red_t) * (division_of_disp_red) <= 255,
           E_red_s + (target_image[:, :, 0] - E_red_t) * (division_of_disp_red))
np.putmask(target_image[:, :, 1],
           E_green_s + (target_image[:, :, 1] - E_green_t) * (division_of_disp_green) <= 255,
           E_green_s + (target_image[:, :, 1] - E_green_t) * (division_of_disp_green))
np.putmask(target_image[:, :, 2],
           E_blue_s + (target_image[:, :, 2] - E_blue_t) * (division_of_disp_blue) <= 255,
           E_blue_s + (target_image[:, :, 2] - E_blue_t) * (division_of_disp_blue))
target_image = target_image.astype('uint8')

print("--- %s seconds ---" % (time.time() - start_time))

plt.imshow(target_image)
plt.show()
