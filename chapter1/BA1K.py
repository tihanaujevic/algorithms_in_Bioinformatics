#Generate the Frequency Array of a String

def findAllKmers (k):
    from itertools import product
    letters = ['A','T','C','G']

    combs = list(product(letters, repeat=k))

    result=[]
    for comb in combs:
        helper = ''
        for letter in comb:
            helper+=letter
        result.append(helper)
    return result

def frequency (dna, k):
    kmers = findAllKmers(k)
    d={}
    for kmer in kmers:
        d[kmer] = 0
        for i in range(len(dna) - k + 1):
            if dna[i: i+k] == kmer:
                d[kmer]+=1
    d=dict(sorted(d.items())) #!!!!

    result = ''
    for value in d.values():
        result += str(value) + ' '
    return result

if __name__ == '__main__':
    import sys

    inlines = [x.strip('\n') for x in sys.stdin.readlines()]

    dna = inlines[0]
    k = int(inlines[1])

    result = frequency(dna, k)

    sys.stdout.write(result)
