from game_controller.controller import Controller
from game_model.game_mode.article_game import ArticleGame

CORRECT = True
WRONG = False

class ArticleController(Controller):
    def __init__(self, ui_controller):
        super().__init__(ui_controller)
        self.game_model = ArticleGame()

        self.connect_buttons()

    def start_game(self):
        self.ui_controller.set_article_mode_window()

        self.game_model.load_questions()

        text_to_show = f"<html>Select the article<br>German: <i>'{self.game_model.list_of_words[0].german_word}'</i><br>Italian: <i>'{self.game_model.list_of_words[0].italian_word}'</i></html>"
        self.ui_controller.article_mode_window.title_label.setText(text_to_show)

    def check_answer(self):
        user_answer = self.ui_controller.article_mode_window.read_user_answer()

        if user_answer == self.game_model.list_of_words[self.game_model.current_word].article:
            result = "<html><font color='green'>Genau!</font></html>"
            self.ui_controller.article_mode_window.comparison_result_label.setText(result)
            self.game_model.score.update_partial_score()
            self.ui_controller.article_summary_window.append_row_to_summary_table(
                self.game_model.list_of_words[self.game_model.current_word].article,
                user_answer,
                self.game_model.list_of_words[self.game_model.current_word].german_word,
                self.game_model.list_of_words[self.game_model.current_word].italian_word,
                CORRECT
            )
            self.game_model.guessed_entries.append(True)
        else:
            result = f"<html><font color='red'>Wrong!</font> The word was <i><font color='green'>'{self.game_model.list_of_words[self.game_model.current_word].article}'</font></i> {self.game_model.list_of_words[self.game_model.current_word].german_word}</html>"
            self.ui_controller.article_mode_window.comparison_result_label.setText(result)
            self.ui_controller.article_summary_window.append_row_to_summary_table(
                self.game_model.list_of_words[self.game_model.current_word].article,
                user_answer,
                self.game_model.list_of_words[self.game_model.current_word].german_word,
                self.game_model.list_of_words[self.game_model.current_word].italian_word,
                WRONG
            )
            self.game_model.guessed_entries.append(False)
        self.update_question()
        if self.game_model.current_word == self.game_model.QUESTIONS_PER_GAME:
            self.ui_controller.article_mode_window.enable_go_to_summary_button()
            self.game_model.score.update_total_score()
            self.game_model.update_score_in_database()

    def update_question(self):
        self.game_model.update_current_word()
        if self.game_model.current_word < self.game_model.QUESTIONS_PER_GAME:
            text_to_show = f"<html>Select the article<br>German: <i>'{self.game_model.list_of_words[self.game_model.current_word].german_word}'</i><br>Italian: <i>'{self.game_model.list_of_words[self.game_model.current_word].italian_word}'</i></html>"
            self.ui_controller.article_mode_window.title_label.setText(text_to_show)

    def show_summary(self):
        self.ui_controller.stacked_widget.setCurrentWidget(self.ui_controller.article_summary_window)
        # #I don't like a lot the previous function, should it be higher level?
        self.ui_controller.article_summary_window.show_score(
            self.game_model.score.partial_score,
            self.game_model.score.total_score,
            self.game_model.number_of_matches
        )

    def play_again(self):
        self.ui_controller.reset_article_mode_view()
        self.game_model.reset_game()
        self.start_game()

    def connect_buttons(self):
        self.ui_controller.select_game_mode_window.connect_article_mode_button(self.start_game)

        self.ui_controller.article_mode_window.connect_der_button(self.check_answer)
        self.ui_controller.article_mode_window.connect_die_button(self.check_answer)
        self.ui_controller.article_mode_window.connect_das_button(self.check_answer)
        self.ui_controller.article_mode_window.connect_go_to_summary_button(self.show_summary)

        self.ui_controller.article_summary_window.connect_play_again_button(self.play_again)
        self.ui_controller.article_summary_window.connect_quit_button(self.ui_controller.summary_window.quit_game)
