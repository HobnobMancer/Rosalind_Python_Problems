# A signed permutation of length n is some ordering of the positive integers {1,2,…,n} in which each integer is then
# provided with either a positive or negative sign (for the sake of simplicity, we omit the positive sign). For example,
# =(5,−3,−2,1,4) is a signed permutation of length 5.

# Given: A positive integer n≤6.

# Return: The total number of signed permutations of length n, followed by a list of all such permutations
# (you may list the signed permutations in any order).


import itertools

# generate list of numbers
givenInterger = 4
intergerList = list(range(1, givenInterger+1))
permutationList = []
permutationCount = 0

# create all variations of list orders
for i in itertools.permutations(intergerList):
    for j in itertools.product([-1, 1], repeat=len(intergerList)):
        permutation = [a * sign for a, sign in zip(i, j)]
        permutationList.append(permutation)
        permutationCount += 1

# output number of permutations
print(permutationCount)
with open("output.txt", "a") as f:
    print(permutationCount, file=f)

# create output in correct style (e.g. '1 2 3 4') for permutations
for i in range(len(permutationList)):
    print(*permutationList[i], sep=' ')

for i in range(len(permutationList)):   # output to text file for easier copying/extraction
    with open("output.txt", "a") as f:
        print(*permutationList[i], sep=' ', file=f)

