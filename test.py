from gltk.std import symbols, normalize
from gltk.reader import read_lines
from gltk.phonemes import vowels, consonants

from pyfoma import *
fsts = {}

words = []
for line in read_lines('gltk/words.txt'):
    for word in line.split():
        words.append(normalize(word))

fsts['alphabet'] = FST.re(f"({'|'.join(vowels + consonants + symbols)})*")
W = words

fsts['words'] = FST.re('|'.join([w for w in W]))
fsts['grammar'] = FST.re("$words @ $alphabet", fsts)

print(Paradigm(fsts['grammar'], ".*"))
