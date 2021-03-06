# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(831, 600)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(115, 110, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 110, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(115, 110, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-10, 0, 831, 541))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.button_confirm = QtWidgets.QPushButton(self.page)
        self.button_confirm.setGeometry(QtCore.QRect(250, 410, 301, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.button_confirm.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Alef")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.button_confirm.setFont(font)
        self.button_confirm.setObjectName("button_confirm")
        self.label_img = QtWidgets.QLabel(self.page)
        self.label_img.setGeometry(QtCore.QRect(310, 160, 181, 131))
        self.label_img.setText("")
        self.label_img.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img.setObjectName("label_img")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(270, 50, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_fileName = QtWidgets.QLabel(self.page)
        self.label_fileName.setGeometry(QtCore.QRect(160, 300, 491, 81))
        self.label_fileName.setText("")
        self.label_fileName.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileName.setWordWrap(True)
        self.label_fileName.setObjectName("label_fileName")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(280, 50, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_img_9 = QtWidgets.QLabel(self.page_3)
        self.label_img_9.setGeometry(QtCore.QRect(260, 160, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_img_9.setFont(font)
        self.label_img_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img_9.setObjectName("label_img_9")
        self.button_confirm_4 = QtWidgets.QPushButton(self.page_3)
        self.button_confirm_4.setGeometry(QtCore.QRect(440, 410, 301, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.button_confirm_4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Alef")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.button_confirm_4.setFont(font)
        self.button_confirm_4.setObjectName("button_confirm_4")
        self.button_back_3 = QtWidgets.QPushButton(self.page_3)
        self.button_back_3.setGeometry(QtCore.QRect(110, 410, 301, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.button_back_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Alef")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.button_back_3.setFont(font)
        self.button_back_3.setObjectName("button_back_3")
        self.comboBox = QtWidgets.QComboBox(self.page_3)
        self.comboBox.setGeometry(QtCore.QRect(240, 250, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(380, 170, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.button_confirm_2 = QtWidgets.QPushButton(self.page_2)
        self.button_confirm_2.setGeometry(QtCore.QRect(440, 410, 301, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.button_confirm_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Alef")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.button_confirm_2.setFont(font)
        self.button_confirm_2.setObjectName("button_confirm_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(280, 50, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_img_2 = QtWidgets.QLabel(self.page_2)
        self.label_img_2.setGeometry(QtCore.QRect(270, 130, 131, 51))
        self.label_img_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img_2.setObjectName("label_img_2")
        self.button_back = QtWidgets.QPushButton(self.page_2)
        self.button_back.setGeometry(QtCore.QRect(110, 410, 301, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.button_back.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Alef")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.button_back.setFont(font)
        self.button_back.setObjectName("button_back")
        self.label_img_3 = QtWidgets.QLabel(self.page_2)
        self.label_img_3.setGeometry(QtCore.QRect(270, 210, 131, 51))
        self.label_img_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img_3.setObjectName("label_img_3")
        self.label_img_4 = QtWidgets.QLabel(self.page_2)
        self.label_img_4.setGeometry(QtCore.QRect(270, 300, 131, 51))
        self.label_img_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img_4.setObjectName("label_img_4")
        self.line_title = QtWidgets.QLineEdit(self.page_2)
        self.line_title.setGeometry(QtCore.QRect(410, 150, 113, 21))
        self.line_title.setText("")
        self.line_title.setObjectName("line_title")
        self.line_city = QtWidgets.QLineEdit(self.page_2)
        self.line_city.setGeometry(QtCore.QRect(410, 230, 113, 21))
        self.line_city.setObjectName("line_city")
        self.line_center = QtWidgets.QLineEdit(self.page_2)
        self.line_center.setGeometry(QtCore.QRect(410, 320, 113, 21))
        self.line_center.setObjectName("line_center")
        self.stackedWidget.addWidget(self.page_2)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_3 = QtWidgets.QLabel(self.page_5)
        self.label_3.setGeometry(QtCore.QRect(280, 50, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.button_back_2 = QtWidgets.QPushButton(self.page_5)
        self.button_back_2.setGeometry(QtCore.QRect(110, 410, 301, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.button_back_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Alef")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.button_back_2.setFont(font)
        self.button_back_2.setObjectName("button_back_2")
        self.button_confirm_3 = QtWidgets.QPushButton(self.page_5)
        self.button_confirm_3.setGeometry(QtCore.QRect(440, 410, 301, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.button_confirm_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Alef")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.button_confirm_3.setFont(font)
        self.button_confirm_3.setObjectName("button_confirm_3")
        self.label_img_5 = QtWidgets.QLabel(self.page_5)
        self.label_img_5.setGeometry(QtCore.QRect(140, 250, 131, 51))
        self.label_img_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img_5.setObjectName("label_img_5")
        self.label_img_6 = QtWidgets.QLabel(self.page_5)
        self.label_img_6.setGeometry(QtCore.QRect(140, 320, 131, 51))
        self.label_img_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img_6.setObjectName("label_img_6")
        self.label_img_7 = QtWidgets.QLabel(self.page_5)
        self.label_img_7.setGeometry(QtCore.QRect(140, 180, 131, 51))
        self.label_img_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img_7.setObjectName("label_img_7")
        self.label_img_8 = QtWidgets.QLabel(self.page_5)
        self.label_img_8.setGeometry(QtCore.QRect(140, 120, 131, 51))
        self.label_img_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img_8.setObjectName("label_img_8")
        self.label_fileName_3 = QtWidgets.QLabel(self.page_5)
        self.label_fileName_3.setGeometry(QtCore.QRect(290, 120, 501, 51))
        self.label_fileName_3.setText("")
        self.label_fileName_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fileName_3.setWordWrap(True)
        self.label_fileName_3.setObjectName("label_fileName_3")
        self.label_title_3 = QtWidgets.QLabel(self.page_5)
        self.label_title_3.setGeometry(QtCore.QRect(290, 180, 411, 51))
        self.label_title_3.setText("")
        self.label_title_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_3.setObjectName("label_title_3")
        self.label_city_3 = QtWidgets.QLabel(self.page_5)
        self.label_city_3.setGeometry(QtCore.QRect(290, 250, 411, 51))
        self.label_city_3.setText("")
        self.label_city_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_city_3.setObjectName("label_city_3")
        self.label_center_3 = QtWidgets.QLabel(self.page_5)
        self.label_center_3.setGeometry(QtCore.QRect(290, 320, 411, 51))
        self.label_center_3.setText("")
        self.label_center_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_center_3.setObjectName("label_center_3")
        self.stackedWidget.addWidget(self.page_5)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_img_10 = QtWidgets.QLabel(self.page_4)
        self.label_img_10.setGeometry(QtCore.QRect(20, 140, 131, 51))
        self.label_img_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img_10.setObjectName("label_img_10")
        self.button_confirm_5 = QtWidgets.QPushButton(self.page_4)
        self.button_confirm_5.setEnabled(False)
        self.button_confirm_5.setGeometry(QtCore.QRect(440, 410, 301, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.button_confirm_5.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Alef")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.button_confirm_5.setFont(font)
        self.button_confirm_5.setObjectName("button_confirm_5")
        self.label_6 = QtWidgets.QLabel(self.page_4)
        self.label_6.setGeometry(QtCore.QRect(280, 50, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.button_back_4 = QtWidgets.QPushButton(self.page_4)
        self.button_back_4.setEnabled(False)
        self.button_back_4.setGeometry(QtCore.QRect(110, 410, 301, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.button_back_4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Alef")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.button_back_4.setFont(font)
        self.button_back_4.setObjectName("button_back_4")
        self.progressBar = QtWidgets.QProgressBar(self.page_4)
        self.progressBar.setGeometry(QtCore.QRect(150, 150, 631, 31))
        self.progressBar.setProperty("value", 5)
        self.progressBar.setObjectName("progressBar")
        self.textEdit = QtWidgets.QTextEdit(self.page_4)
        self.textEdit.setGeometry(QtCore.QRect(110, 200, 631, 191))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.stackedWidget.addWidget(self.page_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 831, 26))
        self.menubar.setObjectName("menubar")
        self.menuselect = QtWidgets.QMenu(self.menubar)
        self.menuselect.setObjectName("menuselect")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionConfigure = QtWidgets.QAction(MainWindow)
        self.actionConfigure.setObjectName("actionConfigure")
        self.menuselect.addAction(self.actionOpen)
        self.menuselect.addAction(self.actionConfigure)
        self.menubar.addAction(self.menuselect.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "导入工具"))
        self.button_confirm.setText(_translate("MainWindow", "Confirm"))
        self.label.setText(_translate("MainWindow", "Choose File"))
        self.label_4.setText(_translate("MainWindow", "sheets"))
        self.label_img_9.setText(_translate("MainWindow", "seet："))
        self.button_confirm_4.setText(_translate("MainWindow", "Confirm"))
        self.button_back_3.setText(_translate("MainWindow", "Back"))
        self.button_confirm_2.setText(_translate("MainWindow", "Confirm"))
        self.label_2.setText(_translate("MainWindow", "settings"))
        self.label_img_2.setText(_translate("MainWindow", "标题列数："))
        self.button_back.setText(_translate("MainWindow", "Back"))
        self.label_img_3.setText(_translate("MainWindow", "城市所在列："))
        self.label_img_4.setText(_translate("MainWindow", "中心所在列："))
        self.label_3.setText(_translate("MainWindow", "confirm settings"))
        self.button_back_2.setText(_translate("MainWindow", "Back"))
        self.button_confirm_3.setText(_translate("MainWindow", "Confirm"))
        self.label_img_5.setText(_translate("MainWindow", "城市所在列："))
        self.label_img_6.setText(_translate("MainWindow", "中心所在列："))
        self.label_img_7.setText(_translate("MainWindow", "标题列数："))
        self.label_img_8.setText(_translate("MainWindow", "文件："))
        self.label_img_10.setText(_translate("MainWindow", "正在生成："))
        self.button_confirm_5.setText(_translate("MainWindow", "Close"))
        self.label_6.setText(_translate("MainWindow", "create"))
        self.button_back_4.setText(_translate("MainWindow", "Back"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Agency FB\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menuselect.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionConfigure.setText(_translate("MainWindow", "Exit"))
