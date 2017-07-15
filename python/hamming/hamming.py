def distance(p, q):
    if len(p) != len(q):
        raise ValueError
    count = 0
    for nucleotide_p, nucleotide_q in zip(p, q):
        if nucleotide_p != nucleotide_q:
            count += 1
    return count
