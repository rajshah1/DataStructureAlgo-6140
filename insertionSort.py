def insertionSort(array):
   
    for x in range(1,len(array)):
        key=array[x]
        y=x-1
        while y>=0 and array[y]>key:
            array[y+1]=array[y]
            y=y-1
        array[y+1]=key
    print(array)


# Use for Indiviual Analysis and Code Correctness

#array=[2,1,6,9,10,11,60,14,15,22,8,88,40,24,36,75,888,14]
#InsertSort(array)
#print(array)