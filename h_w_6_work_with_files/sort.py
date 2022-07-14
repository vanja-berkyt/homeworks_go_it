import sys
import os
from pathlib import PurePath, Path

def inputs():
    list_of_inputs = sys.argv
    return list_of_inputs

list_of_commands = inputs()


list_all_files = []
list_all_files_pathes = []
dict_of_files = {}
image = []
video = []
music = []
archive = []
doc = []
else_file = []
list_of_known_suffixes = set()
list_of_unknown_suffixes = set()


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


all_list = files_in_dir(list_of_commands[1])
all_files = all_list[0]
all_files_pathes = all_list[1]


def sort_files(list_of_files:list):
    for file in list_of_files:
        sufix = PurePath(file).suffix
        if sufix in ('.jpeg', '.png', '.jpg', '.svg'):
            image.append(file)
            list_of_known_suffixes.add(sufix)
        elif sufix in ('.avi', '.mp4', '.mov', '.mkv'):
            list_of_known_suffixes.add(sufix)
            video.append(file)
        elif sufix in ('.mp3', '.ogg', '.wav', '.amr'):
            music.append(file)
            list_of_known_suffixes.add(sufix)
        elif sufix in ('.zip', '.gz', '.tar'):
            archive.append(file)
            list_of_known_suffixes.add(sufix)
        elif sufix in ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'):
            doc.append(file)
            list_of_known_suffixes.add(sufix)
        else:
            else_file.append(file)
            list_of_unknown_suffixes.add(sufix)

    dict_of_files.update({'image': image})
    dict_of_files.update( {'video': video})
    dict_of_files.update({'music': music})
    dict_of_files.update({'archive': archive})
    dict_of_files.update({'doc': doc})
    dict_of_files.update({'else': else_file})
    return dict_of_files


def normalize(file_adress: str):
    cyrylic_symbols_little = "абвгдеєжзийклмнопрстуфхцчшщьєюяії"
    cyrylic_symbols_big = "АБВГДЕЄЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЄЮЯІЇ"
    translation = (
    "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
    "f", "h", "ts", "ch", "sh", "sch", "", "je", "yu", "ya", "i", "ji")
    new_file_name = []
    for symbol in file_adress:
        if symbol.isalpha() or symbol.isdigit():
            if symbol in cyrylic_symbols_little:
                letter_index = cyrylic_symbols_little.find(symbol)
                new_file_name.append(translation[letter_index])
            elif symbol in cyrylic_symbols_big:
                letter_index = cyrylic_symbols_big.find(symbol)
                new_file_name.append(translation[letter_index].upper())
            else:
                new_file_name.append(symbol)
        else:
            new_file_name.append('_')
    new_file_name_string = ''.join(new_file_name)
    print(new_file_name_string)
    return new_file_name_string

def rename(adress:str):
    adress_splited = adress.split('/')
    full_name = adress_splited.pop()
    name = full_name.split('.', 1)
    print(name[1])
    name_normalized = normalize(name[0])
    file_name_new = name_normalized + '.' + name[1]
    print(file_name_new)
    adress_splited.append(file_name_new)
    new_name = '/'.join(adress_splited)
    os.rename(adress, new_name)
    return new_name




    # name = os.path.splitext(file_adress)[0]
    # os.rename(file, dst)

print(3)