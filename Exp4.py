"""1.	Write a program to building a simple student grade management system for a class of students. The system will store student names and their grades (both as lists) and should be able to perform the following operations:
●	Add a new student and their grade.
●	Update the grade of an existing student.
●	Remove a student from the list.
●	Calculate and display the average grade of the class.
●	Display the highest and lowest grades in the class.
Tasks:
●	Use lists to store the student names and their corresponding grades.
●	Implement functions to add, update, remove, and calculate the average and extreme grades"""

students = []
grades = []

def add_students(name, grade_value):
    students.append(name)
    grades.append(grade_value)
    print(f"{name} is added successfully!")

def update_grade(name, new_grade):
    if name in students:
        index = students.index(name)
        grades[index] = new_grade
        print(f"{name}'s grade is updated to {new_grade} successfully!")
    else:
        print("Student not found!")

def remove_student(name):
    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        print(f"{name} is removed successfully!")
    else:
        print("Student not found!")

def calu_avg():
    if len(grades) == 0:
        print("Students not found!")
    else:
        avg = sum(grades) / len(grades)
        print(f"Average grade is {avg}")

def dis_highest():
    if len(grades) == 0:
        print("Students not found!")
    else:
        highest = max(grades)
        lowest = min(grades)
        print("Highest Grade:", highest)
        print("Lowest Grade:", lowest)

def display():
    if len(students) == 0:
        print("Students not found!")
    else:
        print("Student list:\n")
        for i in range(len(students)):
            print(students[i], ":", grades[i])

while True:
    print("\n--- Student Grade Management System ---")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Remove Student")
    print("4. Display Students")
    print("5. Calculate Average Grade")
    print("6. Display Highest and Lowest Grades")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the name: ")
        grade_value = float(input("Enter grades: "))
        add_students(name, grade_value)

    elif choice == "2":
        name = input("Enter the name: ")
        new_grade = float(input("Enter grades: "))
        update_grade(name, new_grade)

    elif choice == "3":
        name = input("Enter the name: ")
        remove_student(name)

    elif choice == "4":
        display()

    elif choice == "5":
        calu_avg()

    elif choice == "6":
        dis_highest()

    elif choice == "7":
        print("Exiting program!...")
        break

    else:
        print("Invalid input!.. please try again!")




"""2.	Write a program to develope a system that manages the positions of points in a 2D plane. The position of each point is represented as a tuple of two values: (x, y). Write a program that:
●	Takes a list of points as input.
●	Calculates the distance between two given points.
●	Finds the point that is farthest from the origin (0, 0).
Tasks:
●	Use tuples to represent the coordinates of each point.
●	Implement a function to calculate the Euclidean distance between two points using their tuple representations.
●	Implement a function to find the farthest point from the origin"""

import math

# Function to calculate Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Function to find the farthest point from the origin
def farthest_point(points):
    origin = (0, 0)
    farthest = points[0]
    max_distance = distance(origin, farthest)

    for point in points:
        d = distance(origin, point)
        if d > max_distance:
            max_distance = d
            farthest = point

    return farthest, max_distance

# Main Program
points = []

n = int(input("Enter the number of points: "))

for i in range(n):
    x = float(input(f"Enter x-coordinate of point {i+1}: "))
    y = float(input(f"Enter y-coordinate of point {i+1}: "))
    points.append((x, y))     # Store point as a tuple

print("\nPoints:", points)

# Distance between two given points
p1 = int(input("\nEnter the index of first point (1 to n): ")) - 1
p2 = int(input("Enter the index of second point (1 to n): ")) - 1

d = distance(points[p1], points[p2])
print("Distance between", points[p1], "and", points[p2], "=", round(d, 2))

# Farthest point from origin
point, dist = farthest_point(points)
print("Farthest point from origin:", point)
print("Distance from origin:", round(dist, 2))





