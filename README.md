GITHUB.COM

Playwright Tests

](https://github.com/rvbeckford/playwright-qa-portfolio/actions/workflows/playwright.yml)

A Python + Playwright + pytest test suite built hands-on, session by session. 21 tests, all passing, running in GitHub Actions on every push.

What it covers
SauceDemo — login (happy path + locked-out, wrong password, empty username), cart and checkout journeys, sort by price, remove-from-cart badge checks
The Internet — JavaScript alerts, dropdowns, checkboxes, file upload, add/remove elements, dynamic loading, hovers
JSONPlaceholder API — GET, POST, DELETE, plus a hybrid test verifying the same API data in the browser
Structure
pages/ — Page Object Model: LoginPage, InventoryPage, CartPage, CheckoutPage
test_saucedemo_login.py, test_cart_checkout.py, test_the_internet.py, test_api.py
conftest.py — login_page and logged_in_page fixtures
pytest.ini — smoke/regression markers, screenshots and traces on failure
How to run it
python -m venv .venv
.venv\Scripts\activate (Windows) or source .venv/bin/activate (Mac/Linux)
pip install -r requirements.txt
playwright install chromium
pytest

Useful variations:

pytest -m smoke — quick happy-path check only
pytest -n auto — run in parallel
pytest --html=report.html --self-contained-html — generate an HTML report

Failures leave a screenshot and a trace in test-results/, viewable with playwright show-trace <trace.zip>.


So the three Session 8 files are separate:

1. `requirements.txt` — the package list
2. `.github/workflows/playwright.yml` — the CI workflow
3. `README.md` — all of the above
