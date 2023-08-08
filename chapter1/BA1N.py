#Generate the d-Neighborhood of a String

def findAllKmers (k):
    from itertools import product

    letters = ['A', 'C', 'G', 'T']
    kmers = list(product(letters, repeat=k))

    result = []
    for kmer in kmers:
        helper = ''
        for letter in kmer:
            helper += letter
        result.append(helper)

    return result

def mismatch (first, second):
    count = 0
    for i in range(len(first)):
        if first[i] != second[i]:
            count += 1

    return count

def neigborhood (dna, d):
    resultArray = []

    kmers = findAllKmers(len(dna))

    for kmer in kmers:
        if mismatch(dna, kmer) <= d:
            resultArray.append(kmer)
    
    result = '\n'.join(str(x) for x in resultArray)

    return result

if __name__ == '__main__':
    import sys

    inlines = [x.strip('\n') for x in sys.stdin.readlines()]

    dna = inlines[0]
    d = int(inlines[1])

    result = neigborhood(dna, d)

    sys.stdout.write(result)

    