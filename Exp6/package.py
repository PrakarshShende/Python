# 1. Import complete package
import my_package

print("----- Using import my_package -----")

print(my_package.add(10, 5))
print(my_package.subtract(10, 5))
print(my_package.multiply(10, 5))
print(my_package.divide(10, 5))


# 2. Import specific functions
from my_package import reverse_string, capitalize_words, count_vowels

print("\n----- Using from my_package import -----")

print(reverse_string("hello world"))
print(capitalize_words("hello world"))
print(count_vowels("hello world"))


# 3. Import package with alias
import my_package as mp

print("\n----- Using import my_package as mp -----")

print(mp.add(10, 5))
print(mp.subtract(10, 5))
print(mp.multiply(10, 5))
print(mp.divide(10, 5))

print(mp.arithmetic.add(20, 4))
print(mp.arithmetic.subtract(20, 4))
print(mp.arithmetic.multiply(20, 4))
print(mp.arithmetic.divide(20, 4))

print(mp.reverse_string("hello world"))
print(mp.capitalize_words("hello world"))
print(mp.count_vowels("hello world"))

print(mp.string_ops.reverse_string("python"))
print(mp.string_ops.capitalize_words("quick brown fox"))
print(mp.string_ops.count_vowels("CogniBoost"))