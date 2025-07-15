#vaiables and types

x= 5
print(x)
y = 3.14
print(y)

print(type(x))
print(type(y))

name = 'John'

print(name)
print(type(name))

x = True
print(x)
print(type(x))

# Data structures 

my_list = [1,2,3,4]
print(my_list)
print(type(my_list))

#Operators
1+1
4*5
5**2
print(1+1)
print(4*5)  
print(5**2) 
print(10/2) 

#Control flow   

a = False
if a:
    print("a is True")  
else:  
    print("a is False") 

a=[1,2,3,4,5] 
for item in a:
    print(item)   

a=0
while a < 5:
    print(a)
    a = a + 1  

# Functions 

def multiplyByThree(val):
    return val * 3

print(multiplyByThree(4))

def addNumbers(a, b):
    return a + b
print(addNumbers(3, 5))

# Classes and Objects      

class dog: 
    # A simple class to represent a dog
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        return f"{self.name} says Woof!"   

# Create an instance of the dog class
my_dog = dog("Buddy", 5)
print(my_dog.name)  


