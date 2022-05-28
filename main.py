import torch
import shutil
import cv2
import os
import moviepy.video.io.ImageSequenceClip

# Read the video from specified path
cam = cv2.VideoCapture(
    "C:\\Users\\zakar\\Desktop\\School\\InHolland\\Jaar 3\\Periode 4\\Project Bouwflix\\mecanoo_mec_bl_210719-avi_2022-05-07_1920\\MEC_BL2_220406.avi")
try:

    # creating a folder named data
    if not os.path.exists("C:\\Users\\zakar\\Desktop\\School\\InHolland\\Jaar 3\\Periode 4\\Project Bouwflix\\Dataset"):
        os.makedirs("C:\\Users\\zakar\\Desktop\\School\\InHolland\\Jaar 3\\Periode 4\\Project Bouwflix\\Dataset")

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
list = os.listdir(
    "C:\\Users\\zakar\\Desktop\\School\\InHolland\\Jaar 3\\Periode 4\\Project Bouwflix\\Dataset")  # dir is your directory path
currentframe = len(list)
while (True):

    # reading from frame
    ret, frame = cam.read()

    if ret:
        # if video is still left continue creating images
        name = 'C:\\Users\\zakar\\Desktop\\School\\InHolland\\Jaar 3\\Periode 4\\Project Bouwflix\\Dataset\\frame' + str(
            currentframe) + '.jpg'
        print('Creating...' + name)

        # writing the extracted images
        cv2.imwrite(name, frame)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model.conf = 0.25  # NMS confidence threshold
model.classes = 0
# Images

d = "C:\\Users\\zakar\\Desktop\\School\\InHolland\\Jaar 3\\Periode 4\\Project Bouwflix\\Dataset\\"
destination_path = "Files"

for path in os.listdir(d):
    full_path = os.path.join(d, path)
    if os.path.isfile(full_path):
        imgs = full_path
        results = model(imgs)
        # If picture has a person detection, move to files folder
        if 0 in results.pandas().xyxy[0]['class']:
            results.print()
            new_location = shutil.move(full_path, destination_path)
        else:
            os.remove(full_path)

fps = 30

image_files = [os.path.join(destination_path, img)
               for img in sorted(os.listdir(destination_path), key=len)
               if img.endswith(".jpg")]
clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile('CutVideo.mp4')
