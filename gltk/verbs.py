from gltk.std import normalize

def read_verb_table():
    with open('gltk/infinitives-a.txt', 'r') as file:
        table = [
            [
                normalize(w.strip()) for w in line.split('|')
            ] 
            for line in file.readlines() if len(line) >= 2
        ]

    return table
