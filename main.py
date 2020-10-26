import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QApplication, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSlot


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Chess Tournament Manager'
        self.left = 30
        self.top = 50
        self.width = 800
        self.height = 600
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('New Swiss Tournament')

        exit_button = QAction(QIcon(), 'Exit', self)
        exit_button.setShortcut('Ctrl+Q')
        exit_button.setStatusTip('Exit application')
        exit_button.triggered.connect(self.close)
        main_menu.addAction(exit_button)

        # Create image
        label = QLabel(self)
        pixmap = QPixmap('logo.jpg')
        label.setPixmap(pixmap)
        label.move(int((self.width - 250) / 2), int((self.height - 200) / 2))
        label.resize(250, 200)
        self.show()

    def new_swiss_tournament(self):
        self.setWindowTitle('New Swiss Tournament')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
