# For DNA strings s1 and s2 having the same length, their transition/transversion ratio R(s1,s2)
# is the ratio of the total number of transitions to the total number of transversions, where symbol substitutions are
# inferred from mismatched corresponding symbols as when calculating Hamming distance (see “Counting Point Mutations”).

# Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp)
# Return: The transition/transversion ratio R(s1,s2).

# Transition: change within same base class: purine to purine, pyrimidine to pyrimidine (C - T, G - A)
# Transversion: change between different base classes (C - A + G - T)



# define function to calculate the transition/transversion ratio between two given strings
def transition_transvertionRATIO(stringS1, stringS2):
    """Calculate the ratio of transition to transversion events between two given DNA strings"""

    # define purines and pyrimidines and transition/transversion count stores
    purines = ["A", "G"]
    pyrimidines = ["C", "T"]
    Transitions = 0
    Transversions = 0

    # Compare nucleotide by nucleotide the two sequeunces, columinating all mistmathced bases in an array
    mismatchedNucleotides = []
    for indexNumber in range(len(stringS1)):
        if stringS1[indexNumber] in purines:
            if stringS2[indexNumber] in purines and stringS1[indexNumber] != stringS2[indexNumber]:
                Transitions += 1
            elif stringS2[indexNumber] in pyrimidines:
                Transversions += 1
        elif stringS1[indexNumber] in pyrimidines:
            if stringS2[indexNumber] in pyrimidines and stringS1[indexNumber] != stringS2[indexNumber]:
                Transitions += 1
            elif stringS2[indexNumber] in purines:
                Transversions += 1

    # calculate transition to transverion ratio:
    ttRatio = float(Transitions) / float(Transversions)
    return(ttRatio)




# Extract data from data file
# open file with read only permit, read line by line
# Open file containing DNA sequences, and assign DNA sequences data to a variable (dnaSeq)
fastaFILE = open(r"C:\Users\Emma\Documents\PhD\Computational\Python\Rosalind\Rosalind_Python_Problems\Bioinformatics Stronghold\Transitions and Transversions.txt", "rt")
allData = fastaFILE.readlines()
fastaFILE.close()


# Extract and define the two strings of DNA
# Create variables to store the working DNA sequence
currentID = ""              # tempoary store for working rosalind ID
currentDNA = ""
idSeqDictionary = {}
intron = ""                 # tempoary store of working intron sequence

# extraction of data from downloaded file and storage in dictionary
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


# separate strings from rest of data and convert dna strings to list variables, make compatiable with for loop
dnaSTRINGS = list(idSeqDictionary.keys())
stringS1 = list(dnaSTRINGS[0])
stringS2 = list(dnaSTRINGS[1])

# call function to calculate transition/transversion ratio of strings
print(transition_transvertionRATIO(stringS1, stringS2))
