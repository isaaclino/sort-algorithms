# SELECTION SORT
# Runnig time best and worst O(n^2)
# List size n outer loop executes n-1 times
# 1st pass through outer loop executes n-1 times.
# 2nd pass through outer loop, the inner loop executes n-2
# Last pass through outer loop, the inner lopp executes once.
# Thus the total number of comparisons for a list of size n is:
# = (n-1) + (n-2) + ... + 1
# = n(n-1) /2
# = 1/2(n^2) - 1/2(n)

# The algorithm is call SELECTION sort because each pass through the main loop selects a sigle
# item to be moved.

# the purpose of this strategy is search the entire list for the position of the
# smalest item. If smallest position is not equal to first position, the algorithm swaps
# items at those positions.

# The algorithm returns the second position adn repeats the process,
# swapping the smallest item with the item at the second position. When algorithm reaches
# last position the list should be sorted
import os

def selection(list):
    
    #iterates the list n times (which is the length size)
    for i in range(len(list) -1):
        # for the smallest
        minIndex = i            # saves the position
        minValue = list[i]      # saves the value
        j = i + 1               # initializes j for inner loop with the position of i + 1

        # it starts the search
        while j < len(list):
            if list[j] < list[minIndex]:
                minIndex=j
                minValue = list[j]
            j += 1

        # using temp to swap the items at given position
        temp = list[i]
        list[i] = list[minIndex]
        list[minIndex] = temp


    print list

def main():

    os.system('clear')
    list = [1,3,5,7,'r',22,1,23,98,'a','c','b',43,12,54,0,22,56,9,90,2,3,6,34,54,22,'z','Z',99,'A']

    print "\nSelection Sort\n"
    print "\nOriginal list: "
    print list
    
    print "\ncalling selection sort..."
    selection(list)

if __name__ == '__main__': main()
