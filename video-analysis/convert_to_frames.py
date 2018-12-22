import cv2
import os
from glob import glob

files = []
start_dir = os.getcwd()
pattern   = "*.mp4"

for dir,_,_ in os.walk(start_dir):
    files.extend(glob(os.path.join(dir,pattern)))

count = 0
counter = 1
vid_no = 1

for file in files:
    vid_no += 1
    vidcap = cv2.VideoCapture(file)
    success,image = vidcap.read()
    count = 0
    counter += 1
    while success:
        success,image = vidcap.read()
        print('read a new frame:',success)
        if count%50 == 0 :
             cv2.imwrite('frames_data/' + str(vid_no) + '_frame%d.jpg'%count,image)
        count+=1
