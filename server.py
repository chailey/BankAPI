from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('sqlite:///USCCreditUnion.db')
app = Flask(__name__)
api = Api(app)

class Account(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from Account")
        return {'Account': [i[0] for i in query.cursor.fetchall()]}
    def post(self):
        pass

class CreditCard(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from CreditCard")
        return {'CreditCard': [i[0] for i in query.cursor.fetchall()]}
    def post(self):
        pass

class Transaction(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from Transaction")
        return {'Transaction': [i[0] for i in query.cursor.fetchall()]}
    def post(self):
        pass

class User(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from User")
        return {'User': [i[0] for i in query.cursor.fetchall()]}
    def post(self):
        pass

class CardTypes(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from CardTypes")
        return {'CardTypes': [i[0] for i in query.cursor.fetchall()]}

class AccountTypes(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from AccountTypes")
        return {'AccountTypes': [i[0] for i in query.cursor.fetchall()]}

api.add_resource(CardTypes, '/CardTypes')
api.add_resource(AccountTypes, '/AccountTypes')
api.add_resource(User, '/User')

if __name__ == '__main__':
     app.run(port='5002')