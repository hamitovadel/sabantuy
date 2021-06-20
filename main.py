from flask import Flask, request
from psycopg2.extras import RealDictCursor
import os

from utils.psql_config import PsqlConnection
from utils.utils import *
from core.user import User
from core.transaction import Transaction


CONNECTION = PsqlConnection().connection

app = Flask(__name__)


@app.route('/ping')
def ping():
    """Just ping"""
    return {'pong': True}


@app.route('/get-all-users')
def get_all_users():
    """Return all users from the Users table"""
    return User().get_all(CONNECTION.cursor(cursor_factory=RealDictCursor))


@app.route('/get-user/<id>')
def get_one_user(id):
    """Return user's info"""
    return User().get_one(CONNECTION.cursor(cursor_factory=RealDictCursor), id)


@app.route('/create-user', methods=['POST'])
def create_user():
    return User().create(CONNECTION.cursor(), **request.json)


@app.route('/delete-user/<id>', methods=['POST'])
def delete_user(id):
    return User().delete(CONNECTION.cursor(), id)


@app.route('/update-user/<id>', methods=['POST'])
def update_user(id):
    return User().update(CONNECTION.cursor(cursor_factory=RealDictCursor), id, **request.json)


@app.route('/get-all-transactions/<user_id>')
def get_all_transaction_by_user(user_id):
    """Return all transactions by User from the Transaction table"""
    return Transaction().get_all_by_user(CONNECTION.cursor(cursor_factory=RealDictCursor), user_id)


@app.route('/get-transaction/<id>')
def get_one_transaction(id):
    """Return transaction info"""
    return Transaction().get_one(CONNECTION.cursor(cursor_factory=RealDictCursor), id)


@app.route('/create-transaction/<user_id>', methods=['POST'])
def create_transaction(user_id):
    return Transaction().create(CONNECTION.cursor(), user_id, **request.json)


@app.route('/delete-transaction/<id>', methods=['POST'])
def delete_transaction(id):
    return Transaction().delete(CONNECTION.cursor(), id)


@app.route('/get-report/<user_id>')
def get_report_by_user(user_id):
    return Transaction().get_report(CONNECTION.cursor(cursor_factory=RealDictCursor), user_id)

@app.route('/fibonacci/<last_number>')
def fibonacci_last(last_number):
    return fibonacci(last_number)


if __name__ == "__main__":
    app.run(debug=True)