from rich.table import Table as _Table
from rich import print
import sys as _sys

def print_help():
    table = _Table()
    table.add_column('[bold yellow]Command[/bold yellow]')
    table.add_column('[bold yellow]Arguments[/bold yellow]')
    table.add_column('[bold yellow]Usage[/bold yellow]')
    table.add_column('[bold yellow]Information[/bold yellow]')

    table.add_row('[bold green]create[/bold green]' ,'database , table','create database/table name','Create a new SQlite Database or a new table in an existing database.')
    table.add_row('[bold green]show[/bold green]'   ,'databases , tables ','show databases/tables','Show indexed databases or existing tables in the current database.')
    table.add_row('[bold green]use[/bold green]'    ,'database_name ','use database_name','Create a new SQlite Database or a new table in an existing database.')
    table.add_row('[bold green]desc[/bold green]'   ,'table_name','desc table_name','Describe a table in an existing database.')
    table.add_row('[bold green]load[/bold green]'   ,'file','load path_to_file.sql','Execute Queries from a file.')
    table.add_row('[bold green]index[/bold green]'  ,'database_name file','index database_name path_to_file.db','Index an existing SQLite database to be used from LDBMS')
    table.add_row('[bold green]describe[/bold green]'   ,'table_name','describe table_name','Describe a table in an existing database.')
    table.add_row('[bold green]unlist[/bold green]'   ,'database_name','unlist database_name','Unlist a database from LDBMS , Database remains unchanged.')
    table.add_row('[bold green]delete[/bold green]'   ,'database_name','delete database_name','Delete a database permanently.')
    table.add_row('[bold green]database[/bold green]'   ,'none','database','View the currently selected database.')
    table.add_row('[bold green]relocate[/bold green]'   ,'database_name relocation_path','relocate database_name relocation_path','Relocate a staged database into a custom location')
    table.add_row('[bold green]history[/bold green]'   ,'none','history','Print the previous successful commands on the terminal')
    table.add_row('[bold green]export[/bold green]'   ,'path_to_file.txt','export path_to_file.txt','Export the successful commands of the current commands in a text file.')
    table.add_row('[bold green]exit[/bold green]'   ,'none','exit','Quit the application.')
   
    if _sys.platform.startswith('win32'):
        table.add_row('[bold green]cls[/bold green]'   ,'none','cls','Clear terminal. (Windows Only)')
    else:
        table.add_row('[bold green]clear[/bold green]'   ,'none','clear','Clear terminal. (Linux/Mac OS Only)')


    table.add_row('[bold green]help[/bold green]'   ,'command','help command','Print this message or information about a specific command.')
    print(table)
    print('[bold white]The above listed commands are basic commands[/bold white]')
    print('Type [bold yellow]help command[/bold yellow] with any command to see detailed information')

def print_create_help():
    print('[bold yellow]create[bold yellow] - Create a database or a table')
    print('[bold white] create database database_name[/bold white] - Creates a database with the name "database_name" in the selected database')
    print('[bold white] create table table_name[/bold white] - Creates a table with the name "table_name" in the selected database')

    print('[bold yellow]NOTE:[/bold yellow]')
    print('The newly created database exists at [italic]~/.ldbms/databases/[/italic] , use [bold yellow]relocate database_name relocation_path[/bold yellow] to save at different location')

def print_show_help():
    print('[bold yellow]show[bold yellow] - Show databases or tables')
    print('[bold white]show databases[/bold white] - Show list of currently indexed databases.')
    print('[bold white]show tables[/bold white] - Show the tables in the current database')
    print('[bold yellow]NOTE:[/bold yellow]')
    print('The [bold yellow]show[bold yellow] command is unique to LDBMS and is not a standard SQLite Supported Query')
    print('The newly created database exists at [italic]~/.ldbms/databases/[/italic] also appear with a tag [bold red]staging[bold red]')
    
def print_use_help():
    print('[bold yellow]use[bold yellow] - Change the current database')
    print('[bold white]use database_name[/bold white] - Sets the current database to "database_name" , all queries henceforth affect "database_name"')
    print('If there are no indexed databases , the command will print [bold white]"Database not indexed or does not exist"[/bold white] , same for if the database is non existent ')
    print('[bold yellow]NOTE:[/bold yellow]')
    print('The newly created database exists at [italic]~/.ldbms/databases/[/italic] can be used by their name , using the path will cause an error.')
    print('The [bold yellow]use[bold yellow] command is unique to LDBMS and is not a standard SQLite Supported Query')
        
