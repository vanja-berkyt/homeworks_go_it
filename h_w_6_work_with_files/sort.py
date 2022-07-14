import sys
import os
import shutil
import pathlib
from all_files import files_in_dir
from sorted_files import sort_files
from normalised_pass import normalize
from sorted_files import dict_of_files

input_comand = sys.argv
MAIN_PATH = input_comand[1]             # main path where will be created dict with sorted files
all_list = files_in_dir(MAIN_PATH)               #sorted all dict and files
all_files = all_list[0]                          #list of ALL files
all_files_pathes = all_list[1]                   #list of PASES for all files
sort_files(all_files_pathes)

for key, value in dict_of_files.items():
    os.makedirs(MAIN_PATH + '/' + key, exist_ok=True)
    for path in value:
        shutil.move(path, MAIN_PATH + '/' + key)
        try:
            path = pathlib.Path(path)
            path.rmdir()
        except ValueError:
            print('dir is not empty')
        finally:
            continue


    print(key, value)





# def normalize(file_adress: str):
#     cyrylic_symbols_little = "абвгдеєжзийклмнопрстуфхцчшщьєюяії"
#     cyrylic_symbols_big = "АБВГДЕЄЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЄЮЯІЇ"
#     translation = (
#     "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
#     "f", "h", "ts", "ch", "sh", "sch", "", "je", "yu", "ya", "i", "ji")
#     new_file_name = []
#     for symbol in file_adress:
#         if symbol.isalpha() or symbol.isdigit():
#             if symbol in cyrylic_symbols_little:
#                 letter_index = cyrylic_symbols_little.find(symbol)
#                 new_file_name.append(translation[letter_index])
#             elif symbol in cyrylic_symbols_big:
#                 letter_index = cyrylic_symbols_big.find(symbol)
#                 new_file_name.append(translation[letter_index].upper())
#             else:
#                 new_file_name.append(symbol)
#         else:
#             new_file_name.append('_')
#     new_file_name_string = ''.join(new_file_name)
#     print(new_file_name_string)
#     return new_file_name_string

def rename(adress: str):
    adress_splited = adress.split('/')
    full_name = adress_splited.pop()
    name = full_name.split('.', 1)
    name_normalized = normalize(name[0])
    file_name_new = name_normalized + '.' + name[1]
    adress_splited.append(file_name_new)
    new_name = '/'.join(adress_splited)
    os.rename(adress, new_name)
    return new_name



