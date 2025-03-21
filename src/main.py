from PyQt6.QtWidgets import QApplication
from controllers.main_controller import MainController

def main():
    """
    Instantiates the main application and executes it
    """
    app = QApplication([])
    main_controller = MainController()
    main_controller.start_app()
    app.exec()

main()