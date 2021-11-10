# dictionary.py

class Dictionary:
    def __init__(self):
        self.dictionary = {}

    def new_header(self, letter):
        self.dictionary[letter] = {}
