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
        self.window = QVBoxLayout()

        button = QPushButton('click')
        button.clicked.connect(self.clickBtn)
        button.show()
        self.window.addWidget(button)
        self.setLayout(self.window)

    def clickBtn(self):
        print('you clicked btn')


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    sys.exit(app.exec_())