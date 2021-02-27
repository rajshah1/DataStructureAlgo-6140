from numpy import random as rand
from insertionSort import InsertSort as insertionSortCall

# Random Array Generator which Generates 1-D Array 
# Passing The same array to the import function call 

arrayInput=rand.randint(10000,size=1000)

# Function Call to InsertionSort
insertionSortCall(arrayInput)