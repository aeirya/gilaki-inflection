from gltk.verb_table import read_full_verb_table
from pyfoma import *

fsts = {}

table = read_full_verb_table()

# fsts['present_stem_vocab'] = FST.re('|'.join(table['pres']))
# fsts['past_stem_vocab'] = FST.re('|'.join(table['past']))
fsts['inf_vocab'] = FST.re('|'.join(table['inf']))
# fsts['vocab'] = FST.re('$inf_vocab', fsts)

fsts['person_tag'] = FST.re(
    "( '[1p,Sg]' | '[2p,Sg]' | '[3p,Sg]' | '[1p,Pl]' | '[2p,Pl]' | '[3p,Pl]' )"
)
fsts['tense_tag'] = FST.re(
    "( '[Present]' | '[Past]' | '[PastCont]')"
)

fsts['tags'] = FST.re(''.join([
    "$tense_tag",
    "$person_tag",
    ]), fsts)

fsts['present_person_ending'] = FST.re(
    "|".join([
        "('[1p,Sg]'):(əm)",
        "('[2p,Sg]'):(i)",
        "('[3p,Sg]'):(e)",
        "('[1p,Pl]'):(im)",
        "('[2p,Pl]'):(id)",
        "('[3p,Pl]'):(id)",
    ]))

fsts['past_person_ending'] = FST.re(
    "|".join([
        "('[1p,Sg]'):(əm)",
        "('[2p,Sg]'):(i)",
        "('[3p,Sg]'):(ə)",
        "('[1p,Pl]'):(im)",
        "('[2p,Pl]'):(id)",
        "('[3p,Pl]'):(id)",
    ]))

fsts['past_cont_person_ending'] = FST.re(
    "|".join([
        "('[1p,Sg]'):(im)",
        "('[2p,Sg]'):(i)",
        "('[3p,Sg]'):(i)",
        "('[1p,Pl]'):(im)",
        "('[2p,Pl]'):(id)",
        "('[3p,Pl]'):(id)",
    ]))


# fsts['lexicon'] = FST.re('$inf_vocab @ $tags', fsts)
fsts['present'] = FST.re("('[Present]') ($present_person_ending)", fsts)
fsts['past'] = FST.re("('[Past]') ($past_person_ending)", fsts)
fsts['tag_grammar'] = FST.re('.* ($tags @ (($present | $past)))', fsts)

# fsts['grammar']   = FST.re('($inf_vocab $tags) @ $tag_grammar', fsts)
# print(Paradigm(fsts['grammar'], ".*"))

grammar = fsts['tag_grammar']
