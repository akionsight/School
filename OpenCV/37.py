## Save a greyscale image

import cv2

img = cv2.imread('octopus.jpg')
saved_image_name = 'Saved_Grey_Octopus.jpg'

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite(saved_image_name, grey)
