from Especificacion1 import Especificacion1
from Especificacion2 import Especificacion2
from Farmaco import Farmaco

class Remedio(Especificacion1, Especificacion2, Farmaco):
    __codigo = 0
    __nombre = ""

    def __init__(self):
        pass

    def getCodigo(self):
        return self.__codigo
    
    def setCodigo(self, codigo):
        self.__codigo = codigo

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre