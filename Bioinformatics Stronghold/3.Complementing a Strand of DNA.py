# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
# The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.

# Define the original DNA sequence
originalSeqDNA = "CCCGTATAGCGCAAGCGAGGCTTGAGCTGACTCGAGCTCCTCTGTCCCTGGGCCCCTTAAGTCGACAAGACAATGAACCCCAATTTGCCTTGGCGCAAGTAGATCAAACAAACAATATTGAAAACCGACATCTTAAGTTCGTCATTCGTGTGTAAGACGTAACGCGTTTGGGTAAGATACATTCTCTGCGGGACTAGGCAGTCCAATGATGATATTGAGACTCGCCAATTGGCCGAGTCATATGTAAAGTTTTTTGGCTATTGTCCTACACTTATGATAAGAAAGATAGCTCGGGCATAGCATGCCCCTGATTACTTAGCCGCGGTCCTAAGGAGCCCGACTAAGGGATATCTCTTGATCCATCCTATGACCACACCCTCCAGGACCTCCCGGATCGTGTTGCGGATCTTCGGGAACCGGGCCGACGCAACTGCCGAATATACCAGCGTCTCGTTAAGCACACCGCGGGAAGCCTATTAATGGTGACTTGTGAATTTCCACAGAGAATGTTAGAACCCAAGGTTTTCCTGACTTTGAGCTTTATGTTAGATAACCGGCGTGTGATTTTACGCGTCTGTATGCGCCATTATGACCAAGATTTAGGCTTAAAAGCCAAATTACTGCTAGCGCAAAATGACCATCGCCTAAGGGGCATCGGAGTCGTCGCCCGGTCAAGTCGGCGCTCGCTACGGACGTATCGTAATGAGAAGATTGTTGAAACGGAAGCAGCTGGTAGTGATTTTATTGAGCTTCGCACGTTATAACAAGTCGCGAAGTCGCCAGTCGAATTGCCGTTCGGGGTCAGGGGCAGTCATGGTCGCGGCACAGACGATTAGCCTCATGGACAGTTTAAAGTCCTCAGCAACTCGGTATGACCATCGAAGCGGACCTTCCTACCCTTACCTCGTAAACACAGGAAGCTCGGTAGTTAGCTGTGGCAGACGTTATTGTAAGGGTTAGATCTGTAACAGTACTATCATGT"
complementarySeqDNA = originalSeqDNA

#convery complementary sequence to a list
complementarySeqLIST = list(complementarySeqDNA)
print(complementarySeqLIST)


# Convert original DNA sequence to complement bases (A = T, C = G), using .replace method
indexNumber = 0
for nucleotide in complementarySeqLIST:
    if nucleotide is "A":
            complementarySeqLIST[indexNumber] = "T"
    elif nucleotide is "C":
            complementarySeqLIST[indexNumber] = "G"
    elif nucleotide is "G":
            complementarySeqLIST[indexNumber] = "C"
    elif nucleotide is "T":
            complementarySeqLIST[indexNumber] = "A"
    indexNumber = indexNumber + 1

#create reverse order of list using .reverse methof
complementarySeqLIST.reverse()

# convert complementary sequence list to a string
convertedComplementarySeq = "".join(complementarySeqLIST)

print(convertedComplementarySeq)


# Lesson to remember: Strings are immutable and to work through each character of a string it must be first converted to a list, list(string_name), which can be reverted back to a string using "".join(list_name)
