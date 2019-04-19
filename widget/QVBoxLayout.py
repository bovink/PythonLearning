from PyQt5.QtWidgets import *
import sys


class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.left = 100
        self.top = 100
        self.width = 1024
        self.height = 720
        self.title = 'hello world'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

        # 垂直排列
        layout = QVBoxLayout(self)

        btn1 = QPushButton('btn1')
        btn2 = QPushButton('btn2')
        btn3 = QPushButton('btn3')
        btn4 = QPushButton('btn4')
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    sys.exit(app.exec_())
