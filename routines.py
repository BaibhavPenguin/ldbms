import globals as _globs
from pathlib import Path
from tools import index
from sql import db_state as _db_state

def setup_ldbms_enviornment():
    #Inirialize Directories
    _globs.PATH_DB_INDEX.mkdir(parents=True,exist_ok=True)  
    _globs.SESSION_HISTORY_PATH.mkdir(parents=True,exist_ok=True)
    _globs.PATH_DB_DATA.mkdir(parents=True,exist_ok=True)
    #Remove Old Session History
    (_globs.SESSION_HISTORY_PATH / _globs.filename_session_history).unlink(missing_ok=True)    #Try and Delete the Session History File
    #Make Session Files
    (_globs.PATH_DB_INDEX / _globs.filename_database_index).touch(exist_ok=True)           #Try and Create the Index File
    (_globs.SESSION_HISTORY_PATH / _globs.filename_session_history).touch(exist_ok=True)    #Try and Create the Session History File
    #Prepare Database List
    _debug = index.read_index((_globs.PATH_DB_INDEX / _globs.filename_database_index),_globs.global_indexed_databases)
    #Read Indexed Databases
    

def cleanup_ldbms_enviornment():
    (_globs.SESSION_HISTORY_PATH / _globs.filename_session_history).unlink(missing_ok=True)    #Try and Delete the Session History File
    try:
        _db_state.active_database_connection.close()
        _db_state.active_database_connection.close()
    except AttributeError:
        pass

