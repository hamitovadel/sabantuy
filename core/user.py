"""User module."""
import logging
from flask import abort
from psycopg2 import sql


LOGGER = logging.getLogger('my_super_puper_app')


class User:
    """The common class for working with Users."""

    @staticmethod
    def get_all(cursor):
        """Return all users from the Users table"""
        query = sql.SQL('select * from {}').format(sql.Identifier('users'))
        cursor.execute(query)
        results = cursor.fetchall()
        return {'results': results}

    @staticmethod
    def get_one(cursor, id):
        try:
            cursor.execute(
                sql.SQL('select * from {table} where {pkey} = %s').format(
                    table=sql.Identifier('users'),
                    pkey=sql.Identifier('id')),
                (id,))

            results = cursor.fetchone()
            return {'results': results}

        except Exception as err:
            LOGGER.exception("Opps! Select from the table getting error!. Error: %s" % (id, err))
            return abort(500, description=err)

    @staticmethod
    def create(cursor, **kwargs):
        """Insert new record to the DB."""

        try:
            cursor.execute(
                sql.SQL("insert into {} (first_name, last_name, email) values (%s, %s, %s) returning id").format(sql.Identifier('users')),
                [kwargs.get('first_name'),
                 kwargs.get('last_name'),
                 kwargs.get('email')])

            user_id_new = cursor.fetchone()[0]

        except Exception as err:
            LOGGER.exception("Opps! Can't insert to the table!. Error: %s" % err)
            return abort(500, description=err)

        return {'result': 'Ok', 'user_id_new': user_id_new}

    @staticmethod
    def delete(cursor, id):
        """Delete user from the DB."""

        try:
            cursor.execute(
                sql.SQL('delete from {table} where {pkey} = %s').format(
                    table=sql.Identifier('users'),
                    pkey=sql.Identifier('id')),
                (id,))

        except Exception as err:
            LOGGER.exception("Opps! Can't delete the Id %s from the table!. Error: %s" % (id, err))
            return abort(500, description=err)

        return {'result': 'Ok'}

    @staticmethod
    def update(cursor, id, **kwargs):
        """Make some changes based on the input."""

        try:
            cursor.execute(
                sql.SQL("""update {} 
                            set first_name = coalesce(%s, first_name), 
                                last_name  = coalesce(%s, last_name), 
                                email = coalesce(%s, email)
                            where {pkey} = %s """).format(sql.Identifier('users'),
                                                          pkey=sql.Identifier('id')),
                [kwargs.get('first_name'),
                 kwargs.get('last_name'),
                 kwargs.get('email'),
                 id])


            return {'result': 'Ok'}

        except Exception as err:
            LOGGER.exception("Opps! Can't insert to the table!. Error: %s" % err)
            return abort(500, description=err)
