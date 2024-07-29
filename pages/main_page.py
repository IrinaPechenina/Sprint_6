import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Соглашаемся на использование куки')
    def click_on_cookie_confirm_button(self):
        self.click_on_element(MainPageLocators.COOKIE_CONFIRM_BUTTON)

    @allure.step('Кликаем на вопрос')
    def click_on_question(self, num):
        formatting_q_locator = self.format_locator(MainPageLocators.QUESTION_LOCATOR, num)
        self.click_on_element(formatting_q_locator)

    @allure.step('Получаем текст ответа на вопрос')
    def get_text_from_response(self, num):
        formatting_r_locator = self.format_locator(MainPageLocators.RESPONSE_LOCATOR, num)
        return self.get_text_from_element(formatting_r_locator)

    @allure.step('Кликаем на вопрос и получаем текст ответа')
    def click_on_question_and_get_text_from_response(self, num):
        self.click_on_question(num)
        return self.get_text_from_response(num)
