import sys
from PyQt6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel("PDF Craft стартовал!")
label.show()
sys.exit(app.exec())

