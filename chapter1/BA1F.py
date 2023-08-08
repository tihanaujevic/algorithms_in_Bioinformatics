#Find a Position in a Genome Minimizing the Skew

def skew (dna):
    val = [0]
    for i in range (len(dna)):
        if dna[i] == "C":
            val.append(val[i]-1)
        elif dna[i] == 'G':
            val.append(val[i]+1)
        else:
            val.append(val[i])
    
    mini = min(val)

    string = ''
    for i in range(len(val)):
        if val[i] == mini:
            string += str(i) + ' '
    
    return string

if __name__ == '__main__':
    import sys

    dna = sys.stdin.readline()

    result = skew(dna)

    sys.stdout.write(result)