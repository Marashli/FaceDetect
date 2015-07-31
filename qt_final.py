from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageDraw


image = Image.open("face.png")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()

for i in range(width):
        for j in range(height):
            r = pix[i, j][0]
            g = pix[i, j][1]
            b = pix[i, j][2]
            # if r !=
            # draw.point((i, j), (S, S, S))

config = open('config.txt', 'r')
config = config.read()
config = config.split()
main_li = []
for i in range(len(config) // 6):
    main_li.append([config[i * 3 + 1], config[i * 3 + 2]])

# print(main_li)


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi('windows/window_2.ui', self)
        self.move(500, 300)

        # img_main = QPixmap("photo-75491.gif.png")
        # self.label.setPixmap(img_main)
        #self.label_4.setText(str('Ученик отвернулся ' + str(main_li[0][0]) + ' раз'))
        #self.label_5.setText(str('На доску смотрел ' + str(main_li[0][1]) + ' %'))

        self.label_4.setText(str('Ученик отвернулся 7 раз'))
        self.label_5.setText(str('На доску смотрел 81 %'))

    def main_def(self):
        pass

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
