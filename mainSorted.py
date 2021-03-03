from numpy import random as rand
import random
from insertionSort import insertionSort as insertionSortCall
from mergeSort import mergeSort as mergeSortCall
from heapSort import heapSort as heapSortCall
from quicksort import quickSortIterative as quickSortCall
from modifiedQuickSort import mquick_sort as mquickSortCall
import time as t
# Random Array Generator which Generates 1-D Array 
# Passing The same array to the import function call 

# Input Test Data Size Array
inputTestDataarr = [1000,2000,3000,5000,10000,20000,30000,40000,50000,60000]

# Plot Y Axis Values
yTicks_insertion_sort = [] 
yTicks_merge_sort = []
yTicks_inplaceQuick_sort = []
yTicks_medianQuick_sort = []
yTicks_heap_sort = []

time_insertion_sort = []
time_merge_sort = []
time_inplaceQuick_sort = []
time_medianQuick_sort = []
time_heap_sort = []
for index in range(0, len(inputTestDataarr)):


    arrayInput = []
    for a in range(0,inputTestDataarr[index]):
        arrayInput.append(a)
    
    insertionSort_Start=t.time()
    insertionSortCall(arrayInput[:])
    insertionSort_End=t.time()
    time_insertion_sort.append((insertionSort_End-insertionSort_Start)*1000)
    #print("InsertionSort Takes : ",insertionSort_End-insertionSort_Start)

    #### Function Call to MergeSort
    mergeSort_Start=t.time()
    mergeSortCall(arrayInput[:])

    # Use This Print to verify  while invoking from main file
    #print(mergeSortCall(arrayInput))

    mergeSort_End=t.time()
    time_merge_sort.append((mergeSort_End-mergeSort_Start)*1000)
    #print("MergeSort Takes : ",mergeSort_End-mergeSort_Start)


    #### Function Call to HeapSort
    HeapSort_Start=t.time()
    #heapSortCall(arrayInput)

    # Use This Print to verify  while invoking from main file
    #print(heapSortCall(arrayInput))
    heapSortCall(arrayInput[:])

    HeapSort_End=t.time()
    time_heap_sort.append((HeapSort_End-HeapSort_Start)*1000)
    #print("HeapSort Takes : ",HeapSort_End-HeapSort_Start)
    
    #### Function Call to inplcae quickSort
    quickSort_Start=t.time()
    quickSortCall(arrayInput[:],0,inputTestDataarr[index]-1)
    # Use This Print to verify  while invoking from main file
    quickSort_End=t.time()
    time_inplaceQuick_sort.append((quickSort_End-quickSort_Start)*1000)
    #print("QuickSort Takes : ",quickSort_End-quickSort_Start)


    #### Function Call to modifed quickSort
    mquickSort_Start=t.time()
    mquickSortCall(arrayInput[:])
    # Use This Print to verify  while invoking from main file
    mquickSort_End=t.time()
    #print(randomArray)
    time_medianQuick_sort.append((mquickSort_End-mquickSort_Start)*1000)
    #print("Modifed - QuickSort Takes : ",mquickSort_End-mquickSort_Start)


## Final Timing alanaysis Print:
print("Insertion Sort Timing ",time_insertion_sort)
print("Merge Sort Timing ",time_merge_sort)
print("Heap Sort Timing ",time_heap_sort)
print("inPlace Quick Sort Timing ",time_inplaceQuick_sort)
print("Modified Quick Sort Timing ",time_medianQuick_sort)

    


