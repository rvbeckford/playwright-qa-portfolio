from playwright.sync_api import Page, expect


def login(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()


def test_checkout_happy_path(page: Page):
    login(page)
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    page.locator("[data-test='add-to-cart-sauce-labs-bike-light']").click()
    expect(page.locator("[data-test='shopping-cart-badge']")).to_have_text("2")
    page.locator("[data-test='shopping-cart-link']").click()
    page.locator("[data-test='checkout']").click()
    page.locator("[data-test='firstName']").fill("Test")
    page.locator("[data-test='lastName']").fill("User")
    page.locator("[data-test='postalCode']").fill("12345")
    page.locator("[data-test='continue']").click()
    page.locator("[data-test='finish']").click()
    expect(page.locator("[data-test='complete-header']")).to_have_text(
        "Thank you for your order!"
    )


def test_sort_price_low_to_high(page: Page):
    login(page)
    page.locator("[data-test='product-sort-container']").select_option("lohi")
    expect(page.locator("[data-test='inventory-item-name']").first).to_have_text(
        "Sauce Labs Onesie"
    )
    expect(page.locator("[data-test='inventory-item-price']").first).to_have_text(
        "$7.99"
    )


def test_remove_item_drops_badge(page: Page):
    login(page)
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    page.locator("[data-test='add-to-cart-sauce-labs-bike-light']").click()
    page.locator("[data-test='shopping-cart-link']").click()
    page.locator("[data-test='remove-sauce-labs-backpack']").click()
    expect(page.locator("[data-test='shopping-cart-badge']")).to_have_text("1")
