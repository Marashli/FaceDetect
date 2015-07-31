from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui

config = open('config.txt', 'w')

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi('windows/window.ui', self)
        self.pushButton.clicked.connect(self.main_def)
        # pixmap = QPixmap("photo-75491.gif.png")

        pixmap = QPixmap("face.png")
        self.label_4.setPixmap(pixmap)
        self.move(300, 200)

        # self.label_4.mousePressEvent(self.main_def)
        # self.graphicsView.addpixmap(pixmap)

    def main_def(self):
        print(self.lineEdit.text())
        config.write(self.lineEdit.text() + ' ')

    def mousePressEvent(self, QMouseEvent):
        # print(self.lineEdit.text())
        # cur = str(QtGui.QCursor.pos().x()) + ' | ' + str(QtGui.QCursor.pos().y())
        # print(cur)

        cur = str(QtGui.QCursor.pos())
        cur = cur[20:-2]
        cur = cur.replace(",", "")
        cur = cur.split()
        cur[0] = int(cur[0]) - 310
        cur[1] = (int(cur[1]) - 23) * (479 // 49)
        print(cur)

        config.write(str(int(cur[0])) + ' ')
        config.write(str(int(cur[1])) + ' ')

        # print((int(cur[0]) - 310), (int(cur[1]) - 23))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()

