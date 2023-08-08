#Find the Most Frequent Words in a String

def mostFrequent (dna, k):
    d = {}
    for i in range(len(dna) - k + 1):
        if dna[i:i+k] not in d:
            d[dna[i:i+k]]=1
        else:
            d[dna[i:i+k]]+=1
    
    maks = max(d.values())
    result = []

    for key, value in d.items():
        if value==maks:
            result.append(key)
    
    return ' '.join(x for x in result)

if __name__ == '__main__':
    import sys

    lines = [x.strip('\n') for x in sys.stdin.readlines()]

    dna = lines[0]
    k= int(lines[1])

    result = mostFrequent(dna, k)
    sys.stdout.write(str(result))