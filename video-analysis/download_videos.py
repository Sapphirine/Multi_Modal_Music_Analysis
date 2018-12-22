from pytube import YouTube
import glob
import pandas as pd

f1 = 'data/1.txt'
f2 = 'data/2.txt'
f3 = 'data/3.txt'
f4 = 'data/4.txt'
f5 = 'data/5.txt'

f = [f1, f2, f3, f4, f5]

ids = []
count = 0
for i in f:
    with open(f1) as f:
        content = f.readlines()
        for line in content:
            #print('line', line)
            if (line[0].isdigit()):
                #print('line', line)
                ids.append(line)
                count += 1

print('count', count)
#YouTube('https://www.youtube.com/watch?v=LPY4u9Gx-xM').streams.first().download()
#yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

t = 0
s = 'https://www.youtube.com/watch?v='
for i in range(0, len(ids)):
    if (i %100 == 0):
        r = s + ids[i]
        print('r', r)
        try:
            YouTube(r).streams.first().download()
            t += 1
            print('t', t)
            if (t > 300 ):
                break
        except Exception as e:
            pass
        #yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
