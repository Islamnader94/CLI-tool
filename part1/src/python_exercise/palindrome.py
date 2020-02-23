import os
import sys

# function to check if project's name is palindrome
def is_palindrome(file_name):
    name = file_name[::-1]
    if file_name == name:
        return True
    else:
        return False