# After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

# Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

# Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)




# Prepare data from downloaded file containing data
# open file with read only permit, read line by line
# Open file containing DNA sequences, and assign DNA sequences data to a variable (dnaSeq)
fastaFILE = open(r"C:\Users\Emma\Documents\PhD\Computational\Python\Rosalind\Rosalind_Python_Problems\Bioinformatics Stronghold\RNA_Splicing_File.txt", "rt")
allData = fastaFILE.readlines()
fastaFILE.close()

# Create variables to store the working DNA sequence
givenGENE = ""             # entire DNA sequence of protein
intronSEQ = []            # list of introns nucleotide sequences
currentID = ""              # tempoary store for working rosalind ID
currentDNA = ""
idSeqDictionary = {}
intron = ""                 # tempoary store of working intron sequence


# extraction of data from downloaded file and storage in appropriate variables
for fileLine in allData:
    if fileLine[0] is ">":
        currentID = fileLine[1:].replace('\n','')
        currentDNA = ""
    else:
        strngFileline = str(fileLine)
        currentDNA = currentDNA + strngFileline[:-1]
        if currentID not in idSeqDictionary.values():
            idSeqDictionary[currentDNA] = currentID
        else:
            for key, value in dict(idSeqDictionary).items():
                if value is currentID:
                    del idSeqDictionary[key]
            idSeqDictionary[currentDNA] = currentID

# transfer DNA sequences from dictionary to list (intronSEQ)
intronSEQ = list(idSeqDictionary.keys())


# separate gene sequence from introns
givenGENE = intronSEQ[0]
del intronSEQ[0]
print('GENE', givenGENE)
print(intronSEQ)

# remove introns from gene
exonSEQ = ""        # exon nucleotide sequence of gene
index = 0           # index number of intron in intronSEQ list

for intron in intronSEQ:
    if index is 0:
        intron = intronSEQ[index]
        exonSEQ = givenGENE.replace(intron, "")
        index += 1
    else:
        intron = intronSEQ[index]
        exonSEQ = exonSEQ.replace(intron, "")
        print(index, "=", exonSEQ)
        index += 1





# translate DNA sequence of gene into protein sequence

# Create DNA codon to amino acid translation dictionary
dnaCodonDICTIONARY = {"TTT": "F", "CTT": "L", "ATT": "I", "GTT": "V",
                      "TTC": "F", "CTC": "L", "ATC": "I", "GTC": "V",
                      "TTA": "L", "CTA": "L", "ATA": "I", "GTA": "V",
                      "TTG": "L", "CTG": "L", "ATG": "M", "GTG": "V",
                      "TCT": "S", "CCT": "P", "ACT": "T", "GCT": "A",
                      "TCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
                      "TCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
                      "TCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
                      "TAT": "Y", "CAT": "H", "AAT": "N", "GAT": "D",
                      "TAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
                      "TAA": "STOP", "CAA": "Q", "AAA": "K", "GAA": "E",
                      "TAG": "STOP", "CAG": "Q", "AAG": "K", "GAG": "E",
                      "TGT": "C", "CGT": "R", "AGT": "S", "GGT": "G",
                      "TGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
                      "TGA": "STOP", "CGA": "R", "AGA": "R", "GGA": "G",
                      "TGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
                      }

# separate nucleotides into 3 nucleotide codons, use inbuilt wrap function
dnaCodenSeq = []
codonLength = 3
for codon in range(0, len(exonSEQ), codonLength):
   dnaCodenSeq.append(exonSEQ[codon: codon + codonLength])
print(dnaCodenSeq)
# loop through list of codons in gene to find corresponding amino acid
proteinSeq = ""
for codon in dnaCodenSeq:
    aminoacid = dnaCodonDICTIONARY[codon]
    proteinSeq = proteinSeq + aminoacid

print(proteinSeq)
