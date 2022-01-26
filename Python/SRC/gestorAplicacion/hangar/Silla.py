from gestorAplicacion.adminVuelos import *

class Silla:
    def __init__(self, clase, numero_de_silla, ubicacion):
        self._pasajero = None
        #instance fields found by Java to Python Converter:
        self._estaDisponible = True
        self._clase = clase
        self._numero_de_silla = numero_de_silla
        self._ubicacion = ubicacion

    #GETTERS Y SETTERS

    def getClase(self):
        return self._clase

    def setClase(self, clase):
        self._clase = clase

    def getNumero_de_silla(self):
        return self._numero_de_silla

    def setNumero_de_silla(self, numero_de_silla):
        self._numero_de_silla = numero_de_silla

    def getPasajero(self):
        return self._pasajero

    def setPasajero(self, pasajero):
        self._pasajero = pasajero

    def isEstado(self):
        return self._estaDisponible

    def setEstado(self, estado):
        self._estaDisponible = estado

    def getUbicacion(self):
        return self._ubicacion
        
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion