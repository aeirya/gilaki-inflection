from gltk.verb_table import infinitive_past_lists
from gltk.fst import infinitive2past, past2present

from pyfoma import *
fsts = {}

infinitives, pasts = infinitive_past_lists()
fsts['verbs'] = FST.re('|'.join(infinitives))

fsts['tags'] = FST.re(
    "( '[Present]' | '[Past]' )" #+\
    # "( '[Sg]' | '[Pl]' )" +\
    # "( '[1p]' | '[2p]' | '[3p]' )"
    )

fsts['inf2past'] = infinitive2past.grammar
fsts['past2pre'] = past2present.grammar

fsts['lexicon'] = FST.re('$verbs $tags', fsts)

fsts['past'] = FST.re("$inf2past ('[Past]':'')", fsts)
fsts['present'] = FST.re(
    "($inf2past @ $past2pre) ('[Present]':'')",
    fsts)

fsts['grammar'] = FST.re("$lexicon @ ($past | $present) ", fsts)

print(Paradigm(fsts['grammar'], ".*"))
