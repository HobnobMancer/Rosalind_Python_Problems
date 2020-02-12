# A common substring of a collection of strings is a substring of every member of the collection.
# We say that a common substring is a longest common substring if there does not exist a longer common substring.
# For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible;
# in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

# Note that the longest common substring is not necessarily unique; for a simple example,
# "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

# Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

# Return: A longest common substring of the collection. (If multiple solutions exist,
# you may return any single solution.)




# Extract data from data file
# open file with read only permit, read line by line
# Open file containing DNA sequences, and assign DNA sequences data to a variable (dnaSeq)
fastaFILE = open(r"C:\Users\Emma\Documents\PhD\Computational\Python\Rosalind\Rosalind_Python_Problems\Bioinformatics Stronghold\Finding a Shared Motif.txt", "rt")
allData = fastaFILE.readlines()
fastaFILE.close()

# Create variables to store the working DNA sequence
givenSEQ = ""             # entire DNA sequence of protein
subsequence = []            # list of introns nucleotide sequences
currentID = ""              # tempoary store for working rosalind ID
currentDNA = ""
idSeqDictionary = {}
sequence = ""                 # tempoary store of working intron sequence


# extraction of data from downloaded file and store the sequences as strings in a list
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

sequencesList = list(idSeqDictionary.keys())     # list of sequences stored as strings


# the longest possible shared motif cannot be longer than the shorted sequence
# find the shortest sequence
sortedSequenceList = sorted(sequencesList)

# separate the shortest sequence from other sequences so as not to compare the shorest sequence against itself
shortestSequence = sortedSequenceList[0]
comparisonSequences = sortedSequenceList[1:]

# create empty variable to store the shared motif
sharedMotif = ""

shortestSequence

# find the shared motif
for i in range(len(shortestSequence)):                  # go through the shortest sequence one nucleotide at a time
    for j in range(i, len(shortestSequence)):           # do not continue comparison longer than shortest sequence
        workingCommonMotif = shortestSequence[i: j + 1] # determine which nucleotides to compare
        found = False                                   # define default condition
        for sequence in comparisonSequences:            # set up comparison
            if workingCommonMotif in sequence:          # if bases match, comparison is True
                found = True
            else:
                found = False
                break                                   # if bases do not match, move along in comparison sequence
        if found and len(workingCommonMotif) > len(sharedMotif):
            sharedMotif = workingCommonMotif

# print out shared motif
print(sharedMotif)
