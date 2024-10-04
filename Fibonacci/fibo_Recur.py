# fibonacci through recursion

print(0)
print(1)
count = 2

def fibonacci(value1, value2):
    global count
    if(count<=19):
        newFib = value1 + value2
        print(newFib)
        value1 = value2
        value2 = newFib
        count += 1
        fibonacci(value1,value2)

fibonacci(0,1)