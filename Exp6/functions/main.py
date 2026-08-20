'''Functions'''

'1.basic syntax'
# def funct_name():
    #code

'Example'
def greet():
    print("Hello Developers!")
greet()

'2.Function with Parameters'
def greet(name):
    print("Helloo",name)
greet("Prakarsh")


'3.Function with multiple Parameters'
def add(a,b):
    print(a+b)
add(4,5)

'4.Function with return'

def add(a,b):
    return a+b

result = add(5,6)
print(result)

'5.Function with default arguments'

def greet(name="Developer"):
    print("Hello",name)
greet()
greet("Prakarsh")

'6.Function with Multiple Return Values'

def calculate(a,b):
    return a+b,a-b

x,y = calculate(10,5)
print(x)
print(y)

'''Types of functions'''
'A. Built-in Functions'
name = input("Enter your name: ")
nums = [10, 20, 30, 40, 50]

print(name)
print(type(name))
print(nums)
print(type(nums))
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))

'B. User-defined Functions'

def square(x):
    return x * x

'C. Lambda Functions'

square = lambda x: x * x

print(square(5))

'8. *args'
'Used when you dont know how many arguments will be given'

def add(*numbers):
    return(sum(numbers))
print(add(10,20,30,40))

'9. **kwargs'
'Used for multiple keyword arguments'

def student(**details):
    print(details)

student(name="Prakarsh", age=20)

