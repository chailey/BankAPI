from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine



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

class CreditCardTypes(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select type_num, type from CreditCardTypes")
        return {'CreditCardTypes': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}

class AccountTypes(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from AccountTypes")
        return {'AccountTypes': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor.fetchall()]}

@app.route('/')
def hello_world():
    return 'Hello, World!'


api.add_resource(CreditCardTypes, '/CreditCardTypes')
api.add_resource(AccountTypes, '/AccountTypes')
api.add_resource(User, '/User')

if __name__ == '__main__':
     app.run()