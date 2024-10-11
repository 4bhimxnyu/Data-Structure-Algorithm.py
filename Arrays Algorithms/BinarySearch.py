# binary search is searching array method in which we divide the array and check if the value is equal to the middle and check if the value is greater or smaller than the middle value 

def binary_search(arr, targetVal):
    left = 0
    right = len(arr)-1

    while(left<=right):
        mid= (left+right)//2

        if(arr[mid] == targetVal):
            return mid
        
        if(mid<targetVal):
            left = mid+1
        else:
            right = mid-1

    return -1


array = [1,2,3,4,5,7,19,22,29,33]
target = int(input("enter the value you want to be searched :  "))

result = binary_search(array,target)

if(result  != -1):

    print("value is found at index",result)
else:
    print("value is not found in the array")