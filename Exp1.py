# int
# addition of two numbers
a=10
b=20
print(a+b)
print(b-a)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

# float

c=12.5
d=20.7
print(c+d)
print(d-c)
print(c*d)
print(c/d)
print(c//d)
print(c%d)
print(c**d)

# Complex (complex)
c = 2 + 3j
print("Complex:", c)
print(type(c))

# Type Conversion
x = 15
y = float(x)
z = int(12.8)

print("Integer to Float:", y)
print("Float to Integer:", z)

# char

str1 = "prakarsh"
str2 = "shende"
print(str1+str2)
print(str1.replace('pra','qwe'))
print(str1*3)
print(str1.upper)
print(str1.lower)
print(str2.upper)
print(str2.lower)
print(str1[0:3])   
print(str2[2:])   
print(str1[:4])    
print(str2[::-1])
print("Python" in str1)      
print("Java" not in str2)
print(len(str1))
print(len(str2))

# Boolean

# Boolean values
a = True
b = False

print(a)       
print(b)        

# Comparison operators
x = 10
y = 5

print(x > y)  
print(x < y)   
print(x == y)  
print(x != y) 
print(x >= y) 
print(x <= y)  

# Logical operators
print(a and b) 
print(a or b) 
print(not a)   

# Boolean in if statement
age = 18

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

# bool() function
print(bool(1))     
print(bool(0))      
print(bool("Hi"))  
print(bool(""))     
print(bool([]))     
print(bool([1, 2])) 

# List 

fruits = ["Apple", "Banana", "Mango", "Orange"]
print("Original List:", fruits)
print("First Element:", fruits[0])
print("Last Element:", fruits[-1])

# Slicing
print("First Two Elements:", fruits[0:2])

# Adding elements
fruits.append("Grapes")
print("After Append:", fruits)

fruits.insert(1, "Pineapple")
print("After Insert:", fruits)

# Removing elements
fruits.remove("Banana")
print("After Remove:", fruits)

fruits.pop()
print("After Pop:", fruits)

fruits[1] = "Kiwi"
print("After Update:", fruits)

# List operations
print("Length:", len(fruits))
print("Count of Apple:", fruits.count("Apple"))
print("Index of Mango:", fruits.index("Mango"))

# Sorting and reversing
numbers = [5, 2, 8, 1, 3]
numbers.sort()
print("Sorted List:", numbers)

numbers.reverse()
print("Reversed List:", numbers)

# Loop through list
print("List Elements:")
for item in fruits:
    print(item)


# Tuple in Python

# Creating a tuple
fruits = ("Apple", "Banana", "Mango", "Orange")
print("Original Tuple:", fruits)

# Accessing elements
print("First Element:", fruits[0])
print("Last Element:", fruits[-1])

# Slicing
print("First Two Elements:", fruits[0:2])

# Length
print("Length:", len(fruits))

# Count and Index
print("Count of Apple:", fruits.count("Apple"))
print("Index of Mango:", fruits.index("Mango"))

# Loop through tuple
print("Tuple Elements:")
for item in fruits:
    print(item)


# Set in Python

# Creating a set
fruits = {"Apple", "Banana", "Mango"}
print("Original Set:", fruits)

# Adding elements
fruits.add("Orange")
print("After Add:", fruits)

# Removing elements
fruits.remove("Banana")
print("After Remove:", fruits)

# Membership
print("Apple" in fruits)

# Length
print("Length:", len(fruits))

# Loop through set
print("Set Elements:")
for item in fruits:
    print(item)




# Dictionary in Python

student = {
    "Name": "Rahul",
    "Age": 20,
    "Course": "CSE"
}

print("Original Dictionary:", student)

# Accessing values
print("Name:", student["Name"])

# Adding a new key-value pair
student["City"] = "Kolhapur"
print("After Adding:", student)

# Updating a value
student["Age"] = 21
print("After Updating:", student)

# Removing a key
student.pop("Course")
print("After Removing:", student)

# Keys, Values, Items
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Loop through dictionary
print("Dictionary Elements:")
for key, value in student.items():
    print(key, ":", value)

