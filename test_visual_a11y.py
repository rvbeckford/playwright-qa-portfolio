import pytest
from playwright.sync_api import Page
from axe_playwright_python.sync_playwright import Axe


@pytest.mark.visual
def test_login_page_visual(page: Page, assert_snapshot):
    page.goto("https://www.saucedemo.com/")
    assert_snapshot(page)


@pytest.mark.regression
def test_login_page_accessibility(page: Page):
    page.goto("https://www.saucedemo.com/")
    results = Axe().run(page)

    # SauceDemo is a demo site we don't own: it has 2 known moderate
    # best-practice findings (no <h1>, logo outside a landmark).
    # Gate on critical/serious only, so a real barrier still fails the suite.
    blocking = [
        v for v in results.response["violations"]
        if v["impact"] in ("critical", "serious")
    ]
    if results.violations_count:
        print(f"\nAxe violations found: {results.violations_count} (moderate only, not blocking)")
    assert not blocking, results.generate_report()
