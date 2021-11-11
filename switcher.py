class Switcher:


    def NewWord(self):
        self.isNewWord = not self.isNewWord
        pass

    def NewHeader(self):
        self.isNewHeader = not self.isNewHeader
        pass

    def Grammer(self):
        self.isGrammer = not self.isGrammer
        pass

    def Definition(self):
        self.isDef = not self.isDef
        pass

    def Quote(self):
        self.isquote = not self.isquote
        pass

    def switch(self, argument):
        func = self.options.get(argument, "Invalid Argument")
        if callable(func):
            func()
        return func



    def __init__(self):
        self.isNewWord = False
        self.isNewHeader = False
        self.isGrammer = False
        self.isDef = False
        self.isquote = False
        self.options = {
            "<orth>": self.NewWord,
            "<head>": self.NewHeader,
            "<gramGrp>": self.Grammer,
            "<def>": self.Definition,
            "<quote>": self.Quote,
        }