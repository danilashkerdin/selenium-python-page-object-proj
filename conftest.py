import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def config_chrome(language):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    return browser


def config_firefox(language):
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", language)
    browser = webdriver.Firefox(firefox_profile=fp)
    return browser


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")


@pytest.fixture(scope="class")
def browser(request):
    browser = None
    browser_name = request.config.getoption("browser")
    language = request.config.getoption("language")
    if browser_name.lower() == "chrome":
        browser = config_chrome(language)
    elif browser_name.lower() == "firefox":
        browser = config_firefox(language)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()


@pytest.fixture(autouse=True)
def wait():
    time.sleep(0.2)
