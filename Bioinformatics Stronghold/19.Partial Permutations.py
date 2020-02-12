# A partial permutation is an ordering of only k objects taken from a collection containing n objects (i.e., k≤n).
# For example, one partial permutation of three of the first eight positive integers is given by (5,7,2).

# The statistic P(n,k) counts the total number of partial permutations of k objects that can be formed from a
# collection of n objects. Note that P(n,n) is just the number of permutations of n objects, which we found to be equal
# to n!=n(n−1)(n−2)⋯(3)(2) in “Enumerating Gene Orders”.

# Given: Positive integers n and k such that 100≥n>0 and 10≥k>0.

# Return: The total number of partial permutations P(n,k), modu


import itertools

# define given values
numberOfObjects = 93 # referred to as 'n' above
totalSelectedObjects = 8 # referred to as 'k' above
permutationCount = 0 # number of permutations possible in range n, length k

# calculate number of partial permutations
for permutation in itertools.permutations(range(1, numberOfObjects + 1), totalSelectedObjects):
    permutationCount += 1

# modulo 1,000,000
result = permutationCount % 1000000
print(result)


Faster method found online:
n = 21
k = 7
partial_perm = 1
for i in range(k):
    partial_perm *= (n - i)
print(partial_perm % 1000000)
