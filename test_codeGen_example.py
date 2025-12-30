import re
from playwright.sync_api import Playwright, sync_playwright, expect

# Method to test sign-in of automationplayground.com
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://automationplayground.com/crm/")
    expect(page.get_by_role("heading", name="Customers Are Priority One!")).to_be_visible()
    # Click Link - Sign In
    page.get_by_role("link", name="Sign In").click()
    # Verify the Page contains Login
    expect(page.get_by_role("heading", name="Login")).to_be_visible()
    # Enter the Email
    page.get_by_role("textbox", name="Enter email").click()
    page.get_by_role("textbox", name="Enter email").fill("droptoyuva89@gmail.com")
    # Enter the password
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("password")
    page.get_by_role("button", name="Submit").click()
    # Verify the Page - Our Happy Customers
    expect(page.get_by_role("heading", name="Our Happy Customers")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)