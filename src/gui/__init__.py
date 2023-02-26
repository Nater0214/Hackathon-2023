# gui/__init__.py
# Handles the gui


# Imports
from PySide6 import QtCore as Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QApplication, QMainWindow

from . import ui_start, ui_setup


# Definitions

# Window handlers
class StartWindow(QMainWindow, ui_start.Ui_MainWindow):
    def __init__(self, app: QApplication):
        # Init
        
        super(StartWindow, self).__init__()
        self.setupUi(self)
        
        self.app = app
        
        # Button connections
        self.setupButton.clicked.connect(self.setup_ui_start)
    
    
    def closeEvent(self, event) -> None:
        self.app.quit()
    
    
    # Window changers
    def setup_ui_start(self) -> None:
        """Open the setup UI"""
        
        setup_window.show()


class SetupWindow(QMainWindow, ui_setup.Ui_MainWindow):
    def __init__(self):
        # Init
        
        super(SetupWindow, self).__init__()
        self.setupUi(self)


# Create the windows
def create_windows(app: QApplication) -> None:
    global start_window
    global setup_window
    
    start_window = StartWindow(app)
    setup_window = SetupWindow()