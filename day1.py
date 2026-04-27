import cv2

img = cv2.imread('logo.png', 1)
img = cv2.resize (img, (300, 300)) # or (0,0) , fx = 0.5, fy=0.5 make half the size
img = cv2.rotate (img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite('char2.png', img) # creates new img generated above

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()