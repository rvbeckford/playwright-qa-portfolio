from playwright.sync_api import Page, expect


def test_successful_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_locked_out_user(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("locked_out_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page.locator("[data-test='error']")).to_have_text(
        "Epic sadface: Sorry, this user has been locked out."
    )


def test_wrong_password(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("wrong_password")
    page.get_by_role("button", name="Login").click()
    expect(page.locator("[data-test='error']")).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )


def test_empty_username(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page.locator("[data-test='error']")).to_have_text(
        "Epic sadface: Username is required"
    )
