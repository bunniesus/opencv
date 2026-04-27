import cv2
import random

#IMAGE MANIPULATION 
img = cv2.imread('logo.png', 0)

# print(type(img))     #<class 'numpy.ndarray'>
# print(img.shape) #(373, 360, 4) height, width ,channel

#in opencv color is like- BGR  .. blue green red pixels

# print(img[257][230])
#
# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [
#     random.randint(0,255),  # B
#     random.randint(0,255),  # G
#     random.randint(0,255),  # R
#     255                     # A (full opacity)
# ]

#copy and paste a part of an image
tag = img[200:300, 230:330]
img[100:200, 200:300]  = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()