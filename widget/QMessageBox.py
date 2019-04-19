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

        button = QPushButton('click', self)
        button.clicked.connect(self.clickBtn)
        button.setToolTip('click btn show console msg')
        button.setGeometry(0, 0, 100, 100)
        button.move(button.geometry().width(), button.geometry().height())
        button.show()

    def clickBtn(self):
        # 点击按钮后，直接显示MessageBox
        buttonReply = QMessageBox.question(self, 'Message', 'Do you like PyQt5', QMessageBox.Yes, QMessageBox.No)
        # 点击选项后才会继续执行
        if buttonReply == QMessageBox.Yes:
            print('yes')
        else:
            print('no')


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    sys.exit(app.exec_())
