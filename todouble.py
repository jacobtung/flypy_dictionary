from pypinyin import pinyin, lazy_pinyin, Style

# local dir files

dict_old        = "dictionary.txt"
dict_new        = "dictionary_new.txt"
initials        = "initials.txt"
finals1         = "finals1.txt"
finals2         = "finals2.txt"

# functions 

def create_dict(textfile):
    dict = {}
    with open(textfile, "r", encoding="utf-8") as file:

        for line in file:
            (key, value) = line.split()
            dict[key] = value
    #print(dict)
    return dict

def change_initials_flypy(initials):
    """
    :param initials:
    :return:
    """
    return initials_dict.get(initials, "Invalid initials!")


def change_finals_flypy1(finals): 
    return finals1_dict[finals]

def change_finals_flypy2(finals): 
    return finals2_dict[finals]

# main function

# dir files to dict

initials_dict   = create_dict(initials)
finals1_dict    = create_dict(finals1)
finals2_dict    = create_dict(finals2)

# main loop

with open(dict_old, 'r', encoding='utf-8') as fp_dict_old:
    for line in fp_dict_old:

        words_han       = line.split()[1]
        words_flypy     = ""
        
        for word_han in words_han:

            word_initials   = lazy_pinyin(word_han, style=Style.INITIALS, strict=False)[0]
            #print(word_initials)
            word_finals     = lazy_pinyin(word_han, style=Style.FINALS, strict=False)[0]
            #print(word_finals)
            if word_initials == "":
                word_initials2  = ""
                word_finals2    = change_finals_flypy2(word_finals)
            else:
                word_initials2  = change_initials_flypy(word_initials)
                word_finals2    = change_finals_flypy1(word_finals)
            word_flypy    = word_initials2 + word_finals2
            #print(word_flypy)
            words_flypy = words_flypy + word_flypy
            line_flypy    = words_flypy + "\t" + words_han + "\t" + "zh-CN" + "\n"

        with open(dict_new, "a", encoding="utf-8") as file_dict_new:
            file_dict_new.write(line_flypy)

