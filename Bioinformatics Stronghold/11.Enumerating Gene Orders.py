# A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5
# Given: A positive integer n≤7
# Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

import itertools

# generate list of numbers
givenInterger = 7
intergerList = list(range(1, givenInterger+1))

# create all variations of list orders
listCombinations = tuple(itertools.permutations(intergerList))

# find number of variations
variationCount = len(listCombinations)
print(variationCount)

# create output in correct style (e.g. '1 2 3 4')
stringCombinations = str(listCombinations)
result = stringCombinations.replace('(','')
result = result.replace('), ','\n')
result = result.replace(')','')
result = result.replace(',','')
print(result)