def print_index_help():
    print('[bold yellow]index[bold yellow] - Index/Register an existing database.')
    print('[bold white]index database_name path_to_file.db[/bold white] - Indexes the SQLite database located at [bold white]path_to-file.db[/bold white] under the name "database_name"')
    print('If the .db file is missing or corrupted , the command will print [bold white]"Database does not exist"[/bold white] , same for if the database is non existent ')
    print('[bold yellow]NOTE:[/bold yellow]')
    print('The newly created database exists at [italic]~/.ldbms/databases/[/italic] are automatically indexed under their respective name')
    print('The index command is used for regestering databases which were not created within LDBMS and exist at other file locations.')
            
def print_desc_help():
    print('[bold yellow]desc[bold yellow] - Describe the attributes (columns) of a given table')
    print('[bold white]desc table_name[/bold white] - Describe the attributes of the table "table_name".')
    print('[bold white]describe table_name[/bold white] - The [purple italic]describe[/purple italic] also works for describing a table')
    print('[bold yellow]NOTE:[/bold yellow]')
    print('The [bold yellow]desc[bold yellow] command is unique to LDBMS and is not a standard SQLite Supported Query')
    
def print_unlist_help():
    print('[bold yellow]unlist[bold yellow] - Unlist a database from the LDBMS Index ')
    print('[bold white]unlist database_name[/bold white] - Unlist an existing database , unlisted databases stop appearing in [bold white]show databases[/bold white]')
    print('[bold yellow]NOTE:[/bold yellow]')
    print('No data is affected when you unlist a database. It just removes its entry from the LDBMS Index. To permanently remove a database use [bold red]delete database_name[/bold red]')

def print_relocate_help():
    print('[bold yellow]relocate[bold yellow] - Relocate a database to another directory and automatically index with the new path')
    print('[bold white]relocate database_name new_database_path[/bold white] - Relocates "database_name" to "new_database_path" and re-indexes against "database_name"')
    print('[bold yellow]NOTE:[/bold yellow]')
    print('Relocation works for indexed databases only , providing paths for both the database_name and the database_path will cause an error.')
    
def print_load_help():
    print('[bold yellow]load[bold yellow] - Load a file containing LDBMS Commands')
    print('[bold white]load path_to_file.txt[/bold white] - Load a .txt file containing ldbms commands, they will be executed line by line till the end.')
    print('[bold yellow]NOTE:[/bold yellow]')
    print('All rules still apply to files , they need semicolon for termination and :/: for colapsing the terminal for multiline inputs.')
    print('If any errors are encountered , the subsequent commands will be skipped.')

def print_delete_help():
    print('[bold yellow]delete[bold yellow] - Permanently delete a database.')
    print('[bold red]delete database_name[/bold red] - Permenantly unlists a database and deletes the underlying .db file.')
    print('[bold yellow]NOTE:[/bold yellow]')
    print('The delete command is considered a dangerous command as it will remove the .db file , thus your data may be lost if backup is not prepared.')
    print('If you want to declutter the [bold white]show databases[/bold white] output use [bold green]unlist database_name[/bold green] This wiil preserve underlying .db file exactly where it was.')

def print_database_help():
    print('[bold yellow]database[bold yellow] - Get the name and path of the currently used database.')
    print('[bold white]database[/bold white] - Get the PATH and NAME of the current database. It print NONE if no database is being used ')
    print('[bold yellow]NOTE:[/bold yellow]')
    print('The output database command relflects the currently used database. To change databases run the [bold green]use database_name[/bold green] command')
    
def print_clear_help():
    print('[bold yellow]clear[bold yellow] - Clear the terminal screen.')
    print('[bold white]clear[/bold white] - Clears the LDBMS Terminal on Linux/Mac OS')
    print('[bold yellow]NOTE:[/bold yellow]')
    print('[bold white]clear[/bold white] works on Windows too. Compatibility has been handeled by LDBMS')

def print_cls_help():
    print('[bold yellow]cls[bold yellow] - Clear the terminal screen.')
    print('[bold white]cls[/bold white] - Clears the LDBMS Terminal on Windows')
    print('[bold yellow]NOTE:[/bold yellow]')
    print('[bold white]cls[/bold white] works on Linux/Mac OS too. Compatibility has been handeled by LDBMS')

def print_exit_help():
    print('[bold yellow]exit[bold yellow] - Exit the LDBMS Command Line Client')

def print_history_help():
    print('[bold yellow]history[bold yellow] - View the previous successful commands of the current session')

def print_export_help():
    print('[bold yellow]export[bold yellow] - Save the history of the session in a text file')
    print('[bold white]export path_to_file.txt[/bold white] - Export the successfull commands of the current session and save in a text file.')




