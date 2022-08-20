import py
# import os


class UsersProvider:

    @staticmethod
    def fake_user():
        return {
            'login': 'llfhnfneihr',
            'id': 6446926,
            'password' : 'someoiqhe'
        }
    
    @staticmethod
    def existing_user():
        return {
            'login': 'a-telehin',
            'id': 2,
            'password': ''
        }

    # @staticmethod
    # def existing_user_from_env():
    #     return {
    #         'login' : os.environ.get("EXISTING_GITHUB_USER_LOGIN"),
    #         'id' : int(os.environ.get("EXISTING_GITHUB_USER_ID"))
    #     }