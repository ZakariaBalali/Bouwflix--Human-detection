import torch
import shutil
import cv2
import os
import moviepy.video.io.ImageSequenceClip
from IPython.external.qt_for_kernel import QtGui

from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog

from PyQt5 import QtCore

import sys



def human_detection(filepath):
    # FRAME SPLITTER
    direc = filepath
    for path in os.listdir(direc):
        full_path = os.path.join(direc, path)
        if os.path.isfile(full_path):
            # Read the video from specified path
            cam = cv2.VideoCapture(
                full_path)
            try:

                # creating a folder named data
                if not os.path.exists(
                        "Data"):
                    os.makedirs(
                        "Data")

            # if not created then raise error
            except OSError:
                print('Error: Creating directory of data')

            # frame
            list = os.listdir(
                "Data")  # dir is your directory path
            currentframe = len(list)
            while (True):

                # reading from frame
                ret, frame = cam.read()

                if ret:
                    # if video is still left continue creating images
                    name = 'Data\\frame' + str(
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

    # MODEL/YOLOV5
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    model.conf = 0.25  # NMS confidence threshold
    model.classes = 0
    # Images

    d = "Data"
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

    # MOVIEPY

    fps = 30

    image_files = [os.path.join(destination_path, img)
                   for img in sorted(os.listdir(destination_path), key=len)
                   if img.endswith(".jpg")]
    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
    clip.write_videofile('CutVideo.mp4')

    filelist = [f for f in os.listdir(destination_path) if f.endswith(".jpg")]
    for f in filelist:
        os.remove(os.path.join(destination_path, f))

files = "none selected"


def dialog():
    files = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
    label.setText(files)
    print(files)
    return files


def checkPath():
    print(label.text())


app = QApplication(sys.argv)

win = QMainWindow()

win.setGeometry(1000, 1000, 1000, 1000)

win.setWindowTitle("Bouwflix")

button = QPushButton(win)

button.setText("Import filmpjes")
label = QtWidgets.QLabel(win)

label.setText(files)
label.resize(1000, 20)
button.clicked.connect(dialog)

button.move(50, 50)
button2 = QPushButton(win)

button2.clicked.connect(checkPath)

button2.move(100, 100)
button2.setText("check file path")

button3 = QPushButton(win)

button3.clicked.connect(lambda: human_detection(label.text()))

button3.move(200, 200)
button3.setText("Start human detection")
win.show()

sys.exit(app.exec_())
