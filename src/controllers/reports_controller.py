from PyQt6.QtWidgets import QMainWindow, QVBoxLayout
from views.reports_view import ReportsView
from views.main_window_view import MainWindowView

class ReportsController(object):

    def __init__(self, parent:MainWindowView=None) -> None:
        self.parent = parent

    def show(self):
        self.main_view = ReportsView(self.parent)        
        self.main_view.main_ui.setupUi(self.main_view)
        self.parent.setCentralWidget(self.main_view)
        self.main_view.show()