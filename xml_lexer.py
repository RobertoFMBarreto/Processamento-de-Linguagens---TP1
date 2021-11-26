# xml_lexer.py
from os import walk
import ply.lex as plex
from tag_switcher import TagSwitcher

# Lexer de xml


class XMLLex:
    # CTAGS -> close tags ex: </def>
    # OTAGS -> open tags ex: <def>
    # TRASH -> guarda coisas não necessárias ex: type="Text">
    # TEXT -> ler texto que está dentro das tags
    tokens = ("CTAGS", "OTAGS", "TRASH", "TEXT")
    t_ignore = '\n'
    # função de reconhecimento de tokens CTAGS
    # REGEX:
    # </ -> reconhecer a parte inicial da tag </def>
    # [^>]+ -> reconhecer qualquer token até " " ou ">"

    def t_CTAGS(self, t):
        r"</[^>]+>(\n?)"
        tag = t.value.strip()   # valor do token, ex: <def>
        # retirar o "<" substituindo por uma string vazia -> def>
        tag = tag.replace('<', '')
        # retirar o ">" substituindo por uma string vazia -> def
        tag = tag.replace('>', '')

        # verificar se a tag lida existe no dicionario dotag_switcher
        if tag in self.tag_switcher.options:
            self.tag_switcher.currentTag = tag     # colocar a tag atual como a tag lida
            # executar o switch e as funções adequadas a cada tag e texto
            self.tag_switcher.switch(tag)
        pass

    # função de reconhecimento de tokens OTAGS
    # REGEX:
    # < -> reconhecer a parte inicial da tag <def>
    # [^ >]+ -> reconhecer qualquer token até " " ou ">"
    # (>?) -> reconhece ">" caso exista (?)
    def t_OTAGS(self, t):
        r"<[^ >]+(>?)(\n?)"
        tag = t.value.strip()
        tag = tag.replace('<', '')
        tag = tag.replace('>', '')
        if tag in self.tag_switcher.options:
            self.tag_switcher.currentTag = tag
        pass

    # função de reconhecimento de tokens TRASH
    # REGEX:
    # [^><]+ -> reconhecer qualquer token até "<" ou ">" para assim ler tudo o que não seja de interesse
    def t_TRASH(self, t):
        r"[^><]+>"
        pass

    # função de reconhecimento de tokens TEXT
    # REGEX:
    # [^<]+ -> reconhecer qualquer token até "<" ou seja ler até a começar uma tag
    def t_TEXT(self, t):
        r"[^<]+"
        self.tag_switcher.switch(t.value)
        # print(t)
        pass

    def t_error(self, t):
        print(f"Unexpected tokens: {t.value[:10]}")
        exit(1)

    def __init__(self, files):
        self.lexer = None
        self.filenames = files
        self.tag_switcher = TagSwitcher()

    def initialize(self, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)

        for file in self.filenames:
            self.tag_switcher.new_file(file[:1])
            with open(f"Files/{file}", "r") as fh:
                contents = fh.read()

            self.lexer.input(contents)
            for _ in iter(self.lexer.token, None):
                pass

            print(f"Finished processing: {file[:1]}")

            self.tag_switcher.end_file()


f = []
for (_, _, filenames) in walk("Files"):
    f.extend(filenames)
    break

processor = XMLLex(f)
processor.initialize()
