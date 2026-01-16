from pyfoma import *
from gltk.std import _symbols

# insert space before and after punctuation to make split easier
def _insert_punc_spaces():
    symbols_re = '|'.join(f"'{x}'" for x in _symbols)

    fsts = {}
    fsts['punc_spc_before'] = FST.re("$^rewrite('':' ' / _ ('!'|','|':'))")
    fsts['punc_spc_after'] = FST.re("$^rewrite('':' ' / ('!'|','|':') _ )")
    fsts['punc'] = FST.re("$punc_spc_before @ $punc_spc_after", fsts)
    fsts['cleanup'] = FST.re("$^rewrite(' ':'' / ' ' _)")
    grammar = FST.re(".* @ $punc @ $cleanup", fsts)
    return lambda text: list(grammar.generate(text))[0]

insert_punc_spaces = _insert_punc_spaces()

def read_lines(filename):
    with open(filename) as file:
        for line in file.readlines():
            yield insert_punc_spaces(line)
