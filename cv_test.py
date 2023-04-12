import cv2 as cv
import numpy as np

img=cv.imread('image.jpg')
img_1=cv.resize(img,(500,650),interpolation=cv.INTER_LINEAR)

#cv.imshow('image', img_1)
#cv.waitKey(0)
#cv.destroyAllWindows()


#img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#print(img_1.shape)
#for i in range(img_1.shape[0]):
    #for j in range(img_1.shape[1]):
        #img_1[i,j]=(sum(img_1[i,j]))/3

for k in range(3):
    for i in range(img_1.shape[0]):
        for j in range(img_1.shape[1]):
            if k==3:
                img_1[i,j,k]=0;
            else:
                if img_1[i,j,k]<0:
                    img_1[i,j,k]=0


img_2=cv.copyMakeBorder(img,15,15,15,15,cv.BORDER_WRAP)

#img_rect=cv.circle(img_1,(350,350), 240,(0,255,0),(15))

pts=np.array([[100,100],[200,200],[200,300],[100,400],[0,300],[0,200]],np.int32).reshape(-1,1,2)
img_poly=cv.polylines(img_1,)

cv.imshow('image', img_rect)
cv.waitKey(0)
cv.destroyAllWindows()
