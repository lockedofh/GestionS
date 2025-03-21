from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QDialog
from ui.ui_vendors import Ui_ShowVendors
from ui.ui_add_vendor import Ui_AddVendor
from ui.ui_delete_vendor_confirm import Ui_DialogDeleteVendor
from ui.ui_edit_vendor import Ui_EditVendor

class VendorsView(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_ui = Ui_ShowVendors()
        self.main_ui.setupUi(self)

class AddVendorView(QWidget):

    def __init__(self, parent:QWidget=None) -> None:
        super().__init__(parent)
        self.add_vendor_ui = Ui_AddVendor()
        self.add_vendor_ui.setupUi(self)

class EditVendorView(QWidget):

    def __init__(self, parent:QWidget=None) -> None:
        super().__init__(parent)
        self.edit_vendor_ui = Ui_EditVendor()
        self.edit_vendor_ui.setupUi(self)

class DeleteDialogView(QDialog):

    def __init__(self, parent:QWidget=None) -> None:
        super().__init__(parent)
        self.delete_dialog_ui = Ui_DialogDeleteVendor()
        self.delete_dialog_ui.setupUi(self)
        self.rejected.connect(self.reject)

    def reject(self):
        self.close()

