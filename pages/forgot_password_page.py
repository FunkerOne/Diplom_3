import allure
from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик по ссылке 'Восстановить пароль'")
    def click_on_password_reset_link(self):
        self.click_on_element(ForgotPasswordPageLocators.PASSWORD_RECOVERY_LINK)

    @allure.step("На странице 'Восстановление пароля'")
    def check_navigate_to_recovery_page(self):
        return self.get_text_from_element(ForgotPasswordPageLocators.PASSWORD_RECOVERY_FORM_TEXT)

    @allure.step("Заполнить поле email")
    def fill_email_field(self, email):
        self.paste_text_into_element(ForgotPasswordPageLocators.EMAIL_FIELD, email)

    @allure.step("Клик по кнопке 'Восстановить'")
    def click_on_recovery_button(self):
        self.click_on_element(ForgotPasswordPageLocators.RECOVERY_BUTTON)

    @allure.step("Локализовать кнопку показать/скрыть пароль")
    def find_show_hide_button(self):
        self.element_is_visible(ForgotPasswordPageLocators.SHOW_HIDE_PASSWORD)

    @allure.step("Клик по кнопке показать/скрыть пароль")
    def click_on_show_hide_button(self):
        self.click_on_element(ForgotPasswordPageLocators.SHOW_HIDE_PASSWORD)

    @allure.step("Локализовать активное поле 'Пароль'")
    def find_active_password_field(self):
        return self.element_is_visible(ForgotPasswordPageLocators.ACTIVE_PASSWORD_FIELD)
