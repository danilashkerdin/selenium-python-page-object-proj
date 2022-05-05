from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    TOTAL_PRICE_BIG_SCREEN_LOCATOR = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs")
    TOTAL_PRICE_SMALL_SCREEN_LOCATOR = (By.CSS_SELECTOR, ".btn.btn-default.navbar-btn.btn-cart.navbar-right.visible-xs-inline-block")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ALERT_INNER_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    ALERT_INNER_TITLE = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "#content_inner h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
