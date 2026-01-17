
# note for ĕ:
# In a position after the consonant y and also after other consonants, including the tongue in a mid-position (š, č, ǰ), ə is pronounced with the tongue much further forward in the mouth, coming closer in phonation to e: šənå ‘swimming’; ǰəngəl ‘wood(s)’; yək ‘one’ (they are pro- nounced: šĕnå, ǰĕngəl, yĕk).

special_char_vowels = "ə ı̄ ū å á ú í ə́".split()
special_char_consonants = "č ǰ ɣ ž".split() # no š
special_letters = special_char_vowels + special_char_consonants


def get_vowels():
    ascii_vowels = 'i e a o u'.split()
    # extra_phonetics = "'ĕ'"
    return ascii_vowels + special_char_vowels


def get_consonants():
    return ' '.join([
        "p b t d k g",
        "č ǰ",
        "m n",
        "f v y x ɣ h",
        "s z",
        "š ž",
        "l",
        "r"
    ]).split()


vowels = get_vowels()
stable_vowels = "ı̄ ū å e o".split()
unstable_vowels ="ə u i".split()

consonants = get_consonants()

