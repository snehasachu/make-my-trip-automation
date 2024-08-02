
import os
import sys
import time
import pytest
from pytest import fixture
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as ec
from platform import python_version, platform


reports_path = "reports"
# report = reports_path + "/UI_Test_Reports_" + str(
#    time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))) + ".html"
report = reports_path + "/report.html"
secret = ""
environment = ""
scenario = ""
reports = ""
admin = ""
browser = ""
web_driver = None

def get_chromedriver_path():
    return "C:\\Users\\DELL\\OneDrive\\Documents\\project\\chromedriver\\chromedriver.exe"

# pytest related fixtures
def pytest_addoption(parser):
    parser.addoption("--browser",action="store",help="Browser to run tests against")
    parser.addoption("--scenario",action="store",help="Scenario to run tests against")
    group = parser.getgroup('selenium', 'selenium')

    group.addoption('--headless',action='store_false',help='enable headless mode for supported browsers.')

@fixture(scope='session', autouse=True)
def get_scenario(request) -> str:
    global scenario
    scenario = request.config.getoption("-m")
    os.environ['scenario'] = scenario
    return scenario


@fixture(scope='session', autouse=True)
def get_browser(request) -> str:
    global browser
    os.environ['browser'] = request.config.getoption("--browser")
    browser = os.environ['browser']
    return browser

@fixture(scope='session')
def base_url() -> str:
    base_url = "https://www.makemytrip.com/"
    print("BASE_URL: ", base_url)
    return base_url

@pytest.mark.hookwrapper(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    set_generate_report(True)
    item.config._metadata = {"Browser name": web_driver.capabilities["browserName"],
                             "Browser version": web_driver.capabilities['browserVersion'],
                             "Python version": python_version(),
                             "Platform": platform()}
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when in ("setup", "call"):
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            time.sleep(1)
            screenshot = web_driver.get_screenshot_as_base64()
            extra.append(pytest_html.extras.html('<img src="' + 'data:image/png;base64,' + screenshot +
                                                 '" style="width:304px;height:228px;"  align="right"/>'))
    report.extra = extra

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    global web_driver
    options = None
    headless = False
    if web_driver is None:
        # Include other browsers
        if config.getoption("--browser") == 'chrome':
            if headless:
                options = ChromeOptions()
                options.add_argument("start-maximized")  # open Browser in maximized mode
                options.add_argument("disable-infobars")  # disabling infobars
                options.add_argument("--disable-extensions")  # disabling extensions
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--no-sandbox")
                options.add_argument('headless')
                options.add_argument("window-size=1920x1080")

            # Using custom Chrome Driver Installer instead of ChromeDriverManager
            if get_chromedriver_path() is None:
                print("Chrome Driver not found")
                sys.exit(1)

            service_obj = Service(get_chromedriver_path())
            web_driver = Chrome(service=service_obj, options=options)
        web_driver.maximize_window()


@pytest.fixture(scope='function', autouse=True)
def login_once(base_url):
    web_driver.get(base_url)

def set_generate_report(value):
    global generate_report
    generate_report = value