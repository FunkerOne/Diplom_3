import allure
import random
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик по кнопке «Конструктор»")
    def click_on_constructor_button(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("В разделе 'Соберите бургер'")
    def check_navigate_to_make_burger(self):
        self.element_is_visible(MainPageLocators.MAKE_BURGER_TEXT)
        return self.get_text_from_element(MainPageLocators.MAKE_BURGER_TEXT)

    @allure.step("Клик по кнопке «Лента заказов»")
    def click_on_feed_order_button(self):
        self.click_on_element(MainPageLocators.FEED_LIST_BUTTON)

    @allure.step("В разделе 'Лента заказов'")
    def check_navigate_to_feed(self):
        self.element_is_visible(MainPageLocators.FEED_ORDER_TEXT)
        return self.get_text_from_element(MainPageLocators.FEED_ORDER_TEXT)

    @allure.step("Клик на произвольный ингредиент")
    def click_on_random_ingredient(self):
        random.choice(self.driver.find_elements(*MainPageLocators.LIST_OF_INGREDIENTS)).click()

    @allure.step("Показ модального окна с деталями ингредиента")
    def show_ingredient_modal_window(self):
        self.element_is_visible(MainPageLocators.MODAL_WINDOW_INGREDIENT)
        return self.get_text_from_element(MainPageLocators.MODAL_WINDOW_INGREDIENT)

    @allure.step("Клик по кнопке закрыть в модальном окне")
    def close_modal_window(self):
        self.click_on_element(MainPageLocators.CLOSE_MODAL_WINDOW_BUTTON)

    @allure.step("Модальное окно не представлено")
    def modal_window_is_invisible(self):
        self.element_is_invisibility(MainPageLocators.MODAL_WINDOW_INGREDIENT)

    @allure.step("Модальное окно не отображается")
    def modal_window_is_not_displayed(self):
        return self.element_is_presence(MainPageLocators.MODAL_WINDOW_INGREDIENT).is_displayed()

    @allure.step("Получить значение счётчика ингредиента")
    def get_counter_value(self):
        return self.get_text_from_element(MainPageLocators.SECOND_INGREDIENT_COUNT)

    @allure.step("Добавить ингредиент в корзину")
    def add_ingredient_to_card(self):
        self.element_is_clickable(MainPageLocators.SECOND_INGREDIENT)
        self.drag_and_drop(MainPageLocators.SECOND_INGREDIENT, MainPageLocators.ORDER_BASKET)

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_on_create_order_button(self):
        self.click_on_element(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step("Показ модального окна об оформлении заказа")
    def show_order_created_modal_window(self):
        self.element_is_visible(MainPageLocators.MODAL_WINDOW_ORDER_CREATED)
        return self.get_text_from_element(MainPageLocators.MODAL_WINDOW_ORDER_CREATED)

    @allure.step("Получить номер заказа из модального окна")
    def get_order_number_from_created_modal_window(self):
        self.element_is_visible(MainPageLocators.MODAL_WINDOW_ORDER_CREATED)
        order_id_before_format = self.get_text_from_element(MainPageLocators.ORDER_ID_IN_MODAL_WINDOW)
        while order_id_before_format == '9999':
            order_id_before_format = self.get_text_from_element(MainPageLocators.ORDER_ID_IN_MODAL_WINDOW)
            order_id_after_format = f'0{order_id_before_format}'
        return order_id_after_format

    @allure.step("Клик по кнопке закрыть в модальном окне создания заказа")
    def close_create_order_modal_window(self):
        self.element_is_visible(MainPageLocators.CLOSE_ORDER_CREATE_MODAL_WINDOW)
        self.click_on_element(MainPageLocators.CLOSE_ORDER_CREATE_MODAL_WINDOW)
