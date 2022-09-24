from gui import MyWindow_UI
from PyQt6 import QtWidgets


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    window = MyWindow_UI()
    window.show()
    app.exec()