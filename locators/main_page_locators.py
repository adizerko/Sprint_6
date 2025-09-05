from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_BUTTON_BOTTOM = (By.CLASS_NAME, 'Button_UltraBig__UU3Lp')
    MAIN_TITLE = (By.CLASS_NAME, "Home_Header__iJKdX")
    FAQ_QUESTIONS = (By.CLASS_NAME, "accordion")

    @staticmethod
    def faq_question_items(number):
        return By.XPATH, f'//div[@class="accordion"]/div[{number}]/div/div'

    @staticmethod
    def faq_answer_items(number):
        return By.XPATH, f'//div[@class="accordion"]/div[{number}]/div[2]/p'
