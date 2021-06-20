import os
import logging

import psycopg2


LOGGER = logging.getLogger('my_super_puper_app')


class PsqlConnection():
    def __init__(self):
        self.connection = None

        try:
            self.connection = psycopg2.connect(
                host=os.environ.get('DB_HOST', '/cloudsql/pragmatic-will-317205:us-central1:sabantuy'),
                database=os.environ.get('DB', 'postgres'),
                user=os.environ.get('DB_USER', 'postgres'),
                password=os.environ.get('DB_PASSWORD', 'E8I0muzAfkKGaBdv'))

            self.connection.autocommit = True
        except Exception as err:
            LOGGER.error("Opps! I can't connect to the DB Server! Err: %s" % err)
