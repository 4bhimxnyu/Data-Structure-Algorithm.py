# this algorithm needs two different function first to divide th4e  array into two halves and second to merge the two halves

def mergeSort(arr):
    if len(arr) <=1 :
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        sortedLeft = mergeSort(left)
        sortedRight = mergeSort(right)

        return  merge(sortedLeft,sortedRight)
    


def merge(left,right):
    result = []
    i = j = 0 

    while i < len(left) and j < len(right):
        if(left[i]<right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        
    result.extend(left[i:])
    result.extend(right[j:])

    return result


unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergeSort(unsortedArr)
print("Sorted array:", sortedArr)