#creating an empty list 

emptyHash = [None ,None ,None ,None ,None ,None ,None ,None ,None ,None ]

def hashFunction(value):
    #converting the value to a string to be able to use the hash function
    sum_of_char = 0
    for char in str(value):
        sum_of_char += ord(char)

    return sum_of_char % 10

def indexChanger(name):
    #converting the name to a string to be able to use the hash function
    index = hashFunction(name)
    return emptyHash[index] == name

name1 = str(input("enter the name: "))
name2 = str(input("enter the name: "))
name3 = str(input("enter the name: "))

indexChanger(name1)
indexChanger(name2)
indexChanger(name3)

print(emptyHash)