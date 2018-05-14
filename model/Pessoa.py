class Pessoa:

    def __init__(self, id, login, nome, senha):
        self.__id = id
        self.__login = login
        self.__nome = nome
        self.__senha = senha

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        self.__login = value

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, value):
        self.__senha = value

