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
            self.dic[self.currentHeader][t.value] = {'palavra': t.value.strip()}
            self.currentWord = t.value
        elif self.switch.isDef:
            self.dic[self.currentHeader][self.currentWord]['def'] = self.dic[self.currentHeader][self.currentWord].get('def', '') + t.value.strip()
        elif self.currentTag == "gramGrp":
            self.dic[self.currentHeader][self.currentWord][self.currentTag] = t.value.strip()
        elif self .currentTag == "etym":
            self.dic[self.currentHeader][self.currentWord][self.currentTag] = t.value.strip()
        return t


    def t_CTAGS(self, t):
        r"</[^>]+>"
        self.currentTag = ''
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

    def t_error(self, t):
        print(f"Unexpected tokens: {t.value[:10]}")
        exit(1)

    def __init__(self, filenames):
        self.lexer = None
        self.dic = {}
        self.filenames = filenames
        self.switch = Switcher()
        self.currentHeader = ''
        self.currentTag = ''
        self.currentWord = ''

    def initialize(self, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)
        for file in filenames:

            with open(f"Files/{file}", "r") as fh:
                contents = fh.read()

            self.lexer.input(contents)
            for token in iter(self.lexer.token, None):
                pass


            print(f"Finished processing: {file[:1]}")

        print(self.dic)


f = []
for (dirpath, dirnames, filenames) in walk("D:\escola\Processamento de linguagens\TP1\Files"):
    f.extend(filenames)
    break

processor = XMLLex(f)
processor.initialize()
