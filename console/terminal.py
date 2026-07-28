import sys
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich import print


EXIT_CHARACTER = r'\c'
INLINE_CHARACTER = r'\\'

def console_greetings() -> None:
    print(Panel("[bold white]LDBMS v0.01 - Copyright 2026 Baibhav Bhattacharya[/bold white]"))
    print('[bold white]LDBMS - Lite Database Management Subsystem CLI[/bold white] is a command line wrapper around [bold yellow]SOLite[/bold yellow]')
    print('[bold white]LDBMS[/bold white] offers a similar experience to dbms as provided by production grade software such as [bold yellow]MySQL Command Line Client[/bold yellow] and' \
    ' [bold yellow]PostgresSQL[/bold yellow]')
    print('[bold white]LDBMS[/bold white] is developed by [bold white]Baibhav Bhattacharya[/bold white] and is licenced under [bold white]Apache 2.0 Open Source License[/bold white]')
    print('This software comes with [bold red]absolutely no warranty![/bold red] and is free and open source for anyone to use and modify.')
    print('Type [bold yellow]help[/bold yellow] to get started')

def console_errors(line : str , message :str , banner :str):
    print(Panel(line,title=f"[bold red]{banner}[/bold red]",title_align="right"))
    print(f"[bold red]{message}[/bold red]")

def console_goodbye():
    print(Panel('[bold yellow]Goodbye![/bold yellow]',title='[bold white]LDBMS - Lite Database Management Subsystem CLI [/bold white]',title_align='right'))

def prompt_user() -> str:
    string = str()
    try:
        string = Prompt.ask("[bold white]LDBMS [/bold white]")

        #Check whether command inlining is demamded
        while string.endswith(INLINE_CHARACTER):
            string = string.strip(INLINE_CHARACTER)

            #if Semicolon is there , means command needs execution
            if string.endswith(';'):            #Remove the inline character
                break
            #Semicolon not there , hence we prompt more
            substr = Prompt.ask("[bold white]   -> [/bold white]")

            #If the mysql ininling escape is entered, clear string and break
            if(substr.lower() == EXIT_CHARACTER):
                string = ''
                break

            #finally calculate the new conjoint string
            string = f"{string}{substr}"

        #Return raw user input
        return string
    
    except KeyboardInterrupt:
        return ''

    except EOFError:
        return 'exit;'

    except:
        print("[bold red]Error! Couldn't process keystrokes.")
        sys.exit(1)

def print_generic_table(columns :list, rows :list , lines=False):
    table = Table(show_lines=lines)
    for entry in columns:
        table.add_column(str(entry))

    for row in rows:
        table.add_row(*row)

    print(table)