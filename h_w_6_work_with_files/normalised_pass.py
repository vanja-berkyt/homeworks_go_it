
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

    return new_file_name_string