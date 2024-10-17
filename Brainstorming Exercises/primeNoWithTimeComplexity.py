import math

a = int(input(" enter the number to be checked:  "))

if(a<2):
    print("the number is not  prime")
else:
    count = 0

for i in range(2,int(math.sqrt(a))+1):
    if(a%i==0):
        count= 1
    

if(count == 0):
    print("the number is prime" , a )
else:
    print("the numnber is not prime", a) 