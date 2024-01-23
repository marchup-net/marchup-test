def test_example(browser):
    browser.get("https://www.example.com")
    title = browser.title
    assert title == "Example Domain"
