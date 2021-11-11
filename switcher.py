class Switcher:

    def new_word(self):
        self.isNewWord = not self.isNewWord
        pass

    def new_header(self):
        self.isNewHeader = not self.isNewHeader
        pass

    def definition(self):
        self.isDef = not self.isDef
        pass

    def switch(self, argument):
        func = self.options.get(argument, "Invalid Argument")
        if callable(func):
            func()
        pass

    def __init__(self):
        self.isNewWord = False
        self.isNewHeader = False
        self.isDef = False
        self.options = {
            "<orth>": self.new_word,
            "<head>": self.new_header,
            "<gramGrp>": '',
            "<def>": self.definition,
            "<etym>": '',
            "<quote>": '',
        }