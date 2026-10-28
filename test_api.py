import pytest
from playwright.sync_api import Page

BASE_URL = "https://jsonplaceholder.typicode.com"


def api_context(playwright):
    return playwright.request.new_context(base_url=BASE_URL)


@pytest.mark.regression
def test_get_post(playwright):
    context = api_context(playwright)
    response = context.get("/posts/1")
    assert response.ok
    assert response.status == 200
    data = response.json()
    assert data["id"] == 1
    assert data["userId"] == 1
    assert data["title"] == (
        "sunt aut facere repellat provident occaecati "
        "excepturi optio reprehenderit"
    )
    context.dispose()


@pytest.mark.regression
def test_create_post(playwright):
    context = api_context(playwright)
    response = context.post(
        "/posts",
        data={"title": "foo", "body": "bar", "userId": 1},
    )
    assert response.status == 201
    data = response.json()
    assert data["title"] == "foo"
    assert data["body"] == "bar"
    assert data["userId"] == 1
    assert data["id"] == 101
    context.dispose()


@pytest.mark.regression
def test_delete_post(playwright):
    context = api_context(playwright)
    response = context.delete("/posts/1")
    assert response.status == 200
    context.dispose()


@pytest.mark.regression
def test_api_data_matches_ui(playwright, page: Page):
    # API channel: fetch post 1 and grab its title.
    context = api_context(playwright)
    response = context.get("/posts/1")
    assert response.ok
    title = response.json()["title"]
    context.dispose()

    # UI channel: open the same post in the browser and
    # verify that same title is on the page.
    page.goto(f"{BASE_URL}/posts/1")
    assert title in page.content()
