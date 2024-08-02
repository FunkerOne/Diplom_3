import allure
from data import LoginData
from pages.account_page import AccountPage


@allure.suite("Личный кабинет")
class TestAccountPage:

    @allure.title("Осуществляется переход в ЛК по клику на кнопку «Личный кабинет»")
    def test_navigate_to_account_page(self, driver):
        page = AccountPage(driver)
        page.log_in(*LoginData.USER)
        page.click_on_account_button()
        result = page.check_navigate_to_account_page()
        assert 'Профиль' in result

    @allure.title("Осуществляется переход в раздел «История заказов»")
    def test_navigate_to_order_history_page(self, driver):
        page = AccountPage(driver)
        page.log_in(*LoginData.USER)
        page.click_on_account_button()
        page.click_on_order_history_button()
        result = page.check_navigate_to_order_history_page()
        assert 'История заказов' in result

    @allure.title("Выход из аккаунта")
    def test_log_out(self, driver):
        page = AccountPage(driver)
        page.log_in(*LoginData.USER)
        page.click_on_account_button()
        page.log_out()
        result = page.check_navigate_to_login_page()
        assert 'Вход' in result
