import cv2
  
  
# define a video capture object
vid = cv2.VideoCapture(0)
while(True):
    ret, frame = vid.read()
    scale_percent = 150# percent of original size
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
  
    # resize image
    frame_resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow('frame', frame_resized)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
vid.release()
cv2.destroyAllWindows()