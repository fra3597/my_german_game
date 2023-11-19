import sys
from PyQt5 import QtWidgets
from game_view.ui_controller import UIController
from master_controller import MasterController


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    game_view = UIController()
    game_view.show()

    master_controller = MasterController(game_view)

    sys.exit(app.exec_())
