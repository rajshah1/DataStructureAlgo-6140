from numpy import random as rand
from insertionSort import insertionSort as insertionSortCall
from mergeSort import mergeSort as mergeSortCall
from heapSort import heapSort as heapSortCall
import time as t
# Random Array Generator which Generates 1-D Array 
# Passing The same array to the import function call 
maxNumRange=10000;
testDataSize=1000;

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
heapSortCall(arrayInput)

# Use This Print to verify  while invoking from main file
#print(heapSortCall(arrayInput))

HeapSort_End=t.time()

print("HeapSort Takes : ",HeapSort_End-HeapSort_Start)
