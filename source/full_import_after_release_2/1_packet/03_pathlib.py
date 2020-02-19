from pathlib import Path
path_obj = Path('.')
some_obj = [x for x in path_obj.iterdir() if x.is_dir()]

files = list(path_obj.iterdir())
path_obj.is_dir()
path_obj.is_dir()