#Reconstruct a String from its Genome Path

def genomePath (collection):
    result = collection[0]

    for i in range(1, len(collection)):
        result += collection[i][-1]

    return result

if __name__ == '__main__':
    import sys

    collection = [x.strip('\n') for x in sys.stdin.readlines()]
    print(collection)

    result = genomePath(collection)

    sys.stdout.write(result)