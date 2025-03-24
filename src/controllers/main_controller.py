from views.main_window_view import MainWindowView
from controllers.vendors_controller import VendorsController
from controllers.invoices_controller import InvoicesController
from controllers.reports_controller import ReportsController

class MainController(object):

    def __init__(self) -> None:
        self.main_window_view = MainWindowView()
        self.vendors_controller = VendorsController(self.main_window_view)
        self.invoices_controller = InvoicesController(self.main_window_view)
        self.reports_controller = ReportsController(self.main_window_view)
        self.main_window_view.ui.centralwidget.show()

    def start_app(self):
        """
        Starts the app, showing the main window
        """        
        self.main_window_view.ui.mainVendorsAction.triggered.connect(self.go_to_vendors)
        self.main_window_view.ui.mainInvoicesAction.triggered.connect(self.go_to_invoices)
        self.main_window_view.ui.mainreportsAction.triggered.connect(self.go_to_reports)
        self.main_window_view.show()

    def go_to_vendors(self):
        """
        Delegates control to the vendors controller
        """
        self.vendors_controller.show()

    def go_to_invoices(self):
        """
        Delegates control to the invoices controller
        """
        self.invoices_controller.show()

    def go_to_reports(self):
        """
        Delegates control to the reports controller
        """
        self.reports_controller.show()



        