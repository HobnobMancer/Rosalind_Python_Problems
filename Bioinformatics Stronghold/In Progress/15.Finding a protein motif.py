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
