a = int(input(" enter the number to be checked:  "))
count = 0

for i in range(1,a+1):
    if(a%i == 0):
        count = count + 1
    
if(count == 2):
    print("number is prime " , a )
else:
    print("number is not prime" , a)