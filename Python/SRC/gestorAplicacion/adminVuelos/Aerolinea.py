from excepciones.ErrorAsignacion import ExcepcionIdTiquete
from gestorAplicacion.hangar import *
from gestorAplicacion.adminVuelos.Vuelo import Vuelo
from gestorAplicacion.adminVuelos.Tiquete import Tiquete

# ALMACENA LA INFORMACION DE TODAS LAS AEROLINEAS CREADAS, ADEMAS DE LOS VUELOS Y AERONAVES ASOCIADOS A CADA UNA DE ELLAS 
# CON LOS METODOS NECESARIOS PARA ACCEDER A ESTA INFORMACION A TRAVES DE DISTINTOS PARAMETROS.
class Aerolinea():

    #ATRIBUTOS
    _aerolineas = []

    #CONSTRUCTOR
    def __init__(self, nombre):
        self._aeronaves = []
        self._vuelos = []

        self._nombre = nombre
        Aerolinea._aerolineas.append(self)

    def toString(self):
        return self._nombre

    #BUSCAR AEROLINEA

    # METODO DE CLASE QUE RECIBE UN NOMBRE DE AEROLINEA Y BUSCA ENTRE LAS AEROLINEAS DISPONIBLES SI HAY ALGUNA CON ESTE NOMBRE, 
    #SI ES ASÍ, RETORNA ESE OBJETO AEROLINEA, SI NO, DEVUELVE NULL.
    @staticmethod
    def buscarAerolineaPorNombre(nombre2):
        retorno = None
        i = 0
        while i < len(Aerolinea.getAerolineas()):
            if Aerolinea.getAerolineas()[i].getNombre().lower() == nombre2.lower():
                # SI ENCUENTRA UNA AEROLINEA CUYO NOMBRE COINCIDA CON EL PARAMETRO PASADO, IGNORANDO MINUSCULAS Y MAYUSCULAS,
                # RETORNA ESA AEROLINEA.
                retorno = Aerolinea.getAerolineas()[i]
            i += 1
        return retorno

    #BUSCAR VUELO POR...

    # RECIBE UNA LISTA DE VUELOS (ARRAYLIST<VUELO>) Y UN ID (INT) Y SE ENCARGA DE RETORNAR EL OBJETO VUELO QUE TENGA EL ID QUE PASAMOS 
    # COMO PARAMETRO, SI NO LO ENCUENTRA EN ESA LISTA DE VUELOS RETORNA NULL.
    def buscarVueloPorID(self, vuelos, ID):
        i = 0
        while i < len(vuelos):
            if vuelos[i].getID() == ID:
                return vuelos[i]
            i += 1
        return None

    # RECIBE UNA LISTA DE VUELOS (ARRAYLIST<VUELO>) Y UN NOMBRE_AERONAVE(STRING) Y SE ENCARGA DE RETORNAR EL OBJETO VUELO QUE TENGA 
    # ASOCIADA LA AERONAVE QUE TIENE EL NOMBRE QUE PASAMOS COMO PARAMETRO, SI NO LO ENCUENTRA EN ESA LISTA DE VUELOS RETORNA NULL.
    def buscarVueloPorAeronave(self, vuelos, nombre_Aeronave):
        i = 0
        while i < len(vuelos):
            if vuelos[i].getAeronave().getNombre().casefold() ==  nombre_Aeronave.casefold():
                return vuelos[i]
            i += 1
        return None

    # RECIBE UNA LISTA DE VUELOS (ARRAYLIST<VUELO>) Y UN DESTINO(STRING) Y SE ENCARGA DE RETORNAR UNA LISTA DE VUELOS, 
    # CON TODOS LOS VUELOS QUE TENGAN ASOCIADO EL DESTINO QUE PASAMOS COMO PARAMETRO.
    def buscarVueloPorDestino(self, vuelos, destino):
        vuelosPorDestino = []
        i = 0
        while i < len(vuelos):
            if vuelos[i].getDestino().casefold() == destino.casefold(): # cambio del equals
                vuelosPorDestino.append(vuelos[i])
            i += 1
        return vuelosPorDestino

    # RECIBE UNA LISTA DE VUELOS (ARRAYLIST<VUELO> ) Y UNA FECHA (STRING) Y SE ENCARGA DE RETORNAR UNA LISTA DE VUELOS, 
    # CON TODOS LOS VUELOS QUE TENGAN ASOCIADA LA FECHA QUE PASAMOS COMO PARAMETRO.
    def buscarVueloPorFecha(self, vuelos, fecha):
        vuelosPorFecha = []
        i = 0
        while i < len(vuelos):
            if vuelos[i].getFecha_de_salida() == fecha:
                vuelosPorFecha.append(vuelos[i])
            i += 1
        return vuelosPorFecha

    #VUELOS DISPONIBLES

    # RECIBE UNA LISTA DE VUELOS (ARRAYLIST<VUELO>) Y SE ENCARGA DE RETORNAR UNA LISTA DE VUELOS, CON TODOS LOS VUELOS DE LA AEROLINEA
    # QUE NO ESTEN COMPLETOS, ES DECIR QUE SU ATRIBUTO ESTACOMPLETO SEA IGUAL A false.
    def vuelosDisponibles(self, vuelos):
        vuelosDisponibles = []
        i = 0
        while i < len(vuelos):
            if not vuelos[i].isEstaCompleto():
                vuelosDisponibles.append(vuelos[i])
            i += 1
        return vuelosDisponibles

    # AGREGAR O CANCELAR UN VUELO

    # RECIBE COMO PARAMETRO UN VUELO (VUELO) Y SE ENCARGA DE ANADIRLO A LA LISTA DE VUELOS DE LA AEROLINEA.
    def agregarVuelo(self, vuelo):
        self._vuelos.append(vuelo)

    # RECIBE COMO PARÁMETRO UN ENTERO, QUE CONTIENE EL ID DEL VUELO A ELIMINAR, Y SE ENCARGA DE RECORRER SU LISTA DE VUELOS PARA ELIMINAR 
    # EL VUELO QUE CONTENGA EL ID QUE COINCIDE CON EL PARAMETRO, SI LO ENCONTRO Y LO ELIMINO, RETORNA true, EN CASO CONTRARIO RETORNA false.
    def cancelarVuelo(self, vuelo_a_eliminar):
        i = 0
        while i < len(self._vuelos):
            if self._vuelos[i].getID() == vuelo_a_eliminar:
                self._vuelos.pop(i)
                return True
            i += 1
        return False

    # BUSCAR TIQUETE POR ID

    # METODO DE CLASE QUE RECIBE UN ID (INT) Y SE ENCARGA DE BUSCAR ENTRE CADA AEROLÍNEA Y ENTRE CADA VUELO DE ESTA AEROLINEA, 
    # SI HAY UN TIQUETE ASOCIADO EN LA LISTA DE TIQUETES DE CADA VUELO QUE TENGA POR ID EL QUE LE PASAMOS COMO PARÁMETRO Y RETORNAR ESTE TIQUETE, 
    # HACIENDO USO DEL METODO BUSCARTIQUETEPORID() DE VUELO.

    @staticmethod
    def BuscarTiquete(ID):
        tiquete_buscado = None
        aerolineasDisponibles = Aerolinea.getAerolineas()
        i = 0
        while i < len(aerolineasDisponibles):
            aerolinea = aerolineasDisponibles[i]
            j = 0
            while j < len(aerolinea.getVuelos()):

                vuelo = aerolinea.getVuelos()[j]
                tiquete_buscado = vuelo.buscarTiquetePorID(vuelo.getTiquetes(), ID)
                if tiquete_buscado is not None:
                    return tiquete_buscado
                j += 1
            i += 1
        
        if tiquete_buscado == None:
            raise ExcepcionIdTiquete(ID)
        return None

    # SETTERS Y GETTERS

    def getNombre(self):
        return self._nombre


    def setNombre(self, nombre):
        self._nombre = nombre


    def getVuelos(self):
        return self._vuelos


    def setVuelos(self, vuelos):
        self._vuelos = vuelos

    def getAeronaves(self):
        return self._aeronaves

    def setAviones(self, aviones):
        self._aeronaves = aviones

    @staticmethod
    def getAerolineas():
        return Aerolinea._aerolineas

    @staticmethod
    def setAerolineas(aerolineas):
        Aerolinea._aerolineas = aerolineas
