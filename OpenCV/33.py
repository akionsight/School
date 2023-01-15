## turn image to grayscale

import cv2

img = cv2.imread('octopus.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
title = 'Gray (Grey?) Octopus'

cv2.imshow(title, gray)

cv2.waitKey(0)


