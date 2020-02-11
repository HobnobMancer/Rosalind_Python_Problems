# Given: A protein string of length at most 1000 aa.
#
# Return: The total number of different RNA strings from which the protein could have been translated,
# modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)


# define given protein sequence
inputSEQ = input("What is the protein sequence? ")
caseSEQ = inputSEQ.upper()
proteinSEQ = list(caseSEQ)


# create dictionary storing the number of associated codons per amino acid
codonFrequencyDictionary = {'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 4,
                            'H': 2, 'I': 3, 'J': 0, 'K': 2, 'L': 6, 'M': 1,
                            'N': 2, 'O': 0, 'P': 4, 'Q': 2, 'R': 6, 'S': 6,
                            'T': 4, 'V': 4, 'W': 1, 'Y': 2, 'stop': 3}


# calculate total number of RNA strings that code for the amino acid sequence
possibilitiesCounter = 1 # the number of possible RNA strings that code for the amino acid sequence

for aminoAcid in proteinSEQ:
    possibilitiesCounter = possibilitiesCounter * codonFrequencyDictionary[aminoAcid]
possibilitiesCounter = possibilitiesCounter * codonFrequencyDictionary['stop']

result = possibilitiesCounter % 1000000
print(result)
