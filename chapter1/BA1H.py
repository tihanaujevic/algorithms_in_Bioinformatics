#Find All Approximate Occurrences of a Pattern in a String

def hamming(first, second):
    count = 0
    for i in range(len(first)):
        if first[i] != second[i]:
            count += 1
    
    return count

def approximate(pattern, dna, mismatch):
    result = ''
    for i in range (len(dna) - len(pattern) + 1):
        first = dna[i: i+len(pattern)]
        if hamming(first, pattern) <= mismatch:
            result += str(i) + ' '
    
    return result

if __name__ == '__main__':
    import sys

    inlines = [x.strip('\n') for x in sys.stdin.readlines()]

    pattern = inlines[0]
    dna = inlines[1]
    mismatch = int(inlines[2])

    result = approximate(pattern, dna, mismatch)

    sys.stdout.write(result)