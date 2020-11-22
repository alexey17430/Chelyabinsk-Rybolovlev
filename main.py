import sys
from random import randint
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtGui import QColor, QPainter, QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 300, 500, 500)
        self.setWindowTitle('Git и случайные окружности')

        font = QFont()
        font.setPointSize(16)
        self.flag = False

        self.btn = QPushButton(self)
        self.btn.resize(200, 100)
        self.btn.move(150, 200)
        self.btn.setText('Начать рисование')
        self.btn.setFont(font)
        self.btn.clicked.connect(self.btn_pushed)

    def btn_pushed(self):
        self.btn.deleteLater()
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            for i in range(1000):
                self.paint()

    def paint(self):
        qp = QPainter()
        qp.begin(self)
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        qp.setBrush(color)
        qp.setPen(color)
        r = randint(50, 350)
        qp.drawEllipse(randint(50, 450) - (r // 4), randint(50, 450) - (r // 4), r // 2, r // 2)
        qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
