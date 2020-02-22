# A DNA strings is a reverse palindrom if it is equal to its reverse complement. For instance, GCATGC is a reverse
# palindrome becuase its reverse complement is GCATGC.

# Given a DNA string of length at most 1kbp in FASTA format
# Return the prosition and length of every reverse palindrome in the string having length 4 and 12. You may return these
# pairs in any order

from Bio import SeqIO

# Extract and prepare the given data
record = SeqIO.read('Locating_Restriction_Sites_Data.fasta', 'fasta')
forwardSequence = str(record.seq)
reverseSequence = str(record.seq.complement())

for i in range(len(forwardSequence)):
    for j in range(i, len(forwardSequence)):
        motif = forwardSequence[i:j + 1]
        reverseMotif = reverseSequence[i:j + 1]
        if len(motif) >= 4 and len(motif) <= 12: # ensures the restriction site length is witihn the range defined above
            if motif == reverseMotif[::-1]:
                print(i + 1, len(motif)) # print out locus (in 1 base numbering) and length of the restriction site
                
