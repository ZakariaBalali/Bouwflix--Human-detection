import string
import torch
import shutil
import cv2
import os
import moviepy.video.io.ImageSequenceClip

from PyQt5.QtCore import *

class MainBackgroundThread(QThread):

    #custom signal for progress
    update_progress = pyqtSignal(int)
    current_state = pyqtSignal(str)
    
    def __init__(self, uploadPath, destinationPath):
        QThread.__init__(self)
        self.uploadPath, self.destinationPath = uploadPath, destinationPath

    def run(self):
        self.current_state.emit("De Applicatie is gestart")
        # FRAME SPLITTER
        self.update_progress.emit(10)
        direc = self.uploadPath
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
                self.update_progress.emit(20)
                # frame
                list = os.listdir(
                    "Data")  # dir is your directory path
                currentframe = len(list)
                self.current_state.emit("Creating frames...")
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
        self.update_progress.emit(50)
        # MODEL/YOLOV5
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        model.conf = 0.25  # NMS confidence threshold
        model.classes = 0
        # Images
        self.current_state.emit("Fusing layers...")

        d = "Data"
        self.update_progress.emit(60)
        if not os.path.exists(
                "Files"):
            os.makedirs(
                "Files")

        destination_path = "Files"
        self.update_progress.emit(70)

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
        self.current_state.emit("Creating video...")
        self.update_progress.emit(80)
        fps = 30

        image_files = [os.path.join(destination_path, img)
                    for img in sorted(os.listdir(destination_path), key=len)
                    if img.endswith(".jpg")]
        clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
        #clip.write_videofile(os.path.expanduser(f"~/Desktop/{self.fileName}.mp4"))
        clip.write_videofile(self.destinationPath)
        self.update_progress.emit(90)

        filelist = [f for f in os.listdir(destination_path) if f.endswith(".jpg")]
        for f in filelist:
            os.remove(os.path.join(destination_path, f))
        self.update_progress.emit(100)
        self.current_state.emit("Finished!")