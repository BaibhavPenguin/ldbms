from pathlib import Path as _Path
import json 

def read_index(index_file : _Path , global_index : dict ):
    try:
        with open(index_file,"r") as index:
            global_index.update(json.load(index))
    except json.JSONDecodeError:
        global_index.clear()

    return [True,f"[bold white]{len(global_index)} local databases indexed currently.[/bold white]"]
    

def write_index(index_file :_Path , db_name :str , db_path :str):
    resolved_path = _Path(db_path).resolve()
    if resolved_path.is_file():
        try:    
            with open(index_file,"r") as index:
                existing_records = json.load(index)
        except json.JSONDecodeError:
            existing_records = {}

        entry = {str(db_name) : str(resolved_path)}
        existing_records.update()
        existing_records.update(entry)
        with open(index_file,"w") as index:
            json.dump(existing_records,index)
        return [True,f"[bold white]Indexed database located at [italic green]{resolved_path}[/italic green] as [bold yellow]{db_name}[/bold yellow]"]  
     
    else:
        return [False,f"[italic]{resolved_path}[/italic] does not exist"]


def validate_indexed_databases(global_index :dict , index_file : _Path):
    for key in global_index.keys():
        if _Path(global_index[key]).is_file():
            pass
        else:
            global_index.pop(key)

    return len(global_index)

def update_index(index_file : _Path , global_index :dict , database_name :str):
    pass