# Counting Sort calculates and works for a definite set of values

def CountingSort(arr):
    maxvalue =  max(arr)
    count = [0] *(maxvalue+1)

    while len(arr) > 0:
        num =  arr.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i]>0:
            arr.append(i)
            count[i] -= 1
    
    return arr

unsortedArray = [0,3,2,1,3,2,3,2,3,3]

sortedarrary = CountingSort(unsortedArray)
print(sortedarrary)




