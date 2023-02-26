# gui/__init__.py
# Handles the gui


# Imports
from PySide6 import QtCore as Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QApplication, QMainWindow

from . import ui_start


# Definitions

# Window handlers
class StartWindow(QMainWindow, ui_start.Ui_MainWindow):
    def __init__(self, app: QApplication):
        # Init
        
        super(StartWindow, self).__init__()
        self.setupUi(self)
        
        self.app = app
    
    
    def closeEvent(self, event) -> None:
        self.app.quit()


# Create the windows
def create_windows(app: QApplication) -> None:
    global start_window 
    
    start_window = StartWindow(app)