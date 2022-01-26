# CLASE ADMIN PARA LA INTERACCION DEL USUARIO CON EL SISTEMA
import random
import pickle
from ssl import ALERT_DESCRIPTION_ACCESS_DENIED

from gestorAplicacion.alojamiento.Alojamiento import Alojamiento
from gestorAplicacion.adminVuelos.Aerolinea import Aerolinea
from gestorAplicacion.adminVuelos.Pasajero import Pasajero 
from gestorAplicacion.adminVuelos.Tiquete import Tiquete
from gestorAplicacion.adminVuelos.Vuelo import Vuelo
from gestorAplicacion.hangar.Aeronave import Aeronave
from gestorAplicacion.hangar.Avion import Avion
from gestorAplicacion.hangar.Avioneta import Avioneta
from gestorAplicacion.hangar.Silla import Silla
from gestorAplicacion.hangar.Ubicacion import Ubicacion


class Admin(object):

    @staticmethod
    def main():
        
        picklefile = open('Aerolineas','rb')
        picklefile2 = open('Alojamientos','rb')
        Aerolinea.setAerolineas(pickle.load(picklefile))
        Alojamiento.setAlojamientos(pickle.load(picklefile2))
        picklefile.close()
        picklefile2.close()
        
        #MENU PRINCIPAL
        opcion = None
        condition = True
        while condition:
            print("---- SISTEMA DE RESERVAS DE VUELO ----")
            print("Que operacion desea realizar?")
            print("1. Ver todos los vuelos disponibles por Aerolinea")
            print("2. Comprar tiquete para un vuelo por destino y fecha")
            print("3. Agregar alojamiento en el destino del vuelo")
            print("4. Modificar tiquete comprado")
            print("5. Ver opciones de administrador")
            print("6. Terminar")
            print("Por favor escoja una opcion: ")
            opcion = int(input())

            if opcion == 1:
                pass
                Admin.mostrarVuelosPorAerolineas()
            elif opcion == 2:
                Admin.generarTiquete()
            elif opcion == 3:
                Admin.agregarAlojamiento()
            elif opcion == 4:
                Admin.modificarTiquete()
            elif opcion == 5:
                Admin.opcionesAdministrador()
            elif opcion == 6:
                Admin.salirDelSistema()

            condition = opcion != 6

    # CASE 1 MAIN: VER TODOS LOS VUELOS DISPONIBLES POR AEROLINEAS

    # MUESTRA UNA TABLA POR CADA AEROLINEA CON LOS VUELOS QUE SE TIENEN
    # DISPONIBLES, HACIENDO USO DEL generadorDeTablas.
    @staticmethod
    def mostrarVuelosPorAerolineas():
        aerolineasDisponibles = Aerolinea.getAerolineas()
        Admin.mostrarTablaDeVuelosDisponiblesPorAerolineas(aerolineasDisponibles)
        
    # CASE 2 MAIN: GENERAR TIQUETE DE COMPRA DE VUELO
    # EL METODO PERMITE GENERAR UN TIQUETE DE COMPRA DE UN VUELO AL BUSCAR POR DESTINO O POR DESTINO Y FECHA
    # LUEGO DE ELEGIR UN VUELO SE TOMAN LOS DATOS DEL PASAJERO Y SE ELIGE UNA SILLA EN LA AERONAVE
    # AL FINAL SE IMPRIME UN RESUMEN DE LA COMPRA
    @staticmethod
    def generarTiquete():
        print("Quieres buscar un vuelo por:")
        print("1. Destino")
        print("2. Destino y fecha")
        print("3. Regresar")
        opcion = int(input())
        while opcion != 1 and opcion != 2 and opcion != 3:
            print("Por favor ingresa una opcion valida")
            opcion = int(input())

        if opcion == 1:
            print("Por favor ingrese un destino:")
            destino_1 = input()
            hayVuelos = Admin.consultarVuelosPorDestino(destino_1)
            if not hayVuelos:
                return
        elif opcion == 2:
            print("Por favor ingrese un destino")
            destino_2 = input()
            print("Por favor ingrese una fecha (dd-mm-aaaa):")
            fecha_2 = input()
            hayVuelos = Admin.consultarVuelosPorDestinoYFecha(destino_2, fecha_2)
            if not hayVuelos:
                return
        else:
            return

        print("Por favor ingrese el nombre de la aerolinea con la que desea viajar")
        nombre_aerolinea = input()
        aerolinea = Aerolinea.buscarAerolineaPorNombre(nombre_aerolinea)

        while aerolinea is None:
            print("Por favor ingrese un nombre valido")
            nombre_aerolinea = input()
            aerolinea = Aerolinea.buscarAerolineaPorNombre(nombre_aerolinea)

        print("Por favor ingrese el ID del vuelo que desea comprar")
        ID = int(input())
        vuelo = aerolinea.buscarVueloPorID(aerolinea.getVuelos(), ID)
        while vuelo is None:
            print("Por favor ingrese un ID valido")
            ID = int(input())
            vuelo = aerolinea.buscarVueloPorID(aerolinea.getVuelos(), ID)

        ID_tiquete = 100 + random.random() * 900 # DEVUELVE UN NUMERO ALEATORIO DE 3 CIFRAS
        while Aerolinea.BuscarTiquete(int(ID_tiquete)) is not None:
            ID_tiquete = 100 + random.random() * 900

        # SECUENCIA DE PASOS PARA ELEGIR UNA SILLA
        print("Que tipo de silla desea comprar?")
        silla = Admin.elegirSilla(vuelo)
        if silla is None:
            print("Lo sentimos no se encuentran sillas disponibles con esas caracteristicas\n")
            return
        tiquete = Tiquete(int(ID_tiquete), vuelo.getPrecio(), vuelo)
        tiquete.setSilla(silla)

        # TOMAR DATOS DEL PASAJERO
        print("DATOS DEL PASAJERO:")
        print("Ingrese el nombre:")
        nombre = input()
        print("Ingrese su edad:")
        edad = int(input())
        print("Ingrese el numero de su pasaporte:")
        pasaporte = input()
        print("Ingrese un e-mail")
        correo = input()

        #SE CREA EL OBJETO PASAJERO Y SE LE ASIGNA AL TIQUETE GENERADO EN EL METODO
        pasajero = Pasajero(pasaporte, nombre, tiquete, edad, correo)
        tiquete.setPasajero(pasajero)

        # IMPRIME RESUMEN DE LA COMPRA
        tiquete.asignarPrecio()
        print(tiquete)

    # CASE 3 MAIN: AGREGAR ALOJAMIENTO EN EL DESTINO DEL VUELO COMPRADO

    # EL METODO PERMITE AGREGAR UN ALOJAMIENTO A UN TIQUETE COMPRADO PREVIAMENTE, VERIFICANDO QUE NO SE TENGA UN ALOJAMIENTO COMPRADO
    # NI SE QUIERA AGREGAR UN ALOJAMIENTO EN UNA LOCACION DISTINTA A LA DEL DESTINO ASOCIADO AL TIQUETE.
    # AL INGRESAR EL NOMBRE DEL ALOJAMIENTO QUE SE DESEA AGREGAR SE SOLICITA EL NUMERO DE DIAS QUE SE QUIERE QUEDAR
    # PARA RECALCULAR EL PRECIO DEL TIQUETE, Y AL FINAL MOSTRAR EL RESUMEN DE LA COMPRA
    @staticmethod
    def agregarAlojamiento():
        print("Deseas agregar un alojamiento a tu compra?")
        print("Por favor ingresa el ID del tiquete que se genero al comprar su vuelo:")
        tiqueteID = int(input())
        tiquete_solicitado = Aerolinea.BuscarTiquete(tiqueteID)

        if tiquete_solicitado is None:
            print("Lo sentimos, no tenemos un tiquete identificado con ese ID")
            print()
        elif tiquete_solicitado.getAlojamiento() is not None:
            print("El tiquete ya posee un alojamiento, si quiere cambiarlo hagalo desde la opcion 4.\n")
            return
        else:
            destino = tiquete_solicitado.getVuelo().getDestino()
            hayAlojamientos = Admin.mostrarAlojamientosPorUbicacion(destino) #ESTE METODO SE DETALLA MAS ABAJO
            if not hayAlojamientos:
                return
            print("Por favor ingresa el nombre del alojamiento que desea anadir a su compra:")
            alojamiento = input()
            alojamiento_solicitado = Alojamiento.buscarAlojamientoPorNombre(alojamiento)
            if alojamiento_solicitado is None:
                print("Lo sentimos, no tenemos un alojamiento con ese nombre")
                print()
            elif not alojamiento_solicitado.getLocacion() is destino:
                print("Lo sentimos, no tenemos un alojamiento con ese nombre en esa locacion\n")
                return
            else:
                print("Cuantos dias desea quedarse en el alojamiento?")
                num_dias = int(input())
                tiquete_solicitado.setAlojamiento(alojamiento_solicitado)
                tiquete_solicitado.asignarPrecio(num_dias)

                print("Perfecto! el alojamiento " + alojamiento_solicitado.getNombre() + " se ha agregado correctamente a su tiquete de compra.")
                print()
                print(tiquete_solicitado)
            