from PyQt5.QtWidgets import *


class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.left = 0
        self.top = 10
        self.width = 1024
        self.height = 720
        self.title = 'hello world!'
        self.initUI()

    def initUI(self):
        # todo 添加更多的方法使用
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
