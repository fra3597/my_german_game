import os
import sys
import pytest
from PyQt5.QtWidgets import QApplication
from my_app.game_view.backend.mode_views.translate_mode_view import TranslateMode


# os.environ["PYTHONWARNINGS"] = "ignore::DeprecationWarning"

@pytest.fixture
def app():
    window = QApplication(sys.argv)
    game_view = TranslateMode()

    return window, game_view


@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_translate_mode_window(app):
    window, game_view = app
    print("******* Test Initiated *******")
    assert game_view.widget.question_label.text() == "The word to be translated is: "
    assert game_view.widget.input_line_edit.text() == ""
    assert game_view.widget.check_button.isEnabled()
    assert game_view.widget.check_button.text() == "Check!"
    assert game_view.widget.give_me_a_hint_button.isEnabled()
    assert game_view.widget.give_me_a_hint_button.text() == "Give me \na hint"
    assert game_view.widget.character_combo_box.currentText() == "ä"
    assert game_view.widget.add_character_button.isEnabled()
    assert game_view.widget.add_character_button.text() == "Add"
    assert game_view.widget.open_database_button.isEnabled()
    assert game_view.widget.open_database_button.text() == "Open Database"
    assert game_view.widget.solution_label.text() == ""




