"""
This module defines functions and classes related to DB access.

(c) Joao Galamba, 2022
"""

from hashlib import sha256 as default_hashalgo
from mysql.connector import connect, Error as MySQLError


DB_CONN_PARAMS = {
    'host': '192.168.56.104',
    'user': 'operator',
    'password': 'abc',
    'database': 'BuyPy',
}

def login(username: str, passwd: str) -> dict:
    hash_obj = default_hashalgo()
    hash_obj.update(passwd.encode())
    hash_passwd = hash_obj.hexdigest()
    with connect(**DB_CONN_PARAMS) as connection:
        with connection.cursor() as cursor:
            cursor.callproc('AuthenticateOperator', [username, hash_passwd])
            user_info = next(cursor.stored_results())
            if user_info.rowcount != 1:
                return None
            user_row = user_info.fetchall()[0]
            return dict(zip(user_info.column_names, user_row))
#:
