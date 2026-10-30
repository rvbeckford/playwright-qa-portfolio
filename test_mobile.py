import pytest
from playwright.sync_api import Playwright, expect


@pytest.mark.mobile
@pytest.mark.parametrize("device_name", ["Pixel 7", "iPhone 14"])
def test_mobile_login(playwright: Playwright, device_name: str):
    device = playwright.devices[device_name]
    browser = playwright.chromium.launch()
    context = browser.new_context(**device)
    page = context.new_page()
    try:
        page.goto("https://www.saucedemo.com/")
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.get_by_role("button", name="Login").click()
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        # Both devices are narrow phones, not a desktop viewport
        assert page.viewport_size["width"] < 500
    finally:
        context.close()
        browser.close()
