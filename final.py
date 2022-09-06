import os
import subprocess
import glob
from pathlib import Path
import cv2
import datetime
from operator import contains
from os import times
from sqlite3 import Timestamp
from tkinter.filedialog import Open
#from pathlib import Path, PureWindowsPath

# Getting your file paths
videoPath = input('What is video Path: ') # Getting Video file path
videoFileName = input('What is your video name: ') # Getting video file name
timeStampPath = input('What is your TimeStamp Path: ') # Getting timestamp path from user
videoFull = videoPath + "\\" + videoFileName + ".mp4" # Creating full video path and file name
timeStamp = timeStampPath + "\\" + "Timestamp_" + videoFileName + ".txt" #Creating full timestamp path and file name
timeStampFileOnly = "Timestamp_" + videoFileName + ".txt"
# Prints for testing user input stuff
print('Video File Path = ' + videoPath)
print('Video File Name = ' + videoFileName)
print('TimeStamp File Path = ' + timeStampPath)
print("your video Full (path + filename + .mp4) = " + videoFull)
print("your timestamp full (path + \\ + Timestamp_ + videoFileName + .txt" + timeStamp)
print("your timestamp file only..." + timeStampFileOnly)





#we need to get the number of lines in the text file...
with open(timeStampPath + "\\" + timeStampFileOnly) as f: #open up your text file to read the desired timestamps
    count = sum(1 for _ in f)
print(count) #this will print out your total number of lines in the text file

file = open(timeStampPath + "\\" + timeStampFileOnly)
read = file.readlines()

for i in read: 
    if "Nice Clip" in i:
        foundNiceClip = i
        foundNiceClip1 = foundNiceClip[14]
        foundNiceClip2 = foundNiceClip[15]
        foundNiceClip3 = foundNiceClip[17]
        foundNiceClip4 = foundNiceClip[18]
        foundNiceClip5 = foundNiceClip[20]
        foundNiceClip6 = foundNiceClip[21]
        firstOctet = foundNiceClip1 + foundNiceClip2
        secondOctet = foundNiceClip3 + foundNiceClip4
        thirdOctet = foundNiceClip5 + foundNiceClip6    
        print( firstOctet + ":" + secondOctet + ":" + thirdOctet )

#your desired clips timestamp and frames
GetMyHour = int(input('Enter the hour value: '))
GetMyMin = int(input('Enter the min value: '))
GetMySec = int(input('Enter the sec value: '))
MyStartSec = ((GetMyHour * 60) * 60) + (GetMyMin *60) + GetMySec
RealStartSec = MyStartSec - 30


# create video capture object
print("the path I'm opening for video is... " + videoFull)
#data = cv2.VideoCapture(videoPath + "/" + videoFileName)
data = cv2.VideoCapture(videoFull)
# count the number of frames
frames = data.get(cv2.CAP_PROP_FRAME_COUNT) #total frames
fps = data.get(cv2.CAP_PROP_FPS) #total frames per second
# calculate duration of the video
print(frames)
print(fps)

seconds = round(frames / 60) #/fps
#print(fps)
video_time = datetime.timedelta(seconds=seconds)
#print(f"duration in seconds: {seconds}")
#print(f"video time: {video_time}")
totalFrames = seconds * fps 
#myStartFrame = 1560 * fps
myStartFrame = RealStartSec * fps


cap = cv2.VideoCapture(videoFull)
#cap = cv2.VideoCapture("2022-08-28-15-52-24.mp4") 
start_frame_number = myStartFrame
cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame_number)
while(cap.isOpened()):
    ret,frame = cap.read()
  
    frame = cv2.resize(frame,(2560,1440))
    cv2.imshow("video", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


     
        