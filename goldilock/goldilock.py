"""Main module."""

import string
import random


def generate_random_string(length, upper = False, digits = False, punctuation = False):
    letters = string.ascii_lowercase
    if upper:
        letters += string.ascii_uppercase
    
    if punctuation:
        letters += string.punctuation
        
    if digits:
        letters += string.digits
    
    print(letters)
    return ''.join(random.choice(letters) for i in range(length))



'''The string module in Python is a built-in module that provides a collection of constants (strings) that are commonly used when working with strings. These constants include various sets of characters, such as letters, digits, punctuation, and whitespace. It's useful for tasks like generating random strings, sanitizing input, or performing specific character manipulations.

Here are some of the constants and functions provided by the string module:

string.ascii_letters: This constant is a string containing all uppercase and lowercase letters of the alphabet, i.e., "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".

string.ascii_lowercase: This constant contains all lowercase letters, i.e., "abcdefghijklmnopqrstuvwxyz".

string.ascii_uppercase: This constant contains all uppercase letters, i.e., "ABCDEFGHIJKLMNOPQRSTUVWXYZ".

string.digits: This constant contains all the decimal digits, i.e., "0123456789".

string.punctuation: This constant contains all the ASCII punctuation characters, such as "!@#$%^&*()-_+=<>?/|{}[]:;'", etc.

string.whitespace: This constant contains all whitespace characters, including spaces, tabs, and newline characters.

string.printable: This constant contains all the printable characters, which include letters, digits, punctuation, and whitespace.

These constants can be used when you need to filter, manipulate, or generate strings with specific character sets. For example, you might use string.ascii_letters and string.digits when generating random alphanumeric strings, as shown in the previous response.
'''