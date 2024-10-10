# linear search is an array function in which we check all the elements and compare it with the desired value

def linear(arr,target):
    for i in range(len(arr)):
        if(arr[i]==target):
            return i
    return -1

arr = [12, 3 , 4, 22,34, 96]
target = int(input("enter a target value: "))

result = linear(arr,target)

if(result!=-1):
    print("Value is found through linear Search :  ", target)
else:
    print("Value is not found, given value was : ", target)