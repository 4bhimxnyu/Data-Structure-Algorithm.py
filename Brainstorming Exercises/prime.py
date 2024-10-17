a = int(input("enter a number to be checked:  "))

count = 0

for i in range(2,a+1):
    if (a % i == 0) :
        count += 1
    
if(count==1):
    print("the number is prime  " , a)
else:
    print("the number is not prime  " , a)