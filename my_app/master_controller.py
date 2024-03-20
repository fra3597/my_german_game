from game_controller.paradigm_controller import ParadigmController
from game_controller.translation_controller import TranslationController
from game_controller.article_controller import ArticleController


class MasterController:
    def __init__(self, game_view):
        self.paradigm_controller = ParadigmController(game_view)
        self.translation_controller = TranslationController(game_view)
        self.article_controller = ArticleController(game_view)
        self.game_view = game_view
