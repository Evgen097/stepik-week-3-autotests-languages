
import pytest
import time
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru", help="Choose language: ru, es, fr... Default: russian")


@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("language")
    print("\n--------------------------------------")
    print(F"Check for language: {lang}")
    
    browser = webdriver.Chrome()
	
    link = f"http://selenium1py.pythonanywhere.com/{lang}/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(1)
	
    yield browser
    browser.quit()
    print("\n--------------------------------------")
























