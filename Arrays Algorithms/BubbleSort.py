#sorting the array through bubbleSort

myArr = [9,7,15,4,11,3]
n=len(myArr)

print(myArr)

for i in range(n-1):
    for j in range(0, n-i-1):
        if(myArr[j]>myArr[j+1]):
            temp = myArr[j]
            myArr[j]=myArr[j+1]
            myArr[j+1] = temp


print("Sorted array:" ) 
print(myArr)                        