from insertionSort import insertionSort as insertionSortCall

def partitionMedian(array, leftend, rightend):
    pivot = array[leftend]
    i = leftend + 1
    for j in range(leftend + 1, rightend):
        if array[j] < pivot:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i += 1

    leftendval = array[leftend]
    array[leftend] = array[i-1]
    array[i-1] = leftendval
    return i - 1 
def mquickSort(array, leftindex, rightindex):
    while leftindex<rightindex:
        if(rightindex<=leftindex+9):
            insertionSortCall(array)
            break
        else:
            newpivotindex = partitionMedian(array, leftindex, rightindex)
            if newpivotindex-leftindex<rightindex-newpivotindex:
                mquickSort(array, leftindex, newpivotindex-1)
                leftindex=newpivotindex+1
            else:
                mquickSort(array, newpivotindex + 1, rightindex)
                rightindex=newpivotindex-1
    return array

#arr = [2,1,6,9,10,11,60,14,15,22,8,88,40,24,36,75,888,14] 
#n = len(arr)
#mquickSort(arr,0,n)
#print(arr)
#quick_sort1(arr, 0, n) 
#for i in range(n): 
#	print(arr[i])