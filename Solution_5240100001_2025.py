"solution to Assignment 3"

"""
1. Write a python program to reverse the string  "programming".
===============================================================
"""

def reverse_string():
    original="programming"
    reverse_string = original [::-1]
    print(reverse_string)
    
    
"""
2. Create a python programm that takes a user's full name as input and print the initial 
in Uppercase
=========================================================================================
"""

def print_initials():
    full_name = input("Enter your full name: ")
    parts = full_name.split()
    initials = [part[0].upper() for part in parts]
    print(".".join(initials) + ".")
    
    
"""
3. Write a python programm to check if a given string is palindrome.
====================================================================
"""

def is_palindrome():
    word = input("Enter a word to check: ").lower()
    if word == word[::]:
        print(f"{word} is a palindrome!")
        
    else:
        print(f"{word} is not a palindrome.")
        
        
"""
4.Create a python program that ask the user to enter a sentence and count the number
of words in the sentences
======================================================================================
"""
def count_words():
    sentence = input("Enter the sentence: ")
    words = sentence.split()
    print(f"Number of words: {len(words)}")
    
    
"""
5. Write a python program to replace all occurrences of "is" with "was" in the string
"This is a string and it is an example
======================================================================================
"""
    
def replace_is_with_was():
    original = "This is a string and it is an example"
    modified = original.replace|("is" , "was")
    print(modified)