import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
import os
import PyQt5
from UI import *
import math
from object_detector import *
import numpy as np
#import measure_object_size
import cv2
from PIL import Image as im

#YÜKLENEN FOTOĞRAFLAR REAL IMAGE OLANLAR JPG OLMASI LAZIM TEKNİK ÇİZİMLER FARK ETMİYOR ŞİMDİLİK.


#os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = user_interface()
        self.ui.setupUi(self)
        self.path = r'C:\Users\musta\Desktop\Image_Processing_Project\Objects_File'
        self.first_folders = os.listdir(self.path)
        os.chdir(self.path)
        for i in self.first_folders:
            if os.path.isdir(i):
                print(i)
                self.ui.listwidget.addItem(i)

        self.ui.selectFileButton.clicked.connect(self.showSelectedItem)
        self.ui.refreshFileButton.clicked.connect(self.refreshFolders)
        self.ui.TopViewButton.clicked.connect(self.showTopView)
        self.ui.FrontViewButton.clicked.connect(self.showFrontView)
        self.ui.RightViewButton.clicked.connect(self.showRightView)
        self.ui.measureButton.clicked.connect(self.measureLength)
        self.ui.measureAutoButton.clicked.connect(self.measureAuto)

        self.ui.imageBox.mousePressEvent = self.getPos
        # 2 tıklamadaki x ve y noktalarını x1,y1 ve x2,y2 olarak değişkenlerde tut!
        self.clickcount = 0

    def measureAuto(self):
        try:
            measured_img = self.contour_det()
            data = im.fromarray(measured_img)
            data.save('measured_image.png')
            self.ui.imageBox.setPixmap(QPixmap("measured_image.png"))
        except Exception as ex:
            print(ex)
    def measureLength(self):
        print("!Measuring Distance!")
        try:
            total_W = 2 * (math.tan(float(self.ui.camAOV_W.text()) / 2) * float(self.ui.photo_Height.text()))
            ppm_W = total_W / float(self.ui.Megapixel_W.text())
            distance_W = ppm_W * abs((self.x2 - self.x1))

            total_H = 2 * (math.tan(float(self.ui.camAOV_H.text()) / 2) * float(self.ui.photo_Height.text()))
            ppm_H = total_H / float(self.ui.Megapixel_H.text())
            distance_H = ppm_H * abs((self.y2 - self.y1))

            print("Width distance: ", distance_W)
            print("Height distance: ", distance_H)

            self.distance = math.sqrt(distance_W**2 + distance_H**2)
            print("==Measuring Done==")

            print("Full distance: ", self.distance)
            self.showMeasurement()
        except Exception as ex:
            print(ex)


    def showMeasurement(self):
        if self.clickcount % 2 == 0 and self.clickcount != 0:
            self.ui.measure.setText(str(self.distance))

        self.clickcount = 0




    # Foto üzerinde tıklanan noktalar.
    def getPos(self, event):
        if self.clickcount % 2 == 0:
            self.x1 = event.pos().x()
            self.y1 = event.pos().y()
            print("x1: ", self.x1)
            print("y1: ", self.y1)


        elif self.clickcount % 2 == 1:
            self.x2 = event.pos().x()
            self.y2 = event.pos().y()
            print("x2: ", self.x2)
            print("y2: ", self.y2)

        self.clickcount += 1

    def showSelectedItem(self):
        content = self.ui.listwidget.currentText()
        self.selected_path = os.path.join(self.path, content)
        print(self.selected_path)

    def showTopView(self):
        try:
            self.ui.imageBox.setPixmap(QPixmap(self.selected_path + "/Top"))
            self.ui.CADBox.setPixmap(QPixmap(self.selected_path + "/Top_Cad"))
            self.photopath = self.selected_path + "\\Top.JPG"
            self.clickcount = 0
        except Exception as ex:
            self.clickcount = 0
            print(ex)

    def showFrontView(self):
        try:
            self.ui.imageBox.setPixmap(QPixmap(self.selected_path + "/Front"))
            self.ui.CADBox.setPixmap(QPixmap(self.selected_path + "/Front_Cad"))
            self.photopath = self.selected_path + "\\Front.JPG"
            self.clickcount = 0
        except Exception as ex:
            self.clickcount = 0
            print(ex)

    def showRightView(self):
        try:
            self.ui.imageBox.setPixmap(QPixmap(self.selected_path + "/Right"))
            self.ui.CADBox.setPixmap(QPixmap(self.selected_path + "/Right_Cad"))
            self.photopath = self.selected_path + "\\Right.JPG"
            self.clickcount = 0
        except Exception as ex:
            self.clickcount = 0
            print(ex)

    # YENİ DOSYA EKLENİNCE LİSTEYİ YENİLEMEK İÇİN. AMA DOSYA SİLİNCE DOSYA SİLİNMİYOR ONA BİR ARA BAK!!!
    def refreshFolders(self):
        new_list = os.listdir(self.path)
        refreshed_folders = list(set(new_list) - set(self.first_folders))
        print(refreshed_folders)
        for i in refreshed_folders:
            if os.path.isdir(i):
                self.ui.listwidget.addItem(i)

        self.first_folders = new_list

    def contour_det(self):
        try:
            # Load Aruco detector
            parameters = cv2.aruco.DetectorParameters_create()
            aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)

            # Load Object Detector
            detector = HomogeneousBgDetector()

            # Load Image
            print(self.photopath)
            img = cv2.imread(self.photopath)
            #img = cv2.imread("C:/Users/musta/Desktop/Image_Processing_Project/Objects_File/Kalem/Right.JPG")

            # Get Aruco marker
            corners, _, _ = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)

            # Draw polygon around the marker
            int_corners = np.int0(corners)
            cv2.polylines(img, int_corners, True, (0, 255, 0), 5)

            # Aruco Perimeter
            # aruco_perimeter = cv2.arcLength(corners[0], True)

            # Pixel to cm ratio
            #AOV = float(self.ui.camAOV_W.text()) * (180 / math.pi)
            AOV_W = math.radians(float(self.ui.camAOV_W.text()))

            #total_W = 2 * (math.tan((float(self.ui.camAOV_W.text()) * (180 / math.pi)) / 2) * float(self.ui.photo_Height.text()))
            total_W = 2 * (math.tan(AOV_W / 2) * float(self.ui.photo_Height.text()))
            ppm_W = total_W / float(self.ui.Megapixel_W.text())

            AOV_H = math.radians(float(self.ui.camAOV_H.text()))
            total_H = 2 * (math.tan(AOV_H / 2) * float(self.ui.photo_Height.text()))
            ppm_H = total_H / float(self.ui.Megapixel_H.text())

            # pixel_cm_ratio = aruco_perimeter / 20

            contours = detector.detect_objects(img)

            # Draw objects boundaries
            for cnt in contours:
                # Get rect
                rect = cv2.minAreaRect(cnt)
                (x, y), (w, h), angle = rect

                # Get Width and Height of the Objects by applying the Ratio pixel to cm
                object_width = w * ppm_W
                object_height = h * ppm_H

                # Display rectangle
                box = cv2.boxPoints(rect)
                box = np.int0(box)

                cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
                cv2.polylines(img, [box], True, (255, 0, 0), 2)
                cv2.putText(img, "Width {} cm".format(round(object_width, 1)), (int(x - 100), int(y - 20)),
                            cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
                cv2.putText(img, "Height {} cm".format(round(object_height, 1)), (int(x - 100), int(y + 15)),
                            cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)

            return img
        except Exception as ex:
            print(ex)

if __name__ == "__main__":

    app = QApplication(sys.argv)

    mainWindow = MainWindow()

    sys.exit(app.exec_())
