from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://127.0.0.1:8000/admin/login/?next=/admin/
    page.goto("http://127.0.0.1:8000/admin/login/?next=/admin/")

    # Click input[name="password"]
    page.locator("input[name=\"password\"]").click()

    # Fill input[name="password"]
    page.locator("input[name=\"password\"]").fill("ronny")

    # Click input[name="username"]
    page.locator("input[name=\"username\"]").click()

    # Fill input[name="username"]
    page.locator("input[name=\"username\"]").fill("ronny")

    # Click text=Log in
    page.locator("text=Log in").click()
    assert page.url == "http://127.0.0.1:8000/admin/"

    # ---------------------
    context.storage_state(path="auth.json")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
