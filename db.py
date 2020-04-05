import common
import sqlite3


def verify_at_table(cursor):
    cursor.execute("select * from sqlite_master where type='table';".format(common.AT_TABLE_NAME))
    value = cursor.fetchone()
    if not value:
        cursor.execute("create table {}(link text primary key, last_update_timestamp text);".format(common.AT_TABLE_NAME))


def db_decorator(callback):
    def db_decorator_impl(*args, **kwargs):
        with sqlite3.connect(common.AT_DATABASE) as conn:
            cursor = conn.cursor()
            verify_at_table(cursor)
            value = callback(cursor, *args, **kwargs)
            conn.commit()
        return value

    return db_decorator_impl


@db_decorator
def get_last_update_timestamp(cursor, link):
    value = cursor.execute("select * from {} where link='{}';".format(common.AT_TABLE_NAME, link)).fetchone()
    if value:
        return value[1]
    cursor.execute("insert into {} values('{}', '{}');".format(common.AT_TABLE_NAME, link, "NaN"))
    return "NaN"


@db_decorator
def set_last_update_timestamp(cursor, link, last_update_timestamp):
    cursor.execute("update {} set last_update_timestamp='{}' where link='{}'".format(common.AT_TABLE_NAME, last_update_timestamp, link))
