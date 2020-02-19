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



# Prepare Data

# Extract IDs from text file
# open file with read only permit, read line by line
# Open file containing UniProt IDs, and assign IDs to a variable (uniprotIDs)
fastaFILES = open(r"C:\Users\Emma\Documents\PhD\Computational\Python\Rosalind\Rosalind_Python_Problems\Bioinformatics Stronghold\UniProtIDs.txt", "rt")
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



# Find N-glycosylation motif in protein sequences
# N-glycosylaion motif: N{P}[ST]{P}.


# i = 0
# for i in fastaSeq
#   if N:
#       if i+1 is not P:
#           if i+2 is S or T:
#               if i+3 is not P:
#                   add to dictionarty
#                   dictionaryNAME['key'].append(i)

# print dictionary
