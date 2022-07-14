
from pathlib import PurePath

image = []
video = []
music = []
archive = []
doc = []
else_file = []
list_of_known_suffixes = set()
list_of_unknown_suffixes = set()
dict_of_files = {}

def sort_files(list_of_pathes:list):
    for file in list_of_pathes:
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