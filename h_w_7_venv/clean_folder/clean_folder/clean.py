import sys
import os
import shutil

from all_files import files_in_dir
from sorted_files import sort_files, dict_of_files, list_of_known_suffixes, list_of_unknown_suffixes
from remove_dirs import rem_dir

def name_from_path(pas):
    ''' take path to file and return file name

    :param pas: path to file (/home/text.txt)
    :return: file mame       (text)
    '''
    split_path = os.path.split(pas)
    split = os.path.splitext(split_path[1])
    file_name = split[0]
    return file_name

def unpack(pas):
    '''
    unpack archives into new directory, named like archive
    :param pas: path to archive
    :return: None
    '''
    arch_name = name_from_path(pas)
    os.makedirs(arch_name,exist_ok=True)
    dest = MAIN_PATH +"/" + "archive"+ "/" + arch_name
    try:
        shutil.unpack_archive(pas, dest)
        os.remove(pas)
    except OSError as e:
        print(e.strerror)
        shutil.move(path, MAIN_PATH + '/' + 'else_file')


input_comand = sys.argv
MAIN_PATH = input_comand[1]                 # main path where will be created dict with sorted files

sort = files_in_dir(MAIN_PATH)              #sorted all dict and files
all_files = sort[0]
all_files_pathes = sort[1]
all_sub_dir = sort[2]

sort_files(all_files_pathes)
for key, value in dict_of_files.items():
    os.makedirs(MAIN_PATH + '/' + key, exist_ok=True)
    if key == 'archive':
        for path in value:
            unpack(path)
    else:
        for path in value:
            try:
                shutil.move(path, MAIN_PATH + '/' + key)
            except OSError as e:
                print('file alredy copeid')
            finally:
                continue
rem_dir(all_sub_dir)

print(f'Files found and sorted {all_files} ')
print(f'list of known suffixes: {list_of_known_suffixes}')
print(f'list of UNknown suffixes: {list_of_unknown_suffixes}')