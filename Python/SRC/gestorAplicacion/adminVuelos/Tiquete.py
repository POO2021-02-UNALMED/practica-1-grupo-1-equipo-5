from tkinter.messagebox import NO
from gestorAplicacion.hangar.Aeronave import Aeronave
from gestorAplicacion.hangar.Avion import Avion
from gestorAplicacion.hangar.Avioneta import Avioneta
from gestorAplicacion.hangar.Clase import Clase
from gestorAplicacion.hangar.Silla import Silla
from gestorAplicacion.hangar.Ubicacion import Ubicacion
from gestorAplicacion.alojamiento.Alojamiento import Alojamiento

class Tiquete:


    #CONSTRUCTOR
    def __init__(self, id, precio, vuelo):
        self._id = id
        self._precio = precio
        self._vuelo = vuelo
        self._silla = None
        self._pasajero = None
        self._alojamiento = None
        vuelo.getTiquetes().append(self)

    # METODOS

    #	Este metodo no tiene parametros de entra o de salida porque el valor resultante
    #	  es guardado en el atributo precio de cada instancia
    def asignarPrecio(self,*args):
        hayDescuento = False
        precio_total =self._vuelo.getPrecio() + self.getSilla().getClase().value
        if self._pasajero.getEdad()<5:
            hayDescuento = True
            self._precio = int((precio_total - (precio_total*0.25)))
        elif self._pasajero.getEdad()>5 and self._pasajero.getEdad()<=10:
            self._precio = int((precio_total - (precio_total*0.15)))
            hayDescuento = True
        else:
            self._precio = precio_total

        if len(args) != 0 :

            self._precio += self._alojamiento.calcularPrecio(args[0]) 

        return hayDescuento



    def confimarCompra(self):
        self._vuelo.getTiquetes().append(self)

    def __str__(self):
        if self._alojamiento is None:
            return "*************************************\n"+ "      Su compra ha sido exitosa\n"+ "    Gracias por confiar en nostros\n"+ "*************************************\n"+ "------------------------------------\n"+ "      Tiquete No."+ str(self._id) + "\n"+ "------------------------------------\n"+ "Nombre Pasajero: " + self._pasajero.nombre + "\n" + "Fecha: " + self._vuelo.getFecha_de_salida() + "\n" + "Vuelo: " + str(self._vuelo.getID()) + "\n" + "Num Silla: " + str(self._silla.getNumero_de_silla()) + " " + self._silla.getUbicacion().value + "\n" + "Origen: " + self._vuelo.getOrigen() + "\n" + "Destino: " + self._vuelo.getDestino() + "\n" + "Precio Total: " + str(self.getPrecio()) + "\n" + "------------------------------------\n"


        else:

            return "*************************************\n"+ "      Su compra ha sido exitosa\n"+ "    Gracias por confiar en nostros\n"+ "*************************************\n"+ "------------------------------------\n"+ "      Tiquete No."+ str(self._id) + "\n"+ "------------------------------------\n"+ "Nombre Pasajero: " + self._pasajero.nombre + "\n" + "Fecha: " + self._vuelo.getFecha_de_salida() + "\n" + "Vuelo: " +str(self._vuelo.getID()) + "\n" + "Silla: " + str(self._silla.getNumero_de_silla()) + " - " + self._silla.getUbicacion().value + "\n" + "Origen: " + self._vuelo.getOrigen() + "\n" + "Destino: " + self._vuelo.getDestino() + "\n" + "Alojamiento: " + self._alojamiento.getNombre() + "\n" + "Precio Total: " + str(self.getPrecio()) + "\n" + "------------------------------------\n"


    #GETTERS Y SETTERS

    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id

    def getPrecio(self):
        return self._precio

    def setPrecio(self, precio):
        self._precio = precio

    def getVuelo(self):
        return self._vuelo

    def setVuelo(self, vuelo):
        self._vuelo = vuelo

    def getSilla(self):
        return self._silla

    def setSilla(self, silla):
        self._silla = silla
        silla.setEstado(False)

    def getPasajero(self):
        return self._pasajero

    def setPasajero(self, pasajero):
        self._pasajero = pasajero

    def getAlojamiento(self):
        return self._alojamiento
        
    def setAlojamiento(self, alojamiento):
        self._alojamiento = alojamiento
