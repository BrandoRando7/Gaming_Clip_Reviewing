import cv2
import datetime
import numpy as np
import os
import subprocess
import math 

#your desired clips timestamp and frames
GetMyHour = int(input('Enter the hour value: '))
GetMyMin = int(input('Enter the min value: '))
GetMySec = int(input('Enter the sec value: '))
MyStartSec = ((GetMyHour * 60) * 60) + (GetMyMin *60) + GetMySec
RealStartSec = MyStartSec - 30


# create video capture object
data = cv2.VideoCapture("2022-11-27-18-38-31.mp4")
# count the number of frames
frames = data.get(cv2.CAP_PROP_FRAME_COUNT) #total frames
fps = data.get(cv2.CAP_PROP_FPS) #total frames per second
# calculate duration of the video
seconds = round(frames / fps)
print(fps)
video_time = datetime.timedelta(seconds=seconds)
#print(f"duration in seconds: {seconds}")
#print(f"video time: {video_time}")
totalFrames = seconds * fps 
#myStartFrame = 1560 * fps
myStartFrame = RealStartSec * fps


cap = cv2.VideoCapture("2022-11-27-18-38-31.mp4") 
start_frame_number = myStartFrame
cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame_number)
while(cap.isOpened()):
    ret,frame = cap.read()
  
    frame = cv2.resize(frame,(2560,1440))
    cv2.imshow("video", frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

 # cap.release()
 # cv2.destroyAllWindows()
  #https://www.youtube.com/watch?v=vvq6xRziKns
#openCVCapture.set(cv2.CAP_PROP_POS_MSEC,20000) 