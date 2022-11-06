from db.db import db


class UserModel(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(150))

    # connection = sqlite3.connect('test.db', check_same_thread=False)

    def __init__(self, username, password):
        # self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        return UserModel.query.filter_by(username=username).first()
        # cursor = cls.connection.cursor()
        # query = "SELECT * FROM users WHERE username = ?"
        # result = cursor.execute(query, [username])

        # row = result.fetchone()

        # return row

    @classmethod
    def find_by_id(cls, user_id):
        return UserModel.query.filter_by(id=user_id).first()

    @classmethod
    def save_user(cls, username, password):
        user = cls(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        # cursor = cls.connection.cursor()

        # query = "INSERT INTO users(username,password) VALUES (?,?)"
        # cursor.execute(query, [username, password])
        # cls.connection.commit()
        # cls.connection.close()
