import allure
from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик по кнопке 'Личный кабинет'")
    def click_on_account_button(self):
        self.click_on_element(AccountPageLocators.ACCOUNT_BUTTON)

    @allure.step("В разделе 'Профиль'")
    def check_navigate_to_account_page(self):
        self.element_is_visible(AccountPageLocators.PROFILE_LINK)
        return self.get_text_from_element(AccountPageLocators.PROFILE_LINK)

    @allure.step("Клик по ссылке 'История заказов'")
    def click_on_order_history_button(self):
        self.element_is_visible(AccountPageLocators.ORDER_HISTORY_LINK)
        self.click_on_element(AccountPageLocators.ORDER_HISTORY_LINK)

    @allure.step("В разделе 'История заказов'")
    def check_navigate_to_order_history_page(self):
        return self.get_text_from_element(AccountPageLocators.ORDER_HISTORY_LINK)

    @allure.step("Получить номер заказа из профиля")
    def get_order_number_from_profile(self):
        self.all_elements_is_presence(AccountPageLocators.LIST_OF_ORDERS_IN_PROFILE)
        return self.get_text_from_element(AccountPageLocators.LIST_OF_ORDERS_IN_PROFILE)

    @allure.step("Клик по кнопке 'Выход'")
    def log_out(self):
        self.element_is_visible(AccountPageLocators.LOG_OUT_BUTTON)
        self.click_on_element(AccountPageLocators.LOG_OUT_BUTTON)

    @allure.step("На странице авторизации")
    def check_navigate_to_login_page(self):
        self.element_is_visible(AccountPageLocators.LOG_IN_TEXT)
        return self.get_text_from_element(AccountPageLocators.LOG_IN_TEXT)
