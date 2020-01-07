# Given two positive intergers a and b, when a < b < 10000
# Return the sum of all intergers from a through b, inclusively

# define variables
a = 4783
b = 9654

# create array of all numbers between a and b
arrayAB = []
for number in range(a, b):
    if (number % 2) is not 0:
        arrayAB.append(number)

# ensure inclusion of b if off
if (b % 2) is not 0:
    arrayAB.append(b)
else:
    print("b not included because not odd")

# calculate sum of all odd numbers between a and b
abSum = 0
for oddNumber in arrayAB:
    abSum = abSum + oddNumber
print(abSum)
