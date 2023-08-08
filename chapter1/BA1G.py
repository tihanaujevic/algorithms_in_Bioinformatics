#Compute the Hamming Distance Between Two Strings

def hamming(first, second):
    count = 0
    for i in range(len(first)):
        if first[i] != second[i]:
            count += 1
    
    return count

if __name__ == "__main__":
    import sys

    inlines = [x.strip('\n') for x in sys.stdin.readlines()]

    first = inlines[0]
    second = inlines[1]

    result = hamming(first, second)

    sys.stdout.write(str(result))