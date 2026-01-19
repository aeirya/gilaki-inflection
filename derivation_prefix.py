from gltk.verb_table import read_full_verb_table
from gltk.fst import infinitive2past, past2present, verb_person

import pandas as pd

from pyfoma import *
fsts = {}

def de_prefix_table():
    return pd.DataFrame({
        'inf': ["dukudən", "dəkəftən", "kudən", "kəftən"],
        'past': ["dukud", "dəkəft", "kud", "kəft"],
        'pres': ["dukun", "dəkəf", "kun", "kəf"],
    })

table = de_prefix_table()

fsts['inf'] = FST.re(f"({'|'.join(table['inf'])})") 
fsts['simple_inf'] = FST.re("$inf @ ~((du | də) .*)", fsts)

# print(Paradigm(fsts['inf'], ".*"))
# print(Paradigm(fsts['simple_inf'], ".*"))

# fsts['inf_vocab']
fsts['d_prefix_insert'] = FST.re("'[də-prefix]':('dD') $simple_inf", fsts)
fsts['də_prefix'] = FST.re("$^rewrite(('dD'):(də)/ # _ . (a | ə))")
fsts['du_prefix'] = FST.re("$^rewrite(('dD'):(du)/ # _ . (a | u))")
fsts['d_prefix'] = FST.re("$d_prefix_insert @ $də_prefix @ $du_prefix", fsts)

fsts['fa_prefix_insert'] = FST.re("'[fa-prefix]':(fa) $simple_inf", fsts)
fsts['fu_prefix'] = FST.re("$^rewrite((fa):(fu) / # _ . (o|u))")
fsts['fa_prefix'] = FST.re("$fa_prefix_insert @ $fu_prefix", fsts)

fsts['va_prefix'] = FST.re("'[va-prefix]':(va) $simple_inf", fsts)

fsts['prefixes'] = FST.re("$d_prefix | $fa_prefix | $va_prefix", fsts)

fsts['grammar'] = FST.re("$prefixes", fsts)
print(Paradigm(fsts['grammar'], ".*"))

# print(list(
#     fsts['prefixes'].analyze('dəkəftən')
# ))
# print(table)