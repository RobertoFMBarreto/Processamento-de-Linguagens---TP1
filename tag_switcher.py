class TagSwitcher:

    def new_word(self):
        self.isNewWord = not self.isNewWord
        pass

    def new_header(self):
        self.isNewHeader = not self.isNewHeader
        pass

    def definition(self):
        self.isDef = not self.isDef
        pass

    # argument -> tag a verificar se existe e a executar a função
    def switch(self, argument):
        # verificar se a tag existe e se existir obter o value da tag caso não exista obter um erro
        func = self.options.get(argument, "Invalid Argument")
        # verificar se o value obtido é uma função
        if callable(func):
            func()
        pass

    def __init__(self):
        self.isNewWord = False
        self.isNewHeader = False
        self.isDef = False
        self.options = {
            "orth": self.new_word,
            "head": self.new_header,
            "gramGrp": '',
            "def": self.definition,
            "etym": '',
            "quote": '',
            "term": '',
            "usg": '',
            "phon": '',
        }
