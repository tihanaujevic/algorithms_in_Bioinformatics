#Generate the k-mer Composition of a String

def kmerComposition (k, dna):
    kmers = []

    for i in range(len(dna)- k + 1):
        kmers.append(dna[i: i+k])
    
    kmers.sort()
    return '\n'.join(x for x in kmers)

if __name__ == '__main__':
    import sys

    inlines = [x.strip('\n') for x in sys.stdin.readlines()]

    k = int(inlines[0])
    dna = inlines[1]

    result = kmerComposition(k, dna)

    sys.stdout.write(result)