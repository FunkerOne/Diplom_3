import allure
from data import LoginData
from pages.main_page import MainPage


@allure.suite("Проверка основного функционала")
class TestMainPage:

    @allure.title("Осуществляется переход в «Конструктор»")
    def test_navigate_to_constructor(self, driver):
        page = MainPage(driver)
        page.click_on_constructor_button()
        result = page.check_navigate_to_make_burger()
        assert 'Соберите бургер' in result

    @allure.title("Осуществляется переход в ленту заказов")
    def test_navigate_to_feed(self, driver):
        page = MainPage(driver)
        page.click_on_feed_order_button()
        result = page.check_navigate_to_feed()
        assert 'Лента заказов' in result

    @allure.title("При клике на ингредиент - появится всплывающее окно с деталями")
    def test_show_ingredient_modal_window(self, driver):
        page = MainPage(driver)
        page.click_on_constructor_button()
        page.click_on_random_ingredient()
        result = page.show_ingredient_modal_window()
        assert 'Детали ингредиента' in result

    @allure.title("При клике на 'крест' - всплывающее окно закрывается")
    def test_close_ingredient_modal_window(self, driver):
        page = MainPage(driver)
        page.click_on_constructor_button()
        page.click_on_random_ingredient()
        page.close_modal_window()
        page.modal_window_is_invisible()
        result = page.modal_window_is_not_displayed()
        assert result is False

    @allure.title("При добавлении ингредиента в заказ - увеличивается каунтер данного ингредиента")
    def test_increase_ingredient_counter_value(self, driver):
        page = MainPage(driver)
        page.click_on_constructor_button()
        initial_value = page.get_counter_value()
        page.add_ingredient_to_card()
        actual_value = page.get_counter_value()
        assert actual_value > initial_value

    @allure.title("Авторизованный пользователь может оформить заказ")
    def test_create_order(self, driver):
        page = MainPage(driver)
        page.log_in(*LoginData.USER)
        page.click_on_constructor_button()
        page.add_ingredient_to_card()
        page.click_on_create_order_button()
        result = page.show_order_created_modal_window()
        assert 'Ваш заказ начали готовить' in result
