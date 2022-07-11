from external import UsernameLookup

class UserSource():
    def __init__(self):
        self.username_lookup = UsernameLookup()
        

    def fetch(self, user_id, username):
        user_namespace = self._adapt_arguments(user_id, username)
        return self.username_lookup.search(user_namespace)

    @staticmethod
    def _adapt_arguments(user_id, username):
        return f'{user_id}:{username}'