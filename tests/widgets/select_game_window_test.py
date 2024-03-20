import os
import sys
import pytest
from PyQt5.QtWidgets import QApplication
from my_app.game_view.backend.select_game_view import SelectGameMode

# os.environ["PYTHONWARNINGS"] = "ignore::DeprecationWarning"

@pytest.fixture
def app():
    window = QApplication(sys.argv)
    game_view = SelectGameMode()

    return window, game_view


@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_select_game_window(app):
    window, game_view = app
    print("*******Test Initiated*******")
    assert game_view.widget.welcome_game_label.text() == "Who gets more Genaus wins!"
    assert game_view.widget.label.text() == "Select your game mode"
    assert game_view.widget.translate_mode_button.text() == "Translate the Word"
    assert game_view.widget.paradigm_mode_button.text() == "Complete the\nVerb Paradigm"
    assert game_view.widget.article_mode_button.text() == "Der, Die, oder Das?"



