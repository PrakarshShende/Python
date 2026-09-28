import re

# 1. Find a word
text = "Python is easy to learn"

if re.search(r"Python", text):
    print("1. Word found")
else:
    print("1. Word not found")


# 2. Find all numbers
text = "I have 10 apples and 20 bananas"

numbers = re.findall(r"\d+", text)
print("2. Numbers:", numbers)


# 3. Find all words
text = "Python is easy"

words = re.findall(r"\b\w+\b", text)
print("3. Words:", words)


# 4. Validate mobile number
mobile = "9876543210"

if re.fullmatch(r"[6-9]\d{9}", mobile):
    print("4. Valid mobile number")
else:
    print("4. Invalid mobile number")


# 13. Validate time HH:MM
time = "14:30"

pattern = r"([01]\d|2[0-3]):[0-5]\d"

if re.fullmatch(pattern, time):
    print("13. Valid time")
else:
    print("13. Invalid time")


# 6. Validate PIN code
pin = "416003"

if re.fullmatch(r"\d{6}", pin):
    print("6. Valid PIN")
else:
    print("6. Invalid PIN")


# 7. Remove special characters
text = "Python@123 is #easy!"

result = re.sub(r"[^a-zA-Z0-9\s]", "", text)

print("18. Without special characters:", result)


# 8. Find words ending with 'ing'
text = "I am learning programming and coding."

result = re.findall(r"\b\w+ing\b", text)

print("20. Words ending with ing:", result)


# 9. Replace a word
text = "I love Java. Java is easy."

result = re.sub(r"Java", "Python", text)

print("9. Replaced:", result)


# 10. Split string using regex
text = "Python,Java;C++:JavaScript"

result = re.split(r"[,;:]", text)

print("10. Split:", result)




# 'Programs : email, mobile number, password'

# Email Validation

import re

email = input("Enter email: ")

pattern = r"\w+@\w+\.\w+"

if re.fullmatch(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")


# password Validation

import re

password = input("Enter password: ")

pattern = r"\w{8,}"

if re.fullmatch(pattern, password):
    print("Valid Password")
else:
    print("Invalid Password")


# Mobile number Validation
 
import re

mobile = input("Enter mobile number: ")

pattern = r"[6-9]\d{9}"

if re.fullmatch(pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")


# IMPORTANT REGEX SYMBOLS

"""
\d      -> Digit [0-9]
\D      -> Non-digit
\w      -> Word character
\W      -> Non-word character
\s      -> Whitespace
\S      -> Non-whitespace

.       -> Any character
^       -> Starts with
$       -> Ends with
*       -> 0 or more
+       -> 1 or more
?       -> 0 or 1
{n}     -> Exactly n times
{n,}    -> n or more times
{n,m}   -> Between n and m times

[]      -> Character set
[^]     -> Not in character set
()      -> Group
|       -> OR
\b      -> Word boundary
"""

'''
| Name             | Meaning                               |
| ---------------- | ------------------------------------- |
|  import re       | Import Regular Expression module      |
|  re.search()     | Search pattern anywhere in string     |
|  re.match()      | Match pattern at beginning            |
|  re.fullmatch()  | Match the complete string             |
|  re.findall()    | Find all matching occurrences         |
|  re.finditer()   | Return iterator of matches            |
|  re.sub()        | Replace matching text                 |
|  re.split()      | Split string using pattern            |
|  re.compile()    | Compile a regex pattern               |
|  re.escape()     | Escape special characters             |
|  re.IGNORECASE   | Ignore uppercase/lowercase difference |
|  re.MULTILINE    | Treat each line separately            |
|  re.DOTALL       |  .  also matches newline              |
|  re.match        | Beginning-of-string matching          |
|  group()         | Get matched text                      |
|  groups()        | Get all captured groups               |
|  start()         | Starting position of match            |
|  end()           | Ending position of match              |
|  span()          | Start and end positions               |

'''