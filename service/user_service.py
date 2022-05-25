import bcrypt
import re

from flask import request, jsonify, abort


class UserService:
    def __init__(self, user_dao):
        self.user_dao = user_dao

    def create_user(self, user):

        try:
            user['password'] = bcrypt.hashpw(
                user['password'].encode('UTF-8'),
                bcrypt.gensalt()
            )

            new_user = self.user_dao.create_user(user)
            return new_user

        except KeyError:
            abort(400, description="INVALID_KEY")
