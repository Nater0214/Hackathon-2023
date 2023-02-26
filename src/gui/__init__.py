# gui/__init__.py
# Handles the gui


# Imports
from PySide6 import QtCore as Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QApplication, QMainWindow

from . import ui_start, ui_setup, ui_input
import src.garb_input as garb_input


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
        
        # Button connections
        self.gototaskButton.clicked.connect(self.input_window_start)
    
    
    # Window changers
    def input_window_start(self) -> None:
        """Open the input UI"""
        
        input_window.show()


class InputWindow(QMainWindow, ui_input.Ui_MainWindow):
    def __init__(self):
        # Init
        
        super(InputWindow, self).__init__()
        self.setupUi(self)
        
        # Input connections
        self.taskinputEdit.returnPressed.connect(self.add_task)
    
    
    def add_task(self):
        """Add the input task"""
        
        # Get text and clear
        task_text = self.taskinputEdit.text()
        self.taskinputEdit.clear()
        
        # Run decipher on text
        deciphered_text = garb_input.decipher(task_text)
        
        self.taskList.addItem(f"{deciphered_text['date']}: {deciphered_text['name']}")


# Create the windows
def create_windows(app: QApplication) -> None:
    global start_window
    global setup_window
    global input_window
    
    start_window = StartWindow(app)
    setup_window = SetupWindow()
    input_window = InputWindow()