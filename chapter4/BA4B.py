#Find Substrings of a Genome Encoding a Given Amino Acid String

genetic_code = {
        "AAA": "K",
        "AAC": "N",
        "AAG": "K",
        "AAU": "N",
        "ACA": "T",
        "ACC": "T",
        "ACG": "T",
        "ACU": "T",
        "AGA": "R",
        "AGC": "S",
        "AGG": "R",
        "AGU": "S",
        "AUA": "I",
        "AUC": "I",
        "AUG": "M",
        "AUU": "I",
        "CAA": "Q",
        "CAC": "H",
        "CAG": "Q",
        "CAU": "H",
        "CCA": "P",
        "CCC": "P",
        "CCG": "P",
        "CCU": "P",
        "CGA": "R",
        "CGC": "R",
        "CGG": "R",
        "CGU": "R",
        "CUA": "L",
        "CUC": "L",
        "CUG": "L",
        "CUU": "L",
        "GAA": "E",
        "GAC": "D",
        "GAG": "E",
        "GAU": "D",
        "GCA": "A",
        "GCC": "A",
        "GCG": "A",
        "GCU": "A",
        "GGA": "G",
        "GGC": "G",
        "GGG": "G",
        "GGU": "G",
        "GUA": "V",
        "GUC": "V",
        "GUG": "V",
        "GUU": "V",
        "UAA": "*",
        "UAC": "Y",
        "UAG": "*",
        "UAU": "Y",
        "UCA": "S",
        "UCC": "S",
        "UCG": "S",
        "UCU": "S",
        "UGA": "*",
        "UGC": "C",
        "UGG": "W",
        "UGU": "C",
        "UUA": "L",
        "UUC": "F",
        "UUG": "L",
        "UUU": "F"
    }

def toRna (dna):
    rna = ''
    for i in range(len(dna)):
        if dna[i] != 'T':
            rna += dna[i]
        else:
            rna += 'U'
    return rna

def toDna (rna):
    dna = ''
    for i in range(len(rna)):
        if rna[i] != 'U':
            dna += rna[i]
        else:
            dna += 'T'
    return dna

def reverseComplement(dna):
    complement = ''
    for i in range (len(dna)):
        if dna[i] == 'A':
            complement += 'T'
        elif dna[i] == 'T':
            complement += 'A'
        elif dna[i] == 'C':
            complement += 'G'
        elif dna[i] == 'G':
            complement += 'C'
    return complement[::-1]

def find (rna, aminoAcid):
    result = []
    k = len(aminoAcid)*3

    for i in range(0,len(rna)-k + 1):
        string = rna[i: i+k]
        acid = ''      
        for j in range (len(aminoAcid)):
            if genetic_code[string[j*3: j*3+3]] == '*':
                break
            acid += genetic_code[string[j*3: j*3+3]]  
        
        if acid == aminoAcid:
            result.append(string)
    return result

def encode (dna, aminoAcid):
    rna1 = toRna(dna)
    revComplement = reverseComplement(dna)
    rna2 = toRna(revComplement)
    
    result1 = find(rna1, aminoAcid)
    result2 = find(rna2, aminoAcid) #translate again to reverse complement

    res1 = []
    for string in result1:
        dna1 = toDna(string)
        res1.append(dna1)

    res2 = []
    for string in result2:
        dna2 = toDna(string)
        res2.append(reverseComplement(dna2))

    return '\n'.join(x for x in res1) + '\n' + '\n'.join(x for x in res2)


if __name__ == '__main__':
    import sys
    inlines = [x.strip('\n') for x in sys.stdin.readlines()]

    dna = inlines[0]
    aminoAcid = inlines[1]

    result = encode(dna, aminoAcid)

    sys.stdout.write(result)
        