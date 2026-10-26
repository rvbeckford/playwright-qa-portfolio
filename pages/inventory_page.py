from playwright.sync_api import Page, expect


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.first_item_name = page.locator("[data-test='inventory-item-name']").first
        self.first_item_price = page.locator("[data-test='inventory-item-price']").first

    def add_to_cart(self, product_slug):
        self.page.locator(f"[data-test='add-to-cart-{product_slug}']").click()

    def go_to_cart(self):
        self.cart_link.click()

    def sort_low_to_high(self):
        self.sort_dropdown.select_option("lohi")

    def expect_cart_count(self, count):
        expect(self.cart_badge).to_have_text(str(count))

    def expect_first_item(self, name, price):
        expect(self.first_item_name).to_have_text(name)
        expect(self.first_item_price).to_have_text(price)
