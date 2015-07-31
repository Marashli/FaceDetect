from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi('windows/window.ui', self)
        self.pushButton.clicked.connect(self.main_def)
        pixmap = QPixmap("photo-75491.gif.png")
        # self.label_4.mousePressEvent(self.main_def)
        # self.graphicsView.addpixmap(pixmap)

    def main_def(self):
        print(self.lineEdit.text())
        cur = str(QtGui.QCursor.pos())
        cur = cur[20:-2]
        cur = cur.replace(",", "")
        cur = cur.split()
        print(cur)

    def mousePressEvent(self, QMouseEvent):
        print(self.lineEdit.text())
        cur = str(QtGui.QCursor.pos())
        cur = cur[20:-2]
        cur = cur.replace(",", "")
        cur = cur.split()
        print(cur)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
