def test_add_todo(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий")
    page.get_by_placeholder("What needs to be done?").press("Enter")

    # ---------------------
    page.close()
    page.close()
