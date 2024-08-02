import allure
from data import LoginData
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:

    _EMAIL_FIELD = (By.XPATH, "//input[@type='text' and @name='name']")
    _PASSWORD_FIELD = (By.XPATH, "//input[@type='password' and @name='Пароль']")
    _LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Кликаем по элементу")
    def click_on_element(self, element):
        self.driver.find_element(*element).click()

    @allure.step("Получить текст из элемента")
    def get_text_from_element(self, element):
        return self.driver.find_element(*element).text

    @allure.step("Вставить текст")
    def paste_text_into_element(self, element, text):
        self.driver.find_element(*element).send_keys(text)

    @allure.step("Элемент видимый")
    def element_is_visible(self, element):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(element))

    @allure.step("Элемент отсутствует")
    def element_is_invisibility(self, element):
        return WebDriverWait(self.driver, 3).until(ec.invisibility_of_element_located(element))

    @allure.step("Элемент представлен")
    def element_is_presence(self, element):
        WebDriverWait(self.driver, 3).until(ec.presence_of_element_located(element))
        return self.driver.find_element(*element)

    @allure.step("Элемент кликабельный")
    def element_is_clickable(self, element):
        WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable(element))

    @allure.step("Представлены все элементы")
    def all_elements_is_presence(self, element):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located(element))

    @allure.step("Перетаскивание ингредиента в корзину")
    def drag_and_drop(self, element_first, element_second):
        draggable = self.driver.find_element(*element_first)
        droppable = self.driver.find_element(*element_second)
        ActionChains(self.driver).drag_and_drop(draggable, droppable).perform()

    @allure.step("Авторизация пользователя")
    def log_in(self, email, password):
        self.driver.find_element(*self._EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*self._PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*self._LOGIN_BUTTON).click()
