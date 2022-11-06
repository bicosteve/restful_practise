from datetime import timedelta

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager


# from utils.security import authenticate, identity
from resources.Item import Item, ItemList
from resources.User import Register, Login
from resources.Store import Store, Stores

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

# JWT CONFIGS
app.config["JWT_SECRET_KEY"] = "secret_key"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=2)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=2)
api = Api(app)
# app.secret_key = "secret_key"
jwt = JWTManager(app)


@app.before_first_request
def create_tables():
    db.create_all()


# item end points
api.add_resource(Item, "/api/item/<string:name>")
api.add_resource(ItemList, "/api/items")

# store endpoints
# api.add_resource(Store, "/api/store/<string:name>")
api.add_resource(Store, "/api/store")
api.add_resource(Stores, "/api/stores")

# auth routes
api.add_resource(Register, "/api/register")
api.add_resource(Login, "/api/login")


if __name__ == "__main__":
    from db.db import db

    db.init_app(app)
    app.run(port=6050, debug=True)
