from selenium.webdriver.common.by import By


class AccountPageLocators:
    ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    PROFILE_LINK = (By.XPATH, "//a[@href='/account/profile']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[@href='/account/order-history']")
    LIST_OF_ORDERS_IN_PROFILE = (By.XPATH, "//p[@class='text text_type_digits-default']")
    LOG_OUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    LOG_IN_TEXT = (By.XPATH, "//h2[text()='Вход']")
