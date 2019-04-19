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

        self.edit = QLineEdit(self)
        self.edit.move(20, 20)
        self.edit.resize(280, 50)
        self.edit.show()

        button = QPushButton('click', self)
        button.move(100, 100)
        button.clicked.connect(self.clickBtn)
        button.show()

    def clickBtn(self):
        text = self.edit.text()
        # 点击按钮后，直接显示MessageBox
        buttonReply = QMessageBox.question(self, 'Message', 'you typed ' + text, QMessageBox.Yes, QMessageBox.Yes)
        # 点击选项后才会继续执行
        if buttonReply == QMessageBox.Yes:
            print('yes')


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    sys.exit(app.exec_())
