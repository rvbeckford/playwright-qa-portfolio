import pytest
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def logged_in_page(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    return page
