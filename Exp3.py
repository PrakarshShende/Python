# ●	Write a program to input a string and display its length without using the len() function. 
# str1 = input(":")
# len = 0
# for i in str1:
#     len+=1
# print(len)

# ●	Count the number of vowels, consonants, digits, spaces, and special characters in a given string. 
# str2 = "Enter the given String 123!"
# vowels = 0
# consonants = 0
# digits = 0
# spaces = 0
# special_chars = 0

# for i in str2:
#     if i.lower() in ('a', 'e', 'i', 'o', 'u'):
#         vowels += 1
#     elif i == ' ':
#         spaces += 1
#     elif i.isdigit():
#         digits += 1
#     else:
#         consonants += 1

# print(vowels)
# print(consonants)
# print(digits)
# print(spaces)
    
# ●	Reverse the given string without using built-in reverse functions. 

# str3=input(":")
# for i in str3[::-1]:
#     print(i,end='')

# ● Check whether the entered string is a palindrome.
# str4 = input(':')
# if str4 == str4[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# ●	Count the number of uppercase and lowercase letters in a string. 
# str5=input(':')
# lower =0
# upper=0
# for i in str5:
#     if(i.islower()):
#         lower+=1
#     elif(i.isupper()):
#         upper+=1
#     else:
#         print("Wrong Input")
# print(lower)
# print(upper)

# ●	Replace all occurrences of a given character with another character. 

# str6=input(':')
# repl = str6.replace('a','o')
# print(repl)

# ●	Remove all spaces from the input string. 
# str7=input(':')
# repl = str7.replace(' ','')
# print(repl)

# ●	Find the number of times a specified character appears in a string
# str8=input(':')
# co=str8.count('a')
# print(co)

# ●	Print the first and last character of a string. 
# str9=input(':')
# print(str9[0])
# print(str9[-1])

# ●	Display each character of a string along with its ASCII value.
# str10=input(':')
# for i in str10:
#     print(i,':',ord(i))

# Count the total number of words in a sentence. 
# str11=input(":")
# space=str11.count(' ')
# print("Words are:",space+1)

# a. Find the longest word in a given sentence
# str12 = input(':')
# words = str12.split()
# longest = ""

# for word in words:
#     if len(word) > len(longest):
#         longest = word
# print(longest)
    
# Find the shortest word in a sentence

# str12 = input(':')
# words = str12.split()

# if words:
#     shortest = min(words, key=len)
#     print(shortest)
# else:
#     print("No words")

# convert the first letter of every word to uppercase. 
# str13=input(':')
# senten=str13.split()
# for i in senten:
#     print(i.title(),end=' ')

# Print all duplicate characters in a string





# a.	Display the frequency of every character in a string. 








# check whether two strings are anagrams. 
# str1 = input(':')#"listen"
# str2 = input(':')#"silent"
# if sorted(str1) == sorted(str2):
#     print("Anagram")
# else:
#     print("Not an Anagram")


# Remove duplicate characters while maintaining the original order
# str1 = input(':')
# result = ""
# for char in str1:
#     if char not in result:
#         result += char
# print(result)

# Check whether a given substring exists in the main string. 
# str19=input(':')
# str10=input(':')
# if str10 in str19:
#     print("exist")
# else:
#     print("Not exsist")

# Count how many times a specific word appears in a sentence
# str20=input(':')
# count=0
# word=input(':')
# occur=str20.split()
# for i in occur:
#     if word in occur:
#         count+=1
# print(count)


# 21.	Password Validator
# ●	Validate a password based on these conditions: 
# o	Minimum 8 characters 
# o	At least one uppercase letter 
# o	One lowercase letter 
# o	One digit 
# o	One special character

password = input("Enter password: ")

upper = 0
lower = 0
digit = 0
special = 0

for i in password:
    if i.islower():
        lower += 1
    elif i.isupper():
        upper += 1
    elif i.isdigit():
        digit += 1
    else:
        special += 1

if len(password) >= 8 and upper >= 1 and lower >= 1 and digit >= 1 and special >= 1:
    print("Valid Password")
else:
    print("Invalid Password")
