# 1. Create an array (list)
arr = [10, 20, 30, 40, 50]
print("Original array:", arr)

# 2. Access elements
print("First element:", arr[0])
print("Last element:", arr[-1])

# 3. Traversing
print("Array elements:")
for x in arr:
    print(x)

# 4. Length
print("Length:", len(arr))

# 5. Add element at the end
arr.append(60)
print("After append:", arr)

# 6. Insert element at specific position
arr.insert(2, 25)
print("After insert:", arr)

# 7. Add multiple elements
arr.extend([70, 80])
print("After extend:", arr)

# 8. Update an element
arr[0] = 100
print("After update:", arr)

# 9. Remove element by value
arr.remove(25)
print("After remove:", arr)

# 10. Remove last element
arr.pop()
print("After pop:", arr)

# 11. Remove element by index
arr.pop(1)
print("After pop by index:", arr)

# 12. Delete element
del arr[0]
print("After delete:", arr)

# 13. Search an element
if 40 in arr:
    print("40 is present")
else:
    print("40 is not present")

# 14. Find index
print("Index of 50:", arr.index(50))

# 15. Count occurrences
arr.append(50)
print("Count of 50:", arr.count(50))

# 16. Sort in ascending order
arr.sort()
print("Ascending order:", arr)

# 17. Sort in descending order
arr.sort(reverse=True)
print("Descending order:", arr)

# 18. Reverse
arr.reverse()
print("After reverse:", arr)

# 19. Find maximum
print("Maximum:", max(arr))

# 20. Find minimum
print("Minimum:", min(arr))

# 21. Find sum
print("Sum:", sum(arr))

# 22. Copy array
arr2 = arr.copy()
print("Copied array:", arr2)

# 23. Slicing
print("First 3 elements:", arr[:3])
print("Last 3 elements:", arr[-3:])

# 24. Concatenation
arr3 = [1, 2, 3]
arr4 = [4, 5, 6]
result = arr3 + arr4
print("Concatenation:", result)

# 25. Repeat array
print("Repeated array:", arr3 * 2)

# 26. Clear all elements
arr.clear()
print("After clear:", arr)