import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simpel')
    w.show()

    sys.exit(app.exec_())

class Exampele(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon('web.png')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Exampele()
    sys.exit(app.exec_())
