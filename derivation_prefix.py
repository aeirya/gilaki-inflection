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

fsts['inf'] = FST.re(f"({'|'.join(table['inf'])})") 
fsts['simple_inf'] = FST.re("$inf @ ~((du | də) .*)", fsts)

# print(Paradigm(fsts['inf'], ".*"))
# print(Paradigm(fsts['simple_inf'], ".*"))

def join(*args):
    return f"({'|'.join(args)})"

# fsts['inf_vocab']
fsts['du_infinitives'] = FST.re(join('kudən', 'kəftən', 'xadən'))
fsts['d_prefix_insert'] = FST.re("'[də-prefix]':('dD') $du_infinitives", fsts)
fsts['də_prefix'] = FST.re("$^rewrite(('dD'):(də)/ # _ . (a | ə))")
fsts['du_prefix'] = FST.re("$^rewrite(('dD'):(du)/ # _ . (a | u))")
fsts['d_prefix'] = FST.re("$d_prefix_insert @ $də_prefix @ $du_prefix", fsts)

fsts['fu_infinitives'] = FST.re(join(
    'kudən', 'bostən', 'rəsen', 'giftən', 'dan', 'nderəsten', 'kəšen', 'turkəstən'
    ))
fsts['fa_prefix_insert'] = FST.re("'[fa-prefix]':(fa) $fu_infinitives", fsts)
fsts['fu_prefix'] = FST.re("$^rewrite((fa):(fu) / # _ . (o|u))")
fsts['fa_prefix'] = FST.re("$fa_prefix_insert @ $fu_prefix", fsts)

fsts['va_infinitives'] = FST.re(join('gərdəstən', 'kəftən', 'kudən', 'ven', 'vərsen'))
fsts['va_prefix'] = FST.re("'[va-prefix]':(va) $va_infinitives", fsts)

fsts['b_prefix_insert'] = FST.re("'[bu-prefix]':('bB') $simple_inf", fsts)
fsts['bi_prefix'] = FST.re("$^rewrite(('bB'):(bi)/ # _ . i)")
fsts['bu_prefix'] = FST.re("$^rewrite(('bB'):(bu)/ # _ . (o|u))")
fsts['bə_prefix'] = FST.re("$^rewrite(('bB'):(bə)/ # _ . ə)")
fsts['b_prefix'] = FST.re("$b_prefix_insert @ $bi_prefix @ $bu_prefix @ $bə_prefix", fsts)

fsts['rare_prefixes'] = FST.re('|'.join([
    "('[ča-prefix]':(ča) (kuddən))",
    "('[ta-prefix]':(ta) (vədan))",
    "('[u-prefix]':(u) (sadən))"
]))


fsts['prefixes'] = FST.re("$b_prefix | $d_prefix | $fa_prefix | $va_prefix | $rare_prefixes", fsts)

fsts['grammar'] = FST.re("$prefixes", fsts)
print(Paradigm(fsts['grammar'], ".*"))

# print(list(
#     fsts['prefixes'].analyze('dəkəftən')
# ))
# print(table)