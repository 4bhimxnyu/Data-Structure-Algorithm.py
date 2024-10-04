# Selection Sort ascending order 
myArr = [7,11,15,3,20]
n=len(myArr)

for i in range(n-1):
    minIndex= i
    for j in range(i+1,n):
        if myArr[minIndex]>myArr[j]:   #for descending order  change '>' to '<'

            minIndex=j
    temp = myArr[i]
    myArr[i]=myArr[minIndex]
    myArr[minIndex]=temp

print(myArr)