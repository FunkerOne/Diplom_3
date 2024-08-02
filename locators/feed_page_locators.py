from selenium.webdriver.common.by import By


class FeedPageLocators:
    LIST_OF_ORDERS = (By.XPATH, "//p[@class='text text_type_digits-default']")
    MODAL_WINDOW_ORDER = (By.XPATH, "//p[text()='Cостав']")
    ORDER_TOTAL = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    ORDER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDER_IN_PROGRESS = (By.XPATH, "//ul[contains(@class,'orderListReady')]/li[contains(@class,'text_type_digits')]")
