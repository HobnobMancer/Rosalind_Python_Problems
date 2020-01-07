# Given a file containing at most 1000 lines
# Return a file containing all even-numbered lines, assume 1-based numbering of lines

# Open text file in read mode
openFile = open(r"rosalind_ini5.txt", "r")

# Solution taken from GitHub and reddit, and modified
i = 1
for line in openFile:
    if (i % 2) is 0:
        print(line)
    i = i + 1