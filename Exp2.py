# print natural number upto n

# n=int(input("Enter a number:"))
# for i in range(n):
#     print(i)

# print even number upto n

# n=int(input("Enter a number:"))
# for i in range(1,n):
#     if i%2==0:
#         print(i)

# print odd number upto n

# n=int(input("Enter a number:"))
# for i in range(1,n):
#     if i%2!=0:
#         print(i)

# write a program that prints 1,2,4,8,16,32..nsquare

# n=int(input("Enter a number:"))
# for i in range(n):
#     print(i**2)

# write a program to print sum of factorials

# n=int(input("Enter a number:"))
# fact = 1
# sum = 1.0
# for i in range(1,n+1):
#     fact *=i
#     sum += 1 / fact
# print(sum)

# write a program to produce the design ABC ABC ABC

# for i in range(1,4):
#     for i in range(65,68):
#         print(chr(i),end="")
#     print()

# Write a program to make design

# n=int(input("Enter a number:"))
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(chr(65+j),end="")
#     print()

# write a program to make design 

# n=int(input("Enter a number:"))
# for i in range(n,0,-1):
#     for j in range(i):
#         print(chr(65+j),end="")
#     print()

# write a program to make numeric design

# n=int(input("Enter a number:"))
# for i in range(1,n):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# write a program to make numeric design

# n=int(input("Enter a number:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()

##########################################################################################

# write a program to print n-number
# n=0
# while(n!=10):
#     print(n)
#     n=n+1

# write a program to print even numbers

# n=int(input("Enter a number:"))
# i=0
# while(i!=n):
#     if i%2==0:
#         print(i)
#     i=i+1

# write a program to print odd numbers

# n=int(input("Enter a number:"))
# i=0
# while(i!=n):
#     if i%2!=0:
#         print(i)
#     i=i+1

# write a program to print sum of natural numbers

# n=int(input("Enter a number:"))
# i=0
# sum =0
# while(i!=n+1):
#     sum+=i
#     i=i+1
# print(sum)

# write a program to print sum of odd numbers

# n=int(input("Enter a number:"))
# i=0
# sum =0
# while(i!=n+1):
#     if i%2!=0:
#         sum+=i
#     i=i+1
# print(sum)

# write a program to print sum of even numbers

# n=int(input("Enter a number:"))
# i=0
# sum =0
# while(i!=n+1):
#     if i%2==0:
#         sum+=i
#     i=i+1
# print(sum)

# write a program to print n natural numbers in reverse order

# n=10
# while(n!=0):
#     print(n)
#     n=n-1

# write a program to print fibonacci series

# n=20
# a,b = 0,1
# while a <= n:
#     print(a, end=" ")
#     a, b = b, a + b
# print()