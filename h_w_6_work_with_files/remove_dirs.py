from pathlib import Path

def rem_dir(list_dir: list):
    '''
    func take list with pathes to directories where all files were removed(sorted to another dir) and return list of
    errors or empty if None
    '''
    list_of_errors = []
    for dirs in list_dir:
        dir_path = Path(dirs)
        try:
            dir_path.rmdir()
        except OSError as e:
            list_of_errors.append(e.strerror)
        finally:
            continue
    return list_of_errors