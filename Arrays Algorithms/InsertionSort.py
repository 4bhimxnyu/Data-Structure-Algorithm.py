# Easy and efficient code for inseertion sort of an array 

# time complexity is O(n^2);

myArr =[64,34,35,23,22,11,90,5]

n = len(myArr)
for i in range(1, n):
    key = myArr[i]
    j = i - 1
    while j >= 0 and key < myArr[j] :
        myArr[j + 1] = myArr[j]
        j -= 1
        myArr[j + 1] = key

print(myArr)
