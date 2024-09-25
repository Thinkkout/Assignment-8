def countBase(seq, base): 
    return seq.count(base.upper())

def gcContent(seq): 
    return (countBase(seq,'G') + countBase(seq,'C'))/len(seq)

def atContent(seq): # got bugs
    return (countBase(seq,'A') + countBase(seq,'T'))/len(seq)

def countBasesDict(seq): # got bugs
    basesM = {}
    for base in seq:
        if base in basesM:
            basesM[base] += 1
        else:
            basesM[base] = 1   
    return basesM

if __name__ == '__main__':
    seq = 'TCAGGGCTAAAGCGCATCCTAC'
    print("test: GC Content:", gcContent(seq))
