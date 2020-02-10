#Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

#Given: Positive integers n≤100 and m≤20
# Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.


kits = 2 # number of kits per litter
nth_month = 6
lifespan = 3 # lifespan of rabbits


# define function based on Fibonacci sequence to calcuate the total number of rabbit pairs in the nth month
def rabbitFibonacci(n):
    """Function to caclulate the number of rabbit paris in the nth month
    Based upon the Fibonacci sequence
    When calling the function 'n' represents the nth term for the sequence to terminate at"""

    # Breading pairs in first month
    if n==1:
        return 1
    # Breeding pairs in second month
    elif n==2:
        return 1
    # Breeding pairs in third month
    elif n==3:
        return 2

    # breading pairs in subsequent months
    elif n <= lifespan:
        return rabbitFibonacci(n - 1) + (rabbitFibonacci(n - 2))
    elif n > lifespan:
        return (rabbitFibonacci(n-1) + (rabbitFibonacci(n-2))) - (rabbitFibonacci(n - lifespan))


# Return number of rabbit pairs after n months
if nth_month <= lifespan:
    print("The number of rabbit pairs after", nth_month, "months is", rabbitFibonacci(nth_month))
elif nth_month > lifespan:
    print("The number of rabbit pairs after", nth_month, "months is", rabbitFibonacci(nth_month)+1)

