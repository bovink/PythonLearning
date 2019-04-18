import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Example(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.initView()

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def initView(self):
        self.window = QVBoxLayout()
        label = QLabel('hello world')
        pixel = QPixmap(self.resource_path('./myresource/ps_danci_k2.png'))
        label.setPixmap(pixel)
        btn = QPushButton('click btn')
        self.window.addWidget(label)
        self.window.addWidget(btn)
        btn.clicked.connect(self.showAlert)
        progress = QProgressBar()
        progress.setMaximum(120)
        self.window.addWidget(progress)
        progress.setValue(10)
        slider = QSlider(Qt.Horizontal)
        slider.valueChanged.connect(self.showSliderValue)
        self.window.addWidget(slider)
        self.setLayout(self.window)
        self.show()

    def showAlert(self):
        msg = QMessageBox()
        msg.setText('show a alert')
        msg.exec_()

    def showSliderValue(self):
        value = self.window.itemAt(3).widget().value()
        print('slider value is {}'.format(value))
        progress = self.window.itemAt(2).widget()
        progress.setValue(value)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Space:
            print('press space')


if __name__ == '__main__':
    app = QApplication([])
    example = Example()
    sys.exit(app.exec_())