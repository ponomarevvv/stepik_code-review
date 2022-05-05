from selenium.webdriver import Firefox, Chrome
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en-gb",
        help="Choose language",
        choices=(
            "en-gb",
            "fr",
            "es",
            "ar",
            "ca",
            "cs",
            "da",
            "de",
            "el",
            "fi",
            "it",
            "ko",
            "nl",
            "pl",
            "pt",
            "pt-br",
            "ro",
            "ru",
            "sk",
            "uk",
        ),
    )

    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="options available: chrome, firefox",
        choices=("chrome", "firefox"),
    )


@pytest.fixture
def language(request):
    return request.config.getoption("--language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    browser = None
    if browser_name == "firefox":
        print("\nstart Firefox browser for test...")
        browser = Firefox()
    elif browser_name == "chrome":
        print("\nstart Chrome browser for test...")
        browser = Chrome()
    else:
        raise pytest.UsageError("--browser should be `chrome` or `firefox`")
    yield browser
    print("\nquit browser...")
    browser.quit()

