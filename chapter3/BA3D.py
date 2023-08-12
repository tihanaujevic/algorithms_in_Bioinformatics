#Construct the De Bruijn Graph of a String

def DeBruijn (dna, k):
    d = {}

    for i in range(len(dna)- k):
        if dna[i: i+k] not in d:
            d[dna[i:i+k]] = [dna[i+1: i+k+1]]
        else:
            d[dna[i: i+k]].append(dna[i+1: i+k+1])
    
    result = []
    
    for key, value in d.items():
        string = key + ' -> ' + ','.join(x for x in sorted(value))
        result.append(string)
    
    result = sorted(result)
    
    return '\n'.join(x for x in result)

if __name__ == '__main__':
    import sys

    inlines = [x.strip('\n') for x in sys.stdin.readlines()]

    k = int(inlines[0]) - 1
    dna= inlines[1]

    result = DeBruijn(dna, k)

    sys.stdout.write(result)