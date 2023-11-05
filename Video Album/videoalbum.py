import os
import cv2

path = "Images/"
Images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    if ext in ['.gif', 'png', '.jpg', '.jpeg', 'jfif']:
        file_name = path+"/"+file
        Images.append(file_name)

imagecount = len(Images)
frame = cv2.imread(Images[0])
height, width, channels = frame.shape
size = (width, height)

out = cv2.VideoWriter('VideoAlbum.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for elem in range(0, imagecount-1):
    frame = cv2.imread(Images[elem])
    out.write(frame)
out.release()
print("Your video has been created! =)")