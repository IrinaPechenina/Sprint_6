import allure
from locators.switch_page_locators import SwitchPageLocators
from pages.base_page import BasePage


class SwitchPage(BasePage):

    @allure.step('Кликаем на логотип Яндекса')
    def click_on_ya_logo(self):
        self.click_on_element(SwitchPageLocators.YANDEX_LOGO)

    @allure.step('На странице ЯндексДзен производим поиск кнопки "Найти"')
    def find_search_button(self):
        self.switch_to_another_window()
        self.find_element_with_wait(SwitchPageLocators.SEARCH_BUTTON)
        return self.get_text_from_element(SwitchPageLocators.SEARCH_BUTTON)

    @allure.step('Кликаем на логотип Самоката')
    def click_on_scooter_logo(self):
        self.click_on_element(SwitchPageLocators.SCOOTER_LOGO)

    @allure.step('На главной странице Самоката ищем текст использования куки')
    def find_scooter_text(self):
        self.find_element_with_wait(SwitchPageLocators.SCOOTER_TEXT)
        return self.get_text_from_element(SwitchPageLocators.SCOOTER_TEXT)
