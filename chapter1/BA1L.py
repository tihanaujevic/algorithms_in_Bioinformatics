#Convert a DNA string to a number

def patternToNumber (dna):
    k = 0
    res = 0
    for x in dna[::-1]: #!!!
        if x == "C":
            res = res + 1 * (4 ** k)
        if x == "G":
            res = res + 2 * (4 ** k)
        if x == "T":
            res = res + 3 * (4 ** k)
        k = k+1
    
    return res

if __name__ == '__main__':
    import sys

    dna = sys.stdin.readline()

    result = patternToNumber(dna)

    sys.stdout.write(str(result))