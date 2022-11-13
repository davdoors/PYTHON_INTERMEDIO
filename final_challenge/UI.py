from dataHandler import dataHandler
class Console:
    hidden_word = ""
    word_buffer = []
    data = dataHandler()
    winner = False
    playing = False

    def __init__(self):
        print("Welcome to the hangman Game.")
        self.data.set_hidden_word()
        self.playing = True
        #self.data.validate_user_input(self.ask_input())
        #self.begin_game()

    def aks_input(self):
        print("")
        return input("enter a letter:")

    def main_screen(self):
        txt = ""
        for l in self.data.get_hangman_buffer():
            txt += (l + " ")
        print(txt)
        self.data.validate_user_input(self.aks_input())



    def restart_game(self):
        self.winner = False
        self.data.reset_user_win()
        self.data.set_hidden_word()
        self.main_screen()


    def is_a_winner(self):
        return self.data.get_user_win()

    def game_on(self):
        return self.playing
    
    def stop_playing(self):
        self.playing = False

