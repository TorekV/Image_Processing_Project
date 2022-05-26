from PyQt5 import QtGui,QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import ctypes
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class user_interface(QWidget, QApplication):
    def setupUi(self,Form):
        Form.setWindowTitle("Image Processing Project")
        Form.showMaximized()
        Form.setStyleSheet("background-color:rgb(220, 220, 220);")


        self.listwidget = QComboBox(Form)
        self.listwidget.setGeometry(20,10,120,20)
        self.listwidget.setStyleSheet("""QComboBox{background:rgb(20, 95, 138);color: white;}""")
        self.listwidget.clear()
        self.listwidget.show()

        self.selectFileButton = QPushButton(Form)
        self.selectFileButton.setGeometry(150, 10, 80, 30)
        self.selectFileButton.setStyleSheet("""QPushButton{background:rgb(20, 95, 138);color: white;}""")
        self.selectFileButton.setText("Select Item")
        self.selectFileButton.show()

        self.refreshFileButton = QPushButton(Form)
        self.refreshFileButton.setGeometry(150, 50, 80, 30)
        self.refreshFileButton.setStyleSheet("""QPushButton{background:rgb(20, 95, 138);color: white;}""")
        self.refreshFileButton.setText("Refresh Items")
        self.refreshFileButton.show()

        self.imageBox = QtWidgets.QLabel(Form)
        self.imageBox.setGeometry(250, 10, 600, 600)
        self.imageBox.setText("")
        # self.imageBox.setAutoFillBackground(True)
        color = QtGui.QColor(0, 0, 0)
        alpha = 140
        values = "{r}, {g}, {b}, {a}".format(r=color.red(),
                                             g=color.green(),
                                             b=color.blue(),
                                             a=alpha
                                             )
        self.imageBox.setStyleSheet("QLabel { background-color: rgba(" + values + "); }")
        self.imageBox.setScaledContents(True)
        self.imageBox.show()



        self.CADBox = QtWidgets.QLabel(Form)
        self.CADBox.setGeometry(1050, 10, 600, 600)
        self.CADBox.setText("")
        # self.imageBox.setAutoFillBackground(True)
        color = QtGui.QColor(0, 0, 0)
        alpha = 140
        values = "{r}, {g}, {b}, {a}".format(r=color.red(),
                                             g=color.green(),
                                             b=color.blue(),
                                             a=alpha
                                             )
        self.CADBox.setStyleSheet("QLabel { background-color: rgba(" + values + "); }")
        self.CADBox.setScaledContents(True)
        self.CADBox.show()

        self.TopViewButton = QPushButton(Form)
        self.TopViewButton.setGeometry(900, 20, 80, 30)
        self.TopViewButton.setStyleSheet("""QPushButton{background:rgb(20, 95, 138);color: white;}""")
        self.TopViewButton.setText("Top View")
        self.TopViewButton.show()

        self.RightViewButton = QPushButton(Form)
        self.RightViewButton.setGeometry(900, 50, 80, 30)
        self.RightViewButton.setStyleSheet("""QPushButton{background:rgb(20, 95, 138);color: white;}""")
        self.RightViewButton.setText("Right View")
        self.RightViewButton.show()

        self.FrontViewButton = QPushButton(Form)
        self.FrontViewButton.setGeometry(900, 80, 80, 30)
        self.FrontViewButton.setStyleSheet("""QPushButton{background:rgb(20, 95, 138);color: white;}""")
        self.FrontViewButton.setText("Front View")
        self.FrontViewButton.show()

        self.hataLabel = QLabel(Form)
        self.hataLabel.setGeometry(1050,620,65,20)
        self.hataLabel.setFont(QFont('Arial', 20))
        self.hataLabel.setText("Hata: ")
        self.hataLabel.show()

        self.GB = QGroupBox(Form)
        self.GB.setStyleSheet("QGroupBox{border: 5px solid red;}")
        self.GB.setTitle('Camera')
        self.GB.setStyleSheet("QGroupBox{background:rgb(20, 95, 138) ;font-size: 18px ;font-weight:bold;color:rgb(0, 0, 0)}")
        self.GB.setFixedWidth(250)
        self.GB.setFixedHeight(200)
        self.GB.setGeometry(0, 250, 250, 200)
        self.GB.show()

        self.camAOV_H_Label = QLabel(Form)
        self.camAOV_H_Label.setGeometry(5,300,40,30)
        self.camAOV_H_Label.setText("AOV H:")
        self.camAOV_H_Label.show()

        self.camAOV_H = QLineEdit(Form)
        self.camAOV_H.setGeometry(45,300,50,30)
        self.camAOV_H.setText("51.98")
        self.camAOV_H.show()

        self.camAOV_W_Label = QLabel(Form)
        self.camAOV_W_Label.setGeometry(105, 300, 40, 30)
        self.camAOV_W_Label.setText("AOV W:")
        self.camAOV_W_Label.show()

        self.camAOV_W = QLineEdit(Form)
        self.camAOV_W.setGeometry(150,300,50,30)
        self.camAOV_W.setText("72.59")
        self.camAOV_W.show()

        self.photo_Height_Label = QLabel(Form)
        self.photo_Height_Label.setGeometry(5,350,50,30)
        self.photo_Height_Label.setText("Height:")
        self.photo_Height_Label.show()

        self.photo_Height = QLineEdit(Form)
        self.photo_Height.setGeometry(45,350,50,30)
        self.photo_Height.setText("20")
        self.photo_Height.show()

        self.Megapixel_H_label = QLabel(Form)
        self.Megapixel_H_label.setGeometry(5, 400, 50, 30)
        self.Megapixel_H_label.setText("MP H:")
        self.Megapixel_H_label.show()

        self.Megapixel_H = QLineEdit(Form)
        self.Megapixel_H.setGeometry(45, 400, 50, 30)
        self.Megapixel_H.setText("1600")
        self.Megapixel_H.show()

        self.Megapixel_W_label = QLabel(Form)
        self.Megapixel_W_label.setGeometry(105, 400, 50, 30)
        self.Megapixel_W_label.setText("MP W:")
        self.Megapixel_W_label.show()

        self.Megapixel_W = QLineEdit(Form)
        self.Megapixel_W.setGeometry(150, 400, 50, 30)
        self.Megapixel_W.setText("900")
        self.Megapixel_W.show()

        self.click1_proof = QLabel(Form)
        self.click1_proof.setGeometry(250,620,65,20)
        self.click1_proof.setText("")
        self.click1_proof.show()

        self.click1_proof = QLabel(Form)
        self.click1_proof.setGeometry(300, 620, 65, 20)
        self.click1_proof.setText("")
        self.click1_proof.show()

        self.measureButton = QPushButton(Form)
        self.measureButton.setGeometry(900, 150, 80, 30)
        self.measureButton.setStyleSheet("""QPushButton{background:rgb(20, 95, 138);color: white;}""")
        self.measureButton.setText("Measure Dist")
        self.measureButton.show()

        self.measureLabel = QLabel(Form)
        self.measureLabel.setGeometry(900, 200, 80, 30)
        self.measureLabel.setText("Distance: ")
        self.measureLabel.show()

        self.measure = QLabel(Form)
        self.measure.setGeometry(950, 200, 50, 30)
        self.measure.show()

        self.measureAutoButton = QPushButton(Form)
        self.measureAutoButton.setGeometry(900, 500, 80, 30)
        self.measureAutoButton.setText("Edge")
        self.measureAutoButton.show()