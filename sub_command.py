from console import terminal as _terminal
from console import help as _helper
from tools import history as _history
from tools import index as _index
from pathlib import Path as _Path
from tools import db_create as _dbs
import sys as _sys
import os as _os
import globals as _globals
import routines as _routines

def scmd_show_databases(_command :list):
    headers = ["[bold yellow]Databases[/bold yellow]"]
    rows = []
    for key in _globals.global_indexed_databases.keys():
        rows.append([f"[bold white]{key}[/bold white]"])

    _terminal.print_generic_table(headers,rows,False)
    return True

def scmd_show_error(_command :list):
    return False



def scmd_create_database(command :list):
   db_name = command[2]
   if  _dbs.create_database(_globals.PATH_DB_DATA,db_name):
        _index.write_index((_globals.PATH_DB_INDEX / _globals.filename_database_index),db_name,(_globals.PATH_DB_DATA / f"{db_name}.db"))
        _index.read_index((_globals.PATH_DB_INDEX / _globals.filename_database_index),_globals.global_indexed_databases)
        return True

   return False
