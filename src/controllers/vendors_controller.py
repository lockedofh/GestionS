from views.vendors_view import VendorsView, AddVendorView, EditVendorView, DeleteDialogView
from PyQt6.QtWidgets import QMainWindow

class VendorsController(object):

    def __init__(self, parent:QMainWindow=None) -> None:
        self.parent = parent
        self.main_view = VendorsView(self.parent)

    def show(self):
        self.parent.setCentralWidget(self.main_view)
        self.main_view.show()
