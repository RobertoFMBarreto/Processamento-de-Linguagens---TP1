# html_generator
from pylatex import Document, Section, Subsection, lists
import os.path


class FilesGenerator:

    def __init__(self, header):
        self.header = header
        if os.path.isdir('generated') is not True:
            os.mkdir("generated")

        if os.path.isdir('generated/html') is not True:
            os.mkdir("generated/html")

        if os.path.isdir('generated/latex') is not True:
            os.mkdir("generated/latex")

        self.htmlFile = open(f"generated/html/{self.header}.html", "w")
        self.latexFile = open(f"generated/latex/{self.header}.tex", "w")

    def remove_underline_latex(self, value):
        value = value.replace('_', '\\textunderscore ')
        return value

    def write_header(self, value):
        self.htmlFile.write(f'<html>\n\t<body>\n<h1>{value}</h1>\n')
        self.latexFile.write(
            '\\documentclass{article}\n\\usepackage[portuguese]{babel}')
        self.latexFile.write('\n\\title{'+f'{value}'+'}')
        self.latexFile.write('\n\\begin{document}')

    def write_word(self, value):
        self.htmlFile.write(f'<h3>{value}</h3>\n')
        self.latexFile.write('\n\\section{' + f'{value}' + '}')

    def write_gramgrp(self, value):
        self.htmlFile.write(f'<li>Grp. gram.: {value}</li>\n')
        self.latexFile.write('\n\\begin{itemize}')
        self.latexFile.write(
            '\n\\item {Grp. gram.:'+f'{self.remove_underline_latex(value)}'+'}')
        self.latexFile.write('\n\\end{itemize}')

    def write_phon(self, value):
        self.htmlFile.write(f'<li>fónica: {value}</li>\n')
        self.latexFile.write('\n\\begin{itemize}')
        self.latexFile.write(
            '\n\\item {fónica:'+f'{self.remove_underline_latex(value)}'+'}')
        self.latexFile.write('\n\\end{itemize}')

    def write_etym(self, value):
        self.htmlFile.write(f'<li>Proveniência: {value}</li>\n')
        self.latexFile.write('\n\\begin{itemize}')
        self.latexFile.write(
            '\n\\item {Proveniência:' + f'{self.remove_underline_latex(value)}' + '}')
        self.latexFile.write('\n\\end{itemize}')

    def write_usg(self, value):
        self.htmlFile.write(f'<li>Utilização: {value}</li>\n')
        self.latexFile.write('\n\\begin{itemize}')
        self.latexFile.write(
            '\n\\item {Utilização:' + f'{self.remove_underline_latex(value)}' + '}')
        self.latexFile.write('\n\\end{itemize}')

    def write_definition(self, value):
        self.htmlFile.write(f'''<p>{value}</p>\n''')
        self.latexFile.write(f'\n{self.remove_underline_latex(value)}')

    def end(self):
        self.htmlFile.write('</body>\n\t</html>')
        self.latexFile.write('\n\\end{document}')

        self.htmlFile.close()
        self.latexFile.close()
        print(f'finished generating: {self.header}')
