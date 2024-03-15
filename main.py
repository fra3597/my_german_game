import sys
from PyQt5.QtWidgets import QApplication
from game_view.ui_controller import UIController
from master_controller import MasterController


if __name__ == '__main__':
    app = QApplication(sys.argv)

    game_view = UIController()
    game_view.show()

    master_controller = MasterController(game_view)

    sys.exit(app.exec_())
