myArr = [64,34,25,12,22,11,90,5]
n = len(myArr)

for i in range(n):
    minVal=i
    for j in range(i+1,n):
        if myArr[j]<myArr[minVal]:
            minVal=j
    temp=myArr[i]
    myArr[i]=myArr[minVal]
    myArr[minVal]=temp

print(myArr)
