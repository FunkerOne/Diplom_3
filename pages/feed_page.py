import allure
import random
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик на произвольный заказ")
    def click_on_random_order(self):
        random.choice(self.driver.find_elements(*FeedPageLocators.LIST_OF_ORDERS)).click()

    @allure.step("Показ модального окна с заказом")
    def show_order_modal_window(self):
        return self.element_is_presence(FeedPageLocators.MODAL_WINDOW_ORDER).is_displayed()

    @allure.step("Получить значение счётчика 'Выполнено за всё время'")
    def get_total_order_counter_value(self):
        return self.get_text_from_element(FeedPageLocators.ORDER_TOTAL)

    @allure.step("Получить значение счётчика 'Выполнено за сегодня'")
    def get_today_order_counter_value(self):
        return self.get_text_from_element(FeedPageLocators.ORDER_TODAY)

    @allure.step("Получить номер заказа из раздела 'В работе'")
    def get_order_number_in_progress(self):
        self.element_is_visible(FeedPageLocators.ORDER_IN_PROGRESS)
        return self.get_text_from_element(FeedPageLocators.ORDER_IN_PROGRESS)
