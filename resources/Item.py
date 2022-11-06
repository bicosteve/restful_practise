import sqlite3

from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from models.item import ItemModel


class Item(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument(
        "price", required=True, type=float, help="This field is required"
    )

    connection = sqlite3.connect("test.db", check_same_thread=False)

    @jwt_required()
    def get(self, name):
        # save_item_to_db

        try:
            item = ItemModel.find_by_name(name)
            if not item:
                return {"message": f"Item {name} not found!"}
        except:
            return {"message": "Something went wrong"}, 500

        (id, name, price) = item  # unpacking the item set

        return {"id": id, "name": name, "price": price}

    @jwt_required()
    def post(self, name):

        if ItemModel.find_by_name(name):
            return {"message": f"Item {name} already exists"}, 400

        data = self.parser.parse_args()

        item = {"name": name, "price": data["price"]}

        try:
            Item.save_item_to_db(item)
        except:
            return {"message": "Internal server error"}, 500

        return item, 201

    @jwt_required()
    def delete(self, name):

        if not ItemModel.find_by_name(name):
            return {"message", f"Item {name} does not exist"}, 400
        try:
            Item.delete_item(name)
        except:
            return {"msg": "Not deleted. Error occured"}, 500

        return {"message": "Item deleted!"}, 200

    @jwt_required()
    def put(self, name):

        data = self.parser.parse_args()
        item = Item.find_by_name(name)
        updated_item = {"name": name, "price": data["price"]}

        if item is None:
            try:
                ItemModel.save_item_to_db(updated_item)
            except:
                return {"message": "Item not inserted. Something bad occured"}, 500
        else:
            try:
                Item.update_item(updated_item)
            except:
                return {"message": "Item not updated. Something bad occured"}, 500

        return updated_item, 200


class ItemList(Resource):
    def get(self):
        items = ItemModel.get_items()
        # try:
        #     items = ItemModel.get_items()
        #     if not items:
        #         return {"message": "No items found"}, 404
        # except:
        #     return {"message": "Something went wrong"}, 500

        return items, 200
