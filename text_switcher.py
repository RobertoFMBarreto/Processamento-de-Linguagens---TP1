class TextSwitcher:

    def write_tag(self, write, tag=''):
        if tag == '':
            tag = self.currentTag

        self.dic[self.currentHeader][self.currentWord][tag] = write

    def write_header(self, value):
        self.dic[value] = {}
        self.currentHeader = value

    def write_orth(self, value):
        self.dic[self.currentHeader][value] = {}
        self.currentWord = value

    def write_def(self, value):
        self.write_tag(self.dic[self.currentHeader][self.currentWord].get(
            'def', '') + value.strip(), tag='def')

    def write_other(self, value):
        self.dic[self.currentHeader][self.currentWord][self.currentTag] = value.strip()

    def switch(self, value):
        func = self.textOptions.get(self.currentTag, "Invalid Argument")
        if callable(func):
            func(value)
        pass

    def __init__(self):
        self.textOptions = {
            "orth": self.write_orth,
            "head": self.write_header,
            "def": self.write_def,
            "gramGrp": self.write_other,
            "etym": self.write_other,
        }
        self.currentHeader = ''
        self.currentTag = ''
        self.currentWord = ''
        self.dic = {}
