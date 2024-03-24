from game_controller.paradigm_controller import ParadigmController
from game_controller.translation_controller import TranslationController
from game_controller.article_controller import ArticleController
from game_view.ui_controller import UIController


class MasterController:
    def __init__(self, game_view):
        self.paradigm_controller:ParadigmController = ParadigmController(game_view)
        self.translation_controller:TranslationController = TranslationController(game_view)
        self.article_controller:ArticleController = ArticleController(game_view)
        self.game_view:UIController = game_view
