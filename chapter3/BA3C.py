#Construct the Overlap Graph of a Collection of k-mers

def overlap (collection):
    result = []
    print(collection)
    for string in collection:
        for i in range(len(collection)):
            helper = string
            if string[1:] == collection[i][:-1]:
                helper += ' -> ' + collection[i]
                result.append(helper)
    result.sort()

    return '\n'.join(x for x in result)

if __name__ == '__main__':
    import sys

    collection = [x.strip('\n') for x in sys.stdin.readlines()]

    result = overlap(collection)

    sys.stdout.write(result)