#Implement MotifEnumeration; Given a collection of strings Dna and an integer d,
# a k-mer is a (k,d)-motif if it appears in every string from Dna with at most d mismatches

def hamming (first, second):
    count = 0

    for i in range(len(first)):
        if first[i] != second[i]:
            count += 1
    
    return count

def findAllKmers (k):
    from itertools import product

    combs = list(product('ATCG', repeat=k))

    res = []
    for comb in combs:
        helper = ''
        for letter in comb:
            helper += letter
        res.append(helper)

    return res

def motifEnumeration (collection, k, d):
    combinations = findAllKmers(k)
    D={}

    for comb in combinations:
        D[comb] = set()
        for string in collection:
            for i in range (len(string) -k +1):
                if hamming(comb,string[i: i+k]) <= d:
                    D[comb].add(string)

    result = []
    for key,value in D.items():
        if len(value) == len(collection):
            result.append(key)

    result.sort()

    return ' '.join(x for x in result)

if __name__ == '__main__':
    import sys

    inlines = [x.strip('\n') for x in sys.stdin.readlines()]

    ints =  inlines[0].split()
    k = int(ints[0])
    d = int(ints[1])

    collection = inlines[1:]
    
    result = motifEnumeration(collection, k, d)

    sys.stdout.write(result)


