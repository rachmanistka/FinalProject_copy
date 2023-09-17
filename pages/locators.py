from selenium.webdriver.common.by import By



class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    TITLE_IN_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    REAL_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    COST_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    REAL_COST = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner ")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
