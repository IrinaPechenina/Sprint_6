import pytest
import allure
from locators.main_page_locators import MainPageLocators


class TestOrderPage:
    @allure.title('Проверка заказа самоката')
    @pytest.mark.parametrize(
        'button, date, comment',
        [
            [MainPageLocators.ORDER_BUTTON_HEADER, '29.07.2024', 'Стучите трижды'],
            [MainPageLocators.ORDER_BUTTON_FOOTER, '01.08.2024', 'Предварительно позвоните'],
        ]
    )
    def test_scooter_order(self, main_page, order_page, button, date, comment):
        main_page.click_on_cookie_confirm_button()
        order_page.click_on_order_button(button)
        order_page.set_personal_info()
        order_page.click_on_further_button()
        order_page.set_order_info(date, comment)
        order_page.click_on_order_approval_buttons()
        assert order_page.confirmation_order_is_done()
