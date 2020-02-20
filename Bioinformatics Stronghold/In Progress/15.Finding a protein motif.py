# Given: At most 15 UniProt Protein Database access IDs.
# Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.

# take IDs and add into http://www.uniprot.org/uniprot/id-here.fasta
# N-glycosylaion motif: N{P}[ST]{P}.
# when {+} means any amino acid except +
# and when [+ =] means with amino acid + or =


# Example output:
# B5ZC00
# 85 118 142 306 395



from urllib.request import urlopen
from Bio import SeqIO
import re



# Create function to find N-Glycosylation motif in a given protein sequence
def findMotifLocus(sequence, id):
    """Find the location of the first amino acid of the N-glycosylation motif N{P}[ST]{P}, when {P} means any amino
    acid except P, and [ST] means either S or T.
    Pass to the function the amino acid sequence of the protein of interest and the index number of the UniProt ID
    in the list of IDs created in the main body of the script"""

    # create search range, motif cannot extend beyond the end of the sequence
    searchRange = len(sequence) - 4

    # create empty list to store starting amino acid position of motif
    positions = []

    # pass through sequence looking for all occurences of mofit, including overlapping occurences, retuning the position
    # of the first amino acid in the protein sequence at which the motif starts
    for j in range(0, searchRange):
        # first, check if S and not T in third position
        if sequence[j] is 'N' and sequence[j+1] is not 'P' and sequence[j+2] is 'S' and sequence[j+3] is not 'P':
            aminoAcidPosition_S = j + 1
            positions.append(aminoAcidPosition_S)
            j += 1
        # second, check if T and not S in third position
        elif sequence[j] is 'N' and sequence[j+1] is not 'P' and sequence[j+2] is 'T' and sequence[j+3] is not 'P':
            aminoAcidPosition_T = j + 1
            positions.append(aminoAcidPosition_T)
            j += 1

    motifPositions = str(positions)
    motifPositions = motifPositions.replace(',', '')
    motifPositions = motifPositions.replace('[', '')
    motifPositions = motifPositions.replace(']', '')

    if len(positions) != 0:
        print(uniprotIDsLIST[id])
        print(motifPositions)

    return




# Prepare the given data

# Extract IDs from text file which must contain no empty lines at the end of the file
# open file with read only permit, read line by line
# Open file containing UniProt IDs, and assign IDs to a variable (uniprotIDs)
fastaFILES = open(r"/home/em/PycharmProjects/Rosalind/Bioinformatics Stronghold/UniProtIDs", "rt")
uniprotIDs = fastaFILES.readlines()
fastaFILES.close()

uniProtDICTIONARY = {}
currentSEQ = ""


# Transfer IDs to list and remove new line character
uniprotIDsLIST = [] # create new empty list to store UniProt IDs

for i in uniprotIDs:
    workingID = i.replace('\n','')
    uniprotIDsLIST.append(workingID)


# Access and extract protein sequences, storing them in a single FASTA file
for i in range(len(uniprotIDsLIST)):
    workingURL = "http://www.uniprot.org/uniprot/" + uniprotIDsLIST[i] + ".fasta"
    sequence = urlopen(workingURL)
    fastaData = sequence.read().decode('utf-8', 'ignore')
    with open('seq_file.fasta', 'a') as text_file:
        text_file.write(fastaData)




# Find N-glycosylation motif in protein sequences and return answer
# N-glycosylaion motif: N{P}[ST]{P}.

# open the fasta file
handle = open('seq_file.fasta', 'r')

# create count to work through list of UniProt IDs
idCount = 0

# create dictionary to store results, and facilitate only printing of sequences containing the N-Glycosylation motif
motifPositionDictionary = {}

for record in SeqIO.parse(handle, 'fasta'):
    if idCount < len(uniprotIDsLIST):   # prevent against index out of range error when adding values to dictionary
        sequence = str(record.seq)
        findMotifLocus(sequence, idCount)
    idCount += 1
