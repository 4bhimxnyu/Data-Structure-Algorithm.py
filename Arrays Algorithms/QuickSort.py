# Simply divinding the code into different methods to reduce our work 
# first method is sorting and the second is for dividing and arranging the  array in the correct order

myarr = [8,2,5,3,9,4,7,6,1]

def quickSort(myarr, low=0,high=None):
    if high is None:
        high = len(myarr) - 1

    if low < high:
        pivotIndex = partition(myarr,low,high)
        quickSort(myarr,low,pivotIndex-1)
        quickSort(myarr,pivotIndex+1,high)



def partition(myarr , low, high):
    pivot = myarr[high] # pivot is the last element in the array
    i = low -1 
     for j in range(low, high):
        if myarr[j] <= pivot:
            i += 1
            myarr[i], array[j] = myarr[j], myarr[i]

    myarr[i+1], myarr[high] = myarr[high], myarr[i+1]
    return i+1

    
    
print(myarr)