import sys
import pytest
from PyQt5.QtWidgets import QApplication
from my_app.game_view.ui_controller import UIController
from my_app.game_controller.translation_controller import TranslationController


@pytest.fixture
def app():
    window = QApplication(sys.argv)
    game_view = UIController()
    controller = TranslationController(game_view)


    return window, game_view, controller


@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_translate_mode_window(app):
    window, game_view, controller = app
    print("******* Test Initiated *******")
    game_view.select_game_mode_window.widget.translate_mode_button.click()
    #TODO Add a check for the current index of the active widget to see if it is the proper one
    controller.select_language_window.widget.german_to_italian_button.click()
    #TODO Add a check for the current index of the active widget to see if it is the proper one
    current_question = controller.game_model.questions[controller.game_model.current_word]
    current_answer = controller.game_model.answers[controller.game_model.current_word]
    assert controller.translate_mode_window.widget.question_label.text() == f"<html>How do you translate <i>'{current_question}'</i> ? </html>"
    controller.translate_mode_window.widget.check_button.click()
    assert controller.translate_mode_window.widget.solution_label.text() == f"<html><font color='red'>Wrong!</font> The correct answer was <i><font color='green'>'{current_answer}'</font></i></html>"




