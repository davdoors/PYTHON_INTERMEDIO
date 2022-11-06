"""
this is the final challenge. Create a hangman game.

Rules:
    1. use comprehensions
    2. error handling
    3. use txt files.

Hints:
    1. Use enumerate().
    2. use the method get on dictionaries.
    3. use os.system("cls") to clear terminal in Windows.
"""
from dataHandler import dataHandler

data = dataHandler()

if __name__ == '__main__':
    print(data.get_random_word())