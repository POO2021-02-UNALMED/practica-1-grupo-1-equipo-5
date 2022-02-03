#FALTA MODIFICAR ALGUNAS COSAS PUNTUALES
import math
from gestorAplicacion.hangar.Aeronave import Aeronave
from gestorAplicacion.hangar.Silla import Silla
from gestorAplicacion.hangar.Clase import Clase
from gestorAplicacion.hangar.Ubicacion import Ubicacion
#from gestorAplicacion.adminVuelos import *

class Avioneta(Aeronave):

    _NUM_SILLAS_ECONOMICAS = 6
    _NUM_SILLAS_EJECUTIVAS = 4

    def __init__(self, nombre, aerolinea):
        super().__init__(nombre, aerolinea)
        #self.setSILLASECONOMICAS([None for _ in range(gestorAplicacion.hangar.Avioneta.__NUM_SILLAS_ECONOMICAS)])
        #self.setSILLASEJECUTIVAS([None for _ in range(gestorAplicacion.hangar.Avioneta.__NUM_SILLAS_EJECUTIVAS)])

        #LA VARIABLE UBICACION VA CAMBIANDO SU VALOR SEGUN LOS SIGUIENTES PROCESOS, SE
		# USA PARA LA ASIGNACION DEL ATRIBUTO UBICACION DE LAS SILLAS.
        ubicacion = None                #------------------------------------------------#
        # EL SIGUIENTE PROCESO CREA Y AGREGA SILLAS A LA LISTA DE SILLAS EJECUTIVAS QUE
        # POSEE LA CLASE AVIONETA("HEREDA LA LISTA DE AERONAVE")
        # NOTA: LAS SILLAS DE TIPO EJECUTIVA SE REPARTEN EN GRUPOS DE 4 EN FILA
        # SEPARADAS POR UN PASILLO.(POR TANTO NO HAY UBICACION CENTRAL)
        for numPosicion in range(0, Avioneta._NUM_SILLAS_EJECUTIVAS):
            if numPosicion % 4 == 0 or numPosicion % 4 == 3:
                ubicacion = Ubicacion.VENTANA
            else:
                ubicacion = Ubicacion.PASILLO

            self.getSILLASEJECUTIVAS().append(Silla(Clase.EJECUTIVA, numPosicion, ubicacion))

        # EL SIGUIENTE PROCESO CREA Y AGREGA SILLAS A LA LISTA DE SILLAS ECONOMICAS QUE
        # POSEE LA CLASE AVIONETA("HEREDA LA LISTA DE AERONAVE")
        # NOTA: LAS SILLAS DE TIPO ECONOMICA SE REPARTEN EN GRUPOS DE 6 EN FILA
        # SEPARADAS POR UN PASILLO.
        for numPosicion in range(0, Avioneta._NUM_SILLAS_ECONOMICAS):
            if numPosicion % 6 == 0 or numPosicion % 6 == 5:
                ubicacion = Ubicacion.VENTANA
            elif math.fmod(numPosicion, 6) == 1 or math.fmod(numPosicion, 6) == 4:
                ubicacion = Ubicacion.CENTRAL
            else:
                ubicacion = Ubicacion.PASILLO

            self.getSILLASECONOMICAS().append(Silla(Clase.ECONOMICA, numPosicion, ubicacion))

    @staticmethod
    def getNumSillasEconomicas():
        return Avioneta._NUM_SILLAS_ECONOMICAS

    @staticmethod
    def getNumSillasEjecutivas():
        return Avioneta._NUM_SILLAS_EJECUTIVAS

    #	
    #	 * Este método recorreran los arreglos de sillas ejecutivos y economicas de cada
    #	 * avión y avioneta
    #	 * para verificar la cantidad de sillas que estan ocupadas y retornaran dicha
    #	 * cantidad
    #	 
    def Calcular_Sillas_Ocupadas(self):
        cont = 0
        for i in self.getSILLASECONOMICAS():
            if i.isEstado():
                cont += 1
        for j in self.getSILLASEJECUTIVAS():
            if j.isEstado():
                cont += 1
        return cont

    #	
    #	 * Este método recibe un tipo de dato double de la distancia que hay desde el
    #	 * lugar de origen al lugar de destino
    #	 * y retornara el costo total de gasolina por recorrer el trayecto
    #	 

    def Calcular_Consumo_Gasolina(self, distancia_en_km):
        consumido = self.getGastoGasolina() * distancia_en_km
        return consumido
