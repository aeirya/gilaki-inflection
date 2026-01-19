from gltk.verb_table import read_full_verb_table
from gltk.fst import infinitive2past, past2present, verb_person

import pandas as pd

from pyfoma import *
fsts = {}

def de_prefix_table():
    return pd.DataFrame({
        'inf': ["dukudən", "dəkəftən", "kudən", "kəftən", "bostən"],
        'past': ["dukud", "dəkəft", "kud", "kəft", "bost"],
        'pres': ["dukun", "dəkəf", "kun", "kəf", "bo"],
    })

table = de_prefix_table()


# print(Paradigm(fsts['inf'], ".*"))
# print(Paradigm(fsts['simple_inf'], ".*"))


def join(*args):
    return f"({'|'.join(args)})"

# lexicon
fsts['inf'] = FST.re(f"({'|'.join(table['inf'])})") 
fsts['simple_inf'] = FST.re("$inf @ ~((du | də) .*)", fsts)

fsts['class_D'] = FST.re(join('kudən', 'kəftən', 'xadən'))
fsts['class_F'] = FST.re(join(
    'kudən', 'bostən', 'rəsen', 
    'giftən', 'dan', 'nderəsten', 
    'kəšen', 'turkəstən'
    ))
fsts['class_VA'] = FST.re(join(
    'gərdəstən', 'kəftən', 'kudən', 
    'ven', 'vərsen'
    ))
fsts["class_CHA"] = FST.re("kudən")
fsts["class_TA"]  = FST.re("vədan")
fsts["class_U"]   = FST.re("sadən")

# morphotactics
fsts["NEG"] = FST.re("'[neg]':(nə)")

fsts["D_path"]  = FST.re("'[der]':(D) ($NEG)? $class_D", fsts)
fsts["F_path"]  = FST.re("'[der]':(F) ($NEG)? $class_F", fsts)
fsts["VA_path"] = FST.re("'[der]':(va) ($NEG)? $class_VA", fsts)

fsts["CHA_path"] = FST.re("'[der]':(ča) ($NEG)? $class_CHA", fsts)
fsts["TA_path"]  = FST.re("'[der]':(ta) ($NEG)? $class_TA", fsts)
fsts["U_path"]   = FST.re("'[der]':(u)  ($NEG)? $class_U",  fsts)

fsts["DERIVED"] = FST.re("$D_path | $F_path | $VA_path | $CHA_path | $TA_path | $U_path", fsts)
fsts["SIMPLE"] = FST.re("'[tense]':(B | $NEG) $simple_inf", fsts)

fsts["MORPH"] = FST.re("$DERIVED | $SIMPLE", fsts)

fsts["D_allo"] = FST.re(
    "$^rewrite((D):(də) / # _ . (a|ə)) @ "
    "$^rewrite((D):(du) / # _ . (a|u))"
)

fsts["F_allo"] = FST.re(
    "$^rewrite((F):(fu) / # _ . (o|u)) @ "
    "$^rewrite((F):(fa) / # _)"
)

fsts["B_allo"] = FST.re(
    "$^rewrite((B):(bi) / # _ . i) @ "
    "$^rewrite((B):(bu) / # _ . (o|u)) @ "
    "$^rewrite((B):(bə) / # _ . ə) @ "
    "$^rewrite((B):(bə) / # _)"
)

fsts['allo'] = FST.re('$D_allo @ $F_allo @ $B_allo', fsts)

fsts["grammar"] = FST.re("$MORPH @ $allo", fsts)

print(Paradigm(fsts['grammar'], ".*"))

# print(list(
#     fsts['prefixes'].analyze('dəkəftən')
# ))
# print(table)