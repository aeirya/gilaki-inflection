from gltk.verb_table import infinitive_past_lists

from pyfoma import *
fsts = {}

infinitives, pasts = infinitive_past_lists()

fsts['verb_infs'] = FST.re('|'.join(infinitives))
fsts['verb_pasts'] = FST.re('|'.join(pasts))

fsts['suffix_tags'] = FST.re("('[Past]'):''")

fsts['lexicon'] = FST.re('$verb_infs $suffix_tags', fsts)


fsts['əstən_suffix'] = FST.re("$^rewrite((əstən):(əst) / _ #)")
fsts['tən_suffix'] = FST.re("$^rewrite((tən):(t) / _ #)")
fsts['dən_suffix'] = FST.re("$^rewrite((dən):(d) / _ #)")
fsts['tən_suffix_group'] = FST.re("$əstən_suffix @ $tən_suffix @ $dən_suffix", fsts)

fsts['een_suffix'] = FST.re("$^rewrite((en):'' / e _ #)")
fsts['en_suffix'] = FST.re("$^rewrite((en):(e) / _ #)")
fsts['an_suffix'] = FST.re("$^rewrite((an):(a) / _ #)")
fsts['en_suffix_group'] = FST.re("$een_suffix @ $en_suffix @ $an_suffix", fsts)

fsts['remove_suffix'] = FST.re("$tən_suffix_group @ $en_suffix_group", fsts)

fsts['grammar'] = FST.re('$lexicon @ $remove_suffix @ $verb_pasts', fsts)

print(Paradigm(fsts['grammar'], ".*"))
