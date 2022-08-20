import pytest
from applications.ui.github_ui import GitHubUI
from config.config import Config
from applications.api.github_api import GitHubAPI

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope='session')
def github_api_client():
    github_api_client = GitHubAPI(Config.base_url_api)
    yield github_api_client

@pytest.fixture()
def github_ui_client():
    driver = webdriver.Chrome(
        service = Service(r"/home/atelehin/QAAutoCourse/qa-auto-22/chromedriver")
        )
    
    github_ui_client = GitHubUI(Config.base_url_ui, driver)

    yield github_ui_client

    github_ui_client.close_browser()