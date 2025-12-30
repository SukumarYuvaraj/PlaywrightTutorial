import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://automationplayground.com/crm/")
    # Expect the Page to have the heading -> Customers Are Priority One!
    expect(page.get_by_role("heading", name="Customers Are Priority One!")).to_be_visible()