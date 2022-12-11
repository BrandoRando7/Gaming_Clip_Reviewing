import cv2
import datetime
import numpy as np
import os
import subprocess
import math 
#Get the video Location and name from the user
vidFilePath = input('What is the path of the video: ')
vidFileName = input('What is the name of the video: ')
path_and_name = vidFilePath + '\\' + vidFileName

#Get the time stamps and frames from the user
GetMyHour = int(input('Enter the hour value: '))
GetMyMin = int(input('Enter the min value: '))
GetMySec = int(input('Enter the sec value: '))
MyStartSec = ((GetMyHour * 60) * 60) + (GetMyMin * 60) + GetMySec
RealStartSec = MyStartSec - 10

#just testing variables for now
print('your video file path: ' + vidFilePath)
print('your video File name: ' + vidFileName)
print('your hour: ')
print(GetMyHour)
print('your min: ')
print(GetMyMin)
print('your sec: ')
print(GetMySec)
print('your StartSEC: ')
print(MyStartSec)
print('your REAL STARTING SEC: ')
print(RealStartSec)
print('your path and name: ' + path_and_name)

# create a video capture object
data = cv2.VideoCapture(path_and_name)
#count the number of frames
frames = data.get(cv2.CAP_PROP_FRAME_COUNT) #total frames
fps = data.get(cv2.CAP_PROP_FPS) #total frames per second
# calculate duration of the video
seconds = round(frames / fps)
print(fps)
video_time = datetime.timedelta(seconds = seconds)
print(f"duration in seconds: {seconds}")
print(f"video time: {video_time}")
totalFrames = seconds * fps
myStartFrame = RealStartSec * fps


cap = cv2.VideoCapture(path_and_name)
strat_frame_number = myStartFrame
cap.set(cv2.CAP_PROP_POS_FRAMES, strat_frame_number)
while(cap.isOpened()):
    ret,frame = cap.read()

    frame = cv2.resize(frame,(1920,1080))
    cv2.imshow("video", frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break




#input('Press ENTER to exit')