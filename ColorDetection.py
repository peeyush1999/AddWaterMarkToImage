import cv2
import threading
import numpy as np
import pytesseract



from threading import Thread

class WebcamVideoStream:
    def __init__(self, src=0):
        # initialize the video camera stream and read the first frame
        # from the stream
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        # initialize the variable used to indicate if the thread should
        # be stopped
        self.stopped = False
    def start(self):
        # start the thread to read frames from the video stream
            Thread(target=self.update, args=()).start()
            return self
    def update(self):
        # keep looping infinitely until the thread is stopped
        while True:
            # if the thread indicator variable is set, stop the thread
            if self.stopped:
                return
            # otherwise, read the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()
    def read(self):
        # return the frame most recently read
        return self.frame
    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True

    

vs = WebcamVideoStream(src=0).start()
frame = vs.read()
    




cnt=0

while True:
    
    f = vs.read()
    f= cv2.flip(f,1)
    cpy = f.copy()
    
    
    f = cv2.cvtColor(f, cv2.COLOR_BGR2HSV)
    f = cv2.GaussianBlur(f, (3, 3), 0)
    
    
    #========Orange
    #lb = np.array([1, 190, 200],np.uint8)
    #ub = np.array([18, 255, 255],np.uint8)
    #==========

    lb = np.array([0,150,50])
    ub = np.array([50,255,255])

    fr = cv2.inRange(f, (10, 60, 100),(30, 100, 255))
    mask = fr

    element = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
    mask = cv2.erode(mask,element, iterations=2)
    mask = cv2.dilate(mask,element,iterations=2)
    mask = cv2.erode(mask,element)

    cnts, hierarchy = cv2.findContours(fr.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(cnts) == 0:
        pass
    else:
        segmented = max(cnts, key=cv2.contourArea)
        cx = 0
        cy = 0
        for p in segmented:
            cx += p[0][0]
            cy += p[0][1]
            cv2.drawContours(cpy, [p], -1, (0, 255, 0), 2)
        cx = int(cx/len(segmented))
        cy = int(cy/len(segmented))
        
        cv2.circle(cpy, (cx, cy), 7, (255, 255, 255), -1)
        

    
    
    
    
    
    

        

        
    #oldframe = f
    
    
    
    print("K:",cnt)
    cnt+=1
    
    cv2.imshow("f", f)
    cv2.imshow("1f", fr)
    cv2.imshow("cpy", cpy)
    
    
    
    

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    



cv2.destroyAllWindows()




