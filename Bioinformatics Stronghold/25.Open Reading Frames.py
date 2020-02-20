# Given a DNA string of length at most 1 kbp in FASTA format

# Return: Every distinct candidate protein string that can be translated from ORFs of the given string. Strings can be
# returned in any order.


# NOTE! Ensure there are not empty blank lines at end of data file


import re
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna


# create function to facilitate generation of reverse complement sequence
def reverse(list):
    """Reverses the order of elements in the passed listed"""
    list.reverse()
    return list


# Prepare given data

# Extract IDs from text file which must contain no empty lines at the end of the file
# open file with read only permit, read line by line
# Open file containing UniProt IDs, and assign IDs to a variable (uniprotIDs)
fastaFILES = open(r"/home/em/PycharmProjects/Rosalind/Bioinformatics Stronghold/ORFs.txt", "rt")
givenSeqRaw = fastaFILES.readlines()
fastaFILES.close()



# Transfer IDs to list and remove new line character
givenSeqCompiled = [] # create new empty list to store all lines of protein sequence from Fasta file

currentDNA = [] # current working DNA sequence

# for loop to separate and store Rosalind ID from protein sequence
for fileline in givenSeqRaw:
    if fileline[0] is not ">":
        strngFileline = str(fileline[:-1])
        currentDNA.append(strngFileline)

stringDNA = str(currentDNA)
stringDNA = stringDNA.replace('[','')
stringDNA = stringDNA.replace(']','')
stringDNA = stringDNA.replace("'","")
stringDNA = stringDNA.replace(" ","")
givenSeqCompiled = stringDNA

# convert sequence into list so that each amino acid is an individual element in the list
singleSeqString = str(givenSeqCompiled)
singleSeqString = singleSeqString.replace('[','')
singleSeqString = singleSeqString.replace(']','')
singleSeqString = singleSeqString.replace("'","")
aminoAcidSeqLIST = list(singleSeqString)


# create complementary sequence in reverse to facilitate finding open reading frames in complementary strand
strandOne = aminoAcidSeqLIST

complementaryStrandOne = strandOne.copy()
for i in range(0, len(strandOne)):
    if strandOne[i] is 'A':
        complementaryStrandOne[i] = 'T'
    elif strandOne[i] is 'T':
        complementaryStrandOne[i] = 'A'
    elif strandOne[i] is 'C':
        complementaryStrandOne[i] = 'G'
    elif strandOne[i] is 'G':
        complementaryStrandOne[i] = 'C'
    i += 1

forwardSequenceLIST = strandOne.copy()
reverseSequenceLIST = reverse(complementaryStrandOne) # this is the inverse complementary sequence to the forward sequence

# convert both sequences from lists to strings and remove all none DNA nucleotide characters (e.g. "'", "," and " ")
forwardSequence = str(forwardSequenceLIST)
forwardSequence = forwardSequence.replace('[','')
forwardSequence = forwardSequence.replace(']','')
forwardSequence = forwardSequence.replace(',','')
forwardSequence = forwardSequence.replace("'","")
forwardSequence = forwardSequence.replace(" ","")

reverseSequence = str(reverseSequenceLIST)
reverseSequence = reverseSequence.replace('[','')
reverseSequence = reverseSequence.replace(']','')
reverseSequence = reverseSequence.replace(",","")
reverseSequence = reverseSequence.replace("'","")
reverseSequence = reverseSequence.replace(" ","")




# find all possible open reading frames resulting amino acid sequences

# create compiler to pass to re.compile to find the open reading frame (orfSearch)
orfSearch = re.compile(r'(?=(ATG(?:...)*?)(?=TAG|TGA|TAA))')

# create empty list to store all resulting amino acid sequences from all possible open reading frames
resultingSequences = []

for i in re.findall(orfSearch, str(forwardSequence)):
    dnaSequence = Seq(i, generic_dna)
    proteinSequence = dnaSequence.translate()
    if proteinSequence not in resultingSequences:
        resultingSequences.append(proteinSequence)

for j in re.findall(orfSearch, str(reverseSequence)):
    reverse_dnaSequence = Seq(j, generic_dna)
    reverse_proteinSequence = reverse_dnaSequence.translate()
    if reverse_proteinSequence not in resultingSequences:
        resultingSequences.append(reverse_proteinSequence)

for k, m in enumerate(resultingSequences):
    print(m)

