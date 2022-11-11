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
from UI import Console

data = dataHandler()
ui = Console()

def run():
    # todo: need to code UI interface. 
    data.validate_user_input(ui.test())

if __name__ == '__main__':
    data.set_hidden_word()
    while True:
        run()