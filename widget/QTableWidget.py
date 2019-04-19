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

        self.createTable()

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

    def createTable(self):
        self.table = QTableWidget()
        self.table.setRowCount(4)
        self.table.setColumnCount(2)
        self.table.setItem(0, 0, QTableWidgetItem('item1'))
        self.table.setItem(0, 1, QTableWidgetItem('item2'))
        self.table.setItem(1, 0, QTableWidgetItem('item3'))
        self.table.setItem(1, 1, QTableWidgetItem('item4'))
        self.table.setItem(2, 0, QTableWidgetItem('item5'))
        self.table.setItem(2, 1, QTableWidgetItem('item6'))
        self.table.setItem(3, 0, QTableWidgetItem('item7'))
        self.table.setItem(3, 1, QTableWidgetItem('item8'))
        self.table.move(0, 0)

        self.table.clicked.connect(self.clickBtn)

    def clickBtn(self):
        for item in self.table.selectedItems():
            print('row is {}, column is {}, text is {}'.format(item.row(), item.column(), item.text()))


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    sys.exit(app.exec_())
