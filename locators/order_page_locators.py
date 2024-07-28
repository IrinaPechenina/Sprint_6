from selenium.webdriver.common.by import By


class OrderPageLocators:

    INPUT_NAME = By.XPATH, './/*[@placeholder="* Имя"]'
    INPUT_SURNAME = By.XPATH, './/*[@placeholder="* Фамилия"]'
    INPUT_ADDRESS = By.XPATH, './/*[@placeholder="* Адрес: куда привезти заказ"]'
    INPUT_METRO_STATION = By.XPATH, './/*[@placeholder="* Станция метро"]'
    METRO_STATION = By.XPATH, '//*[text()="{}"]'
    INPUT_PHONE_NUMBER = By.XPATH, './/*[@placeholder="* Телефон: на него позвонит курьер"]'
    FURTHER_BUTTON = By.XPATH, './/button[text()="Далее"]'
    INPUT_DATE = By.XPATH, './/*[@placeholder="* Когда привезти самокат"]'
    RENTAL_PERIOD_POPUP = By.XPATH, './/div[@class="Dropdown-control"]'
    RENTAL_PERIOD_SELECT = By.XPATH, './/*[text()="{}"]'
    INPUT_SCOOTER_COLOR = By.XPATH, './/*[@id="{}"]'
    INPUT_COMMENT = By.XPATH, './/*[@placeholder="Комментарий для курьера"]'
    ORDER_BUTTON_MIDDLE = By.XPATH, './/button[contains(@class,"Button_Middle") and text()="Заказать"]'
    CONFIRM_BUTTON = By.XPATH, './/button[text()="Да"]'
    ORDER_STATUS_BUTTON = By.XPATH, './/button[text()="Посмотреть статус"]'
