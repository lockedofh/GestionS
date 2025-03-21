from PyQt6.QtCore import Qt
from ui.ui_invoices import Ui_ShowInvoices
from ui.ui_add_invoice import Ui_AddInvoice
from ui.ui_edit_invoice import Ui_EditInvoice
from ui.ui_delete_invoice_confirm import Ui_DialogDeleteInvoice
from PyQt6.QtWidgets import QDialog, QWidget

class InvoicesView(QWidget):

    def __init__(self, parent:QWidget=None) -> None:
        super().__init__(parent)
        self.main_ui = Ui_ShowInvoices()
        self.main_ui.setupUi(self)

class AddInvoiceView(QWidget):

    def __init__(self, parent:QWidget=None) -> None:
        super().__init__(parent)
        self.add_invoice_ui = Ui_AddInvoice()
        self.add_invoice_ui.setupUi(self)

class EditInvoiceView(QWidget):

    def __init__(self, parent:QWidget=None) -> None:
        super().__init__(parent)
        self.edit_invoice_ui = Ui_EditInvoice()
        self.edit_invoice_ui.setupUi(self)

class DeleteInvoiceDialogView(QDialog):

    def __init__(self, parent:QWidget=None) -> None:
        super().__init__(parent)
        self.delete_dialog_ui = Ui_DialogDeleteInvoice()
        self.delete_dialog_ui.setupUi(self)
        self.rejected.connect(self.reject)

    def reject(self):
        self.close()