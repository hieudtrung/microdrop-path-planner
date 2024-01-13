import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit, \
     QPushButton, QWidget, QTabWidget, QMenuBar, QMenu, QAction, QGridLayout,\
     QSplitter, QSizePolicy, QFileDialog, QDialog, QLabel, QLineEdit
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QTimer

class ConfigureDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Configure Dialog')

        # Create widgets for the dialog
        label = QLabel('Enter configuration:')
        self.text_input = QLineEdit(self)

        ok_button = QPushButton('OK', self)
        ok_button.clicked.connect(self.accept)  # Close the dialog on OK

        cancel_button = QPushButton('Cancel', self)
        cancel_button.clicked.connect(self.reject)  # Close the dialog on Cancel

        # Set up the layout
        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(self.text_input)
        layout.addWidget(ok_button)
        layout.addWidget(cancel_button)
