# xml_lexer.py
import ply.lex as plex
from switcher import Switcher
from os import walk

class XMLLex:
    tokens = ("TEXT", "OTAGS", "CTAGS")

    def t_TEXT(self, t):
        r"[^<]+"

        if self.switch.isNewHeader:
            self.dic[t.value] = {}
            self.currentHeader = t.value
        elif self.switch.isNewWord:
            self.dic[self.currentHeader][t.value] = {'palavra': t.value}
            self.currentWord = t.value
        elif self.currentTag == 'def':
            self.insideDef = True
            self.dic[self.currentHeader][self.currentWord]['def'] = t.value
        elif self.insideDef:
            self.dic[self.currentHeader][self.currentWord]['def'] += t.value
        elif self.currentTag == "gramGrp":
            self.dic[self.currentHeader][self.currentWord][self.currentTag] = t.value

        return t


    def t_CTAGS(self, t):
        r"</[^>]+>"
        self.currentTag = ''
        if t.value == '</def>':
            self.insideDef = False
        self.switch.switch(t.value.replace("/",""))
        return t

    def t_OTAGS(self, t):
        r"<[^>]+>"

        if t.value in self.switch.options.keys():
            self.switch.switch(t.value)
            tag = t.value
            tag = tag.replace('<','')
            tag = tag.replace('>','')
            self.currentTag = tag

        return t

    """def t_definition_TEXT(self,t):
        r"</def>"
        print(t.value)
        return t"""

    def t_ANY_error(self, t):
        print(f"Unexpected tokens: {t.value[:10]}")
        exit(1)

    def __init__(self, filename):
        self.lexer = None
        self.dic = {}
        self.filename = filename
        self.switch = Switcher()
        self.currentHeader = ''
        self.currentTag = ''
        self.insideDef = False
        self.currentWord = ''

    def initialize(self, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)
        with open(f"Files/{self.filename}", "r") as fh:
            contents = fh.read()

        self.lexer.input(contents)
        for token in iter(self.lexer.token, None):
            pass
            #print(token)
        print(self.dic)
        print("Finished processing")


f = []
for (dirpath, dirnames, filenames) in walk("D:\escola\Processamento de linguagens\TP1\Files"):
    f.extend(filenames)
    break

processor = XMLLex("A.xml")
processor.initialize()
