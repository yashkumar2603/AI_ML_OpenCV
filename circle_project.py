import cv2
import numpy as np

img_height=500
img_width=500
img=np.zeros((img_height, img_width, 3), np.uint8)

cv2.circle(img, (250,250), 150, (255,255,255), 15)

def erase()

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows