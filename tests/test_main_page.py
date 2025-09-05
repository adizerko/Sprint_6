from pages.main_page import MainPage
from data import data_faq_answer
import allure
import pytest


class TestFAQ:

    @allure.title("Проверка отображения ответов в разделе 'Вопросы о важном'")
    @allure.description("""
    Тест проверяет работу блока 'Вопросы о важном' (FAQ) на главной странице:
    1. Находит список вопросов.
    2. Поочередно кликает на каждый вопрос.
    3. Проверяет, что отображается правильный ответ.
    Ожидаемый результат: при клике на вопрос открывается соответствующий текст ответа.
    """)
    @pytest.mark.parametrize('num, expect_answer', data_faq_answer)
    def test_faq_answers_on_main_page(self, driver, num, expect_answer):
        main_page = MainPage(driver)
        main_page.open()
        main_page.scroll_to_element_faq()
        main_page.click_on_faq_question(num)

        assert main_page.get_text_on_faq_answer(num) == expect_answer
