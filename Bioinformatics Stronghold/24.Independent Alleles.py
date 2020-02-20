# Given: two positive intergers k (k <= 7) and N (N <= 2^k).  In this problem, we begin with Tom, who in the 0th
# generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on.
# Each organism always mates with an organism having genotype Aa Bb.

# Return: The probability that at least N AaBb organisms will belong to the k-th generation of Tom's family tree (don't
# count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors



import math


# define variables given by Rosalind
k = 7
N = 37
P = 2**k    # 2 to the power of k, the upper limit of N

# create variable to add probabilities of each even to
probabilityAaBb = 0

# calculate probability of at least N AaBb organisms will belong to the k-th generation
for i in range(N, P + 1):
    probability = ((math.factorial(P)) / (math.factorial(i) * math.factorial(P - i))) * (0.25**i) * (0.75**(P - i))
    probabilityAaBb += probability

# print probability of at least N AaBb organisms will belong to the k-th generation, rounded to 3 decimal places
print(round(probabilityAaBb, 3))
