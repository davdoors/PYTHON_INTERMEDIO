from dataHandler import dataHandler
class Console:
    hidden_word = ""
    word_buffer = []
    data = dataHandler()

    def __init__(self):
        print("Welcome to the best hangman Game.")
        self.begin_game()

    def test(self):
        return input("enter a letter:")

    def main_screen(self):
        txt = ""
        for l in self.data.get_hangman_buffer():
            txt += (l + " ")
        print(txt)


    def begin_game(self):
        self.data.set_hidden_word()
        self.main_screen()