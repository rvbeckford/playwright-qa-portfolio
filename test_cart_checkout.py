import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.smoke
def test_checkout_happy_path(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_page = CheckoutPage(logged_in_page)
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.add_to_cart("sauce-labs-bike-light")
    inventory_page.expect_cart_count(2)
    inventory_page.go_to_cart()
    cart_page.checkout()
    checkout_page.fill_info("Test", "User", "12345")
    checkout_page.continue_checkout()
    checkout_page.finish_order()
    checkout_page.expect_order_complete()


@pytest.mark.regression
def test_sort_price_low_to_high(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.sort_low_to_high()
    inventory_page.expect_first_item("Sauce Labs Onesie", "$7.99")


@pytest.mark.regression
def test_remove_item_drops_badge(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.add_to_cart("sauce-labs-bike-light")
    inventory_page.go_to_cart()
    cart_page.remove_item("sauce-labs-backpack")
    cart_page.expect_cart_count(1)
