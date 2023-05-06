# -*- coding: utf-8 -*-
"""
Created on Fri May  5 11:20:55 2023

@author: Yash Kumar
"""

import cv2 as cv
import numpy as np

image = cv.imread('image.jpg')
#cv.imshow('image', img)

scale = 0.1
width = int(image.shape[1]*scale)
height=int(image.shape[0]*scale)
dim= (width, height)

img=cv.resize(image, dim, interpolation=cv.INTER_AREA)

b,g,r=cv.split(img)
cv.imshow('blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

cv.waitKey(0)
