# here we are going to create the stack in the form of the modern list way . 
# all the functions we will be commented out to get a clear understanding of the code  and to implement all the functions.


stack =[]

stack.append('James')
stack.append('likes')
stack.append('to')
stack.append('Code')

# here we are going to pop the elements from the stack .

# stack.pop()

#now we will change the index of the pop
 
#stack.pop(0)

#now we will push some new elements at the top of the stack

#stack.append('and')
#stack.append('Music')

# now we will use the peek function for the code 

#topElement = stack[len(stack)-1]
#print(topElement)

# now we will check if the stack is empty or not
# if the stack is empty then it will return true otherwise it will return false.
# this is the standard way of doing the code

#isEmpty = not bool(stack)
#print(isEmpty)

#now we will check if the stack is empty by using if and else conditon
# if the stack is empty then it will print the stack is empty otherwise it will print the stack

#if(topElement):
   # print("the stack is not empty")
#else:
   # print("the stack is empty")

# to learn the size of the stack we will use the python built in method
# len() function is used to get the size of the stack.

size = len(stack)
print(size)
