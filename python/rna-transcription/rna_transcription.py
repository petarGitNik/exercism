def to_rna(sequence):
    if set(sequence) - set(['A', 'C', 'G', 'T']):
        return ''
    return sequence.replace('G', 'c').replace('C', 'g').replace('T', 'a').replace('A', 'u').upper()
