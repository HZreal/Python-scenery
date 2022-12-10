from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("PyQt5 桌面应用")
        self.show()


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())