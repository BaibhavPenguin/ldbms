from pathlib import Path as _path
#Database Variables
global_indexed_databases = {}
current_db = ''
PATH_DB_INDEX = _path.home() / '.ldbms'/ 'config' 
PATH_DB_DATA = _path.home()/'.ldbms' / 'databases' 

#Session History Variables
global_history = []
SESSION_HISTORY_PATH =  _path.home() / '.ldbms'/ 'session' 

filename_database_index = 'db-index.json'
filename_session_history = 'session-history.ldbms'