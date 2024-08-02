from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    MAKE_BURGER_TEXT = (By.XPATH, "//h1[text()='Соберите бургер']")
    FEED_LIST_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    FEED_ORDER_TEXT = (By.XPATH, "//h1[text()='Лента заказов']")
    LIST_OF_INGREDIENTS = (By.XPATH, "//a[contains(@class,'BurgerIngredient_ingredient')]")
    MODAL_WINDOW_INGREDIENT = (By.XPATH, "//h2[text()='Детали ингредиента']")
    CLOSE_MODAL_WINDOW_BUTTON = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")
    SECOND_INGREDIENT = (By.XPATH, "//p[text()='Краторная булка N-200i']")
    SECOND_INGREDIENT_COUNT = (By.XPATH, "//ul[1]/a[2]//p[contains(@class,'counter_counter__num')]")
    ORDER_BASKET = (By.XPATH, "//ul[contains(@class,'BurgerConstructor_basket')]")
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    MODAL_WINDOW_ORDER_CREATED = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")
    ORDER_ID_IN_MODAL_WINDOW = (By.XPATH, "//h2[contains(@class,'Modal_modal__title_shadow')]")
    CLOSE_ORDER_CREATE_MODAL_WINDOW = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
