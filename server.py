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
        return jsonify({'Account': [i[0] for i in query.cursor.fetchall()]})
    def post(self):
        pass

class CreditCard(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from CreditCard")
        return jsonify({'CreditCard': [i[0] for i in query.cursor.fetchall()]})
    def post(self):
        pass

class Transaction(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from Transaction")
        return jsonify({'Transaction': [i[0] for i in query.cursor.fetchall()]})
    def post(self):
        conn = db_connect.connect()
        transaction_id = request.json['transaction_id']
        student_id = request.json['student_id']
        account_number = request.json['account_number']
        amount = request.json['amount']
        query = conn.execute("insert into Transaction"
                             "(transaction_id, student_id, account_number, amount,"
                             " acquiring_account_number) values (?,?,?,?,?)",
                             transaction_id, student_id, account_number, amount, 0)
        return {'status': 'success'}


class User(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from User")
        return jsonify({'User': [i[0] for i in query.cursor.fetchall()]})
    def post(self):
        conn = db_connect.connect()
        student_id = request.json['student_id']
        address = request.json['address']
        email = request.json['email']
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        query = conn.execute("insert into User"
                             "(student_id, address, email, first_name,"
                             " last_name) values (?,?,?,?,?)",
                             student_id, address, email, first_name, last_name)
        return {'status': 'success'}


class UserID(Resource):
    def get(self, student_id):
        conn = db_connect.connect()
        query = conn.execute("select * from User where student_id = %d" %int(student_id))
        return jsonify({'User': [dict(zip(tuple(query.keys()) ,i)) for i in query.cursor]})

class CreditCardTypes(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from CreditCardTypes")
        return jsonify({'CreditCardTypes': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]})

class AccountTypes(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from AccountTypes")
        return jsonify({'AccountTypes': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor.fetchall()]})

@app.route('/')
def hello_world():
    return 'Hello, World!'


api.add_resource(CreditCardTypes, '/CreditCardTypes')
api.add_resource(AccountTypes, '/AccountTypes')
api.add_resource(User, '/User')
api.add_resource(UserID, '/User/<student_id>')

if __name__ == '__main__':
     app.run()