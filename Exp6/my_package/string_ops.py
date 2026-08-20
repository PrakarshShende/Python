def reverse_string(s):
    return s[::-1]


def capitalize_words(s):
    return s.title()


def count_vowels(s):
    vowels = set("aeiouAEIOU")
    return sum(1 for char in s if char in vowels)