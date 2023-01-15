## Load image and give title of image

import cv2

img = cv2.imread('octopus.jpg')
window_title = 'Octopus?'

cv2.imshow(window_title, img)

cv2.waitKey(0)



