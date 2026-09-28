'Exception Handling'

# try:
#     n=0
#     res=100/n
# except ZeroDivisionError:
#     print("You can't divide by zero")

# except ValueError:
#     print("Enter a valid number")

# else:
#     print("Result is: ",res)

# finally:
#     print("Execution is complete")


'User-Defined Exception'

# class InvalidAgeException(Exception):
#     pass
# number =18

# try:
#     input_num = int(input("Enter Age: "))
#     if input_num<number:
#         raise InvalidAgeException
#     else:
#         print("Eligible to Vote")

# except InvalidAgeException:
#     print("Exception Occurred: Invalid Age")


'Handling Multiple Exception in One'

# try:
#     num = int(input("Enter number: "))
#     result = 10 / num
#     print(result)

# except (ValueError, ZeroDivisionError):
#     print("Invalid input or division by zero")

'try-except-else'

# try:
#     a = 10
#     b = 2
#     result = a / b

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# else:
#     print("Result =", result)

'try-except-finally'

# try:
#     a = 10
#     b = 0
#     print(a / b)

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# finally:
#     print("Program execution completed")

'Using finally Without Exception'

# try:
#     print("Hello Python")

# except:
#     print("Exception occurred")

# finally:
#     print("Finally block executed")

'Catching General Exception'

# try:
#     a = 10 / 0

# except Exception as e:
#     print("An error occurred:", e)

'ValueError Exception'

# try:
#     num = int(input("Enter a number: "))
#     print("Number =", num)

# except ValueError:
#     print("Invalid input. Enter a number.")

'IndexError Exception'

# try:
#     numbers = [10, 20, 30]
#     print(numbers[5])

# except IndexError:
#     print("Index is out of range")


'KeyError Exception'

# try:
#     student = {
#         "name": "Prakarsh",
#         "age": 20
#     }

#     print(student["marks"])

# except KeyError:
#     print("Key does not exist")

'TypeError Exception'

# try:
#     a = 10
#     b = "20"
#     print(a + b)

# except TypeError:
#     print("Cannot perform operation between these data types")

'NameError Exception'

# try:
#     print(x)

# except NameError:
#     print("Variable is not defined")

'FileNotFoundError'

# try:
#     file = open("student.txt", "r")
#     print(file.read())
#     file.close()

# except FileNotFoundError:
#     print("File does not exist")

'Using raise'

# age = 16

# try:
#     if age < 18:
#         raise Exception("Age must be 18 or above")

#     print("Eligible")

# except Exception as e:
#     print(e)

'Custom Exception for Marks'

# class InvalidMarksError(Exception):
#     pass


# try:
#     marks = int(input("Enter marks: "))

#     if marks < 0 or marks > 100:
#         raise InvalidMarksError("Marks must be between 0 and 100")

#     print("Valid marks")

# except InvalidMarksError as e:
#     print(e)

'Nested try-except'

# try:
#     print("Outer try block")

#     try:
#         a = 10 / 0
#         print(a)

#     except ZeroDivisionError:
#         print("Cannot divide by zero")

# except Exception:
#     print("Outer exception")

'Exception in Function'

# def divide(a, b):
#     try:
#         return a / b

#     except ZeroDivisionError:
#         return "Cannot divide by zero"


# print(divide(10, 2))
# print(divide(10, 0))

'Exception Handling with User Input'

# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))

#     print("Division =", num1 / num2)

# except ValueError:
#     print("Please enter valid integers")

# except ZeroDivisionError:
#     print("Second number cannot be zero")

# finally:
#     print("Thank you")

'Example-Calculator'

# try:
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))

#     operator = input("Enter operator (+, -, *, /): ")

#     if operator == "+":
#         print("Result =", a + b)

#     elif operator == "-":
#         print("Result =", a - b)

#     elif operator == "*":
#         print("Result =", a * b)

#     elif operator == "/":
#         print("Result =", a / b)

#     else:
#         raise ValueError("Invalid operator")

# except ValueError as e:
#     print("Error:", e)

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# finally:
#     print("Calculator execution completed")