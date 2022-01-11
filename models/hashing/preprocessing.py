import pandas as pd
from jellyfish import metaphone, soundex, nysiis, match_rating_codex
import string
import re

    

def pre_phonetic_encoding(name, method = 'metaphone'):
    if method == 'codex':
        return match_rating_codex(name)
    elif method == 'metaphone':
        return metaphone(name)
    else:
        raise ValueError("Encoding Method not known: specify either codex or metaphone")
        
        
def pre_string_clean(name):
    table = str.maketrans('', '', "!#$%&'()*+,./:;<=>?@[\]^_`{|}~")
    return re.sub("[0-9]+", "", name).lower().translate(table)


def tokenize(name):
    return re.sub("[^\S]+", " ", name).split(" ")


def pre_sort_names(tokenized_names):
    return sorted(list(set(tokenized_names)))




if __name__ == '__main__':
    print(pre_phonetic_encoding("Celeste"))
    print(pre_phonetic_encoding("Celeste", 'codex'))
    print(pre_string_clean("celESe58*%!"))
    print(metaphone("JellyFish"))
    print(soundex("JellyFish"))
    print(nysiis("JellyFish"))
    print(match_rating_codex("JellyFish"))
    print(tokenize("J ell.   y   fi sh"))
    print(pre_sort_names(tokenize("J ell.   y   fi sh")))
    