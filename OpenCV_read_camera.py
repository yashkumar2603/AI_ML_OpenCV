import cv2 as cv

def rescale(frame, scale):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dim=(width,height)
    return cv.resize(frame, dim, interpolation = cv.INTER_AREA)


capture=cv.VideoCapture(0)
while(True):
    isTrue, frame=capture.read()
    new_frame = rescale(frame, 1)
    cv.circle(new_frame, (300, 300), 150, (255, 255, 0), 15)
    cv.putText(new_frame, 'HELLO', (250,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 0, 255), 4)
    cv.imshow('frame', new_frame)
    if cv.waitKey(20) & 0xFF==ord('q'):
        break

capture.release()
cv.destroyAllWindows()
