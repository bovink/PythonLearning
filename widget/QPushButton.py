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

        # 这样不需要window setLayout也可以显示按钮
        button = QPushButton('click', self)
        button.clicked.connect(self.clickBtn)
        button.setToolTip('click btn show console msg')
        button.setGeometry(0, 0, 100, 100)
        button.move(button.geometry().width(), button.geometry().height())
        button.show()

    def clickBtn(self):
        print('you clicked btn')


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    sys.exit(app.exec_())