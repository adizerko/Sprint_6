from selenium.webdriver.common.by import By


class OrdersPageLocators:
    NAME = (By.XPATH, '//input[@placeholder="* Имя"]')
    LAST_NAME = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    METRO_DROPDOWN_OPTIONS = (By.CLASS_NAME, "select-search__option")
    PHONE = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')

    DATE = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    RENT_PERIOD_DROPDOWN = (By.CLASS_NAME, 'Dropdown-root')
    RENT_PERIOD_OPTIONS = (By.CLASS_NAME, 'Dropdown-menu')
    COLOR_BLACK_CHECKBOX = (By.ID, 'black')
    COLOR_GREY_CHECKBOX = (By.ID, 'grey')
    COMMENTS = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')

    BACK_BUTTON = (By.XPATH, '//button[text()="Назад"]')
    ORDER_BUTTON = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]')

    YES_BUTTON = (By.XPATH, '//button[text()="Да"]')
    NO_BUTTON = (By.XPATH, '//button[text()="Нет"]')

    VIEW_STATUS_BUTTON = (By.XPATH, '//button[text()="Посмотреть статус"]')

    @staticmethod
    def metro_choose_station(number):
        return By.XPATH, f'//li[@data-value="{number}"]/button'

    @staticmethod
    def rent_period_choose(number):
        return By.XPATH, f'//div[@class="Dropdown-menu"]/div[{number}]'

    @staticmethod
    def color_choose_scooter(number):
        return By.XPATH, f'//div[contains(text(),"Цвет самоката")]//following-sibling::label[{number}]/input'
