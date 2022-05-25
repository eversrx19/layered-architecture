from flask import Flask, g
from flask_cors import CORS
from pymongo import MongoClient

from model.user_dao import UserDao
from service.user_service import UserService
from endpoint.user_endpoint import UserEndpoint
from config import DB_URL


class Services:
    pass


def get_db():
    if 'db' not in g:
        g.db = MongoClient(DB_URL)
    return g.db


def create_app():
    app = Flask(__name__)

    # 1. DataModel Layer
    user_dao = UserDao(get_db)
    # feed_dao = FeedDao(get_db)

    # 2. Service Layer
    services = Services
    services.user_service = UserService(user_dao)
    # services.feed_service = FeedService(feed_dap)

    # 3. Endpoint Layer
    UserEndpoint.create_endpoints(app, services)

    @app.teardown_appcontext
    def teardown_db(exception):
        print("tear down")
        db = g.pop('db', None)

        if db is not None:
            db.close()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run('0.0.0.0', port=5001, debug=True)
