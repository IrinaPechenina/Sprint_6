import allure
import data


class TestSwitchPage:

    @allure.title('Проверяем переход по клику на логотип «Самоката», переход на главную страницу «Самоката»')
    def test_switch_to_yandex_page(self, switch_page):
        switch_page.get_url(data.MAIN_PAGE_URL)
        switch_page.click_on_ya_logo()
        result = switch_page.find_search_button()
        assert result == data.expected_result_yandex_logo

    @allure.title('Проверяем переход по клику на логотип Яндекс, в новом окне через редирект откроется главная '
                  'страница Дзена')
    def test_switch_to_scooter_page(self, switch_page):
        switch_page.get_url(data.NO_SUCH_ORDER_URL)
        switch_page.click_on_scooter_logo()
        result = switch_page.find_scooter_text()
        assert result == data.expected_result_scooter_logo
