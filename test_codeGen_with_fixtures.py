import pytest
from playwright.sync_api import Page, expect


# 1. Define the fixture
@pytest.fixture
def crm_page(page: Page):
    # SETUP: Everything before yield runs BEFORE the test
    page.goto("https://automationplayground.com/crm/")

    yield page  # The test executes here

    # TEARDOWN: Everything after yield runs AFTER the test
    print("\nTest finished, cleaning up...")
    page.close()
    # (Optional) e.g., page.close() or clearing cookies


# 2. Use the fixture in your test
def test_has_title(crm_page):
    # Note: 'crm_page' is the yielded page object from the fixture above
    expect(crm_page.get_by_role("heading", name="Customers Are Priority One!")).to_be_visible()
