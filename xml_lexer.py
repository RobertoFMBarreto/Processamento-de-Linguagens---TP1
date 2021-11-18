# xml_lexer.py
import ply.lex as plex
from tag_switcher import TagSwitcher
from text_switcher import TextSwitcher
from os import walk


class XMLLex:
    tokens = ("CTAGS", "OTAGS", "TRASH", "TEXT")

    def t_CTAGS(self, t):
        r"</[^ >]+(>?)"
        # usg
        # phon
        # print(t.value)
        tag = t.value
        tag = tag.replace('<', '')
        tag = tag.replace('>', '')

        if tag in self.text_switcher.textOptions:
            self.text_switcher.currentTag = tag
            self.text_switcher.switch(tag)
        self.tag_switcher.switch(t.value.replace("/", ""))
        pass

    def t_OTAGS(self, t):
        r"<[^ >]+(>?)"
        #print(t.value)
        tag = t.value
        tag = tag.replace('<', '')
        tag = tag.replace('>', '')
        #print(tag)
        if tag in self.tag_switcher.options:
            self.tag_switcher.switch(tag)
            self.text_switcher.currentTag = tag
        pass

    def t_TRASH(self, t):
        r"[^><]+>"
        #print(t.value.strip())
        pass

    def t_TEXT(self, t):
        r"[^<]+"
        self.text_switcher.switch(t.value)
        pass

    def t_error(self, t):
        print(f"Unexpected tokens: {t.value[:10]}")
        exit(1)

    def __init__(self, files):
        self.lexer = None
        self.filenames = files
        self.tag_switcher = TagSwitcher()
        self.text_switcher = TextSwitcher()

    def initialize(self, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)

        for file in filenames:
            self.text_switcher.new_file(file[:1])
            with open(f"Files/{file}", "r") as fh:
                contents = fh.read()

            self.lexer.input(contents)
            for _ in iter(self.lexer.token, None):
                pass

            print(f"Finished processing: {file[:1]}")

            self.text_switcher.end_file()


f = []
for (_, _, filenames) in walk("Files"):
    f.extend(filenames)
    break

processor = XMLLex(f)
processor.initialize()


