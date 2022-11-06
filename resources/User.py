from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token


from models.user import UserModel


class Register(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument("username", required=True, type=str, help="Field required")
    parser.add_argument("password", required=True, type=str, help="Field required")

    def post(self):

        data = self.parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {"message": "Username already taken"}, 400

        try:
            UserModel.save_user(data["username"], data["password"])
        except:
            return {"mgs": "Something went wrong while inserting user"}, 500

        return data


class Login(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument("username", required=True, type=str, help="Field required")
    parser.add_argument("password", required=True, type=str, help="Field required")

    def post(self):

        data = self.parser.parse_args()

        user = UserModel.find_by_username(data["username"])

        if user is None:
            return {"message": "User not found!"}, 404

        if user and user.password == data["password"]:
            access_token = create_access_token(identity=user.username, fresh=True)
            refresh_token = create_refresh_token(identity=user.username)
            return {"access_token": access_token, "refresh_token": refresh_token}, 200

        return {"message": "Username and password do not match"}, 400
