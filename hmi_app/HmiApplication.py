from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import (
    QLabel,
    QGridLayout,
    QWidget,
)


class Color(QWidget):
    
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Auto Test SLDD Application")
        self.setGeometry(0, 0, 1280, 720)
        self.addMenu()
        self.add_content()

    def addMenu(self):

        menuBar = self.menuBar() # Create menu bar

        fileMenu = menuBar.addMenu("File")  # Add menu items - file 
        helpMenu = menuBar.addMenu("Help")  # Add menu items - help

        # Create actions - file
        FileAhihiAction = QAction("file-Ahihi", self)
        FileAheheAction = QAction("file-Ahehe", self)
        fileMenu.addAction(FileAhihiAction)
        fileMenu.addAction(FileAheheAction)

        # Create actions - help
        AhihiAction = QAction("help-Ahihi", self)
        AheheAction = QAction("help-Ahehe", self)
        helpMenu.addAction(AhihiAction)
        helpMenu.addAction(AheheAction)
    
    def add_content(self):
        widget = QWidget()
        layout = QGridLayout()
        nameLabel = QLabel('Input TestCase : ')
        # layout.addWidget(nameLabel)
        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(Color('green'), 1, 0)
        layout.addWidget(Color('blue'), 1, 3)
        layout.addWidget(Color('purple'), 2, 1)

        widget.setLayout(layout)
        self.setCentralWidget(widget)




def run_gui():
    application = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    application.exec()
