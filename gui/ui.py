from .ui_tempate import *
from PyQt6 import QtWidgets
class MyWindow_UI(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyWindow_UI,self).__init__()
        self.setupUi(self)

        # new
        self.pushButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        text1 = self.lineEdit.text()
        text2 = self.lineEdit_2.text()

        try:
            num1 = int(text1)
            num2 = int(text2)
        except Exception as e:
            print(e)
            return

        result = num1 + num2
        self.lineEdit_3.setText(str(result))
