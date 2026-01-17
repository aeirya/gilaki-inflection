from gltk.verb_table import infinitive_past_lists

from pyfoma import *
fsts = {}

infinitives, pasts = infinitive_past_lists()
fsts['verbs'] = FST.re('|'.join(infinitives))

fsts['suffixes'] = FST.re(
    "( '[Present]' | '[Past]' )" #+\
    # "( '[Sg]' | '[Pl]' )" +\
    # "( '[1p]' | '[2p]' | '[3p]' )"
    )

fsts['lexicon'] = FST.re('$verbs $suffixes', fsts)
fsts['grammar'] = FST.re('$lexicon', fsts)

print(Paradigm(fsts['grammar'], ".*"))
