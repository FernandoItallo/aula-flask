class Jogo:

    def __init__(self, nome, categoria, console, id=None):
        self.__nome = nome
        self.__categoria = categoria
        self.__console = console
        self.__id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, value):
        self.__categoria = value

    @property
    def console(self):
        return self.__console

    @console.setter
    def console(self, value):
        self.__console = value

