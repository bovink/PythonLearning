from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys


# 必须是QMainWindow
class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 100
        self.top = 100
        self.width = 1024
        self.height = 720
        self.title = 'hello world'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.statusBar()

        mainMenu = self.menuBar()
        # 必须要设置为False才会显示menuBar，至少Mac上是这样
        mainMenu.setNativeMenuBar(False)
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        searchMenu = mainMenu.addMenu('Search')
        toolsMenu = mainMenu.addMenu('Tools')
        helpMenu = mainMenu.addMenu('Help')

        exitButton = QAction(QIcon('exit.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+W')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        # 至少要添加一个控件给窗口，才能激活快捷键
        button = QPushButton('click', self)
        button.setGeometry(0, 0, 100, 100)
        button.move((self.width - button.geometry().width()) / 2, (self.height - button.geometry().height()) / 2)

        self.show()


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    sys.exit(app.exec_())