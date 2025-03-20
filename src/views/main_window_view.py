from PyQt6.QtWidgets import QMainWindow
from ui.ui_main_window import Ui_MainWindow

class MainWindowView(QMainWindow):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)        
