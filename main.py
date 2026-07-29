from console import terminal
from console import help as helper
from tools import history
from tools import index
import globals
import commands
import routines


#Bootup Initialization Code
routines.setup_ldbms_enviornment()
terminal.console_greetings()
db_count = index.validate_indexed_databases(globals.global_indexed_databases,(globals.PATH_DB_INDEX / globals.filename_database_index))
terminal.print(f"[bold white]Databases currently indexed : [/bold white][bold green]{db_count}[/bold green]")

#Main Loop
while(True):
    user_input = terminal.prompt_user()
    if not user_input:
        continue
    line = commands.parse(user_input)
    tokens = commands.tokenizer(line)
    command = {'tokens' : tokens, 'command' : line}
    result = commands.execute(command)

    if result:
        history.history_add_command(line,(globals.SESSION_HISTORY_PATH / globals.filename_session_history),globals.global_history)
        



