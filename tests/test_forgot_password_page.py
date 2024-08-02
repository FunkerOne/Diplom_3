import allure
from data import LoginData
from pages.forgot_password_page import ForgotPasswordPage


@allure.suite("Восстановление пароля")
class TestForgotPasswordPage:

    @allure.title("Осуществляется переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_navigate_to_recovery_page(self, driver):
        recovery_page = ForgotPasswordPage(driver)
        recovery_page.click_on_password_reset_link()
        result = recovery_page.check_navigate_to_recovery_page()
        assert "Восстановление пароля" in result

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_fill_email_and_click_on_recovery_btn(self, driver):
        recovery_page = ForgotPasswordPage(driver)
        recovery_page.click_on_password_reset_link()
        recovery_page.fill_email_field(LoginData.USER[0])
        recovery_page.click_on_recovery_button()
        result = recovery_page.check_navigate_to_recovery_page()
        assert "Восстановление пароля" in result

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_field_is_active(self, driver):
        recovery_page = ForgotPasswordPage(driver)
        recovery_page.click_on_password_reset_link()
        recovery_page.fill_email_field(LoginData.USER[0])
        recovery_page.click_on_recovery_button()
        recovery_page.find_show_hide_button()
        recovery_page.click_on_show_hide_button()
        assert recovery_page.find_active_password_field()
