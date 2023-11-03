import cv2
import numpy
from win32api import GetSystemMetrics
import pyautogui
import time

width=GetSystemMetrics(0)
height=GetSystemMetrics(1)
dim=(width,height)
f=cv2.VideoWriter_fourcc(*"XVID")

output=cv2.VideoWriter("Screenrecorded.mp4",f,20.0,dim)
starttime=time.time()
dur=3600
endtime=starttime+dur
print("Video Started Recording")
while True:

    image=pyautogui.screenshot()
    frame1=numpy.array(image)
    frame=cv2.cvtColor(frame1,cv2.COLOR_BGR2RGB)

    output.write(frame)
    ctime=time.time()
    if ctime>endtime:
        break

output.release()
print("Video Recorded")



