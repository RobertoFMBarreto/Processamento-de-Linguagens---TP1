# html_generator

class HtmlGenerator:

    def iterate_dictionary(self, dictionary):
        for k, v in dictionary.items():
            self.new_file()
            self.write_header(k)
            for k1, v1 in v.items():
                self.write_word(k1)
                # print(k1)
                self.write_gramgrp(v1.get('gramGrp', ''))
                self.write_etym(v1.get('etym', ''))
                self.write_definition(v1['def'])
            self.end()

    def new_file(self):
        self.text='''<html>\n\t<body>\n'''

    def write_header(self, header):
        self.text += f'''<h1>{header}</h1>\n'''
        self.header=header

    def write_word(self, word):
        self.text += f'''<h3>{word}</h3>\n'''

    def write_gramgrp(self, word):
        self.text += f'''<li>Grp. gram.: {word}</li>\n'''

    def write_etym(self, etym):
        if etym != '':
            self.text += f'''<li>Proveniência: {etym}</li>\n'''

    def write_definition(self, definition):
        self.text += f'''<p>{definition}</p>\n'''

    def end(self):
        self.text += '''<body>\n\t<html>'''
        file=open(f"generated/{self.header}.html", "w")
        file.write(self.text)
        file.close()
        print(f'finished generating: {self.header}')

    def show(self):
        print(self.text)
