from numpy import random as rand
from insertionSort import insertionSort as insertionSortCall
import time as t
# Random Array Generator which Generates 1-D Array 
# Passing The same array to the import function call 

arrayInput=rand.randint(10000,size=1000)

# Function Call to InsertionSort
insertionSort_Start=t.time()
insertionSortCall(arrayInput)
insertionSort_End=t.time()

print(insertionSort_End-insertionSort_Start)