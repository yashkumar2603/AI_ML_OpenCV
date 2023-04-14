import cv2 as cv

def rescale(frame, scale):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dim=(width,height)
    return cv.resize(frame, dim, interpolation = cv.INTER_AREA)


capture=cv.VideoCapture(0)
while(True):
    isTrue, frame=capture.read()
    new_frame = rescale(frame, 2)

    #gray = cv.cvtColor(new_frame, cv.COLOR_BGR2GRAY)

    #cv.circle(gray, (300, 300), 150, (255, 255, 0), 15)

    #cv.putText(gray, 'HELLO', (250,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 0, 255), 4)

    blur=cv.GaussianBlur(new_frame, (5,5), cv.BORDER_DEFAULT)
    canny=cv.Canny(blur, 125, 175)

    cv.imshow('frame', canny)
    if cv.waitKey(20) & 0xFF==ord('q'):
        break

capture.release()
cv.destroyAllWindows()
