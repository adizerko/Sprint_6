from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Подождать кликабельности элемента")
    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_clickable(locator, timeout)
        element.click()

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step("Подождать и проверить, что атрибут элемента содержит текст")
    def wait_for_attribute(self, locator, attribute, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, value)
        )

    @allure.step('Ожидаем загрузки страницы URL')
    def wait_for_url_site(self,url, timeout=40):
        WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(url)
        )

    @allure.step("Получить текущий адрес сайта")
    def get_current_url(self, url):
        self.wait_for_url_site(url)
        current_url = self.driver.current_url
        return current_url

    @allure.step('Сохраняем текущую вкладку')
    def save_current_tab(self):
        return self.driver.current_window_handle

    @allure.step('Ждем появления новой вкладки')
    def waiting_for_new_tab(self):
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) == 2)

    @allure.step('# Переключаемся на новую вкладку и получаем текущий URL')
    def switching_to_new_tab(self, original_window):
        new_window = [w for w in self.driver.window_handles if w != original_window][0]
        self.driver.switch_to.window(new_window)
