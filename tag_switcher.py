from files_generator import FilesGenerator


class TagSwitcher:

    def new_file(self, value):
        self.filesGenerator = FilesGenerator(value)

    def end_file(self):
        self.filesGenerator.end()

    def write_header(self, value):
        self.filesGenerator.write_header(value)

    def write_orth(self, value):
        if self.currentdef != '':
            self.write_def()
        self.filesGenerator.write_word(value)

    def write_nl_def(self):
        self.currentdef += '\n'

    def write_def(self):
        self.filesGenerator.write_definition(self.currentdef.strip())
        self.currentdef = ''

    def write_gramgrp(self, value):
        self.filesGenerator.write_gramgrp(value)

    def write_etym(self, value):
        self.filesGenerator.write_etym(value)

    def write_usg(self, value):
        self.filesGenerator.write_usg(value)

    def write_phon(self, value):
        self.filesGenerator.write_phon(value)

    def add_to_def(self, value):
        self.currentdef += value.strip()

    def switch(self, value):
        func = self.options.get(self.currentTag, "Invalid Argument")
        if callable(func):
            if self.currentTag == '/def':
                func()
            else:
                func(value)
        pass

    def __init__(self):
        self.currentTag = ''
        self.currentdef = ''
        self.filesGenerator = None
        self.options = {
            "orth": self.write_orth,
            "head": self.write_header,
            "def": self.add_to_def,
            "/def": self.write_nl_def,
            "gramGrp": self.write_gramgrp,
            "etym": self.write_etym,
            "quote": self.add_to_def,
            "usg": self.write_usg,
            "phon": self.write_phon,
        }
