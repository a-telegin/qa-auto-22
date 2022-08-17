def test_check_repos_can_be_found(github_api_client):
    # Check user can find any existing repo from github
    repos = github_api_client.get_repos('qa-auto-22')

    assert repos['total_count'] != 0
    assert len(repos['items']) != 0


def test_check_repos_cannot_be_found(github_api_client):
    # Check user cannot find any existing repo from github
    repos = github_api_client.get_repos('wiuewrubfeu')

    assert repos['total_count'] == 0
    assert len(repos['items']) == 0