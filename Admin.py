import sys
from PyQt5.QtWidgets import QMainWindow    
from _UI_DESIGNS.backdoorUI import *
from PyQt5.QtWidgets import QDesktopWidget




class AdminApp(QMainWindow,Ui_BackdoorForm):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        # self.setupUi(self)

        # #CENTER ALIGNMENT
        # cp = QDesktopWidget().availableGeometry().center()
        # qr = self.frameGeometry()
        # qr.moveCenter(cp)
        # self.retranslateUi(self)
        # QtCore.QMetaObject.connectSlotsByName(self)
        # self.move(qr.topLeft())


        # self.pushButton.clicked.connect(lambda checked:self.save())


    def save(self):
        print("save btn in pressed")









        




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = AdminApp()
    w.show()
    sys.exit(app.exec_())