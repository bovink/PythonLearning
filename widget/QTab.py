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

        tab = QTabWidget()
        tab.setTabPosition(QTabWidget.South)
        tab1 = QWidget()
        tab2 = QWidget()

        tab.addTab(tab1, 'tab1')
        tab.addTab(tab2, 'tab2')

        layout1 = QVBoxLayout(self)
        layout1.addWidget(tab)

        layout2 = QVBoxLayout(tab1)
        button = QPushButton('click')
        layout2.addWidget(button)
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    sys.exit(app.exec_())
