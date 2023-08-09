#Median String Problem

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

def findMedian (k, collection):
    combs = findAllKmers(k)
    median = ''
    min_distance = float('inf')
    for comb in combs:
        total = 0
        for string in collection:
            mini = float('inf')
            for i in range(len(string)- k +1):
                distance = hamming(comb, string[i: i+k])
                if distance < mini:
                    mini = distance
            total += mini
        if total <= min_distance:
            min_distance = total
            median = comb
    
    return median

if __name__ == '__main__':
    import sys

    inlines = [x.strip('\n') for x in sys.stdin.readlines()]

    k = int(inlines[0])
    collection = [x for x in inlines[1:]]

    result = findMedian(k, collection)

    sys.stdout.write(result)
