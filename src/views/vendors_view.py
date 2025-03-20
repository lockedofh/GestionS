from PyQt6.QtWidgets import QWidget
from ui.ui_vendors import Ui_ShowVendors

class VendorsView(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_ui = Ui_ShowVendors()
        self.main_ui.setupUi(self)
