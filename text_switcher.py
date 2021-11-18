from html_generator import HtmlGenerator


class TextSwitcher:

    def new_file(self,value):
        self.htmlGenerator = HtmlGenerator(value)

    def end_file(self):
        self.htmlGenerator.end()

    def write_header(self, value):
        self.htmlGenerator.write_header(value)

    def write_orth(self, value):
        self.htmlGenerator.write_word(value)

    def write_def(self):
        self.htmlGenerator.write_definition(self.currentdef)
        self.currentdef=''

    """def write_gramgrp(self, value):
        self.htmlGenerator.write_gramgrp(value)

    def write_etym(self, value):
        self.htmlGenerator.write_etym(value)

    def write_usg(self, value):
        self.htmlGenerator.write_usg(value)

    def write_phon(self, value):
        self.htmlGenerator.write_phon(value)"""

    def write_li(self, value):
        self.htmlGenerator.write_li(self.currentTag,value)

    def add_to_def(self, value):
        self.currentdef += value.strip()

    def switch(self, value):
        #print(f'{self.currentTag} : {value}')
        func = self.textOptions.get(self.currentTag, "Invalid Argument")
        if callable(func):
            if self.currentTag == '/def':
                func()
            else:
                func(value)
        pass

    def __init__(self):
        self.currentTag = ''
        self.currentdef = ''
        self.htmlGenerator = None
        self.textOptions = {
            "orth": self.write_orth,
            "head": self.write_header,
            "def": self.add_to_def,
            "/def": self.write_def,
            "gramGrp": self.write_li,
            "etym": self.write_li,
            "quote": self.add_to_def,
            "usg": self.write_li,
            "phon": self.write_li,
        }

