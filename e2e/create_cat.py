from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://127.0.0.1:8000/admin/login/?next=/admin/
    page.goto("http://127.0.0.1:8000/admin/login/?next=/admin/")

    # Click input[name="username"]
    page.locator("input[name=\"username\"]").click()

    # Fill input[name="username"]
    page.locator("input[name=\"username\"]").fill("ronny")

    # Press Tab
    page.locator("input[name=\"username\"]").press("Tab")

    # Fill input[name="password"]
    page.locator("input[name=\"password\"]").fill("ronny")

    # Click #login-form div:has-text("Log in")
    page.locator("#login-form div:has-text(\"Log in\")").click()
    assert page.url == "http://127.0.0.1:8000/admin/"

    # Click text=Add >> nth=2
    page.locator("text=Add").nth(2).click()
    assert page.url == "http://127.0.0.1:8000/admin/cat/cat/add/"

    # Fill input[name="name"]
    page.locator("input[name=\"name\"]").fill("Purry")

    # Press Tab
    page.locator("input[name=\"name\"]").press("Tab")

    # Fill input[name="age"]
    page.locator("input[name=\"age\"]").fill("12")

    # Click input[name="_save"]
    page.locator("input[name=\"_save\"]").click()
    assert page.url == "http://127.0.0.1:8000/admin/cat/cat/"

    # Click #result_list >> text=Purry
    page.locator("#result_list a[href=\"/admin/cat/cat/1/change/\"]").click()
    assert page.url == "http://127.0.0.1:8000/admin/cat/cat/1/change/"

    # ---------------------
    context.storage_state(path="auth.json")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
