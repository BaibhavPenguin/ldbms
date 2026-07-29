from console import terminal as _terminal
from tools import index as _index
from tools import db_create as _dbs
from sql import db_functions as _db_functions
import sqlite3 as _sqlite3
import globals as _globals




#SHOW SUBCOMMANDS
def scmd_show_databases(_command ):
    headers = ["[bold yellow]Databases[/bold yellow]"]
    rows = []
    for key in _globals.global_indexed_databases.keys():
        rows.append([f"[bold white]{key}[/bold white]"])

    _terminal.print_generic_table(headers,rows,False)
    return True

def scmd_show_error(_command ):
    return False

def scmed_show_tables(command_obj :dict):
    query = command_obj['command']
    SHOW_TABLES = ("SELECT name FROM sqlite_schema WHERE type='table' AND name NOT LIKE 'sqlite_%'")
    try:
        data = _db_functions.execute_sql_query(SHOW_TABLES)
    except _sqlite3.Error as err:
        _terminal.console_errors(query,err,'Query failed!')
        return False
    except AttributeError:
        _terminal.console_errors(query,'Query failed to execute as there is no active database.','Query failed!')
        return False;

    print(data[1])
    for row in data[2]:
        print(*row);
    


#CREATE SUBCOMMANDS
def smd_ignore_execution(_command):
    return False

def scmd_create_database(command_obj :dict):
   command = command_obj['tokens']
   db_name = command[2]
   if  _dbs.create_database(_globals.PATH_DB_DATA,db_name):
        _index.write_index((_globals.PATH_DB_INDEX / _globals.filename_database_index),db_name,(_globals.PATH_DB_DATA / f"{db_name}.db"))
        _index.read_index((_globals.PATH_DB_INDEX / _globals.filename_database_index),_globals.global_indexed_databases)
        _terminal.print(f'[bold white]Created new database [bold green]{command[2]}[/bold green] at [italic yellow]"{(_globals.PATH_DB_DATA / command[2])}.db"') 
        return True
   else:
        _terminal.console_errors(command[1],f"Failed to create database named {command[1]}","Command couldn't be executed!")
        return False








#EXECUTE SQL QUERIES - NEEDS MORE WORK
def scmd_execute_sql(command_obj :dict):
    query = command_obj['command']
    try:
        sql_result = _db_functions.execute_sql_query(query)
    except _sqlite3.Error as err:
        _terminal.console_errors(query,err,'Query failed!')
        return False
    except AttributeError:
        _terminal.console_errors(query,'Query failed to execute as there is no active database.','Query failed!')
        return False;

    if sql_result[0] and not sql_result[1]:
        if sql_result[3] == -1 : sql_result[3] = 0
        _terminal.print(f'[bold white]Query successful. Rows affected {sql_result[2] }.[/bold white]')
        return True
