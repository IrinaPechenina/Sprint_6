import allure
import pytest
import data


class TestMainPage:
    @allure.title('Проверка раздела "Вопросы о важном" - при клике на вопрос открывается оответствующий текст ответа')
    @pytest.mark.parametrize(
        'q_num, expected_result',
        [
            (0, data.RESPONSE_Q1),
            (1, data.RESPONSE_Q2),
            (2, data.RESPONSE_Q3),
            (3, data.RESPONSE_Q4),
            (4, data.RESPONSE_Q5),
            (5, data.RESPONSE_Q6),
            (6, data.RESPONSE_Q7),
            (7, data.RESPONSE_Q8)
        ]
    )
    def test_questions(self, main_page, q_num, expected_result):
        main_page.click_on_cookie_confirm_button()
        result = main_page.click_on_question_and_get_text_from_response(q_num)
        assert expected_result == result
