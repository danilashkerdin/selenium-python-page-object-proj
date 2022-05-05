from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def should_be_promo_link(self):
        assert "promo=newYear" in self.browser.current_url, "Not promo url"

    def should_be_add_to_cart_button(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON), "No add to cart button"

    def should_be_in_cart(self):
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        alert_inner_title = self.browser.find_element(*ProductPageLocators.ALERT_INNER_TITLE).text
        assert product_title == alert_inner_title, f"Alert title which is '{alert_inner_title}' not equals to product title which is: '{product_title}'"

    def should_be_equal_price(self):
        product_price = str(self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text)

        cart_price = ""
        if self.browser.get_window_size()['width'] >= 768:
            cart_price = str(self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_BIG_SCREEN_LOCATOR).text)
        else:
            cart_price = str(self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_SMALL_SCREEN_LOCATOR).text)
        cart_price = cart_price.split(': ')[-1].split("\n")[0]
        assert cart_price == product_price, f"Price in cart '{cart_price}' not equal to product price '{product_price}'"

        alert_inner_price = str(self.browser.find_element(*ProductPageLocators.ALERT_INNER_PRICE).text)
        assert alert_inner_price == product_price, f"Price in alert '{alert_inner_price}' not equal to product price '{product_price}'"
