from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    PASSWORD_RECOVERY_LINK = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
    PASSWORD_RECOVERY_FORM_TEXT = (By.XPATH, "//h2[contains(text(),'Восстановление пароля')]")
    EMAIL_FIELD = (By.XPATH, "//div/input[@class='text input__textfield text_type_main-default']")
    RECOVERY_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    SHOW_HIDE_PASSWORD = (By.XPATH, "//div[@class='input__icon input__icon-action']")
    ACTIVE_PASSWORD_FIELD = (By.XPATH, "//div[contains(@class,'input_status_active')]")
