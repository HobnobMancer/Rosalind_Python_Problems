# Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s (as a result, t must be no longer than s).
# The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position i of s is denoted by s[i].
# A substring of s can be represented as s[j:k], where j and k represent the starting and ending positions of the substring in s; for example, if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".
# The location of a substring s[j:k] is its beginning position j; note that t will have multiple locations in s if it occurs more than once as a substring of s (see the Sample below).
# Given: Two DNA strings s and t (each of length at most 1 kbp).
# Return: All locations of t as a substring of s.
# Sample data set uses a 1-based not 0-based numbering system

# Define given strings
givenStringS = "GATATATGCATATACTT"
givenSubStringT = "ATAT"

# Define function to fina all occurences of substring T in string S
def findALLsubstrings(string, substring):
    """Finds all occurences of a substring in a string
    Utilises and builds upon inbuild .find() function"""

    start = 0
    while True:
        start = string.find(substring, start)
        if start == -1: return
        yield start
        start += 1 # finds overlapping matches, += len(substring) would miss overlapping matches

# Use the function findALLsubstrings to find all occurences of substring T in string S
substringOccurencePYTHON = list(findALLsubstrings(givenStringS, givenSubStringT))
print(substringOccurencePYTHON)

# Python uses 0-based numbering, answer needed in 1-based number
# Convert 0-based to 1-based numbering
substringOccurence0BASED = []
i = 0

for index in substringOccurencePYTHON:
    substringOccurence0BASED.append(substringOccurencePYTHON[i]+1)
    i += 1

print(substringOccurence0BASED)

