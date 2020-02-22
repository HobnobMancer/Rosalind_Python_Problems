# Given a collection of DNA strings in FASTA format, having a total length at most 10 kbp
# Return the adjacnecy list corresponding to O3, returning edges in any order. The adjacency list is formed but directed
# edges between nodes (which are the strings) such that the suffix of length k of strings S is the prefix of string T.
# In this case, Ok is the length of the sequence overlap, and here k is 3



# Basic Python Approach


# Define function that compares the suffix of one sequence to the prefix of the other to see if the sequences are
# adjacent
def adjacencyCheck(seqSuffix, seqPrefix):
    """Compares the suffix of one sequence to the prefix of the other to see if the sequences are adjacent.
    Specifically, the function passess along the prefix of the second sequence and compares the nucleotide
    sequence to the suffix of the other string, working through this other string in reverse"""

    # Both sequences are passed to the function as strings
    # Convert sequences from strings to lists to allow individual element calling and comparison
    seqSuffixLIST = list(seqSuffix)
    seqPrefixLIST = list(seqPrefix)


    # Create variable to store rosalind IDs
    directedEdgeRosalindIDs = []


    indexNumberSuffix = len(seqSuffix) - 1 # this makes further working from the 3' of the DNA sequence,
                                           # checking its suffix


    # Check the first base initially for quick termination if not adjacent
    if seqPrefix[0] != seqSuffix[indexNumberSuffix]:
        return # if the first bases checked to do not match the comparison is terminated

    # Check if comparing the same sequence against itself, if true: terminate
    elif string_ID_dictionary[seqSuffix] == string_ID_dictionary[seqPrefix]:
        return # terminate function if comparing the same sequence against itself

    # Check for 03, check the first 3 bases against the last 3 bases of the respecitve sequences
    else:
        if seqPrefix[0] == seqSuffix[indexNumberSuffix] and seqPrefix[1] == seqSuffix[indexNumberSuffix - 1] and seqPrefix[2] == seqSuffix[indexNumberSuffix - 2]:
                # add directed edge to the list 'directedEdgeRosalindIDs'
                directedEdgeRosalindIDs.append(string_ID_dictionary[seqSuffix])
                directedEdgeRosalindIDs.append(string_ID_dictionary[seqPrefix])
                directedEdgeRosalindIDs.append('NewLine') # this will facilitate printing out each directed edge on
                                                          # on a separate line

                # convert the directed edge into a string, from a list, and ensure correct formating
                # e.g. 'Rosalind_0498 Rosalind_2391'
                directedEdgeStringAnswer = str(directedEdgeRosalindIDs)
                directedEdgeStringAnswer = directedEdgeStringAnswer.replace(',','')

                return directedEdgeStringAnswer



# Prepare Data

# Extract data from data file
# Open file with read only permit, read line by line
# Open file containing UniProt IDs, and assign IDs to a variable (uniprotIDs)
fastaFILES = open(r"/home/em/PycharmProjects/Rosalind/Bioinformatics Stronghold/OverlapGraphs", "rt")
rawStringData = fastaFILES.readlines()
fastaFILES.close()

# Separate string sequences and rosalind IDs
# Create variables to store the working DNA sequence and ID
currentID = ""              # current working Rosalind ID
currentDNA = ""             # current working DNA sequence
string_ID_dictionary = {}      # contains Rosalind IDs and associated GC contents

# While loop to separate and store Rosalind IDs
# Specifically store the DNA sequence as the key and Rosalind ID as the value
# e.g. {'AAATAAA': 'Rosalind_0498'}
for fileLine in rawStringData:
    if fileLine[0] is ">":
        currentID = fileLine[1:].replace('\n','')
        currentDNA = ""
    else:
        strngFileline = str(fileLine)
        currentDNA = currentDNA + strngFileline[:-1]
        if currentID not in string_ID_dictionary.values():
            string_ID_dictionary[currentDNA] = currentID
        else:
            for key, value in dict(string_ID_dictionary).items():
                if value is currentID:
                    del string_ID_dictionary[key]
            string_ID_dictionary[currentDNA] = currentID



# Gather string sequences into single list
allStringSequences = []
for key in string_ID_dictionary.keys():
    allStringSequences.append(key)
comparisonList = allStringSequences.copy() # creates list of all sequences to facilitate sequence comparison

# Create variable to store directed edges of adjacent nodes, these will be the rosalind IDs written in the direction
# of the edge, e.g. 'Rosaling_0498 Rosalind_2391'
directedEdges = []

j = 0 # create variable to store index number to pass through squences in comparison list

for i in range(len(allStringSequences)):
    for j in range(len(allStringSequences)):
        directedEdges.append(adjacencyCheck(comparisonList[j], allStringSequences[i]))
        j += 1
    i += 1


# Modify output to be incorrect format
result = []
for element in directedEdges:
    if element != None:
        result.append(element)

result = str(result)
result = result.replace('"', '')
result = result.replace("' 'NewLine'], ['", "\n")
result = result.replace("[['", "")
result = result.replace("' 'NewLine']]", "")
result = result.replace("' '", " ")
print(result)



# BioPython Approach

from Bio import SeqIO

prefixes = []
suffixes = []
handle = open('samplefile.fasta', 'r')
for record in SeqIO.parse(handle, 'fasta'):
    count1 = 0
    count2 = 0
    prefix = [record.id]
    suffix = [record.id]
    pre = ''
    suf = ''
    for nt in record.seq:
        if count1 < 3:
            pre += nt
            count1 += 1
    prefix.append(pre)
    for tn in reversed(record.seq):
        if count2 < 3:
            suf += tn
            count2 += 1
    suffix.append(''.join(reversed(suf)))
    prefixes.append(prefix)
    suffixes.append(suffix)
handle.close()

for i, k in enumerate(suffixes):
    currentsf = suffixes[i][1]
    currentid = suffixes[i][0]
    for j, l in enumerate(prefixes):
        if currentsf == prefixes[j][1] and currentid != prefixes[j][0]:
            print(currentid, prefixes[j][0])   
 
