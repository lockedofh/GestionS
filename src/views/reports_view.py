from PyQt6.QtCore import Qt
from ui.ui_reports import Ui_ShowReports
from PyQt6.QtWidgets import QWidget

class ReportsView(QWidget):
    
    def __init__(self, parent:QWidget=None) -> None:
        super().__init__(parent)
        self.main_ui = Ui_ShowReports()
        # self.main_ui.setupUi(self)