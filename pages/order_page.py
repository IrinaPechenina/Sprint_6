
import allure

import data
import helpers
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Кликаем на кнопку заказать, параметризация - кнопка заказа в футере и разделе "Как это работает"')
    def click_on_order_button(self, button):
        self.click_on_element(button)

    @allure.step('Заполняем поле Имя')
    def set_name(self):
        name = helpers.generate_name()
        self.set_text_to_element(OrderPageLocators.INPUT_NAME, name)

    @allure.step('Заполняем поле Фамилия')
    def set_surname(self):
        surname = helpers.generate_surname()
        self.set_text_to_element(OrderPageLocators.INPUT_SURNAME, surname)

    @allure.step('Заполняем поле Адрес')
    def set_address(self):
        address = helpers.generate_address()
        self.set_text_to_element(OrderPageLocators.INPUT_ADDRESS, address)

    @allure.step('Заполняем поле Телефон')
    def set_phone_number(self):
        phone = helpers.generate_phone_number()
        self.set_text_to_element(OrderPageLocators.INPUT_PHONE_NUMBER, phone)

    @allure.step('Клик на саджест метро')
    def click_on_metro_station_suggest(self):
        self.click_on_element(OrderPageLocators.INPUT_METRO_STATION)

    @allure.step('Выбираем станцию метро')
    def select_metro_station(self):
        metro_name = helpers.generate_metro_station_name()
        locator = self.format_locator(OrderPageLocators.METRO_STATION, metro_name)
        self.click_on_element(locator)

    @allure.step('Заполняем поля персональных данных: Имя, Фамилия, Адрес, Метро, Телефон')
    def set_personal_info(self):
        self.set_name()
        self.set_surname()
        self.set_address()
        self.set_phone_number()
        self.click_on_metro_station_suggest()
        self.select_metro_station()

    @allure.step('Кликаем на кнопку Далее')
    def click_on_further_button(self):
        self.click_on_element(OrderPageLocators.FURTHER_BUTTON)

    @allure.step('Заполняем поле Когда привезти самокат')
    def set_date(self, date):
        self.set_text_to_element(OrderPageLocators.INPUT_DATE, date)

    @allure.step('Выбираем срок аренды')
    def select_rental_period(self):
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD_POPUP)
        days = helpers.generate_rental_period_days()
        locator = self.format_locator(OrderPageLocators.RENTAL_PERIOD_SELECT, days)
        self.click_on_element(locator)

    @allure.step('Выбираем цвет самоката')  # добавить параметризацию в тестах
    def select_scooter_color(self):
        color = helpers.generate_scooter_color()
        locator = self.format_locator(OrderPageLocators.INPUT_SCOOTER_COLOR, color)
        self.click_on_element(locator)

    @allure.step('Заполняем поле Комментарий для курьера')
    def set_comment(self, comment):
        self.set_text_to_element(OrderPageLocators.INPUT_COMMENT, comment)

    @allure.step('Заполняем поля заказа: дата доставки, срок доставки, цвет самоката, комментарий курьеру')
    def set_order_info(self, date, comment):
        self.select_rental_period()
        self.select_scooter_color()
        self.set_comment(comment)
        self.set_date(date)

    @allure.step('Кликаем на кнопку Заказать и подтверждаем заказ')  # добавить параметризацию в тестах
    def click_on_order_approval_buttons(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON_MIDDLE)
        self.click_on_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Проверяем, что заказ создан успешно -всплывающее окно содержит кнопку с текстом "Посмотреть статус"')
    def confirmation_order_is_done(self):
        result = self.get_text_from_element(OrderPageLocators.ORDER_STATUS_BUTTON)
        return result == data.expected_result_order_is_done
