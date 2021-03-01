from numpy import random as rand
from insertionSort import insertionSort as insertionSortCall
from mergeSort import mergeSort as mergeSortCall
from heapSort import MinHeap
from quicksort import quickSortIterative as quickSortCall
from modifiedQuickSort import mquickSort as mquickSortCall
import time as t
# Random Array Generator which Generates 1-D Array 
# Passing The same array to the import function call 
maxNumRange=10000
testDataSize=1000

arrayInput=rand.randint(maxNumRange,size=testDataSize)

# Function Call to InsertionSort

insertionSort_Start=t.time()
insertionSortCall(arrayInput)
insertionSort_End=t.time()

print("InsertionSort Takes : ",insertionSort_End-insertionSort_Start)

#### Function Call to MergeSort

mergeSort_Start=t.time()
mergeSortCall(arrayInput)

# Use This Print to verify  while invoking from main file
#print(mergeSortCall(arrayInput))

mergeSort_End=t.time()

print("MergeSort Takes : ",mergeSort_End-mergeSort_Start)


#### Function Call to HeapSort

HeapSort_Start=t.time()
#heapSortCall(arrayInput)

# Use This Print to verify  while invoking from main file
#print(heapSortCall(arrayInput))
heap=MinHeap(testDataSize)
heap_ar=[]
for i in arrayInput:
    heap.insert(i)
for i in range(len(arrayInput)):
	heap_ar.append(heap.remove())
#print(heap_ar)

HeapSort_End=t.time()

print("HeapSort Takes : ",HeapSort_End-HeapSort_Start)



#### Function Call to inplcae quickSort

quickSort_Start=t.time()
quickSortCall(arrayInput,0,testDataSize-1)

# Use This Print to verify  while invoking from main file
quickSort_End=t.time()

print("QuickSort Takes : ",quickSort_End-quickSort_Start)


#### Function Call to modifed quickSort

mquickSort_Start=t.time()
mquickSortCall(arrayInput,0,testDataSize)

# Use This Print to verify  while invoking from main file
mquickSort_End=t.time()
#print(mquickSortCall(arrayInput,0,testDataSize))

print("Modifed - QuickSort Takes : ",mquickSort_End-mquickSort_Start)
