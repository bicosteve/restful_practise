from flask_restful import Resource, reqparse

from models.store import StoreModel


class Store(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("name", required=True, type=str, help="Field required")

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if not store:
            return {"message": "Store not found"}, 404
        return {"store": store}, 200

    def post(self):
        data = self.parser.parse_args()

        if StoreModel.find_by_name(data["name"]):
            return {"message": "The store already exists"}, 400

        try:
            StoreModel.save_to_db(data["name"])
        except:
            return {"message": "Something went wrong"}, 500

        return {"msg": "Store saved", "store": data}


class Stores(Resource):
    def get(self):
        stores = StoreModel.find_all_stores()
        if not stores:
            return {"message": "No stores was found"}, 404
        return stores, 200
