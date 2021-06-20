"""Transactions module."""
import logging
from datetime import datetime as dt
from flask import abort
from psycopg2 import sql


LOGGER = logging.getLogger('my_super_puper_app')


class Transaction:
    """The common class for working with Transactions."""

    @staticmethod
    def get_all_by_user(cursor, user_id):
        """Return all transcations from the transactions table"""
        try:
            cursor.execute(
                sql.SQL('select * from {table} where {pkey} = %s').format(
                    table=sql.Identifier('transactions'),
                    pkey=sql.Identifier('user_id')),
                (user_id,))

            results = cursor.fetchall()
            return {'results': results}

        except Exception as err:
            LOGGER.exception("Opps! Select from the table getting error!. Error: %s" % (id, err))
            return abort(500, description=err)

    @staticmethod
    def get_report(cursor, user_id):
        """Return a report by user"""
        try:
            cursor.execute(
                sql.SQL('select DATE(date), sum(amount) from {table} where {pkey} = %s group by DATE(date) order by 1 asc').format(
                    table=sql.Identifier('transactions'),
                    pkey=sql.Identifier('user_id')),
                (user_id,))

            results = cursor.fetchall()
            return {'results': results}

        except Exception as err:
            LOGGER.exception("Opps! Select from the table getting error!. Error: %s" % (id, err))
            return abort(500, description=err)

    @staticmethod
    def get_one(cursor, id):
        try:
            cursor.execute(
                sql.SQL('select * from {table} where {pkey} = %s').format(
                    table=sql.Identifier('transactions'),
                    pkey=sql.Identifier('id')),
                (id,))

            results = cursor.fetchone()
            return {'results': results}

        except Exception as err:
            LOGGER.exception("Opps! Select from the table getting error!. Error: %s" % (id, err))
            return abort(500, description=err)

    @staticmethod
    def is_float(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def validate_datetime(date_text):
        try:
            dt.strptime(date_text, '%Y-%m-%d %H:%M:%S')
            return True
        except ValueError:
            return False

    @staticmethod
    def create(cursor, user_id, **kwargs):
        """Insert new record to the DB."""
        if not user_id.isdigit():
            err_message = 'user_id should be only numeric'
            LOGGER.error(err_message)
            return abort(500, description=err_message)

        if kwargs.get('amount') and not Transaction.is_float(kwargs.get('amount')):
            err_message = 'Amount of transaction should be only float'
            LOGGER.error(err_message)
            return abort(500, description=err_message)

        if kwargs.get('date') and not Transaction.validate_datetime(kwargs.get('date')):
            err_message = 'Transaction datetime should be the following format: %Y-%m-%d %H:%M:%S'
            LOGGER.error(err_message)
            return abort(500, description=err_message)

        try:
            cursor.execute(
                sql.SQL("insert into {} (user_id, amount, date) values (%s, %s, %s)").format(sql.Identifier('transactions')),
                [int(user_id),
                 float(kwargs.get('amount')),
                 kwargs.get('date')])

        except Exception as err:
            LOGGER.exception("Opps! Can't insert to the table!. Error: %s" % err)
            return abort(500, description=err)

        return {'result': 'Ok'}

    @staticmethod
    def delete(cursor, id):
        """Delete transaction from the DB."""

        try:
            cursor.execute(
                sql.SQL('delete from {table} where {pkey} = %s').format(
                    table=sql.Identifier('transactions'),
                    pkey=sql.Identifier('id')),
                (id,))

        except Exception as err:
            LOGGER.exception("Opps! Can't delete the Id %s from the table!. Error: %s" % (id, err))
            return abort(500, description=err)

        return {'result': 'Ok'}

