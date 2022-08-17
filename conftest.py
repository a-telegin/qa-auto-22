import pytest
from config.config import Config
from applications.api.github_api import GitHubAPI

@pytest.fixture(scope='session')
def github_api_client():
    github_api_client = GitHubAPI(Config.base_url)

    yield github_api_client
