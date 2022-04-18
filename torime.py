from pypinyin import pinyin, lazy_pinyin, Style

# local dir files

dict_old        = "dictionary.txt"
dict_new        = "dictionary_rime.txt"

# functions 

# main function

# main loop

with open(dict_old, 'r', encoding='utf-8') as fp_dict_old:
    for line in fp_dict_old:

        words_han       = line.split()[1]
        words_rime     = ""
        
        for word_han in words_han:
            word_rime   = lazy_pinyin(word_han)[0]
            words_rime = words_rime + " " + word_rime
            line_rime  = words_han + "\t" + words_rime + "\t" + "1" + "\n"

        with open(dict_new, "a", encoding="utf-8") as file_dict_new:
            file_dict_new.write(line_rime)

