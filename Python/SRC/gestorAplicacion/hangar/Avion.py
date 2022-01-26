import math
from gestorAplicacion.hangar.Aeronave import Aeronave
from gestorAplicacion.hangar.Silla import Silla
from gestorAplicacion.hangar.Clase import Clase
from gestorAplicacion.hangar.Ubicacion import Ubicacion
#from gestorAplicacion.adminVuelos import *

class Avion(Aeronave):
    _NUM_SILLAS_ECONOMICAS = 24
    _NUM_SILLAS_EJECUTIVAS = 12

    # CONSTRUCTOR
    def __init__(self, nombre, aerolinea):
        super().__init__(nombre, aerolinea)
        #self.setSILLASECONOMICAS([None for _ in range(gestorAplicacion.hangar.Avion._NUM_SILLAS_ECONOMICAS)])
        #self.setSILLASEJECUTIVAS([None for _ in range(gestorAplicacion.hangar.Avion._NUM_SILLAS_EJECUTIVAS)])

        # LA VARIABLE UBICACION VA CAMBIANDO SU VALOR SEGUN LOS SIGUIENTES PROCESOS, SE
        # USA PARA LA ASIGNACION DEL ATRIBUTO UBICACION DE LAS SILLAS.
        ubicacion = None

        # EL SIGUIENTE PROCESO CREA Y AGREGA SILLAS A LA LISTA DE SILLAS EJECUTIVAS QUE
        # POSEE LA CLASE AVION("HEREDA LA LISTA DE AERONAVE")
        # NOTA: LAS SILLAS DE TIPO EJECUTIVA SE REPARTEN EN GRUPOS DE 4 EN FILA
        # SEPARADAS POR UN PASILLO.(POR TANTO NO HAY UBICACION CENTRAL)
        for numPosicion in range(0,Avion._NUM_SILLAS_EJECUTIVAS):
            if numPosicion%4 == 0 or numPosicion % 4 == 3:
                ubicacion = Ubicacion.VENTANA
            else:
                ubicacion = Ubicacion.PASILLO

            self.getSILLASEJECUTIVAS().append( Silla(Clase.EJECUTIVA, numPosicion, ubicacion))

        # EL SIGUIENTE PROCESO CREA Y AGREGA SILLAS A LA LISTA DE SILLAS ECONOMICAS QUE
        # POSEE LA CLASE AVION("HEREDA LA LISTA DE AERONAVE")
        # NOTA: LAS SILLAS DE TIPO ECONOMICA SE REPARTEN EN GRUPOS DE 6 EN FILA
        # SEPARADAS POR UN PASILLO
        for numPosicion in range(0, Avion._NUM_SILLAS_ECONOMICAS):
            if numPosicion % 6 == 0 or numPosicion% 6 == 5:
                ubicacion = Ubicacion.VENTANA
            elif numPosicion % 6 == 1 or numPosicion % 6 == 4:
                ubicacion = Ubicacion.CENTRAL
            elif numPosicion % 6 == 2 or numPosicion % 6 == 3:
                ubicacion = Ubicacion.PASILLO
            self.getSILLASECONOMICAS().append(Silla(Clase.ECONOMICA, numPosicion, ubicacion))

    def getNombre(self):
        texto = super().getNombre() + "_A"
        return texto

    @staticmethod
    def getNumSillasEconomicas():
        return Avion._NUM_SILLAS_ECONOMICAS

    @staticmethod
    def getNumSillasEjecutivas():
        return Avion._NUM_SILLAS_EJECUTIVAS

    # METODOS

    #	ESTE METODO RECIBE UN TIPO DE DATO DOUBLE DE LA DISTANCIA QUE HAY DESDE EL LUGAR DE ORIGEN AL LUGAR DE DESTINO
    #	Y RETONARNA EL COSTO TOTAL DE GASOLINA PARA RECORRER EL TRAYECTO
    def Calcular_Consumo_Gasolina(self, distancia_en_km):
        consumido = None
        consumido = self.getGastoGasolina() * distancia_en_km
        return consumido
