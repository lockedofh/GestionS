from PyQt6.QtWidgets import QMainWindow
from views.invoices_view import InvoicesView, AddInvoiceView, EditInvoiceView, DeleteInvoiceDialogView

class InvoicesController(object):

    def __init__(self, parent:QMainWindow=None) -> None:
        self.parent = parent
        self.main_view = InvoicesView(self.parent)

    def show(self):
        self.parent.setCentralWidget(self.main_view)
        self.main_view.show()
