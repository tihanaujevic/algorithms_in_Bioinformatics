#Construct the De Bruijn Graph of a Collection of k-mers

def DeBruijn (collection):
    d = {}

    for string in collection:
        if string [:-1] not in d:
            d[string[:-1]] = [string[1:]]
        else:
            d[string[:-1]].append(string[1:])

    result = []
    
    for key, value in d.items():
        string = key + ' -> ' + ','.join(x for x in sorted(value))
        result.append(string)
    
    result = sorted(result)
    
    return '\n'.join(x for x in result)
    

if __name__ == '__main__':
    import sys

    collection = [x.strip('\n') for x in sys.stdin.readlines()]
    result = DeBruijn(collection)

    sys.stdout.write(result)