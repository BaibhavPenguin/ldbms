from pathlib import Path as _Path
import sql.dbtools as _db_tools
import sql.db_state as _db_state
import sqlite3 as _sqlite3

def update_current_db(db_name,db_path):
    current_db = {
        'db_name' : db_name,
        'db_path' : db_path
    }
    _db_tools.sqlite_current_database.update(current_db)
    _db_state.active_database_connection = _sqlite3.connect(db_path)
    _db_state.active_database_cursor = _db_state.active_database_connection.cursor()
    return True

def get_current_database():
    return [_db_tools.sqlite_current_database['db_name'],_db_tools.sqlite_current_database['db_path']]