# html_generator
import io


class HtmlGenerator:

    def __init__(self, header):
        self.header = header
        self.file = open(f"generated/{self.header}.html", "w")

    def write_header(self, value):
        self.file.write(f'''<html>\n\t<body>\n<h1>{value}</h1>\n''')

    def write_word(self, value):
        self.file.write(f'''<h3>{value}</h3>\n''')

    def write_gramgrp(self, value):
        self.file.write(f'''<li>Grp. gram.: {value}</li>\n''')

    def write_etym(self, value):
        if value != '':
            self.file.write(f'''<li>Proveniência: {value}</li>\n''')

    def write_definition(self, value):
        self.file.write(f'''<p>{value}</p>\n''')

    def end(self):
        self.file.write('''</body>\n\t</html>''')

        self.file.close()
        print(f'finished generating: {self.header}')

