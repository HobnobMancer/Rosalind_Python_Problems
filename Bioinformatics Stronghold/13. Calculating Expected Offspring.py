# Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:
#
#     AA-AA
#     AA-Aa
#     AA-aa
#     Aa-Aa
#     Aa-aa
#     aa-aa
#
# Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.

# Probability of offspring having dominant phenotype for each couple genotype, when couple has two children
AA_AAgenotype = 1 * 2
AA_Aagenotype = 1 * 2
AA_aagenotype = 1 * 2
Aa_Aagenotype = 0.75 * 2
Aa_aagenotype = 0.5 * 2
aa_aagenotype = 0

# Number of couples with each genotype pairing in population
totalAA_AA = 18215
totalAA_Aa = 19735
totalAA_aa = 18315
totalAa_Aa = 19331
totalAa_aa = 16496
totalaa_aa = 19039

# Expected number of offspring with dominant phenotype
expectedOffspringOnlyChild = (totalAA_AA*AA_AAgenotype)+(totalAA_Aa*AA_Aagenotype)+(totalAA_aa*AA_aagenotype)+(totalAa_Aa*Aa_Aagenotype)+(totalAa_aa*Aa_aagenotype)+(totalaa_aa*aa_aagenotype)

print("Expected number of offspring with a dominant phenotye is", expectedOffspringOnlyChild)
