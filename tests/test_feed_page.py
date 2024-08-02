import allure
from data import LoginData
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.account_page import AccountPage


@allure.suite("Раздел «Лента заказов»")
class TestFeedPage:

    @allure.title("При клике на заказ - появится всплывающее окно с деталями")
    def test_show_order_modal_window(self, driver):
        page = MainPage(driver)
        page.click_on_feed_order_button()
        page.check_navigate_to_feed()
        feed_page = FeedPage(driver)
        feed_page.click_on_random_order()
        result = feed_page.show_order_modal_window()
        assert result is True

    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_find_user_order_in_feed_order(self, driver):
        page = MainPage(driver)
        page.log_in(*LoginData.USER)
        page.add_ingredient_to_card()
        page.click_on_create_order_button()
        page.show_order_created_modal_window()
        order_id = page.get_order_number_from_created_modal_window()
        page.close_create_order_modal_window()
        account_page = AccountPage(driver)
        account_page.click_on_account_button()
        account_page.click_on_order_history_button()
        order_id_from_profile = account_page.get_order_number_from_profile()
        assert order_id in order_id_from_profile

    @allure.title("При создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_get_total_order_counter_value(self, driver):
        page = MainPage(driver)
        page.log_in(*LoginData.USER)
        page.click_on_feed_order_button()
        page.check_navigate_to_feed()
        feed_page = FeedPage(driver)
        initial_value = feed_page.get_total_order_counter_value()
        page.click_on_constructor_button()
        page.check_navigate_to_make_burger()
        page.add_ingredient_to_card()
        page.click_on_create_order_button()
        page.get_order_number_from_created_modal_window()
        page.close_create_order_modal_window()
        page.click_on_feed_order_button()
        page.check_navigate_to_feed()
        actual_value = feed_page.get_total_order_counter_value()
        assert actual_value > initial_value

    @allure.title("При создании нового заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_get_today_order_counter_value(self, driver):
        page = MainPage(driver)
        page.log_in(*LoginData.USER)
        page.click_on_feed_order_button()
        page.check_navigate_to_feed()
        feed_page = FeedPage(driver)
        initial_value = feed_page.get_today_order_counter_value()
        page.click_on_constructor_button()
        page.check_navigate_to_make_burger()
        page.add_ingredient_to_card()
        page.click_on_create_order_button()
        page.get_order_number_from_created_modal_window()
        page.close_create_order_modal_window()
        page.click_on_feed_order_button()
        page.check_navigate_to_feed()
        actual_value = feed_page.get_today_order_counter_value()
        assert actual_value > initial_value

    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_get_order_number_in_progress(self, driver):
        page = MainPage(driver)
        page.log_in(*LoginData.USER)
        page.add_ingredient_to_card()
        page.click_on_create_order_button()
        order_id = page.get_order_number_from_created_modal_window()
        page.close_create_order_modal_window()
        page.click_on_feed_order_button()
        page.check_navigate_to_feed()
        feed_page = FeedPage(driver)
        order_id_in_progress = feed_page.get_order_number_in_progress()
        assert order_id_in_progress == order_id
