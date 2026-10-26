from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_successful_login(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_locked_out_user(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("locked_out_user", "secret_sauce")
    login_page.expect_error("Epic sadface: Sorry, this user has been locked out.")


def test_wrong_password(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "wrong_password")
    login_page.expect_error(
        "Epic sadface: Username and password do not match any user in this service"
    )


def test_empty_username(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("", "secret_sauce")
    login_page.expect_error("Epic sadface: Username is required")
