import random


class dataHandler:
    words_dict = {}
    hidden_word = ""
    hangman_buffer = []
    input_buffer = []
    last_check = []

    def __init__(self):
        with open("./files/data.txt","r",encoding="utf-8") as words:
            for count, word in enumerate(words):
                self.words_dict[count] = word

    def get_random_word(self):
        return self.words_dict.get(random.randint(0, len(self.words_dict)))

    def set_hidden_word(self, hidden_word):
        self.hidden_word = hidden_word
        self.__reset_hangman_buffer()
    
    def __reset_hangman_buffer(self):
        self.hangman_buffer =[]
        for l in self.hidden_word:
            self.hangman_buffer.append("_")
    
    def __change_hangman_buffer(self,index,letter):
        self.hangman_buffer[index] = letter

    def __is_in_hidden_word(self,input):
        check={}
        ans = False
        check = {index:l for index,l in enumerate(self.hidden_word) if l == input}
        if len(check) != 0:
            self.last_check = check
            ans = True
        
        return ans

    def validate_user_input(self,input):
        if input.isnumeric():
            print("Invalid input: numeric values are not allowed")
            return
        
        input.lower()
        # *check if input waw already entered
        try:
            index_check = self.input_buffer.index(input)
            print("Invalid input: " + input + "has already been entered")
        except ValueError:
            self.input_buffer.append(input)
        
        if not self.__is_in_hidden_word(input):
            print("keep trying XD")
            return
        
        # TODO: change_hangman_buffer.


    def get_hidden_word(self):
        return self.hidden_word
