from gltk.verb_table import read_full_verb_table
from gltk.fst import infinitive2past, past2present, verb_person

from pyfoma import *
fsts = {}

table = read_full_verb_table().sample(1)

fsts['present_stem_vocab'] = FST.re('|'.join(table['pres']))
fsts['past_stem_vocab'] = FST.re('|'.join(table['past']))
fsts['inf_vocab'] = FST.re('|'.join(table['inf']))
fsts['vocab'] = FST.re('$inf_vocab', fsts)

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

fsts['inf2past'] = infinitive2past.grammar
fsts['past2pre'] = past2present.grammar
fsts['verb_person'] = verb_person.grammar

fsts['past_stem'] = FST.re("$inf2past ('[Past]' | '[PastCont]')", fsts)
fsts['present_stem'] = FST.re(
    "($inf2past @ $past2pre) ('[Present]')",
    fsts)

fsts['stem'] = FST.re('($past_stem) | ($present_stem) ', fsts)
fsts['stemmer'] = FST.re("($stem $person_tag)", fsts)

fsts['delete_tags'] = FST.re("$^rewrite($tense_tag:'')", fsts)

fsts['lexicon'] = FST.re('$vocab $tags', fsts)
fsts['grammar'] = FST.re('$lexicon @ ($stemmer) @ ($verb_person) @ ($delete_tags)', fsts)

# print(Paradigm(verb_person.grammar, ".*"))
print(Paradigm(fsts['grammar'], ".*"))