import os
import shutil
import cv2
vid = cv2.VideoCapture(0)
#vid= cv2.VideoCapture('/home/manu/Downloads/deep/deeplearnset/opencvexamples/26dec2023.avi')
width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = vid.get(cv2.CAP_PROP_FPS)
print("width %d,height %d" % (width,height))
print(width)
print("fps %f" % (fps))
grabbed, frame = vid.read()
if os.path.exists("./output"):
    shutil.rmtree("./output")

os.mkdir("./output")
i=0
while grabbed:
    print(i)
    cv2.imwrite("./output/frame_%d.jpg" % (len(os.listdir("./output"))), frame)
    i=i+1
    grabbed, frame = vid.read()
vid.release()
