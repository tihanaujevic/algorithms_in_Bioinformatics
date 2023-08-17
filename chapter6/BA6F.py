#Implement ChromosomeToCycle

def chromosome_to_cycle(chromosome):
    cycle = []
    for x in chromosome:
        if x > 0:
            cycle.extend([2 * x - 1, 2 * x])
        if x < 0:
            x = abs(x)
            cycle.extend([2 * x, 2 * x - 1])

    return "(" + " ".join([str(x) for x in cycle]) + ")"


def rosalind_print(cycle):
    return "(" + " ".join([str(x) for x in cycle]) + ")"


if __name__ == "__main__":

    import sys

    chromosome = sys.stdin.readline()
    chromosome = [int(x) for x in chromosome[1:-1].split(" ")]

    result = chromosome_to_cycle(chromosome)

    sys.stdout.write(result)