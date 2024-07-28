from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = By.XPATH, './/div[@id="accordion__heading-{}"]'
    RESPONSE_LOCATOR = By.XPATH, './/div[@id="accordion__panel-{}"]'
    COOKIE_CONFIRM_BUTTON = By.XPATH, './/button[text()="да все привыкли"]'  # кнопка согласия на
    # использование куки
    ORDER_BUTTON_HEADER = By.XPATH, './/div[contains(@class, "Header_Nav")]/button[text()="Заказать"]'
    ORDER_BUTTON_FOOTER = By.XPATH, './/div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]'
