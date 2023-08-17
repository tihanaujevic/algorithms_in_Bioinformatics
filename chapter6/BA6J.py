#Implement 2-BreakOnGenomeGraph

def two_break_on_genome_graph(edges, two_breaks):
    helper = edges.copy()
    for edge in edges:
        if edge[0] in two_breaks:
            helper.remove(edge)

    helper.append([two_breaks[0], two_breaks[2]])
    helper.append([two_breaks[1], two_breaks[3]])

    tuples = [tuple(x) for x in helper]
    return repr(tuples)[1:-1]

def string_to_int(text):
    return [int(x) for x in text.strip("(, ").split(",")]

if __name__ == "__main__":

    import sys

    inlines = [x.strip("\n") for x in sys.stdin.readlines()]

    colored = inlines[0]
    two_breaks = inlines[1]

    edges = colored.split(")")[:-1]
    edges = [string_to_int(edge) for edge in edges]

    two_breaks = two_breaks.split(",")
    two_breaks = [int(x) for x in two_breaks]

    result = two_break_on_genome_graph(edges, two_breaks)

    sys.stdout.write(result)