import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMainWindow, QApplication
from PyQt6.QtGui import QPainter, QColor


class CircleWidget(QWidget):
    def __init__(self, diameter, parent=None):
        super().__init__(parent)
        self.diameter = diameter
        self.setFixedSize(diameter, diameter)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor('yellow'))
        # painter.setPen(QtCore.Qt.GlobalColor.transparent)
        painter.drawEllipse(0, 0, self.diameter, self.diameter)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("git_and_yellow_circles/UI.ui", self)
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = random.randint(10, 100)
        circle = CircleWidget(diameter, self)
        max_width, max_height = self.width(), self.height()
        
        x_pos = random.randint(0, max_width - diameter)
        y_pos = random.randint(0, max_height - diameter - 50)
        circle.move(x_pos, y_pos)
        circle.show()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())