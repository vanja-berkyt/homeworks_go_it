import os

list_all_files = []
list_all_files_pathes = []
list_all_dir = []

def files_in_dir(dir_path: str):
    '''
    recursively find all files in this and sub directories
    :param dir_path: path to dir in which we want to see all files
    :return: tuple of lists : list of all files[0] , list of all pathes for all files[1], pathes
    for all directors inside[2]
    '''
    list_of_files = os.listdir(dir_path)

    for i in list_of_files:
        path = dir_path + '\\' + i
        if os.path.isdir(path):
            files_in_dir(path)
            list_all_dir.append(path)
        elif os.path.isfile(path):
            list_all_files.append(i)
            list_all_files_pathes.append(path)
        else:
            print('unknowed type')
    return list_all_files, list_all_files_pathes, list_all_dir
