#from gestorAplicacion.adminVuelos import *
class Aeronave:

    # ATRIBUTOS

    # CONTRUCTOR
    def __init__(self, nombre, aerolinea):
        #instance fields found by Java to Python Converter:
        self.Gasto_gasolina = 120
        self._descompuesto = False
        self._SILLAS_ECONOMICAS = []
        self._SILLAS_EJECUTIVAS = []
        self._nombre = nombre
        self._aerolinea = aerolinea

    # GET AND SET
    def getAerolinea(self):
        return self._aerolinea

    def setAerolinea(self, aerolinea):
        self._aerolinea = aerolinea

    def getSILLASECONOMICAS(self):
        return self._SILLAS_ECONOMICAS

    def setSILLASECONOMICAS(self, sILLAS_ECONOMICAS):
        self._SILLAS_ECONOMICAS = sILLAS_ECONOMICAS

    def getSILLASEJECUTIVAS(self):
        return self._SILLAS_EJECUTIVAS

    def setSILLASEJECUTIVAS(self, sILLAS_EJECUTIVAS):
        self._SILLAS_EJECUTIVAS = sILLAS_EJECUTIVAS

    def getGastoGasolina(self):
        return self.Gasto_gasolina

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    # METODOS

    def isDescompuesto(self):
        return self._descompuesto

    def setDescompuesto(self, descompuesto):
        self._descompuesto = descompuesto

    def __str__(self):
        return self._nombre

    # BUSCAR SILLAS POR UBICACION Y TIPO
    #	EN ESTE METODO SE RECIBE UNA UBICACION(UBICACION) Y UN TIPO(STRING), LOS CUALES UTILIZA PARA BUSCAR DENTRO DE
    #	LAS LISTAS DE LA AERONAVE QUE LO LLAMA UNA SILLA CON LA UBICACION Y TIPO QUE SE INGRESAN.
    def buscarSillaPorUbicacionyTipo(self, ubicacion, tipo):

        if tipo.lower() == "ECONOMICA".lower():
            for i in self._SILLAS_ECONOMICAS:
                if i.isEstado() and i.getUbicacion() == ubicacion:
                    return i
        elif tipo.lower() == "EJECUTIVA".lower():
            for i in self._SILLAS_EJECUTIVAS:
                if i.isEstado() and i.getUbicacion() == ubicacion:
                    return i
        return None
    #	ESTE METODO RECORRAN LOS ARREGLOS DE SILLAS EJECUTIVOS Y ECONOMICAS DE CADA AVION Y AVIONETA 
    #	PARA VERIFICAR LA CANTIDAD DE SILLAS QUE ESTAN OCUPADAS Y RETORNAR DICHA CANTIDAD
    
    def Calcular_Sillas_Ocupadas(self):
        pass

    #	ESTE METODO RECIBE UN TIPO DE DATO DOUBLE DE LA DISTANCIA QUE HAY DESDE EL LUGAR DE ORIGEN AL LUGAR DE DESTINO
    #	Y RETONARNA EL COSTO TOTAL DE GASOLINA PARA RECORRER EL TRAYECTO
    def Calcular_Consumo_Gasolina(self, distancia_en_km):
        pass
