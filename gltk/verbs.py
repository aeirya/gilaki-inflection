from gltk.std import normalize

def read_table(path):
    with open(path, 'r') as file:
        table = [
            [
                normalize(w.strip()) for w in line.split('|')
            ] 
            for line in file.readlines() if len(line) >= 2
        ]
    return table

def read_verb_table():
    return read_table('gltk/infinitives-a.txt')

def read_verb_past2present_table():
    return read_table('gltk/past-present.txt')

def past_present_lists():
    table = read_verb_past2present_table()
    return [v[1] for v in table], [v[0] for v in table]