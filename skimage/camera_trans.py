#-*- coding: utf-8 -*-
# doc_trans.py
import math
import numpy as np
import matplotlib.pyplot as plt

from skimage import io
from skimage import data
from skimage import transform as tf

import cv2

img = io.imread('pattern.png')
margins = dict(hspace=0.01, wspace=0.01, top=1, bottom=0, left=0, right=1)

src = np.array((
    (0, 0),
    (0, 100),
    (100, 100),
    (100, 0)
))
dst = np.array((
    (174, 97),
    (147, 304),
    (520, 302),
    (455, 95)
))

tform3 = tf.ProjectiveTransform()
tform3.estimate(src, dst)
warped = tf.warp(img, tform3, output_shape=(src[:,0].max(), src[:,1].max()))

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 3))
fig.subplots_adjust(**margins)
plt.gray()
ax1.imshow(img)
ax1.plot(dst[:, 0], dst[:, 1], '.r')
ax1.axis('off')
ax2.imshow(warped)
ax2.axis('off')

"""
.. image:: PLOT2RST.current_figure
"""

plt.show()
