import numpy as np
import matplotlib.pyplot as plt

from skimage import measure
from skimage import color
from skimage import io


# Construct some test data
img = io.imread('pattern.png')
gray = color.rgb2gray(img)

# Find contours at a constant value of 0.8
contours = measure.find_contours(gray, 0.8)

# Display the image and plot all contours found
fig, ax = plt.subplots()
ax.imshow(gray, interpolation='nearest', cmap=plt.cm.gray)


def calc_area(contour):
    xmax, xmin = contour[:, 0].max(), contour[:, 0].min()
    ymax, ymin = contour[:, 1].max(), contour[:, 1].min()
    area = (xmax - xmin) * (ymax - ymin)
    return area

areas = np.array([calc_area(contour) for contour in contours])
max_idx = np.where(areas.max())[0][0]

ax.plot(contours[max_idx][:, 1], contours[max_idx][:, 0], linewidth=2)

ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()
