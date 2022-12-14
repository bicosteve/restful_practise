import sqlite3


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM users WHERE username = ?'
        result = cursor.execute(query, (username,))  # always have to be tuple

        # fetching one result
        row = result.fetchone()  # returns None if no row

        if row:
            # creating a user object with user details
            user = cls(row[0], row[1], row[2])
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, user_id):
        connection = sqlite3.connect('/sqlite/test.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM users WHERE id = ?'
        result = cursor.execute(query, (user_id,))

        row = result.fetchone()

        if row:
            user = cls(row[0], row[1], row[2])
        else:
            user = None

        connection.close()
        return user
