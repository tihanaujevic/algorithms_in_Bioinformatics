#Find the Most Frequent Words with Mismatches in a String

def findAllKmers (k):
    from itertools import product

    letters = ["A", "T", "C", "G"]
    combs = list(product(letters, repeat=k)) #returns in a form [('C', 'C', 'G', 'A'), ...]
    
    combsArray = []
    for combination in combs:
        combsArray.append (''.join(combination))
    
    return combsArray

def hamming(first, second):
    count = 0
    for i in range(len(first)):
        if first[i] != second[i]:
            count += 1
    
    return count

def mostFrequent (dna, k, mismatch):
    d = {}
    kmers = findAllKmers(k)

    for kmer in kmers:
        d[kmer]=0
        for i in range(len(dna)-len(kmer)+1):
            first = dna[i: i+k]
            if hamming(first, kmer) <= mismatch:
                d[kmer] = d[kmer] + 1

    maxi = max(d.values())
    result = ''
    for key, value in d.items():
        if value == maxi:
            result += key + ' '
    
    return result

if __name__ == '__main__':
    import sys

    inlines = [x.strip('\n') for x in sys.stdin.readlines()]

    helpInt = 0
    intsArray =[]
    inlines[1]=inlines[1] + ' '
    for i in range(len(inlines[1])):
        if inlines[1][i] == ' ':
            intsArray.append(inlines[1][helpInt: i])
            helpInt=i+1
    

    dna = inlines[0]
    k = int(intsArray[0])
    mismatch = int(intsArray[1])

    result = mostFrequent(dna, k, mismatch)

    sys.stdout.write(result)


