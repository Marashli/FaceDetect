from PyQt5 import uic, QtWidgets


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi('windows/window.ui', self)
        self.pushButton.clicked.connect(self.main_def)

    def main_def(self):
        print(self.lineEdit.text())

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
