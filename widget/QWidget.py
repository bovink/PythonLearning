from PyQt5.QtWidgets import *
from PyQt5 import QtCore


class Window(QWidget):
    resized = QtCore.pyqtSignal()

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
        self.resized.connect(self.somefun)

    def resizeEvent(self, QResizeEvent):
        self.resized.emit()
        return super(Window, self).resizeEvent(QResizeEvent)

    def somefun(self):
        print('somefun')


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
