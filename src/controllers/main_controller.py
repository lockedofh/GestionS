from views.main_window_view import MainWindowView
from controllers.vendors_controller import VendorsController
from controllers.invoices_controller import InvoicesController
from controllers.reports_controller import ReportsController

class MainController(object):

    def __init__(self) -> None:
        self.main_window_view = MainWindowView()

    def start_app(self):
        """
        Starts the app, showing the main window
        """        
        self.main_window_view.ui.menuVendors.triggered.connect(self.go_to_vendors)
        self.main_window_view.ui.menuInvoices.triggered.connect(self.go_to_invoices)
        self.main_window_view.ui.menuReports.triggered.connect(self.go_to_reports)
        self.main_window_view.show()

    def go_to_vendors(self):
        """
        Delegates control to the vendors controller
        """
        print("Vendor btn clicked")
        self.vendors_controller = VendorsController(self.main_window_view)
        self.vendors_controller.show()

    def go_to_invoices(self):
        """
        Delegates control to the invoices controller
        """
        print("Invoice btn clicked")
        self.invoices_controller = InvoicesController(self.main_window_view)
        self.invoices_controller.show()

    def go_to_reports(self):
        """
        Delegates control to the reports controller
        """
        print("Reports btn clicked")
        self.reports_controller = ReportsController(self.main_window_view)
        self.reports_controller.show()



        