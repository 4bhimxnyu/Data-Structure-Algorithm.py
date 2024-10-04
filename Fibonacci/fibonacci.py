# Fibonacci series till 18 through for loop

value1 = 0
value2 = 1

print(value1)
print(value2)

for fib in range(18):
    newFib = value1 + value2
    print(newFib)
    value1 = value2
    value2 = newFib

