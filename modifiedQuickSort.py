medianC = 0
def median(a, b, c):
    if ( a - b) * (c - a) >= 0:
        return a
    elif (b - a) * (c - b) >= 0:
        return b
    else:
        return c

def partition_median(array, smallValArr, highValArr):
    small = array[smallValArr]
    high = array[highValArr - 1]
    length = highValArr - smallValArr
    middle = array[smallValArr + length // 2]
    pivot = median(small, high, middle)
    pivotindex = array.index(pivot)
    array[pivotindex] = array[smallValArr]
    array[smallValArr] = pivot
    i = smallValArr + 1
    for j in range(smallValArr + 1, highValArr):
        if array[j] < pivot:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i += 1

    highEndVal = array[smallValArr]
    array[smallValArr] = array[i - 1]
    array[i - 1] = highEndVal
    return i - 1

def quicksort_median(array, smallIndex, highIndex):
    global medianC
    if smallIndex+ 10  <= highIndex:
        newpivotindex = partition_median(array, smallIndex, highIndex)

        medianC += (highIndex - smallIndex - 1)
        quicksort_median(array, smallIndex, newpivotindex)
        quicksort_median(array, newpivotindex + 1, highIndex)

    else:
        insertion_sortt(array,smallIndex,highIndex)

def insertion_sortt(array,a,b):
    for i in range(a, b):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j],array[j-1]=array[j-1],array[j]
            j = j - 1

def mquick_sort(inputArr):
    quicksort_median(inputArr, 0, len(inputArr))
    return inputArr
