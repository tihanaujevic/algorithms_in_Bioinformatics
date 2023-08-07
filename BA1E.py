#Find Patterns Forming Clumps in a String

def clumps (genome, k, L, t):
    clumps = set()
    for i in range(len(genome) - L +1):
        window = genome[i: i+L]
        kmer_counts = {}
        for j in range(L - k +1):
            kmer = window[j: j+k]
            kmer_counts[kmer] = kmer_counts.get(kmer, 0) + 1
        for key,value in kmer_counts.items():
            if value >= t:
                clumps.add(key)
    return ' '.join(str(x) for x in clumps)

if __name__ == '__main__':
    import sys

    inlines = [x.strip('\n') for x in sys.stdin.readlines()]

    genome = inlines[0]
    
    ints=[]
    helpVar = 0
    string = inlines[1] + ' '
    for i in range (len(string)):
        if string[i] == ' ':
            ints.append(string[helpVar:i])
            helpVar=i+1
    
    k = int(ints[0])
    L = int(ints[1])
    t = int(ints[2])

    result = clumps(genome, k, L, t)

    sys.stdout.write(str(result))
