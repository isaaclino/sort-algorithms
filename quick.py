#   QUICK algorithm
#   Running time average case(n nlog n) wosrt case O(log n)

#   The quick sort uses divide and conquer to gain the same advantages as the merge sort,
#   while not using additional storage. As a trade-off, however, it is possible that the list
#   may not be divided in half. When this happens, we will see that performance is diminished.

#   A quick sort first selects a value, which is called the pivot value.
#   Although there are many different ways to choose the pivot value, we will simply use
#   the first item in the list. The role of the pivot value is to assist with splitting list.
#   Actual position where the pivot value belongs in the final sorted list,
#   commonly called the split point, will be used to divide the list
#   for subsequent calls to the quick sort.

import os

def quick(list):
    
    # sends the list to a helper fuction
    # it sets the first point as 0 and
    # it sets the last point as the lenght of the list
    #      -1 " to avoid counting the null terminator"
    helper(list,0,len(list)-1)



def helper(list,first,last):

    # check and keep splitting
    if first < last:
        splitpoint = partition(list,first,last)
            
        helper(list,first,splitpoint-1)
        helper(list,splitpoint+1,last)



def partition(list,first,last):
    
    # set the pivot position
    pivot = list[first]
    
    # Partitioning begins by locating two position positions
    # (leftPosition and rightPosition marks) the beginning and end of the remaining
    # items in the list
    leftPosition = first+1
    rightPosition = last
    
    # using a boolean done to check and iterate the whole array
    done = False
    while not done:
        
        # It moves items that are on the wrong side with respect to the pivot value
        # while also converging on the split point
        while leftPosition <= rightPosition and list[leftPosition] <= pivot:
            leftPosition = leftPosition + 1
                                
        while list[rightPosition] >= pivot and rightPosition >= leftPosition:
            rightPosition = rightPosition -1
        
        # Stops at the point where rightPosition mark is less than leftPosition mark
        if rightPosition < leftPosition:
            # It calls the bool flags to exit outer while loop
            done = True
        
        else:
        # Swaps until the left and right position meet
            temp = list[leftPosition]
            list[leftPosition] = list[rightPosition]
            list[rightPosition] = temp
                                                                
    temp = list[first]
    list[first] = list[rightPosition]
    list[rightPosition] = temp

    return rightPosition

def main():
    
    os.system('clear')
    list = [1,3,5,7,34,22,1,23,98,43,12,54,23,12,75,22,56,9,90,2,3,6,34,54,22,1]
    
    print "\nQuick Sort\n"
    print "\nOriginal list: "
    print list
    
    print "\ncalling quick sort..."
    quick(list)
    print list


if __name__ == '__main__': main()

