# Compute the Number of Breakpoints in a Permutation

def breakpoints (permutation):
    counter = 0
    for i in range (len(permutation)-1):
        if permutation[i+1] - permutation[i] == 1:
            counter += 1

    return len(permutation) - 1 - counter

if __name__ == '__main__':
    import sys

    permutation = [int(x) for x in sys.stdin.readline()[1:-1].split()]
    permutation = [0] + permutation + [len(permutation)+1]

    result = breakpoints(permutation)

    sys.stdout.write(str(result))