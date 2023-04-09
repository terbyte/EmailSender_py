# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'backdoor.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BackdoorForm(object):
    def setupUi(self, BackdoorForm):
        BackdoorForm.setObjectName("BackdoorForm")
        BackdoorForm.setWindowModality(QtCore.Qt.WindowModal)
        BackdoorForm.resize(815, 573)
        self.frame = QtWidgets.QFrame(BackdoorForm)
        self.frame.setGeometry(QtCore.QRect(10, 10, 521, 501))
        self.frame.setStyleSheet("Background-color:#28AFB0;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(20, 70, 481, 31))
        self.lineEdit.setStyleSheet("Background-color:white;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 170, 481, 31))
        self.lineEdit_2.setStyleSheet("Background-color:white;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white;")
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 270, 481, 201))
        self.lineEdit_5.setStyleSheet("Background-color:white;")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.frame_2 = QtWidgets.QFrame(BackdoorForm)
        self.frame_2.setGeometry(QtCore.QRect(550, 10, 251, 501))
        self.frame_2.setStyleSheet("Background-color:#19647E;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 70, 211, 31))
        self.lineEdit_3.setStyleSheet("Background-color:white;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 170, 211, 31))
        self.lineEdit_4.setStyleSheet("Background-color:white;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(BackdoorForm)
        self.pushButton.setGeometry(QtCore.QRect(728, 520, 71, 41))
        self.pushButton.setStyleSheet("Background-color:#99d98c;")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(BackdoorForm)
        QtCore.QMetaObject.connectSlotsByName(BackdoorForm)

    def retranslateUi(self, BackdoorForm):
        _translate = QtCore.QCoreApplication.translate
        BackdoorForm.setWindowTitle(_translate("BackdoorForm", "Form"))
        self.label_3.setText(_translate("BackdoorForm", "Default email to send:"))
        self.label_4.setText(_translate("BackdoorForm", "Default Subject:"))
        self.label_5.setText(_translate("BackdoorForm", "Default Message:"))
        self.label.setText(_translate("BackdoorForm", "Sender\'s Email:"))
        self.label_2.setText(_translate("BackdoorForm", "Sender\'s Password:"))
        self.pushButton.setText(_translate("BackdoorForm", "SAVE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BackdoorForm = QtWidgets.QWidget()
    ui = Ui_BackdoorForm()
    ui.setupUi(BackdoorForm)
    BackdoorForm.show()
    sys.exit(app.exec_())
