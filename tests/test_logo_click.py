from pages.main_page import MainPage
import allure


class TestLogo:

    @allure.title("Проверка редиректа на Дзен при клике по логотипу Яндекса")
    @allure.description(
        "При клике на логотип Яндекса открывается новая вкладка, "
        "в которой происходит редирект на главную страницу Дзена."
    )
    def test_click_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_on_yandex_logo()
        main_page.check_redirect_to_dzen()

    @allure.title("Проверка перехода на главную страницу Самоката по клику на логотип")
    @allure.description(
        "При клике на логотип «Самокат» со страницы заказа "
        "происходит переход на главную страницу сайта Самоката."
    )
    def test_click_logo_scooter_redirects_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_on_button_order_top()
        main_page.click_on_scooter_logo()
        main_page.check_redirect_to_main_page()
