## Print the most extreme values of BGR in all pixels

import cv2

img = cv2.imread('octopus.jpg')

print(f"Maximum value: {img.max()}")
print(f"Minimum Value: {img.min()}")