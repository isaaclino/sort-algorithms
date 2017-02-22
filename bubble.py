# BUBBLE SORT
# best case is Omega(n) wosrt case O(n^2)
# The strategy is to start at the begining of the list and compare
# pairs of items as it moves down to the end.
#
# Each time the items in the pair are out of order, this algorithm will swap them
# The porcess consists in "bubbleling" the largest item to the end of the list.
# It repeats the process from the beginnign of the list and goes from current to last item,
# until it reaches the last item, by then, the list should be sorted

# This version of bubbble sort is tweked a little to improve the best case Omega(n) but still on
# average and worst case as n^2
# IMPROVED:
# If no swap occurs during the pass through the main outer loop, then the list is sorted
# It happens on any pass and in the best case it will happend in the first pass.
# To track this process, a boolean is created, in this case is called 'swapped', which
# it tracks how many times is swapped and returns from the fucntion when inner loop is not set
# "THIS ONLY IMPROVES BEST CASE TO (n), Worst case still (n^2)"

import os

def bubble(list):

    swapped = True

    # continue sorting until is false
    while swapped:

        # start by assuming nothing is sorted
        swapped = False

        #loop the entire list
        for i in range(len(list)-1):

            #saves the currnet position
            cur = list[i]
            j = i+1

            if list[i] > list [j]:

                # do a swap and reset swap to True if something is sorted
                list[i]=list[j]
                list[j]=cur
                swapped = True

    print list

def main():

    os.system('clear')
    list = [1,3,5,7,34,22,1,23,98,43,12,54,23,12,75,22,56,9,90,2,3,6,34,54,22,1]
    
    print "\nBubble Sort\n"
    print "\nOriginal list: "
    print list
    
    print "\ncalling bubble sort..."
    bubble(list)

if __name__ == '__main__': main()
