import re
from gltk.phonemes import special_letters

def _wrap(char):
    return f"\'{char}\'"

# unwrapped symbols
_symbols = "- , ! . :".split()

symbols = [_wrap(x) for x in _symbols]

special_chars = special_letters + _symbols

def normalize_char(x):
    return _wrap(x) if x in special_chars else x

def normalize(word):
    for c in special_chars:
        word = word.replace(c, _wrap(c))
    return word
