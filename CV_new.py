import cv2 as cv
import numpy as np

img1=cv.imread('image.jpg')
img2=cv.imread('kodai-1077.png')

img1=cv.resize(img1,(500,650),interpolation=cv.INTER_LINEAR)
img2=cv.resize(img2,(500,650),interpolation=cv.INTER_LINEAR)

#img_new=img1+img2

img_new=cv.subtract(img1,img2)

cv.imshow('waterfall', img1)
cv.imshow('didi', img2)
cv.imshow('img', img_new)
cv.waitKey(0)
cv.destroyAllWindows()