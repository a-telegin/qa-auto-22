from providers.data.users_providers import UsersProvider
import requests
import pytest


def test_http_status_code_200(github_api_client):
    r = requests.get('https://api.github.com/zen')
    assert r.status_code == 200
    # assert r.text != "Design for failure."


def test_user_exists(github_api_client):
    user = UsersProvider.existing_user()

    api_user = github_api_client.get_user(user['login'])

    assert api_user['login'] == 'defunkt'
    assert api_user['id'] == 2


def test_user_non_exist(github_api_client):
    user = UsersProvider.fake_user()

    with pytest.raises(requests.exceptions.HTTPError):
        github_api_client.get_user(user['login'])


