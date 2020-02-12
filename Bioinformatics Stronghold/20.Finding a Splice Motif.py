# A subsequence of a string is a collection of symbols contained in order (though not necessarily contiguously)
# in the string (e.g., ACG is a subsequence of TATGCTAAGATC).
# The indices of a subsequence are the positions in the string at which the symbols of the subsequence appear;
# thus, the indices of ACG in TATGCTAAGATC can be represented by (2, 5, 9).

# As a substring can have multiple locations, a subsequence can have multiple collections of indices,
# and the same index can be reused in more than one appearance of the subsequence; for example,
# ACG is a subsequence of AACCGGTT in 8 different ways.

# Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

# Return: One collection of indices of s in which the symbols of t appear as a subsequence of s.
# If multiple solutions exist, you may return any one.



# Extract data from data file
# open file with read only permit, read line by line
# Open file containing DNA sequences, and assign DNA sequences data to a variable (dnaSeq)
fastaFILE = open(r"C:\Users\Emma\Documents\PhD\Computational\Python\Rosalind\Rosalind_Python_Problems\Bioinformatics Stronghold\Finding a Spliced Motif.txt", "rt")
allData = fastaFILE.readlines()
fastaFILE.close()

# Create variables to store the working DNA sequence
givenSEQ = ""             # entire DNA sequence of protein
subsequence = []            # list of introns nucleotide sequences
currentID = ""              # tempoary store for working rosalind ID
currentDNA = ""
idSeqDictionary = {}
sequence = ""                 # tempoary store of working intron sequence


# extraction of data from downloaded file and storage in appropriate variables
for fileLine in allData:
    if fileLine[0] is ">":
        currentID = fileLine[1:].replace('\n','')
        currentDNA = ""
    else:
        strngFileline = str(fileLine)
        currentDNA = currentDNA + strngFileline.replace('\n','')
        if currentID not in idSeqDictionary.values():
            idSeqDictionary[currentDNA] = currentID
        else:
            for key, value in dict(idSeqDictionary).items():
                if value is currentID:
                    del idSeqDictionary[key]
            idSeqDictionary[currentDNA] = currentID

subsequence = list(idSeqDictionary.keys())

# separate string from subsequence
givenSEQ = subsequence[0]
del subsequence[0]
givenString = list(givenSEQ)

# convert subsequence into list of individual nucleotides
splicedMotifSequence = list(subsequence[0]) # splice motif as list of its nucleotides

# find indices of subsequence locations in sequence of given string
indexString = 0 # index number of working item in given string
motifIndicies = [] # list containing indicies of splice motif in given string

for i in range(len(splicedMotifSequence)):
    for j in range(indexString, len(givenString)):
        indexString += 1
        if len(motifIndicies) < len(splicedMotifSequence):
            if splicedMotifSequence[i] == givenString[j]:
                motifIndicies.append(indexString)
                break

# print out answer in desired formating (i.e. no ',')
result = str(motifIndicies)
result = result.replace(',','')
print(result)
