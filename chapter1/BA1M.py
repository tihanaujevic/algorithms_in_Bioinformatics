#Convert an integer to its corresponding DNA string

def numberToPattern (n, k):
    pattern = ''
    d = {0:'A', 1:'C', 2:'G', 3:'T'}
    q = n

    for i in range(k):
        r = q % 4
        q = q // 4
        pattern += d[r]
    
    return pattern[::-1] #!!!

if __name__ == '__main__':
    import sys

    inlines = [x.strip('\n') for x in sys.stdin.readlines()]

    n = int(inlines[0])
    k = int(inlines[1])

    result = numberToPattern(n,k)

    sys.stdout.write(result)