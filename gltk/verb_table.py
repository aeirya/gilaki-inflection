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

def read_verb_infinitive2past_table():
    return read_table('gltk/data/verb/infinitive-past.txt')

def read_verb_past2present_table():
    return read_table('gltk/data/verb/present-past.txt')

def infinitive_past_lists():
    table = read_verb_infinitive2past_table()
    return [v[0] for v in table], [v[1] for v in table]

def past_present_lists():
    table = read_verb_past2present_table()
    return [v[1] for v in table], [v[0] for v in table]

def read_full_verb_table():
    import pandas as pd
    
    inf1,past1 = infinitive_past_lists()
    df1 = pd.DataFrame({
        'inf': inf1,
        'past': past1,
    })

    past2,present2 = past_present_lists()
    df2 = pd.DataFrame({
        'past': past2,
        'pres': present2,
    })

    df_merged = df1.merge(df2, on='past')
    return df_merged


