#Find a Cyclic Peptide with Theoretical Spectrum Matching an Ideal Spectrum

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

def belongs_spectrum(candidate_spectrum, main_spectrum):
    from collections import Counter

    counter_c_spectrum = Counter(candidate_spectrum)
    counter_m_spectrum = Counter(main_spectrum)

    for key, count in counter_c_spectrum.items():
        if key not in counter_m_spectrum:
            return False
        if count > counter_m_spectrum[key]:
            return False
    return True


def check_cyclo(spectrum, peptide):
    parent_mass = max(spectrum)
    n = len(peptide)

    extended_peptide = peptide + peptide[:-1]

    new_spectrum = [0, sum(peptide)]

    for l in range(n):
        for k in range(1, n):
            subpeptide = extended_peptide[l : l + k]
            new_spectrum.append(sum(subpeptide))
    new_spectrum = sorted(new_spectrum)

    if sum(peptide) == parent_mass and new_spectrum == spectrum:
        return True

    return False


def check_linear(spectrum, peptide):
    parent_mass = max(spectrum)

    n = len(peptide)

    new_spectrum = [0]

    for l in range(n):
        for k in range(1, n - l + 1):
            subpeptide = peptide[l : l + k]
            new_spectrum.append(sum(subpeptide))
    new_spectrum = sorted(new_spectrum)

    if sum(peptide) <= parent_mass and belongs_spectrum(
        new_spectrum, spectrum
    ):
        return True

    return False


def branch_and_bound(spectrum):

    all_combinations = []
    aa_masses = set(mass.values())

    parent_mass = max(spectrum)

    peptides = [[]]

    while True:
        candidates = [
            peptide + [aa_mass] for aa_mass in aa_masses for peptide in peptides
        ]

        selected = [
            peptide for peptide in candidates if check_linear(spectrum, peptide)
        ]

        all_combinations.extend(
            [peptide for peptide in selected if check_cyclo(spectrum, peptide)]
        )

        peptides = [peptide for peptide in selected if sum(peptide) != parent_mass]

        if len(peptides) == 0:
            break

    return " ".join(sorted(["-".join([str(y) for y in x]) for x in all_combinations]))


if __name__ == "__main__":

    import sys

    inlines = [x.strip("\n") for x in sys.stdin.readlines()]
    peptide = [int(x) for x in inlines[0].split()]

    res = branch_and_bound(peptide)

    sys.stdout.write(res)