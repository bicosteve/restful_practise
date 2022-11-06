from db.db import db


class StoreModel(db.Model):
    __tablename__ = "store"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    items = db.relationship("ItemModel", backref="items", lazy="dynamic")

    """
    # back reference -> allows store db to check on items db 
    # which items have relationship with store
    #lazy = 'dynamic' -> 
    """

    def __repr__(self) -> str:
        return f"Store name is {self.name}"

    def return_json(self):
        return {"id": self.id, "name": self.name}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def save_to_db(cls, name):
        store = cls(name=name)
        db.session.add(store)
        db.session.commit()

    @classmethod
    def delete_from_db(cls, name):
        db.session.delete(name=name)
        db.session.commit()

    @classmethod
    def find_all_stores(cls):
        stores = cls.query.all()
        return [store.return_json() for store in stores]
