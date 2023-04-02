import os
import cv2

path = "Images/"

images = []

for file in os.listdir(path):
    if images in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        file_name = path+"/"+file
    print(file_name)
    images.append(file_name)
    
print(len(images))
count = len(images)
frame = cv2.imread(images[0])
height,width,channel = frame.shape
size = (width,height)
print(size)
out = cv2.VideoWriter("FRIENDS.avi",cv2.VideoWriter_fourcc(*"DIVX"),0.8,size)
for i in range(0, count-1):
    frame = cv2.imread(images[i])
    out.write(frame)

out.release() # releasing the generated video
print("DONE")

