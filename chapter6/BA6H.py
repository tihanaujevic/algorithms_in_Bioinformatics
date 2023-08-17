#Implement ColoredEdges

def chromosome_to_cycle(permutation):
    cycle = []
    for x in permutation:
        if x > 0:
            cycle.extend([2 * x - 1, 2 * x])
        if x < 0:
            x = abs(x)
            cycle.extend([2 * x, 2 * x - 1])
    return cycle


def get_colored_edges(chromosomes):
    edges = []
    for chrom in chromosomes:
        nodes = chromosome_to_cycle(chrom)
        for j in range(1, len(nodes) - 1, 2):
            edges.append((nodes[j], nodes[j + 1]))
        edges.append((nodes[-1], nodes[0]))
    
    return repr(edges)[1:-1]

def string_to_int(text):
    return [int(x) for x in text.split(" ")]

if __name__ == "__main__":

    import sys

    inlines = [x.strip("\n") for x in sys.stdin.readlines()]
    text = inlines[0]

    chromosomes = text.split(")")
    chromosomes = [string_to_int(chromosome[1:]) for chromosome in chromosomes[:-1]]

    result = get_colored_edges(chromosomes)

    sys.stdout.write(result)