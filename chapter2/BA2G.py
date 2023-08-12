  #Implement GibbsSampler

import random

def profile_most_probable(text, k, profile):
    max_kmer = ""
    max_p = -1
    kmers = []
    for i in range (len(text)- k +1):
        kmers.append(text[i: i+k])

    for kmer in kmers:
        tmp = 1
        for index, letter in enumerate(kmer):
            tmp *= profile[letter][index]

        if tmp > max_p:
            max_kmer = kmer
            max_p = tmp
    return max_kmer

def get_motifs(dna_list, profile):
    k = len(profile["A"])

    motifs = [profile_most_probable(dna_string, k, profile) for dna_string in dna_list]
    return motifs

def create_profile_matrix(pattern_list, pseudo_counts=False):
    k = len(pattern_list[0])

    #create dictionary and assign value of array zeroes with len of k
    profile_matrix = {} 
    profile_matrix["A"] = [0] * k
    profile_matrix["C"] = [0] * k
    profile_matrix["G"] = [0] * k
    profile_matrix["T"] = [0] * k

    #for every pattern count how many times letter (A/B/C/D) occurs in which position
    for pattern in pattern_list:
        for index, letter in enumerate(pattern):
            profile_matrix[letter][index] = profile_matrix[letter][index] + 1

    #pseudo_counts adds 1 for every element
    if pseudo_counts:
        profile_matrix["A"] = [x + 1 for x in profile_matrix["A"]]
        profile_matrix["C"] = [x + 1 for x in profile_matrix["C"]]
        profile_matrix["G"] = [x + 1 for x in profile_matrix["G"]]
        profile_matrix["T"] = [x + 1 for x in profile_matrix["T"]]

    for i in range(0, k):
        #find total to divide elements, it shopuld be k or k+1 (if pseudoCounts)
        total = (
            profile_matrix["A"][i]
            + profile_matrix["C"][i]
            + profile_matrix["G"][i]
            + profile_matrix["T"][i]
        )
        #divide every element with total
        profile_matrix["A"][i] = profile_matrix["A"][i] / total
        profile_matrix["C"][i] = profile_matrix["C"][i] / total
        profile_matrix["G"][i] = profile_matrix["G"][i] / total
        profile_matrix["T"][i] = profile_matrix["T"][i] / total

    return profile_matrix

def score(motifs):
    zzip = zip(*motifs)

    max_count = []
    for x in zzip:
        n_a = sum([y == "A" for y in x])
        n_c = sum([y == "C" for y in x])
        n_g = sum([y == "G" for y in x])
        n_t = sum([y == "T" for y in x])
        max_count.append(len(motifs) - max(n_a, n_c, n_g, n_t))

    return sum(max_count)


def randomized_motif_search_atom(dna_list, k):
    randpos = [random.randint(0, len(dna_list[0]) - k) for dna in dna_list] #take random positions for start of kmers
    bestmotifs = [dna[index : (index + k)] for index, dna in zip(randpos, dna_list)] #take kmers for provided random indexes
    motifs = bestmotifs

    while True:
        profile = create_profile_matrix(motifs, pseudo_counts=True)
        motifs = get_motifs(dna_list, profile)
        if score(motifs) < score(bestmotifs):
            bestmotifs = motifs
        else:
            return bestmotifs
        
#below is difference from previous solution
def profile_randomly_generated_kmer(text, profile, k):
    import random

    L = []

    for i in range(0, len(text) - k + 1):
        prob = 1
        for index, letter in enumerate(text[i : i + k]):
            prob *= profile[letter][index]
        L.append(prob)

    C = sum(L)
    L = [x / C for x in L]

    r = random.uniform(0, 1)
    s = 0
    for ind, x in enumerate(L):
        s = s + x
        if r < s:
            return text[ind : ind + k]


def gibbs_sampler_atom(dna_list, k, N=1000):
    t = len(dna_list)

    bestmotifs = randomized_motif_search_atom(dna_list, k)
    motifs = list(bestmotifs)

    for j in range(1, N):
        i = random.randint(0, t - 1)

        tmp = list(motifs)
        tmp.pop(i)
        profile = create_profile_matrix(tmp, pseudo_counts=True)

        motifs[i] = profile_randomly_generated_kmer(dna_list[i], profile, k)

        if score(motifs) < score(bestmotifs):
            bestmotifs = list(motifs)
    return bestmotifs


def gibbs_sampler(dna_list, k, repeats=20, N=1000):
    bestmotifs = gibbs_sampler_atom(dna_list, k, N)
    for i in range(1, repeats):
        motifs = gibbs_sampler_atom(dna_list, k, N)
        if score(motifs) < score(bestmotifs):
            bestmotifs = list(motifs)
    return '\n'.join(x for x in bestmotifs)


if __name__ == '__main__':
    import sys
    
    inlines = [x.strip('\n') for x in sys.stdin.readlines()]
    ints = inlines[0].split()
    k = int(ints[0])
    N= int(ints[2])

    dna_list = inlines[1:]

    result = gibbs_sampler(dna_list, k, 20, 1000)

    sys.stdout.write(result)
