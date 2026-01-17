from gltk.verbs import read_verb_table, past_present_lists

from pyfoma import *
fsts = {}

pasts, presents = past_present_lists()

# fsts['verb_infs'] = FST.re('|'.join(infinitives))
fsts['verb_pasts'] = FST.re('|'.join(pasts))
fsts['verb_presents'] = FST.re('|'.join(presents))

def paststem2present():
    pass


fsts['suffix_tags'] = FST.re("('[Past2Present]'):''")

fsts['lexicon'] = FST.re('$verb_pasts $suffix_tags', fsts)


fsts['mir'] = FST.re("((murd)|(mərd)):(mir '+')")
fsts['deh'] = FST.re("(da):((deh)|(dih)|d)")
fsts['nəh'] = FST.re("(na):(nəh)")
fsts['ze'] = FST.re("((ze):(zən))")
fsts['other_exceptions'] = FST.re("$^rewrite((amo):(a '+') | (šo):(šu '+') | ((goft):(gu '+')) / # _)")
fsts['irregulars'] = FST.re("(($ze | $mir | $nəh | $deh | $other_exceptions))", fsts)

fsts['isht'] = FST.re("$^rewrite((išt):(iz|is) / _ #)")
fsts['əsht'] = FST.re("$^rewrite((əšt):(ər) / _ #)")
fsts['asht'] = FST.re("$^rewrite((ašt):(ar) / _ #)")

fsts['əst'] = FST.re("$^rewrite((əst):((əd)? '+') / _ #)")
fsts['end_a'] = FST.re("$^rewrite(a:'+' / _ #)")

fsts['st'] = FST.re("$^rewrite((st):(r|y|d) / _ #)")
fsts['xt'] = FST.re("$^rewrite((xt):(s|ǰ) / _ #)")

fsts['ad'] = FST.re("$^rewrite(d:n / a _ #)")
fsts['ud'] = FST.re("$^rewrite(d:n / u _ #)")

fsts['kaft'] = FST.re("$^rewrite((t):'' / kəf _ #)")
fsts['ft'] = FST.re("$^rewrite((ft):(r|s) / _ #)")
fsts['end_t'] = FST.re("$^rewrite((t):'' / (š) _ #)")
fsts['end_d'] = FST.re("$^rewrite((d):'' / (r|n) _ #)")
fsts['td'] = FST.re("$ad @ $ud @ $kaft @ $ft @ $end_t @ $end_d", fsts)

fsts['end_e_rm'] = FST.re("$^rewrite(e:'+' / (š|s|n) _ #)")
fsts['end_e_in'] = FST.re("$^rewrite(e:(in '+') / (v|d|z|h) _ #)")
fsts['end_e'] = FST.re("$end_e_rm @ $end_e_in", fsts)
# fsts['pronounciation_exceptions'] = FST.re()

fsts['remove_ending'] = FST.re("$əst @ $əsht @ $asht @ $isht @ $xt @ $st @ $td @ $end_a @ $end_e", fsts)
fsts['cleanup'] = FST.re("$^rewrite('+':'')")

fsts['grammar'] = FST.re('$lexicon @ $verb_pasts @ $irregulars @ $remove_ending @ $cleanup @ $verb_presents', fsts)

print(Paradigm(fsts['grammar'], ".*"))
