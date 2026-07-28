from pathlib import Path as _Path

_history_block = []
def history_add_command(item :str , session_history : _Path, recent_history : list):
    if len(recent_history) >= 10:
        recent_history.pop(0)       #Circulate Recent history for ui logic

    if len(_history_block) >= 5:
        _save_session_history(session_history)
        _history_block.clear()    #Clean up persistent history
    
    recent_history.append(item)
    _history_block.append(item)


def load_session_history():
    pass

def _save_session_history(session_history :_Path):
    with open(session_history,"a") as file:
        for item in _history_block:
            #print(item)            #Debug
            file.write(f"{item}\n")


def export_history(export_file : _Path , session_history : _Path):

    try:
        export_file.touch(exist_ok=True,)
    except FileNotFoundError:
        return [False,'[bold red]Export Failed![/bold red]',f'{export_file}',f"Couldn't create file structure  [italic]'{export_file}'[/italic], Parent folders missing!."] 

    with open(session_history, "rb") as src:
        binary_data = src.read()

    text_data = binary_data.decode("utf-8")
    with open(export_file,"a") as export:
        export.write(text_data)
        if _history_block and len(_history_block) < 5 :
            for item in _history_block:
                export.write(f"{item}\n")

    return [True,'[bold green]Expot Completed![/bold green]',f"[bold white]Session history saved at [italic]'{export_file}'[/italic][/bold white]"]