from pathlib import Path as _Path

def create_database(default_path : _Path , db_name):
    _Path(default_path).mkdir(parents=True,exist_ok=True)
    database_file = _Path(default_path / f"{db_name}.db")
    database_file.touch(exist_ok=True)
    return True

def remove_database(db_path : _Path):
    if db_path.is_file():
        db_path.unlink(missing_ok=True)
        return True
    else:
       return False