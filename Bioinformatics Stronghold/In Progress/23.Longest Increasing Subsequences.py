# A subsequence of a permutation is a collection of elements of the permutation in the order that they appear.
# For example, (5, 3, 4) is a subsequence of (5, 1, 3, 4, 2).

# A subsequence is increasing if the elements of the subsequence increase, and decreasing if the elements decrease.
# For example, given the permutation (8, 2, 1, 6, 5, 7, 4, 3, 9), an increasing subsequence is (2, 6, 7, 9),
# and a decreasing subsequence is (8, 6, 5, 4, 3). You may verify that these two subsequences are as long as possible.

# Given: A positive integer n≤10000 followed by a permutation π of length n.

# Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.


from math import pi


# store pi to length n, when 'n' in the number in the string '._f' minus 1, thus n=10 becomes '.9f'
''.format(pi)
piLengthN = str(format(pi, '.9f'))

# store digits in pi as individual items in a list
piLengthN = piLengthN.replace('.','')
piLengthN = list(piLengthN)


# Find longest increasing subsequence






givenSequence = 5, 1, 4, 2, 3


subsequenceIndicesList = [None] * len(givenSequence)
                                             # create a list the same length as sequence, with empty elements to store
                                             # the indices of the elementh in given sequence that make up the
                                             # subsequence, i.e. sequence[nextPossibleValue[j]]

# declare variables

minimumLength = 1   # since there is at least one element in the sequence, the longest increasing subsequece
                    # must have a length of at least one

longestLength = minimumLength   # since there is at least one element in the sequence, the longest increasing subsequece
                                # must have a length of at least one, thus initially the longest subsequence is equal
                                # to the shortest subsequence length


# loop over the sequence
# start at second element so that can tested against the first element
for i in range(1, len(givenSequence)):

    upperBoundry = minimumLength    # since the longest increasing subsequence length is 1, the inital upper boundry
                                    # and this facilitates checking the second element against the first
                                    # such that givenSequence[nextValue[j]] < givenSequence[i], becuase j has a
                                    # default value of 0 and thus givenSequence[0] < givenSequence[1] can be checked

    lowerBountry = 0    # this is the lowest possible indices possible


    # first check the currently examined element against the upper boundry
    # specifically check whether the last element added to the subsequence indicies list is less than the element
    # currently being examined/tested

    if givenSequence[subsequenceIndicesList[upperBoundry - 1]] < givenSequence[i]:
        j = upperBoundry    # if yes: the last number taken from the sequence and added to the subsequence list is less
                            # than the current number in the sequence being tested/examined.
                            # Therefore, the index number used to call an element in subsequence indicies list is
                            # changed and we move along the subsequence indicies list, allowing us to add a new index
                            # number to the list of subsequence indicies

    else:
        while upperBoundry - lowerBoundry > 1:
            # continue while the upper and lower boundries are not the same and thus the subsequence length is greater
            # than one and is growing

            midPoint = (upperBoundry + lowerBoundry) // 2           # // implements floor division generating the result
                                                                    # of the division rounded down

            if givenSequence[subsequenceIndicesList[mid - 1]] < givenSequence[i]:
                lowerBoundry = midPoint
            else:
                upperBoundry = midPoint

        j = lowerBountry
# so what is it doing now?
