import pytest
from playwright.sync_api import Page, expect


@pytest.mark.smoke
def test_successful_login(login_page, page: Page):
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


@pytest.mark.regression
@pytest.mark.parametrize(
    "username,password,error",
    [
        (
            "locked_out_user",
            "secret_sauce",
            "Epic sadface: Sorry, this user has been locked out.",
        ),
        (
            "standard_user",
            "wrong_password",
            "Epic sadface: Username and password do not match any user in this service",
        ),
        ("", "secret_sauce", "Epic sadface: Username is required"),
    ],
)
def test_login_failures(login_page, username, password, error):
    login_page.goto()
    login_page.login(username, password)
    login_page.expect_error(error)
