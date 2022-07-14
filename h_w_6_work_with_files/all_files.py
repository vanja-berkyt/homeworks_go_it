import os


list_all_files = []
list_all_files_pathes = []

def files_in_dir(dir_path: str):
    list_of_files = os.listdir(dir_path)

    for i in list_of_files:
        path = dir_path + '\\' + i

        if os.path.isdir(path):
            files_in_dir(path)
        if os.path.isfile(path):
            list_all_files.append(i)
            list_all_files_pathes.append(path)

    return list_all_files, list_all_files_pathes