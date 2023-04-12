import cv2
import numpy as np

img_height=500
img_width=500
img=np.zeros((img_height, img_width, 3), np.uint8)

cv2.rectangle(img, (200,200), (300,300), (0,0,255), -1)

height=100
width=100
color=(0,0,255)
point=[250,250]
step=20
flag=0
black=(0,0,0)

cv2.rectangle(img, (point[0]-int(width/2),point[1]-int(height/2)), (point[0]+int(width/2),point[1]+int(height/2)), (0,0,255), -1)

def erase(point):
    cv2.rectangle(img, (point[0]-int(width/2), point[1]-int(height/2)), (point[0]+int(width/2), point[1]+int(height/2)), black, -1)

while True:
    if flag==0:
        if(point[0]+int(height/2)+step>img_height):
            flag=1
        else:
            erase(point)
            point[0]+=step
    if flag==1:
        if(point[0]-int(height/2)-step<0):
            flag=0
        else:
            erase(point)
            point[0]-=step
    cv2.rectangle(img, (point[0] - int(width / 2), point[1] - int(height / 2)),
                  (point[0] + int(width / 2), point[1] + int(height / 2)), (0, 0, 255), -1)
    cv2.imshow("img", img)
    cv2.waitKey(1)

#cv2.imshow("img", img)
#cv2.waitKey(0)
cv2.destroyAllWindows