from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator("[data-test='checkout']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")

    def remove_item(self, product_slug):
        self.page.locator(f"[data-test='remove-{product_slug}']").click()

    def checkout(self):
        self.checkout_button.click()

    def expect_cart_count(self, count):
        expect(self.cart_badge).to_have_text(str(count))
