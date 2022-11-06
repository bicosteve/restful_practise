from db.db import db


class ItemModel(db.Model):

    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)

    store_id = db.Column(db.Integer, db.ForeignKey("store.id"), nullable=False)

    def __repr__(self):
        return (
            f"Item is {self.name} with price of {self.price} and store {self.store_id}"
        )

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def return_json(self):
        return {"name": self.name, "price": self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def save_item_to_db(cls, item):
        item = cls(name=item["name"], price=item["price"], store_id=item["store_id"])
        db.session.add(item)
        db.session.commit()

    @classmethod
    def update_item(cls, item):
        updated_item = cls(name=item["name"], price=["price"])
        db.session.add(updated_item)
        db.session.commit()

    @classmethod
    def delete_item(cls, name):
        db.session.delete(name=name)
        db.session.commit()

    @classmethod
    def get_items(cls):
        items = cls.query.all()

        for item in items:
            return {"items": item.return_json()}

        # return ItemModel.query.all()
