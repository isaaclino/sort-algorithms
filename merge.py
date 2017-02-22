#   MERGE algorithm (DIVIDE AND CONQUER)

#   Running time is O(n log n) for average and worst case
#
#   This strategy as a way to improve the performance of sorting algorithms.
#   Merge sort is a recursive algorithm that continually splits a list in half.
#   If the list is empty or has one item, it is sorted by definition (the base case).
#   If the list has more than one item, we split the list and recursively invoke a merge sort
#   on both halves. Once the two halves are sorted, the fundamental operation, called a merge,
#   Merging is the process of taking two smaller sorted lists and combining them
#   together into a single, sorted, new list

import os

def merge(list):
    
    # Testing purposes

    if len(list)>1:
        
        # floor division to get a whole number and store it as mid
        mid = len(list)//2
        
        # store and sort the divided list on left and right
        left = list[:mid]
        right = list[mid:]
        merge(left)
        merge(right)
        
        # declare and initialize
        i, j, k = 0, 0, 0
        
        # Iterate trough the array to compare left and right
        # It copies back the smalest element from two halves into original array
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k]=left[i]
                i=i+1 #i++
        
            #If right element is smaller than left
            else:
                list[k]=right[j]
                j=j+1 #j++

            k=k+1 #k++
        
        
        # Iterates to merge back the left and right recursevelly
        # If one iteration is missing (either the left or right)
        
        # Appeds the result to left
        while i < len(left):
            list[k]=left[i]
            i=i+1 #i++
            k=k+1 #k++

        # Appeds the result to right
        while j < len(right):
            list[k]=right[j]
            j=j+1 #j++
            k=k+1 #k++

    return list


def main():
    
    os.system('clear')
    list = [1,3,5,7,34,22,1,23,98,43,12,54,23,12,75,22,56,9,90,2,3,6,34,54,22,1]
    
    print "\Merge Sort\n"
    print "\nOriginal list: "
    print list
    
    print "\ncalling merge sort..."
    print merge(list)

if __name__ == '__main__': main()









