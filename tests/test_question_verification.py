import allure
import pytest
from locators.locators_main_page import LocatorsMainPage
from data import BlockAnswerText
from pages.main_page import MainPage

class TestQuestions:
    @allure.title('Выпадающий список в разделе «Вопросы о важном»')
    @allure.description('Проверить: когда нажимаешь на стрелочку, открывается соответствующий текст.')
    @pytest.mark.parametrize('question, answer, true_answer', [(LocatorsMainPage.QUESTION_1, LocatorsMainPage.ANSWER_1, BlockAnswerText.text_block_1),
                                                               (LocatorsMainPage.QUESTION_2, LocatorsMainPage.ANSWER_2, BlockAnswerText.text_block_2),
                                                               (LocatorsMainPage.QUESTION_3, LocatorsMainPage.ANSWER_3, BlockAnswerText.text_block_3),
                                                               (LocatorsMainPage.QUESTION_4, LocatorsMainPage.ANSWER_4, BlockAnswerText.text_block_4),
                                                               (LocatorsMainPage.QUESTION_5, LocatorsMainPage.ANSWER_5, BlockAnswerText.text_block_5),
                                                               (LocatorsMainPage.QUESTION_6, LocatorsMainPage.ANSWER_6, BlockAnswerText.text_block_6),
                                                               (LocatorsMainPage.QUESTION_7, LocatorsMainPage.ANSWER_7, BlockAnswerText.text_block_7),
                                                               (LocatorsMainPage.QUESTION_8, LocatorsMainPage.ANSWER_8, BlockAnswerText.text_block_8)])
    def test_question(self, question, answer, true_answer, browser):
        main_page = MainPage(browser)
        main_page.click_button_cookie()
        main_page.scrolling_method()
        main_page.click_button(question)
        text_answer = main_page.get_element_text(answer)
        assert text_answer == true_answer
