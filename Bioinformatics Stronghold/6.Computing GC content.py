# The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.
# DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.
# In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.
# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.


# Define GC computing function
def GCcontentCalculator(string):
    """Calculates the GC nucleotide content of a given DNA string as a percentage"""

    # create empty dictionary to store nucleotide counts
    nucleotideCount = {}

    # count nucleotides
    for nucleotide in string:
        if nucleotide not in nucleotideCount:
            nucleotideCount[nucleotide] = {}
            nucleotideCount[nucleotide] = 1
        else:
            if nucleotide in nucleotideCount:
                nucleotideCount[nucleotide] +=1

    # Calculate GC content
    GCcontent = int(((nucleotideCount["C"] + nucleotideCount["G"]) / len(string)) * 100)


# Open file containing DNA sequences, and assign DNA sequences data to a variable (dnaSeq)
fastaFILE = open(r"/home/em/PycharmProjects/Rosalind/Bioinformatics Stronghold/CG_content_testFile", "rt")
dnaSeq = fastaFILE.read()
fastaFILE.close()
dnaSeq.split('\n')
print(dnaSeq)

# Convert file DNA sequence data to a string and separate each sequence
#str(dnaSeq)
#dnaSeq.split('>')
#print(dnaSeq)
# split contents at IDS
# extract DNA sequences as strings
# Convert strings lists
# add characters to dictionaries
# calculate GC content and percentage
# print ID + GC content
