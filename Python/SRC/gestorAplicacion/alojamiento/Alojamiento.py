class Alojamiento:
    
    _alojamientos = []

    #CONSTRUCTORES
    def __init__(self, nombre, locacion, precio_dia, estrellas):
        self._nombre = nombre
        self._locacion = locacion
        self._precio_dia = precio_dia
        self._estrellas = estrellas
        Alojamiento._alojamientos.append(self)


    #CALCULAR PRECIO DEL ALOJAMIENTO
    def calcularPrecio(self, dias):
        return int((dias * self._precio_dia))

    # BUSCAR ALOJAMIENTOS POR...

    @staticmethod
    def buscarAlojamientoPorUbicacion(ubicacion):
        alojamientosEnUbicacion = []
        i = 0
        while i < len(Alojamiento._alojamientos):
            if Alojamiento._alojamientos[i].getLocacion().casefold() == ubicacion.casefold():
                alojamientosEnUbicacion.append(Alojamiento._alojamientos[i])
            i += 1
        return alojamientosEnUbicacion

    @staticmethod
    def buscarAlojamientoPorNombre(nombre):
        i = 0
        while i < len(Alojamiento._alojamientos):
            if Alojamiento._alojamientos[i].getNombre().casefold() == nombre.casefold():
                return Alojamiento._alojamientos[i]
            i += 1
        return None

    #GETTERS Y SETTERS

    def setLocacion(self, locacion):
        self._locacion = locacion

    def setPrecio_dias(self, precio_dias):
        self._precio_dia = precio_dias

    @staticmethod
    def getAlojamientos():
        return Alojamiento._alojamientos

    @staticmethod
    def setAlojamientos(alojamientos):
        Alojamiento._alojamientos = alojamientos

    def getPrecio_dia(self):
        return self._precio_dia

    def setPrecio_dia(self, precio_dia):
        self._precio_dia = precio_dia

    def getLocacion(self):
        return self._locacion

    def getEstrellas(self):
        return self._estrellas

    def setEstrellas(self, estrellas):
        self._estrellas = estrellas

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre
