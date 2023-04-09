from _UI_DESIGNS.UI import *
from PyQt5.QtWidgets import QMainWindow
from _UI_DESIGNS.UI import *
from _UTIL import *
from PyQt5.Qt import Qt
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget



class FirstApp(QMainWindow,Ui_Form): # I added Qwidget
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)

        # QMainWindow.__init__(self, parent=parent)
        # self.setupUi(self)
        # self.ui = AdminApp()
        # self.ui.setupUi(self)
        # self.ui.pushButton.clicked.connect(lambda checked:self.ui.save())
        # self.show()
        

         #CENTER ALIGNMENT
        cp = QDesktopWidget().availableGeometry().center()
        qr = self.frameGeometry()
        qr.moveCenter(cp)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.move(qr.topLeft())



        #DEPRICATE THIS TO MAKE DYNAMIC AND AVOID REPEATING
        email_sender ='jackfrostbyte799@gmail.com'
        # email_password = os.environ.get('EMAIL_PASSWORD')
        email_password = ('boitjyikyvrigbtc')
        email_receiver = 'fernandezerom@gmail.com'
        subject = 'Subject 4'
        body = """Hell-o""" 

        receiver = self.send_totxt.setText(email_receiver)
        subjecter =self.subject_totxt.setText(subject)
        message =self.messagetxt.setText(body)


        self.pushButton.clicked.connect(lambda checked:self.make_send())



    def make_send(self):
        email_sender ='jackfrostbyte799@gmail.com'
        # email_password = os.environ.get('EMAIL_PASSWORD')
        email_password = ('boitjyikyvrigbtc')
        email_receiver = 'fernandezerom@gmail.com'
        subject = 'Subject 4'
        body = "" 

        receiver = self.send_totxt.setText(email_receiver)
        subjecter =self.subject_totxt.setText(subject)
        message =self.messagetxt.setText(body)

        
        receiver = self.send_totxt.toPlainText()
        subjecter =self.subject_totxt.toPlainText()

        mess = self.messagetxt.toPlainText()
        print(receiver,subjecter,mess,email_sender,email_password)

        send(receiver,self.subject_totxt.toPlainText(),self.messagetxt.toPlainText(),email_sender,email_password)
        pass

    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F1:
            from Admin import AdminApp
            print("F1 key pressed")

            
        elif event.key() == Qt.Key_F12:
            print("F12 key pressed")
            self.make_send()
            

            
            

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = FirstApp()
    w.show()
    sys.exit(app.exec_())
    
