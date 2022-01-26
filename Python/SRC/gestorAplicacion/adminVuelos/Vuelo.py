from gestorAplicacion.hangar import *
from gestorAplicacion.adminVuelos.Tiquete import Tiquete

# CONTIENE LA INFORMACION PERTINENTE DE UN VUELO, ADEMAS DE LA LISTA DE TIQUETES QUE FUERON ASOCIADOS AL MISMO.
class Vuelo():

    # ATRIBUTOS

    #CONSTRUCTOR
    def __init__(self, iD, precio, origen, destino, aeronave, distancia, fecha_de_salida, hora_de_salida):
        self._ID = iD
        self._precio = precio
        self._origen = origen
        self._destino = destino
        self._aeronave = aeronave
        self._distancia_en_km = distancia
        self._fecha_de_salida = fecha_de_salida
        self.setHora_de_salida(hora_de_salida)
        self.getAeronave().getAerolinea().agregarVuelo(self)
        self._tiquetes = []
        self._estaCompleto = False

    # RECIBE UNA LISTA DE TIQUETES (ARRAYLIST<TIQUETE>) Y UN ID DE UN TIQUETE (INT), Y SE ENCARGA DE RECORRER ESA LISTA DE TIQUETES.
    # SI ENCUENTRA UNO QUE TENGA EL MISMO ID QUE EL PASADO COMO PAR METRO, LO RETORNA. SI NO ENCUENTRA NINGUNO RETORNA NULL.
    def buscarTiquetePorID(self, tiquetes, ID):
        i = 0
        while i < len(tiquetes):
            if tiquetes[i].getId() == ID:
                return tiquetes[i]
            i += 1
        return None


    #GETTERS Y SETTERS

    def getID(self):
        return self._ID

    def setID(self, iD):
        self._ID = iD

    def getPrecio(self):
        return self._precio

    def setPrecio(self, precio):
        self._precio = precio

    def getOrigen(self):
        return self._origen

    def setOrigen(self, origen):
        self._origen = origen

    def getDestino(self):
        return self._destino

    def setDestino(self, destino):
        self._destino = destino

    #CORREGIR CUANDO SE TENGA LA CLASE ABSTRACTA
    def getAeronave(self):
        return self._aeronave

    def setAeronave(self, aeronave):
        self._aeronave = aeronave

    def getDistancia_en_km(self):
        return self._distancia_en_km

    def setDistancia_en_km(self, distancia_en_km):
        self._distancia_en_km = distancia_en_km

    def getFecha_de_salida(self):
        return self._fecha_de_salida

    def setFecha_de_salida(self, fecha_de_salida):
        self._fecha_de_salida = fecha_de_salida

    def getTiquetes(self):
        return self._tiquetes

    def setTiquetes(self, tiquetes):
        self._tiquetes = tiquetes

    def getHora_de_salida(self):
        return self._hora_de_salida

    def setHora_de_salida(self, hora_de_salida):
        self._hora_de_salida = hora_de_salida

    def isEstaCompleto(self):
        return self._estaCompleto

    def setEstaCompleto(self, estaCompleto):
        self._estaCompleto = estaCompleto