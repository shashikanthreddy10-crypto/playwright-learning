from email.policy import default

import playwright
import pytest
from playwright.sync_api import Playwright, expect
from playwright.sync_api import sync_playwright


from utils.data_reader import DataReader

def pytest_addoption(parser):
    parser.addoption("--browser",action = "store",default="chrome")

@pytest.fixture(scope="session")
def browser_launch(request):
    with sync_playwright() as p:
        browser_name = request.config.getoption("--browser")
        if browser_name == "chrome":
            browser = p.chromium.launch(headless=False)
        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=False)
        elif browser_name == "edge":
            browser = p.webkit.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def context(browser_launch):
    context_new=browser_launch.new_context()
    yield context_new
    context_new.close()

@pytest.fixture(scope="function")
def page(context,request):
    page=context.new_page()
    request.node.page = page
    yield page
    page.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome=yield
    report = outcome.get_result()
    if report.when=="call" and report.failed:
        page = getattr(item,"page",None)
        if page:
            page.screenshot(f"screenshots/{item.name}.png")


@pytest.fixture
def login(page,request):
    username=request.param
    credentials = DataReader()
    user_email = credentials.credentials()[username]["userEmail"]
    user_password = credentials.credentials()[username]["userPassword"]
    #user_password = ["userCredentials"][0]["password"]
    #playwright = sync_playwright().start()
    # browser = playwright.chromium.launch(headless=False)
    # context_new = browser.new_context()
    # page=context_new.new_page()
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill(user_email)
    page.get_by_placeholder("enter your passsword").fill(user_password)
    page.get_by_role("button", name="Login").click()
    return page
