from providers.data.users_providers import UsersProvider


def test_check_login(github_ui_client):
    user = UsersProvider.existing_user()

    github_ui_client.get(user['login'], user['password'])

    assert github_ui_client.title == "GitHub"


def test_check_login_failed(github_ui_client):
    user = UsersProvider.fake_user()

    github_ui_client.login(user['login'], user['password'])

    assert github_ui_client.get_title() == "Sign in to GitHub · GitHub"
