class UserDao:

    def __init__(self, database):
        self.db = database

    def create_user(self, user):
        db_client = self.db()

        doc = {
            'email': user['email'],
            'password' : user['password']
        }

        db_client.insta.insta.insert_one(doc)
