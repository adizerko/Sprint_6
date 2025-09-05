from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPage
import allure
import pytest


class TestOrderPageOrder:

    @allure.title("Позитивное тестирование оформления заказа самоката ")
    @allure.description("""
Тест проверяет полный сценарий оформления заказа, через две точки входа:
1. Заполнение формы личных данных (имя, фамилия, адрес, метро, телефон).
2. Указание даты доставки и периода аренды.
3. Выбор цвета самоката и ввод комментария.
4. Подтверждение заказа в модальном окне.
Ожидаемый результат: заказ успешно оформлен, появляется окно подтверждения.
""")
    @pytest.mark.parametrize('button', [BasePageLocators.ORDER_BUTTON_TOP,
                                        MainPageLocators.ORDER_BUTTON_BOTTOM])
    def test_order_all_field_set(self, driver, button):
        order_page = OrderPage(driver)
        order_page.open()
        order_page.scroll_to_order_button_bottom(button)
        order_page.click_on_button_order(button)
        order_page.set_first_form()
        order_page.set_second_form()
        order_page.click_confirmation_order_button_yes()

        assert order_page.check_displaying_button_status_order()
