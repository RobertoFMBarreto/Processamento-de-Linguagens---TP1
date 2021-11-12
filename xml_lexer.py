# xml_lexer.py
import ply.lex as plex
from html_generator import HtmlGenerator
from tag_switcher import TagSwitcher
from text_switcher import TextSwitcher
from os import walk


class XMLLex:
    tokens = ("TEXT", "OTAGS", "CTAGS")

    def t_TEXT(self, t):
        r"[^<]+"
        self.text_switcher.switch(t.value)
        pass

    def t_CTAGS(self, t):
        r"</[^>]+>"
        self.text_switcher.currentTag = ''
        self.tag_switcher.switch(t.value.replace("/", ""))
        pass

    def t_OTAGS(self, t):
        r"<[^>]+>"
        if t.value in self.tag_switcher.options.keys():
            self.tag_switcher.switch(t.value)
            tag = t.value
            tag = tag.replace('<', '')
            tag = tag.replace('>', '')
            self.text_switcher.currentTag = tag
        pass

    def t_error(self, t):
        print(f"Unexpected tokens: {t.value[:10]}")
        exit(1)

    def __init__(self, files):
        self.lexer = None
        self.filenames = files
        self.tag_switcher = TagSwitcher()
        self.text_switcher = TextSwitcher()
        self.htmlGenerator = HtmlGenerator()

    def initialize(self, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)

        for file in filenames:

            with open(f"Files/{file}", "r") as fh:
                contents = fh.read()

            self.lexer.input(contents)
            for _ in iter(self.lexer.token, None):
                pass

            print(f"Finished processing: {file[:1]}")

        self.htmlGenerator.iterate_dictionary(self.text_switcher.dic)


f = []
for (_, _, filenames) in walk("Files"):
    f.extend(filenames)
    break

processor = XMLLex(f)
processor.initialize()
