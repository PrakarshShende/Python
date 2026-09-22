'Constructor'

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# s1 = Student("Prakarsh", 20)
# s1.display()

'Constructor with calculation'

# class Calculator:
#     def __init__(self, a, b):
#         self.sum = a + b

# c = Calculator(10, 20)
# print(c.sum)

'Constructor with Default Value'

# class Student:
#     def __init__(self, name="Unknown"):
#         self.name = name

# s = Student()
# print(s.name)


'Destructor'

# class Student:
#     def __init__(self, name):
#         self.name = name
#         print("Object created")

#     def __del__(self):
#         print("Object destroyed")


# s1 = Student("Prakarsh")
# del s1

'Inheritance'

# class Animal:     #Parent class
#     def eat(self):
#         print("Animal eats")

# class dog(Animal): #Child class
#     def barks(self):
#         print("Dogs Barks")

# d = dog()

# d.eat() #Inherited from the Animal
# d.barks() #Dog's own method


'Single Inheritance'

# class A:
#     def show(self):
#         print("Parent Class")

# class B(A):
#     def display(self):
#         print("Child class")

# obj = B()
# obj.show()
# obj.display()

'Multilevel Inheritance'

# class A:
#     def show(self):
#         print("Helllo Programmers")

# class B(A):
#     def display(self):
#         print("Hello python")

# class C(B):
#     def print_data(self):
#         print("Hello pyhton coders")

# obj = C()

# obj.show()
# obj.display()
# obj.print_data()

'Multiple Inheritance'

# class Father:
#     def skill1(self):
#         print("Driving")

# class Mother:
#     def skill2(self):
#         print("Cooking")

# class child(Father,Mother):
#     def skill3(self):
#         print("Coding")

# obj = child()

# obj.skill1()
# obj.skill2()
# obj.skill3()


'Hierarchial Inheritance'

# class Animal:
#     def eat(self):
#         print("Eating")

# class Dog(Animal):
#     def bark(self):
#         print("Barking")

# class Cat(Animal):
#     def meow(self):
#         print("Meowing")


# d = Dog()
# c = Cat()

# d.eat()
# d.bark()

# c.eat()
# c.meow()

'Hybrid Inheritance'

# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def display(self):
#         print("B")

# class C(A):
#     def print_data(self):
#         print("C")

# class D(B, C):
#     def result(self):
#         print("D")


# obj = D()

# obj.show()
# obj.display()
# obj.print_data()
# obj.result()

'Use private and protected variables and functions in multilevel inheritance.'
#Grandparent class
class Person:
    def __init__(self):
        self._name = "Prakarsh"       # Protected variable
        self.__age = 20               # Private variable

    def _show_name(self):             # Protected function
        print("Name:", self._name)

    def __show_age(self):             # Private function
        print("Age:", self.__age)


# Parent class
class Student(Person):
    def __init__(self):
        super().__init__()
        self._roll_no = 101           # Protected variable

    def show_student(self):
        print("Roll No:", self._roll_no)
        self._show_name()             # Protected function can be accessed


# Child class
class Result(Student):
    def __init__(self):
        super().__init__()
        self.__marks = 85              # Private variable

    def display_result(self):
        print("Marks:", self.__marks)
        print("Roll No:", self._roll_no)
        self._show_name()


s = Result()

s.show_student()
s.display_result()