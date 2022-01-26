from enum import Enum

class Clase(Enum):
    ECONOMICA = 10000
    EJECUTIVA = 70000
            
    def __init__(self, precio):
       self._precio = precio

    def getPrecio(self):
       return self._precio

    #def setPrecio(self, precio): Parece que no se puede reasignar en el enum
       #self._precio = precio
