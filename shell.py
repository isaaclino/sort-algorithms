#   SHELL algorithm
#   Running time:
#   Best Runing time:       Omega(n logn)
#   Average Running time:   Theta( n(logn)^2 )
#   Worst Running time:     O( n(logn)^2 )
#
#   Shellsort allows the exchange of items that are far apart.
#   It arranges the list of elements so that, starting anywhere,
#   considering every hth element gives a sorted list.
#
#   How it works?
#   Initialize the value of h
#   Divide the list into smaller sub-list of equal interval h
#   Sort these sub-lists using insertion sort
#   Repeat until complete list is sorted

import os

def shell(list):
    
    # get floor division(integer only) from the original list lenght and store it in a gap
    # to calculate the gap or interval
    gap = len(list)//2
    
    while gap > 0:
        
        # starts scan from initial starting position to the length for gap array
        # for start in range(gap):
        for i in range(len(list)):
            
            currentValue = list[i]
            position = i
            
            # until there is no current gap and current value is smaller that position
            while position>=gap and list[position-gap]>currentValue:
            
                # It shifts the elements to the right
                list[position]=list[position-gap]
                position = position-gap
            
            #set the current value and insert the number at list position
            list[position] = currentValue
            
        # After increments of size of gap
        # Get the floor division (integer) of the gap and store it back into gap
        # Finaly it just calculates the interval
        gap = gap // 2


def main():
    
    os.system('clear')
    list = [1,3,5,7,34,22,1,23,98,43,12,54,23,12,75,22,56,9,90,2,3,6,34,54,22,1]
    
    print "\nShell Sort\n"
    print "\nOriginal list: "
    print list
    
    print "\ncalling shell sort..."
    shell(list)
    print list

if __name__ == '__main__': main()

