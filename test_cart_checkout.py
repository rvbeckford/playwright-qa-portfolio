from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_happy_path(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.add_to_cart("sauce-labs-bike-light")
    inventory_page.expect_cart_count(2)
    inventory_page.go_to_cart()
    cart_page.checkout()
    checkout_page.fill_info("Test", "User", "12345")
    checkout_page.continue_checkout()
    checkout_page.finish_order()
    checkout_page.expect_order_complete()


def test_sort_price_low_to_high(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.sort_low_to_high()
    inventory_page.expect_first_item("Sauce Labs Onesie", "$7.99")


def test_remove_item_drops_badge(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.add_to_cart("sauce-labs-bike-light")
    inventory_page.go_to_cart()
    cart_page.remove_item("sauce-labs-backpack")
    cart_page.expect_cart_count(1)
