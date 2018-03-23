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
# "THIS ONLY IMPROVES BEST CASE TO (n), Worst case (n^2)"

def bubble(mylist):

    swapped = True
    while swapped:

        swapped = False
        for i in range(len(mylist)-1):
            
            if mylist[i] > mylist[i+1]:
        
                mylist[i], mylist[i+1] = mylist[i+1], mylist[i]
                swapped = True

    return mylist


def main():
    mylist = map(int, raw_input("Enter a list of numbers to be sorted: ").split(' '))
    
    print "Unsorted list: ", mylist
    print "Sorted list:   ", bubble(mylist)


if __name__=="__main__":main()

