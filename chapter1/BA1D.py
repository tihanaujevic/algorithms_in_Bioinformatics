#Find All Occurrences of a Pattern in a String

def occurrences (pattern, genome):
    result = []
    for i in range(len(genome)):
        if genome[i: i+len(pattern)]==pattern:
            result.append(i)
    return ' '.join(str(x) for x in result)

if __name__ == '__main__':
    import sys

    inlines = [x.strip('\n') for x in sys.stdin.readlines()]

    pattern = inlines[0]
    genome = inlines[1]

    result = occurrences(pattern, genome)

    sys.stdout.write(str(result))