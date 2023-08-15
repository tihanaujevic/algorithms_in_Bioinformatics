#Compute the Number of Peptides of Given Total Mass

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

def countPeptides (mass, aa_masses, counter):
    if mass in counter:
        return counter[mass]

    if mass < 0:
        return 0

    if mass == 0:
        return 1

    counter[mass] = 0
    for aa_mass in aa_masses:
        counter[mass] += countPeptides(mass - aa_mass, aa_masses, counter)

    return counter[mass]


if __name__ == '__main__':
    import sys

    n = int(sys.stdin.readline())
    masses = set(mass.values())

    result = countPeptides(n, masses, {})

    sys.stdout.write(str(result))