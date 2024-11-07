import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMainWindow, QApplication, QPushButton
from PyQt6.QtGui import QPainter, QColor


class CircleWidget(QWidget):
    def __init__(self, diameter, color, parent=None):
        super().__init__(parent)
        self.diameter = diameter
        self.color = color
        self.setFixedSize(diameter, diameter)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(self.color)
        painter.drawEllipse(0, 0, self.diameter, self.diameter)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(700, 300, 500, 500)

        self.pushButton = QPushButton(self)
        self.pushButton.setText('Добавить окружность')
        self.pushButton.setGeometry(170, 470, 160, 30)
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = random.randint(10, 100)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        circle = CircleWidget(diameter, color, self)
        max_width, max_height = self.width(), self.height()
        
        x_pos = random.randint(0, max_width - diameter)
        y_pos = random.randint(0, max_height - diameter - 50)
        circle.move(x_pos, y_pos)
        circle.show()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())