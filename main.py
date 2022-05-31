import torch
import shutil
import cv2
import os
import moviepy.video.io.ImageSequenceClip

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QIcon

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

    if not os.path.exists(
            "Files"):
        os.makedirs(
            "Files")

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
    clip.write_videofile(os.path.expanduser("~/Desktop/CutMovie.mp4"))

    filelist = [f for f in os.listdir(destination_path) if f.endswith(".jpg")]
    for f in filelist:
        os.remove(os.path.join(destination_path, f))



files = "Nog geen folder geselecteerd"


def dialog():
    files = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
    label.setText(files)
    print(files)
    buttonStart.setDisabled(False)

    return files


app = QApplication(sys.argv)

win = QMainWindow()

win.setGeometry(200, 200, 1000, 500)

win.setWindowTitle("Bouwflix")
scriptDir = os.path.dirname(os.path.realpath(__file__))
win.setWindowIcon(QIcon('icon.png'))
# Choose folder button
buttonFolder = QPushButton(win)
buttonFolder.setText("Importeer map met filmpjes")
buttonFolder.setStyleSheet("background-color : rgb(31, 115, 249)")
buttonFolder.clicked.connect(dialog)
buttonFolder.move(20, 100)
buttonFolder.resize(150, 50)

# Label with path
label = QtWidgets.QLabel(win)
label.setText(files)
label.resize(1000, 20)
label.move(28, 150)

# Start button
buttonStart = QPushButton(win)
buttonStart.setDisabled(True)
buttonStart.clicked.connect(lambda: human_detection(label.text()))
buttonStart.move(20, 300)
buttonStart.setText("Start!")
buttonStart.resize(150, 50)

# Image
label2 = QtWidgets.QLabel(win)
pixmap = QPixmap('Logo.png')
label2.resize(pixmap.width(), pixmap.height())
label2.move(20, 20)
label2.setPixmap(pixmap)

# Label with output explanation
label3 = QtWidgets.QLabel(win)
label3.setText("Het eindresultaat kunt u terug vinden op het bureaublad met de naam 'CutVideo.mp4'")
label3.resize(1000, 20)
label3.move(28, 350)

win.show()

sys.exit(app.exec_())
