from selenium.webdriver.common.by import By


class SwitchPageLocators:

    YANDEX_LOGO = By.XPATH, './/*[contains(@class, "Header_LogoYandex")]'
    SEARCH_BUTTON = By.XPATH, './/button[text()="Найти"]'
    SCOOTER_LOGO = By.XPATH, './/*[contains(@class, "Header_LogoScooter")]'
    SCOOTER_TEXT = By.XPATH, './/*[text()="И здесь куки! В общем, мы их используем."]'
