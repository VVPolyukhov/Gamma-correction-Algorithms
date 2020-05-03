import numpy as np
import math
import matplotlib.pyplot as plt
import cv2
import time
start_time = time.time()

# The Gaussian filter will be a matrix n*n,
# where n is an odd number...

# Composing The Gaussian core
def GaussianFilterCreation (sigma, kernelSize):
    radius = kernelSize // 2
    gaussKernel = np.zeros((kernelSize, kernelSize))
    sum = 0.0
    denominator = 2.0 * sigma * sigma
    for m in range(-radius, radius + 1):
        for n in range(-radius, radius + 1):
            gaussKernel[m + radius][n + radius] = \
                (1 / (denominator * math.pi)) * \
                math.exp(-(m * m + n * n) / denominator)
            sum += gaussKernel[m + radius][n + radius]
    gaussKernel[:, :] /= sum
    return gaussKernel

YCC = cv2.cvtColor(cv2.imread('img/SSR/ball.jpg'), cv2.COLOR_BGR2YCrCb)

# Creating a Gaussian core
kernel = GaussianFilterCreation(0.5, 3)  # (0.5, 5) - light
radius = len(kernel[0]) // 2
matrix = np.copy(YCC[:, :, 0])
# Creating a "null shell" for applying the filter
zerosColumn = np.array(np.zeros(matrix.shape[0]))
for i in range(radius):
    matrix = np.column_stack((zerosColumn, matrix, zerosColumn))
zerosRow = np.array(np.zeros([matrix.shape[1]]))
for i in range(radius):
    matrix = np.vstack((zerosRow, matrix, zerosRow))
shape = matrix.shape

for i in range(radius, shape[0] - radius):
    for j in range(radius, shape[1] - radius):

        # The application of the Gaussian filter
        gaussian = np.sum(matrix[i - radius:i + radius + 1, j - radius:j + radius + 1] * kernel)

        if YCC[i - radius][j - radius][0] != 0:
            result = math.log10(YCC[i - radius][j - radius][0]) - math.log10(gaussian)
        else:
            result = 0 - math.log10(gaussian)
        # Pixels must be in the range [-1, 1]
        if result < -1:
            result = -1
        elif result > 1:
            result = 1
        # Normalization of values...
        result = result * 255 + 127.5
        # Checking for 'wrapping'
        if result >= 0 and result <= 255:
            matrix[i][j] = result
        elif result < 0:
            matrix[i][j] = 0
        else:
            matrix[i][j] = 255

YCC[:, :, 0] = matrix[radius:shape[0] - radius, radius:shape[1] - radius]

rgb = cv2.cvtColor(YCC, cv2.COLOR_YCrCb2RGB)

print("--- %s seconds ---" % (time.time() - start_time))

plt.imshow(rgb)
plt.show()