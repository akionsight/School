import cv2

img = cv2.imread('octopus.jpg')

cropped_image = img[200:600, 249:434]

title = "Cropped Octopus"

cv2.imshow(title, cropped_image)
cv2.waitKey(0)