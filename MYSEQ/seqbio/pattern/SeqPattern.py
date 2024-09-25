
import re

def cpgSearch(seq):
    cpgs = []
    for m in re.finditer(r'CG', seq, re.I):
        cpgs.append((m.group(), m.start(), m.end()))
    return cpgs

def enzTargetsScan(seq, enz):
    enzscan = []
    resEnzyme = dict(EcoRI='GAATTC', BamHI='GGATCC', 
                 HindIII='AAGCTT',AccB2I='[AG]GCGC[CT]',
                 AasI='GAC[ATCG][ATCG][ATCG][ATCG][ATCG][ATCG]GTC',
                 AceI='GC[AT]GC')
    
    if enz in resEnzyme:
        if enz == 'EcoRI':
            for m in re.finditer(resEnzyme['EcoRI'],seq):
                enzscan.append((m.group(), m.start(), m.end()))
        elif enz == 'BamHI':
            for m in re.finditer(resEnzyme['BamHI'],seq):
                enzscan.append((m.group(), m.start(), m.end()))
        elif enz == 'HindIII':
            for m in re.finditer(resEnzyme['HindIII'],seq):
                enzscan.append((m.group(), m.start(), m.end()))
        elif enz == 'AccB2I':
            for m in re.finditer(resEnzyme['AccB2I'],seq):
                enzscan.append((m.group(), m.start(), m.end()))
        elif enz == 'AasI':
            for m in re.finditer(resEnzyme['AasI'],seq):
                enzscan.append((m.group(), m.start(), m.end()))
        elif enz == 'AceI':
            for m in re.finditer(resEnzyme['AceI'],seq):
                enzscan.append((m.group(), m.start(), m.end()))
        return enzscan



if __name__ == '__main__':
    seq = 'TCAGGGCTAGAATTCGCGCATCCTAC'
    print("test: cpgSearch:", cpgSearch(seq))
