# html_generator
from pylatex import Document, Section, Subsection
import os.path


class HtmlGenerator:

    def __init__(self, header):
        self.header = header
        if os.path.isdir('generated') is not True:
            os.mkdir("generated")

        if os.path.isdir('generated/html') is not True:
            os.mkdir("generated/html")

        if os.path.isdir('generated/latex') is not True:
            os.mkdir("generated/latex")

        self.htmlFile = open(f"generated/html/{self.header}.html", "w")
        #self.latexFile = Document(documentclass='article')

    def write_header(self, value):
        self.htmlFile.write(f'<html>\n\t<body>\n<h1>{value}</h1>\n')
        # self.latexFile.append(Section(value))

    def write_word(self, value):
        self.htmlFile.write(f'<h3>{value}</h3>\n')
        # self.latexFile.append(Subsection(value))

    """def write_gramgrp(self, value):
        self.htmlFile.write(f'<li>Grp. gram.: {value}</li>\n')
        # self.latexFile.append(value)

    def write_phon(self, value):
        self.htmlFile.write(f'<li>fónica: {value}</li>\n')
        # self.latexFile.append(value)

    def write_etym(self, value):
        if value != '':
            self.htmlFile.write(f'<li>Proveniência: {value}</li>\n')
            # self.latexFile.append(value)

    def write_usg(self,value):
        self.htmlFile.write(f'<li>Utilização: {value}</li>\n')"""

    def write_li(self, tag, value):
        self.htmlFile.write(f'<li>{tag}: {value}</li>\n')


    def write_definition(self, value):

        self.htmlFile.write(f'''<p>{value}</p>\n''')
        # self.latexFile.append(value)

    def end(self):
        self.htmlFile.write('''</body>\n\t</html>''')

        self.htmlFile.close()
        #self.latexFile.generate_pdf(f'generated/Latex/{self.header}', compiler='pdflatex')
        print(f'finished generating: {self.header}')
