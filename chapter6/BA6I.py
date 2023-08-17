#Implement GraphToGenome

def split_edges_to_chromosomes(edges):
    final_pairs = []
    for i, pair in enumerate(edges):
        if pair[0] > pair[1]:
            final_pairs.append(i)

    chromosomes = []
    previous = 0
    for end in final_pairs:
        chromosomes.append(edges[previous : (end + 1)])
        previous = end + 1
    return chromosomes


def colored_edges_to_cycle(edges):
    cycle = []
    for i in range(len(edges) - 1):
        cycle.extend([edges[i][1], edges[i + 1][0]])
    final = [edges[-1][1], edges[0][0]]
    final.extend(cycle)
    return final


def cycle_to_chromosome(cycle):
    chromosome = []
    for i in range(0, len(cycle), 2):
        if cycle[i] < cycle[i + 1]:
            chromosome.append(cycle[i + 1] // 2)
        if cycle[i] > cycle[i + 1]:
            chromosome.append(-1 * cycle[i] // 2)
    return chromosome


def graph_to_genome(colored_edges):
    chromosomes = []
    chromosome_edges = split_edges_to_chromosomes(colored_edges)
    for chrom_edge in chromosome_edges:
        cycle = colored_edges_to_cycle(chrom_edge)
        chromosome = cycle_to_chromosome(cycle)
        chromosomes.append(chromosome)
    return chromosomes

def f(x):
    if x >= 0:
        return f"+{x}"
    else:
        return f"{x}"
    
def string_to_int(text):
    return [int(x) for x in text.strip("(, ").split(",")]

if __name__ == "__main__":

    import sys

    text = sys.stdin.readline()
    edges = text.split(")")[:-1]
    edges = [string_to_int(edge) for edge in edges]

    chromosomes = graph_to_genome(edges)

    final = ""
    for chromosome in chromosomes:
        final += "(" + " ".join([f(x) for x in chromosome]) + ")"

    sys.stdout.write(final)