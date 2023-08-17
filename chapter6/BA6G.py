#Implement CycleToChromosome

def f(x):
    if x >= 0:
        return f"+{x}"
    else:
        return f"{x}"
    
def cycle_to_chromosome(cycle):
    chromosome = []
    for i in range(0, len(cycle), 2):
        if cycle[i] < cycle[i + 1]:
            chromosome.append(cycle[i + 1] // 2)
        if cycle[i] > cycle[i + 1]:
            chromosome.append(-1 * cycle[i] // 2)

    return "(" + " ".join([f(x) for x in chromosome]) + ")"


if __name__ == "__main__":

    import sys

    cycle = sys.stdin.readline()
    cycle = [int(x) for x in cycle[1:-1].split(" ")]

    result = cycle_to_chromosome(cycle)

    sys.stdout.write(result)