import pytest
from playwright.sync_api import Page, expect

BASE = "https://the-internet.herokuapp.com"


@pytest.mark.regression
def test_js_alert_accept(page: Page):
    page.goto(f"{BASE}/javascript_alerts")
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Click for JS Alert").click()
    expect(page.locator("#result")).to_have_text(
        "You successfully clicked an alert"
    )


@pytest.mark.regression
def test_js_confirm_accept(page: Page):
    page.goto(f"{BASE}/javascript_alerts")
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Click for JS Confirm").click()
    expect(page.locator("#result")).to_have_text("You clicked: Ok")


@pytest.mark.regression
def test_js_confirm_dismiss(page: Page):
    page.goto(f"{BASE}/javascript_alerts")
    page.on("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Click for JS Confirm").click()
    expect(page.locator("#result")).to_have_text("You clicked: Cancel")


@pytest.mark.regression
def test_js_prompt(page: Page):
    page.goto(f"{BASE}/javascript_alerts")
    page.on("dialog", lambda dialog: dialog.accept("Hello Playwright"))
    page.get_by_role("button", name="Click for JS Prompt").click()
    expect(page.locator("#result")).to_have_text(
        "You entered: Hello Playwright"
    )


@pytest.mark.regression
def test_dropdown_selection(page: Page):
    page.goto(f"{BASE}/dropdown")
    page.locator("#dropdown").select_option("2")
    expect(page.locator("#dropdown")).to_have_value("2")


@pytest.mark.regression
def test_checkboxes(page: Page):
    page.goto(f"{BASE}/checkboxes")
    checkboxes = page.locator("input[type='checkbox']")
    checkboxes.nth(0).check()
    expect(checkboxes.nth(0)).to_be_checked()
    checkboxes.nth(1).uncheck()
    expect(checkboxes.nth(1)).not_to_be_checked()


@pytest.mark.regression
def test_file_upload(page: Page, tmp_path):
    sample = tmp_path / "sample.txt"
    sample.write_text("Hello from Playwright")
    page.goto(f"{BASE}/upload")
    page.locator("#file-upload").set_input_files(str(sample))
    page.locator("#file-submit").click()
    expect(page.locator("#uploaded-files")).to_have_text("sample.txt")


@pytest.mark.regression
def test_add_remove_elements(page: Page):
    page.goto(f"{BASE}/add_remove_elements/")
    page.get_by_role("button", name="Add Element").click()
    delete_button = page.get_by_role("button", name="Delete")
    expect(delete_button).to_be_visible()
    delete_button.click()
    expect(delete_button).to_have_count(0)


@pytest.mark.regression
def test_dynamic_loading(page: Page):
    page.goto(f"{BASE}/dynamic_loading/1")
    page.get_by_role("button", name="Start").click()
    # No sleep here — expect() auto-waits for "Hello World!" to appear.
    expect(page.locator("#finish")).to_have_text("Hello World!")


@pytest.mark.regression
def test_hovers(page: Page):
    page.goto(f"{BASE}/hovers")
    figure = page.locator(".figure").first
    figure.hover()
    caption = figure.locator(".figcaption")
    expect(caption).to_be_visible()
    expect(caption).to_contain_text("user1")
