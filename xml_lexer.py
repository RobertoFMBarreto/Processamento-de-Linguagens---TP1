# xml_lexer.py
import ply.lex as plex
import dictonary
from os import walk

class XMLLex:
    tokens = ("TEXT", "OTAGS", "CTAGS")


    def t_TEXT(self, t):
        r"[^<]+"

        if self.newHeader:
            self.dic[t.value] = {}
            self.currentHeader = t.value
        elif self.newWord:
            self.dic[self.currentHeader][t.value] = {'palavra': t.value}
        elif self.insideSomething:
            pass
        return t


    def t_CTAGS(self, t):
        r"</[^>]+>"
        if t.value == "</orth>":
            self.newWord = False
        elif t.value == "</head>":
            self.newHeader = False
        elif t.value in ("</gramGrp>", "</def>", "</quote>"):
            self.insideSomething = False
        return t

    def t_OTAGS(self, t):
        r"<[^>]+>"
        if t.value == "<orth>":
            self.newWord = True
        elif t.value == "<head>":
            self.newHeader = True
        elif t.value in ("<gramGrp>", "<def>", "<quote>"):
            self.insideSomething = True
            t.value = str(t.value).replace("<", "")
            t.value = str(t.value).replace(">", "")
        return t

    def t_ANY_error(self, t):
        print(f"Unexpected tokens: {t.value[:10]}")
        exit(1)

    def __init__(self, filename):
        self.lexer = None
        self.dic = {}
        self.filename = filename
        self.newWord = False
        self.insideSomething = False
        self.newHeader = False
        self.currentHeader = ''

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
