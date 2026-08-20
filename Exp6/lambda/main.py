'lambda function'

square = lambda x: x*x
print(square(5))

'add two number'

add = lambda a,b: a+b
print(add(4,5))

'find maximum'

max = lambda a,b: a if a>b else b
print(max(9,15))

'even numbers'

n=int(input("Enter a number: "))
even = lambda n: n%2==0
print(even(n))

'cube of a number'

m=int(input("Enter a number: "))
cube = lambda x: x**3
print(cube(m))

'lambda using map()'

num = [1, 2, 3, 4, 5, 6, 7]
result = list(map(lambda n: n*2,num))
print(result)

'lambda using filter()'
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
solu = list(filter(lambda n:n%2==0, num))
print(solu)