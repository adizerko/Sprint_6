from locators.order_page_locators import OrdersPageLocators
from selenium.webdriver.common.keys import Keys
from helper import GenerationData as GD
from pages.base_page import BasePage
from curl import Curl
import allure


class OrderPage(BasePage):

    @allure.step('Открытие главной страницы')
    def open(self):
        return self.driver.get(Curl.MAIN_PAGE_URl)

    @allure.step('Кликнуть на кнопку "Заказать".')
    def click_on_button_order(self, button):
        self.click_on_element(button)

    @allure.step('Скролл до элемента кнопки "Заказать"')
    def scroll_to_order_button_bottom(self, button):
        self.scroll_to_element(button)

    @allure.step('Ввести имя')
    def set_name(self):
        self.send_keys_to_input(OrdersPageLocators.NAME, GD.generate_name())

    @allure.step('Ввести фамилию')
    def set_last_name(self):
        self.send_keys_to_input(OrdersPageLocators.LAST_NAME, GD.generate_last_name())

    @allure.step('Ввести адрес')
    def set_address(self):
        self.send_keys_to_input(OrdersPageLocators.ADDRESS, GD.generate_address())

    @allure.step('Выбрать метро')
    def set_metro(self):
        self.click_on_element(OrdersPageLocators.METRO)
        self.wait_for_element(OrdersPageLocators.METRO_DROPDOWN_OPTIONS)
        self.click_on_element(OrdersPageLocators.metro_choose_station(GD.generate_random_number_metro()))

    @allure.step('Ввести номер телефона')
    def set_phone(self):
        self.send_keys_to_input(OrdersPageLocators.PHONE, GD.generate_phone())

    @allure.step('Кликнуть на кнопку "Далее"')
    def click_next_button(self):
        self.click_on_element(OrdersPageLocators.NEXT_BUTTON)

    @allure.step('Выбрать дату')
    def set_date(self):
        input_date = self.wait_for_element(OrdersPageLocators.DATE)
        input_date.click()
        input_date.clear()
        input_date.send_keys(GD.generate_date())
        input_date.send_keys(Keys.ENTER)

    @allure.step('Выбрать количество дней аренды')
    def set_rental_period(self):
        self.click_on_element(OrdersPageLocators.RENT_PERIOD_DROPDOWN)
        self.click_on_element(OrdersPageLocators.rent_period_choose(GD.generate_random_number_rent_period()))

    @allure.step('Выбрать цвет самоката')
    def set_color_scooter(self):
        self.click_on_element(OrdersPageLocators.color_choose_scooter(GD.generate_random_number_color_scooter()))

    @allure.step('Ввести комментарий')
    def set_comment(self):
        self.send_keys_to_input(OrdersPageLocators.COMMENTS, GD.generate_comment())

    @allure.step('Кликнуть на кнопку "Заказать"')
    def click_order_button(self):
        self.click_on_element(OrdersPageLocators.ORDER_BUTTON)

    @allure.step('При подтверждении заказа кликнуть на кнопку "Да"')
    def click_confirmation_order_button_yes(self):
        self.click_on_element(OrdersPageLocators.YES_BUTTON)

    @allure.step('Проверяем видимость кнопки "Посмотреть статус"')
    def check_displaying_button_status_order(self):
        return self.wait_for_element(OrdersPageLocators.VIEW_STATUS_BUTTON)

    @allure.step('Заполнение первой части формы аренды самоката')
    def set_first_form(self):
        self.set_name()
        self.set_last_name()
        self.set_address()
        self.set_metro()
        self.set_phone()
        self.click_next_button()

    @allure.step('Заполнение второй части формы аренды самоката')
    def set_second_form(self):
        self.set_date()
        self.set_rental_period()
        self.set_color_scooter()
        self.set_comment()
        self.click_order_button()
