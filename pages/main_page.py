from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from curl import Curl
import allure


class MainPage(BasePage):

    @allure.step('Открытие главной страницы')
    def open(self):
        return self.driver.get(Curl.MAIN_PAGE_URl)

    @allure.step('Скрол до блока "Вопросы о важном"')
    def scroll_to_element_faq(self):
        self.scroll_to_element(MainPageLocators.FAQ_QUESTIONS)

    @allure.step('Кликаем каждый вопрос в блоке FAQ"')
    def click_on_faq_question(self, num):
        self.click_on_element(MainPageLocators.faq_question_items(num))

    @allure.step('Получаем текст и сравниваем с ожидаемым результатом"')
    def get_text_on_faq_answer(self, num):
        actual_answer = self.get_text_on_element(MainPageLocators.faq_answer_items(num))
        return actual_answer

    @allure.step('Кликаем на логотип яндекса в шапке сайта')
    def click_on_yandex_logo(self):
        self.click_on_element(BasePageLocators.YANDEX_LOGO)

    @allure.step('Кликаем по логотипу самоката в шапке сайта')
    def click_on_scooter_logo(self):
        self.click_on_element(BasePageLocators.SCOOTER_LOGO)

    @allure.step('Кликаем по кнопке "Заказать" в шапке сайта')
    def click_on_button_order_top(self):
        self.click_on_element(BasePageLocators.ORDER_BUTTON_TOP)

    @allure.step('Проверяем редирект на главную страницу сайта')
    def check_redirect_to_main_page(self):
        current_url = self.get_current_url(Curl.MAIN_PAGE_URl)
        assert current_url == Curl.MAIN_PAGE_URl

    @allure.step('Переключаемся на новую вкладку (Дзен)')
    def switch_tab_to_dzen(self):
        current_tab = self.save_current_tab()
        self.waiting_for_new_tab()
        self.switching_to_new_tab(current_tab)

    @allure.step('Проверяем редирект на страницу Дзен')
    def check_redirect_to_dzen(self):
        self.switch_tab_to_dzen()
        current_url = self.get_current_url(Curl.DZEN_URL)
        assert Curl.DZEN_URL == current_url

