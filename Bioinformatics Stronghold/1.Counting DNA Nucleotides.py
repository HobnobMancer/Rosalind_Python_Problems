# Counting DNA nucleotides
# Given a DNA string s of length at most 1000 nt, return four intergers (separated by spaces) counting the respective number of times that the symboles 'A', 'C', 'G' and 'T' occur in s.

# define DNA sequence
DNAstring = "CTATGCAACCCCCTTGCATGTTTTAGTGAGGTTTTTATGATACCGGCTGATTCCAGAATGCGTCCGTCGTCTGCCAGCACGGAATTATAGCACCCATGGAACGTTTTCCTGCCAACGCTCTTCATTATTGAGTGTGTAGGGTCAGCGCGTTACACCAGGGCTTTGGGCCTGCGCCTTCTAAACCTCAGCTATCTGGGAACATTGACACCCCAGCAAGAGTACACACAAGTTCCGCGTGCGAGTTCTGAGAACTCAGTCCCTGTTGGGTGTGCAGGTCCCTACGTAGATACAGTTTAAAAGTATCCAGTTTTCGCTTCGTATCCGACTGTTTTCGTAGATTCCGACCGCCTCCACACAAATATATCGTACTATAGTTATTCTGAAAGGAGGGGCTCATCATACACGGCCTCTCAAGAGTGTTGGTGATTGAACCTAAGACCGCAATAGGCCCGGGCATCCCGAACGCGATAAGCAGATTGTTGATGGGACTACGCTGCCCGATCCAGGTTTGAAATATTTATGAGCTAGACCGAGAGGCAAGAAATCTCATGATAGGGATGCATTAGTCAGACGTGCTAGCTTCCCGGAGCGGTAGTACACTTCCCGGCCGTCCGTTGTATTACTAACGAGGCGTCCATCGCCGCTGGAACCTCCTGGTAGGGCAGCCGCCTTCGTGTTATTGCCCACACACAGCTATATGTAACGTAGTTCCCCATCTCGCGAAAGACGGCTCACACAACGAAAATACTTTAGGTGTGAGGGCAAATCTCTGTTTAGACTTAGAGGTATCACTCCTCAAGCGCCTTATGAGCGAGAGAATCAAGTACGTCCAGGCTACGATGACGTAGCGGTAAGATTGCGTGCCGACACAACGTGAGGTTTGATCAGGAGGGCTATTTGGATACAACGTTAGTCGTCCGATCGAACCGTCTCAATTTCGTGCTTATGCTGGGGGGTCGGCGGAAAGATTACAGT"

# set up counts for each nucleotide
AnucleotideCount = 0
CnucleotideCount = 0
GnucleotideCount = 0
TnucleotideCount = 0

# count nucleotides
for nucleotide in DNAstring:
    if nucleotide is 'A':
        AnucleotideCount = AnucleotideCount + 1
    elif nucleotide is 'C':
        CnucleotideCount = CnucleotideCount + 1
    elif nucleotide is 'G':
        GnucleotideCount = GnucleotideCount + 1
    elif nucleotide is 'T':
        TnucleotideCount = TnucleotideCount + 1
    else:
        print("Non-DNA nucleotide incorporation in sequence")

# return nucleotide count (A C G T)
print(AnucleotideCount, CnucleotideCount, GnucleotideCount, TnucleotideCount)
