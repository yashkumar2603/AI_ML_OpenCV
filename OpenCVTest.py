# import the cv2 library
import cv2
 
# The function cv2.imread() is used to read an image.
img = cv2.imread('BAN_0964.jpg',1)
scale_percent = 5 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
# The function cv2.imshow() is used to display an image in a window.
cv2.imshow('color image',resized)
 
# waitKey() waits for a key press to close the window and 0 specifies indefinite loop
cv2.waitKey(0)
 
# cv2.destroyAllWindows() simply destroys all the windows we created.
cv2.destroyAllWindows()
 
