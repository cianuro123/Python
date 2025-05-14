import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("http://127.0.0.1:8000 ")
    # Expect a title "to contain" a substring.
    title = page.content(re.compile("user"))
    print(title)


def test_get_started_link(page: Page):
    page.goto("https://www.youtube.com/watch?v=HtKqSJX7VoM&ab_channel=SoyDalto")

    # Click the get started link.
    page.get_by_role("link", name="...más").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("link", name="soydalto")).to_be_visible()

