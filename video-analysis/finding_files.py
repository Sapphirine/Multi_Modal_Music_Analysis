import glob
f = []
for filename in glob.glob('/Users/mayanksaxena/Desktop/big-data/project/frames_data/*.jpg'): #assuming gif
    f.append(filename)

print('f', f)
