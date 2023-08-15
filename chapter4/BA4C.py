#Generate the Theoretical Spectrum of a Cyclic Peptide

mass = {
        "G": 57,
        "A": 71,
        "S": 87,
        "P": 97,
        "V": 99,
        "T": 101,
        "C": 103,
        "I": 113,
        "L": 113,
        "N": 114,
        "D": 115,
        "K": 128,
        "Q": 128,
        "E": 129,
        "M": 131,
        "H": 137,
        "F": 147,
        "R": 156,
        "Y": 163,
        "W": 186,
    }

import itertools

def theoreticalSpectrum (peptide):
    res=[0]
    extended_peptide = peptide + peptide[:-1]
    res.append(sum([mass[x] for x in peptide]))
    for i in range(len(peptide)):
        for k in range(1, len(peptide)):
            subpeptide = extended_peptide[i : i + k]
            res.append(sum([mass[x] for x in subpeptide]))

    res = sorted(res)
    return ' '.join(str(x) for x in res)

if __name__ == '__main__':
    import sys

    peptide = sys.stdin.readline()

    result = theoreticalSpectrum(peptide)

    sys.stdout.write(result)