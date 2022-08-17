import py


class UsersProvider:

    @staticmethod
    def fake_user():
        return {
            'login': 'llfhnfneihr',
            'id': 6446926
        }
    
    @staticmethod
    def existing_user():
        return {
            'login': 'defunkt',
            'id': 2
        }

