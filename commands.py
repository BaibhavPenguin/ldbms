from console import terminal as _terminal
from console import help as _helper
from tools import history as _history
from tools import index as _index
from pathlib import Path as _Path
import sys as _sys
import os as _os
import globals as _globals
import routines as _routines
import sub_command as _scmd

from sql import db_functions as _db_functions





def parse(line :str):
    if line == '' : return ''
    clean_line = line.strip()
    if clean_line.endswith(';'):
        clean_line = clean_line.rstrip(';')
    else:
        _terminal.console_errors(line,'Command not terminated correctly, Missing ";"',"Command couldn't be executed!")
        return
    return clean_line

def tokenizer(clean_string :str) -> str:
    if not clean_string : return []
    return clean_string.split()

#Handlers
def _command_help(command : list):
    if len(command) > 2:
        _terminal.console_errors(command[1],'The [bold white]help[/bold white] command only takes a single argument.','Extra arguments recieved!')
        return False
    _ARG_TABLE = {
        'default' : _helper.print_help,
        'create' : _helper.print_create_help,
        'show'   : _helper.print_show_help,
        'use'    : _helper.print_use_help,
        'index'  : _helper.print_index_help,
        'desc'   : _helper.print_desc_help,
        'describe' : _helper.print_desc_help,
        'unlist' : _helper.print_unlist_help,
        'relocate' : _helper.print_relocate_help,
        'load'  : _helper.print_load_help,
        'delete' : _helper.print_delete_help,
        'clear' : _helper.print_clear_help,
        'exit' : _helper.print_exit_help,
        'database' : _helper.print_database_help,
        'cls': _helper.print_cls_help,
        'history' : _helper.print_history_help,
        'export' : _helper.print_export_help,
    }
    try:
        argument  = command[1].lower()
    except:
        argument = 'default'

    try:
        _ARG_TABLE[argument]()
        return True
    except KeyError:
        _terminal.console_errors(argument,f'{argument} is not a valid argument for the help command.','Invalid arguments recieved!')
        return False

def _command_clear(command : list):
    if len(command) > 1:
        _terminal.console_errors(command[1],'The [bold white]clear and cls[/bold white] command takes no arguments.','Extra arguments recieved!')
        return False
    _os.system('cls' if _os.name == 'nt' else 'clear')
    return True

def _command_exit(command):
    if len(command) > 1:
        _terminal.console_errors(command[1],'The [bold white]exit[/bold white] command takes no arguments.','Extra arguments recieved!')
        return False
    print()
    _routines.cleanup_ldbms_enviornment()
    _terminal.console_goodbye()
    _sys.exit(0)

def _command_history(command):
    if len(command) > 2:
        _terminal.console_errors(command[1],'The [bold white]history[/bold white] command takes a single argument.','Extra arguments recieved!')
        return False

   
    cols = ['[bold yellow]Session History[/bold yellow]']
    rows = []
    try:
        for entry in _globals.global_history:
            rows.append([entry])
    except IndexError:
        rows.append(['No History'])

    _terminal.print_generic_table(cols,rows,False)

def _command_export(command):
    if len(command) > 2:
        _terminal.console_errors(command[1],'The [bold white]export[/bold white] command only takes a single argument.','Extra arguments recieved!')
        return False;
    result = _history.export_history(_Path(command[1]) , (_globals.SESSION_HISTORY_PATH / _globals.filename_session_history))
    if result[0]:
        _terminal.print(result[1])
        _terminal.print(result[2])
        return True
    else:
        _terminal.console_errors(result[2],result[3],result[1])
        return False

def _command_index(command):
    if len(command) != 3:
        _terminal.console_errors(command[0],f"index command requires three arguments index <database_name> <database_path> , {len(command) - 1} provided!","Too few arguments!")   
        return False
    result = _index.write_index((_globals.PATH_DB_INDEX / _globals.filename_database_index),command[1],command[2])
    if result[0]:
        _terminal.print(result[1])
        _index.read_index((_globals.PATH_DB_INDEX / _globals.filename_database_index),_globals.global_indexed_databases)
        return True
    else:
        _terminal.console_errors(command[3],result[1],"Invalid path provided!")
    
def _command_show(command):

    if len(command) < 2:
        _terminal.console_errors(command[0],'show command takes atleast 1 argument , 0 provided!','Too few arguments recieved!')
        return False
    
    _ARGUMENT_LIST = {
        'databases' : _scmd.scmd_show_databases,
        'tables' : print,
        'columns' : print,
        'index' : print,
        'create' : print,
        'triggers' : print,
        'variables' : print,
    }
    try:
        arg = command[1].lower()
        _ARGUMENT_LIST[arg](command)
        return True
    except KeyError:
        _terminal.console_errors(arg,f'{arg} is not a valid argument for the show command.','Invalid arguments recieved!')
        return False

def _command_create(command):
    if len(command) < 3:
        _terminal.console_errors(command[0],'create command takes atleast 2 arguments , less than two provided provided!','Too few arguments recieved!')
        return False

    _ARGUMENT_LIST = {
        'database' : _scmd.scmd_create_database,
    }
    try:
        arg = command[1].lower()
        result = _ARGUMENT_LIST[arg](command)
        if result:
            _terminal.print(f'[bold white]Created new database [bold green]{command[2]}[/bold green] at [italic yellow]"{(_globals.PATH_DB_DATA / command[2])}.db"') 
            return True
        else:
            _terminal.console_errors(command[1],f"Failed to create database named {command[1]}","Command couldn't be executed!")
            return False
    except KeyError:
        _terminal.console_errors(arg,f'{arg} is not a valid argument for the create command.','Invalid arguments recieved!')
        return False

def _command_use(command):
    if len(command) > 2:
        _terminal.console_errors(command[1],'The [bold white]use[/bold white] command only takes a single argument.','Extra arguments recieved!')
        return False
    elif len(command) < 2:
        _terminal.console_errors(command[0],'The [bold white]use[/bold white] command takes a single argument, 0 provided!','Too few arguments recieved!')
        return False

    db_name = command[1]
    try:
        db_path = _globals.global_indexed_databases[db_name]
    except KeyError:
        _terminal.console_errors(db_name,f'{db_name} is not indexed or does not exist.',f'Tried to use an invalid database namely , {db_name}')
        return False

    _db_functions.update_current_db(db_name,db_path)
    _terminal.print(f'[bold white]Database changed, All subsequent queries will affect [bold green]{db_name}[/bold green][/bold white]')
    return True

def _command_database(command):
    current_database = _db_functions.get_current_database()
    _terminal.print(f'[bold white]Currently addressing [bold green]{current_database[0]}[/bold green][/bold white]')
    _terminal.print(f'[bold white]Database path : [bold yellow]{current_database[1]}[/bold yellow][bold white]')
    return True

_COMMAND_LIST = {
    "clear" : _command_clear,
    "cls"   : _command_clear,
    "show"  : _command_show,
    "create" : _command_create,
    "use" : _command_use,
    "desc" : _command_help,
    "load" : _command_help,
    "describe" : _command_help,
    "delete" : _command_help,
    "config" : _command_help,
    "help" : _command_help,
    "exit" : _command_exit,
    "history" : _command_history,
    "export" : _command_export,
    "index" : _command_index,
    "database" : _command_database,

}

def execute(command :list):
    try:
        result = _COMMAND_LIST[command[0].lower()](command)
        return result
    except KeyError:
        return False
    except IndexError:
        return False


