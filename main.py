from numpy import random as rand
from insertionSort import insertionSort as insertionSortCall
from mergeSort import mergeSort as mergeSortCall
import time as t
# Random Array Generator which Generates 1-D Array 
# Passing The same array to the import function call 

arrayInput=rand.randint(10000,size=1000)

# Function Call to InsertionSort
insertionSort_Start=t.time()
insertionSortCall(arrayInput)
insertionSort_End=t.time()

print("InsertionSort Takes : ",insertionSort_End-insertionSort_Start)

# Function Call to InsertionSort
mergeSort_Start=t.time()
mergeSortCall(arrayInput)

# Use This Print to verify  while invoking from main file
#print(mergeSortCall(arrayInput))

mergeSort_End=t.time()

print("MergeSort Takes : ",mergeSort_End-mergeSort_Start)


