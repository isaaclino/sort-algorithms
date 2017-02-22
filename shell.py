#   SHELL algorithm
#   Running time

import os

def shell(list):
    sublistcount = len(list)//2
    while sublistcount > 0:
        
        for startposition in range(sublistcount):
            gapInsertionSort(list,startposition,sublistcount)
            
        print("After increments of size",sublistcount,"The list is",list)
                
        sublistcount = sublistcount // 2

def gapInsertionSort(list,start,gap):
    for i in range(start+gap,len(list),gap):
        
        currentvalue = list[i]
        position = i
        
        while position>=gap and list[position-gap]>currentvalue:
            list[position]=list[position-gap]
            position = position-gap
        
        list[position]=currentvalue

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

