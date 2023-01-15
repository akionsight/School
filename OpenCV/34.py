## Find dimensions of image

import cv2

img = cv2.imread('octopus.jpg')

height, width, color_channels = img.shape

print(f"The dimensions of the image are ({width},{height}) \nThe image utilises {color_channels} colour channels")

