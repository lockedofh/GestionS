from views.vendors_view import VendorsView, AddVendorView, EditVendorView, DeleteDialogView
from views.main_window_view import MainWindowView
from models.vendor_model import VendorModel

class VendorsController(object):

    def __init__(self, parent:MainWindowView=None) -> None:
        self.parent = parent
        self.model = VendorModel()
    def initialize_table(self):
        """Ensures the Vendors table exists or creates it.
        If any error occurs, handles it."""
        response = self.model.ensure_table_exists()
        if response:
            pass

    def show(self):
        self.main_view = VendorsView(self.parent)
        self.main_view.main_ui.setupUi(self.main_view)
        self.parent.setCentralWidget(self.main_view)
        self.main_view.show()
