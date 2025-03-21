from PyQt6.QtWidgets import QMainWindow
from views.reports_view import ReportsView

class ReportsController(object):

    def __init__(self, parent:QMainWindow=None) -> None:
        self.parent = parent
        self.main_view = ReportsView(self.parent)        

    def show(self):
        self.parent.setCentralWidget(self.main_view)
        self.main_view.show()