'''3.	Write a program to design a configuration system for a web server where some configuration settings should not be changed during runtime, while others can be updated. The server settings are as follows:
●	server_ip: A tuple representing the IP address of the server, which should remain unchanged.
●	allowed_ips: A list of IP addresses allowed to connect to the server, which can be updated during runtime.
Write a program that:
●	Allows updating the allowed_ips list.
●	Prevents updating the server_ip tuple.
●	Displays the updated configuration.
Tasks:
●	Use a tuple for server_ip and a list for allowed_ips.
●	Implement a function to update allowed_ips but prevent changes to server_ip.'''


server_ip = (192, 168, 1, 100)

# Mutable list of allowed IPs
allowed_ips = [
    "192.168.1.10",
    "192.168.1.20"
]

def update_allowed_ips():
    ip = input("Enter IP address to add: ")
    allowed_ips.append(ip)
    print("IP address added successfully.")

def update_server_ip():
    print("Error: server_ip cannot be changed because it is stored as a tuple.")

def display_configuration():
    print("\n--- Server Configuration ---")
    print("Server IP :", server_ip)
    print("Allowed IPs:")
    for ip in allowed_ips:
        print(ip)

# Main Program
while True:
    print("\n1. Add Allowed IP")
    print("2. Change Server IP")
    print("3. Display Configuration")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        update_allowed_ips()

    elif choice == 2:
        update_server_ip()

    elif choice == 3:
        display_configuration()

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")


'''4.	Write a program to manage two different projects in your company, and you need to analyze employee involvement. The employees working on each project are represented as sets. Write a program that:
●	Displays the employees working on both projects (intersection).
●	Displays the employees working only on one project (difference).
●	Displays the total unique employees across both projects (union).
Tasks:
●	Use sets to represent the employees in each project.
●	Perform union, intersection, and difference operations to analyze employee involvement'''


pa = {"Alice", "Bob", "Charlie", "David", "Eva"}
pb = {"Charlie", "David", "Frank", "Grace"}

both = pa.intersection(pb)
a_only = pa.difference(pb)
b_only = pb.difference(pa)
uniq = pa.union(pb)

print("Project A:", pa)
print("Project B:", pb)
print("\n--- Analysis ---")
print("Both projects:", both)
print("Only Project A:", a_only)
print("Only Project B:", b_only)
print("Total unique:", uniq)



'''5.	Write a program to build a simple text analysis tool. The tool should perform the following operations on a given paragraph of text:
●	Count the total number of words.
●	Count the frequency of each word.
●	Identify and display the top 3 most frequent words.
●	Count the number of vowels in the entire text.
Tasks:
●	Use string manipulation to split the text into words and to check for vowels.
●	Use a dictionary to store the word frequencies'''

text = input("Enter a paragraph: ")

words = text.lower().split()

print("Total words:", len(words))

frequency = {}

for word in words:
    word = word.strip(".,!?;:")
    frequency[word] = frequency.get(word, 0) + 1

print("\nWord Frequency:")
for word, count in frequency.items():
    print(word, ":", count)

top3 = sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:3]

print("\nTop 3 frequent words:")
for word, count in top3:
    print(word, ":", count)

vowels = "aeiou"
vowel_count = 0

for char in text.lower():
    if char in vowels:
        vowel_count += 1

print("\nTotal vowels:", vowel_count)


'''6.	Write a program to analyze the vocabulary used in two different books. You need to:
●	Find all unique words used in each book.
●	Identify the common words between both books.
●	Identify words that are unique to each book (not found in the other book).
●	Display the total number of unique words across both books.
Tasks:
●	Use sets to find the unique words in each text, and perform set operations to find the union, intersection, and differences.
'''

book1 = input("Enter text of Book 1: ").lower()
book2 = input("Enter text of Book 2: ").lower()

set1 = set(book1.split())
set2 = set(book2.split())

common = set1.intersection(set2)
unique1 = set1.difference(set2)
unique2 = set2.difference(set1)
all_words = set1.union(set2)

print("\nUnique words in Book 1:")
print(set1)
print("\nUnique words in Book 2:")
print(set2)
print("\nCommon words:")
print(common)
print("\nWords unique to Book 1:")
print(unique1)
print("\nWords unique to Book 2:")
print(unique2)

print("\nTotal unique words across both books:", len(all_words))
