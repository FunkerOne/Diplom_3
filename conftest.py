import pytest
from selenium import webdriver


@pytest.fixture(scope="function", params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'chrome':
        driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")
    yield driver
    driver.quit()
