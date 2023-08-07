#Find the Reverse Complement of a String

def reverseComplement(dna):
    complement = ''
    for i in range (len(dna)):
        if dna[i] == 'A':
            complement+='T'
        elif dna[i] == 'T':
            complement += 'A'
        elif dna[i] == 'C':
            complement += 'G'
        elif dna[i] == 'G':
            complement += 'C'
    
    return complement[::-1]

if __name__ == '__main__':
    import sys

    dna = sys.stdin.readline()

    result = reverseComplement(dna)
    sys.stdout.write(result)