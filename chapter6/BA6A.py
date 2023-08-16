#Implement GreedySorting to Sort a Permutation by Reversals

#if x is positive, add + to string
def f(x):
    if x >= 0:
        return f"+{x}"
    else:
        return f"{x}"
    

def greedy_sorting(str_permutation):
    #convert to integers without brackets
    helper = [int(x) for x in str_permutation[1:-1].split()]

    S = []

    for i in range(0, len(helper)):
        if helper[i] == i + 1:
            continue

        idx = i
        while True:
            if helper[idx] == i + 1 or helper[idx] == -1 * (i + 1):
                break
            idx += 1

        mid = [-1 * x for x in helper[i : (idx + 1)]][::-1]
        helper = helper[0:i] + mid + helper[(idx + 1) :]
        S.append(helper.copy())

        if helper[i] < 0:
            helper[i] = abs(helper[i])
            S.append(helper.copy())
    
    strings = []
    for perm in S:
        strings.append("(" + " ".join([f(x) for x in perm]) + ")")
    return "\n".join(strings)



if __name__ == "__main__":

    import sys

    permutation = sys.stdin.readline()

    result = greedy_sorting(permutation)

    sys.stdout.write(result)