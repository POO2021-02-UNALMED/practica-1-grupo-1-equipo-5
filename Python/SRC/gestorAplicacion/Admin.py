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
            
    # CASE 4 MAIN: MODIFICAR TIQUETE COMPRADO
    # NOS PERMITE MODIFICAR EL ALOJAMIENTO Y LA SILLA DE UN TIQUETE
    # PRIMERO SOLICITANDO UN ID DE TIQUETE Y VERIFICAR QUE SI EXISTE,
    # LUEGO CON UN SWITCH LE PRESENTADOS LAS 2 OPCIONES MODIFICAR ALOJAMIENTO O MODIFICAR SILLA
    # Y SEGUN LO QUE ESCOJA EJECUTAREMOS EL METODO modificarAlojamiento o modificarSilla
    @staticmethod
    def modificarTiquete():
        print("Ingrese el ID del tiquete que desea modificar.")
        ID = int(input())
        tiquete = Aerolinea.BuscarTiquete(ID)
        if tiquete is None:
            print("El ID ingresado no se encuentra\n")
        else:
            print("Que aspectos de su tiquete desea modificar?")
            print("1: Modificar alojamiento")
            print("2: Modificar Silla")

            opcion = int(input())


            if opcion == 1:
                dias = Admin.modificarAlojamiento(tiquete)
                if dias > 0:
                    tiquete.asignarPrecio(dias)
                    print(tiquete)
            elif opcion == 2:
                Admin.modificarSilla(tiquete)

    # METODOS DE MODIFICAR TIQUETE

    # ESTE METODO RECIBE UN TIQUETE AL CUAL SE LE VA A MODIFICAR EL ATRIBUTO SILLA:
    # LO HACE CAMBIANDO EL ATRIBUTO estaDisponible DE SU SILLA ACTUAL A true Y
    # ASIGNANDO OTRA SILLA HACIENDO USO DEL METODO elegirSilla	
    @staticmethod
    def modificarSilla(tiquete):

        print("A que tipo de silla desea cambiar?")
        silla = Admin.elegirSilla(tiquete.getVuelo())
        if silla is None:
            print("Lo sentimos no se encuentran sillas disponibles con esas caracteristicas\n")
            return
        tiquete.getSilla().setEstado(True)
        tiquete.setSilla(silla)

        print("*************************************")
        print("SU SILLA HA SIDO MODIFICADA CON EXITO")
        print("*************************************\n")
        tiquete.asignarPrecio()
        print(tiquete)


    # ESTE METODO RECIBE UN TIQUETE AL CUAL SE LE VA A MODIFICAR EL ATRIBUTO ALOJAMIENTO (DEBE DE TENER UNO YA ASIGANDO
    # EN CASO CONTRARIO NO LE PERMITITRA CONTINUAR Y LO REGRESARA AL MENU DE ADMINISTRADOR )
    # SI SI POSEE UN ALOJAMIENTO, EXTRAERA EL DESTINO DEL VUELO DEL TIQUETE E IMPRIMIRA UNA TABLA CON LOS ALOJAMIENTOS 
    # QUE POSEEN UNA LOCACION IGUAL A ESTE, LUEGO RECIBE EL NOMBRE DEL ALOJAMIENTO QUE DESEE Y BUSCARA UN ALOJAMIENTO
    # POR ESE NOMBRE Y EN ESA LOCACION EN CASO DE ENCONTRARLO SE LO ASIGNARA AL ATRIBUTO alojamiento DEL TIQUETE
    @staticmethod
    def modificarAlojamiento(tiquete_solicitado):
        if tiquete_solicitado.getAlojamiento() is None:
            print("Aun no tiene un alojamiento asociado a su tiquete, puede agregar uno en la opcion 3.")
            print()
            return 0
        destino = tiquete_solicitado.getVuelo().getDestino()
        Admin.mostrarAlojamientosPorUbicacion(destino)
        print("Por favor ingresa el nombre del alojamiento al que desea cambiar")
        alojamiento = input()
        alojamiento_solicitado = Alojamiento.buscarAlojamientoPorNombre(alojamiento)
        if alojamiento_solicitado is None:
            print("Lo sentimos, no tenemos un alojamiento con ese nombre\n")
            return -1
        elif not alojamiento_solicitado.getLocacion() is destino:
            print("Lo sentimos, no tenemos un alojamiento con ese nombre en esa locacion\n")
            return -1

        else:
            print("Por favor ingrese el numero de dias que se va a quedar en el alojamiento")
            dias = int(input())
            tiquete_solicitado.setAlojamiento(alojamiento_solicitado)
            print("Perfecto! su alojamiento ha sido modificado a " + alojamiento_solicitado.getNombre() + " exitosamente.")
            print()
            return dias

    # CASE 5 MAIN: OPCIONES DE ADMINISTRADOR 
    #	 EN ESTE MENU PARA EL ADMINISTRADOR VAN A INTERACTUAR TODAS LAS CLASES PARA PERMITIR
    #	 FUNCIONALIDADES ESPECIFICAS PARA CONTROLAR LOS VUELOS Y LOS ALOJAMIENTOS
    @staticmethod
    def opcionesAdministrador():

        opcion = None
        condition = True
        while condition:

            print("Que opcion desea realizar como administrador?")
            print("1. Listar Pasajeros.")
            print("2. Agregar Vuelo.")
            print("3. Cancelar vuelo.")
            print("4. Retirar un avion.")
            print("5. Agregar Alojamiento.")
            print("6. Eliminar Alojamiento.")
            print("7. Salir del administrador.")
            print("Por favor escoja una opcion: ")

            opcion = int(input())

            if opcion == 1:
                Admin.listarPasajeros()
            elif opcion == 2:
                Admin.agregarNuevoVuelo()
            elif opcion == 3:
                Admin.cancelarVuelos()
            elif opcion == 4:
                Admin.retirarAvion()
            elif opcion == 5:
                Admin.nuevoAlojamiento()
            elif opcion == 6:
                Admin.retirarAlojamiento()
            elif opcion == 7:
                Admin.salirDelAdministrador()

            condition = opcion != 7

    # METODOS DE LAS OPCIONES DE ADMINISTRADOR

    # CASE 1: LISTAR PASAJEROS DE UN VUELO

    #ESTE METODO NO RECIBRE PARAMETROS DE ENTRADAS Y RETORNO ES VACIO. SU OBJETIVO ES
    #MOSTRAR LAS LISTAS DE PASAJAEROS ASOCIADOS A UN VUELO. 
    #PARA ESTO ACCEDEMOS A TRAVES DEL ID DEL VUELO E INVOCAMOS EL METODO BUSCAR VUELO POR ID.
    #AL FINAL NOS MOSTRARA SI EL VUELO TIENE PASAJEROS ASOCIADOS O NO, Y LA INFORMACION ASOCIADA
    #AL ID DEL TIQUETE DEL PASAJAERO, SU NOMBRE, SU PASARTE Y SU EMAIL. 

    @staticmethod
    def listarPasajeros():
        aerolineas = Aerolinea.getAerolineas()
        Admin.mostrarTablaDeVuelosPorAerolineas(aerolineas)

        print("Ingrese el ID del vuelo: ")
        IDBusqueda = int(input())

        tiquetes = []
        vuelo = None
        for i in aerolineas:
            if i.buscarVueloPorID(i.getVuelos(), IDBusqueda) is not None:
                vuelo = i.buscarVueloPorID(i.getVuelos(), IDBusqueda)
                break
        if vuelo is None:
            print("No tenemos vuelos con ese ID.\n")
            return
        tiquetes = vuelo.getTiquetes()
        print("LISTA DE PASAJEROS PARA EL VUELO " + str(IDBusqueda))

        if len(tiquetes) == 0:
            print("El vuelo aun no tiene pasajeros asociados \n")
        else:
            Admin.mostrarTablaDePasajeros(tiquetes)

    # CASE 2: AGREGAR NUEVO VUELO A UNA AEROLINEA
    #	 ESTE METODO NO RECIBE PARAMETROS DE ENTRADA PORQUE SE LE PIDE AL USUARIO ADMINISTRADOR INGREGAR 
    #	   POR CONSOLA LOS DATOS NECESARIOS PARA AGREGAR UN NUEVO VUELO A UN AEROLINEA.
    #	   PARA ESTO SE HARA UNA VERFICACION DE LA EXISTENCIA DE LA AEROLINEA Y POSTERIOEMENTE SE RECIBIRAN LOS
    #	   PARAMETROS NECESARIOS PARA INSTANCIAR UN VUELO Y AREGARLO AL ARREGLO DE VUELOS QUE LA AEROLINEA
    @staticmethod
    def agregarNuevoVuelo():
        aerolineas = Aerolinea.getAerolineas()
        print("AGREGAR NUEVO VUELO \n")
        Admin.mostrarTablaDeAerolineas(aerolineas)
        print("Ingrese el nombre de la aerolinea para agregar vuelo\n")
        nombreAerolinea = input()

        existe = False
        for i in aerolineas:
            if  i.getNombre().lower() == nombreAerolinea.lower():
                existe = True

        while existe == False:
            print("\nESA AEROLINEA NO EXISTE")
            print("Ingrese un nombre del listado anterior\n")
            nombreAerolinean = input()
            existe = nombreAerolinean in list
        print()

        print("Ingrese el ID del nuevo vuelo (3 cifras):")
        iD = int(input())
        aerolinea_busqueda = Aerolinea.buscarAerolineaPorNombre(nombreAerolinea)
        while len(str(iD)) != 3:
            print("Por favor ingrese un ID de 3 cifras.")
            iD = int(input())
        while aerolinea_busqueda.buscarVueloPorID(aerolinea_busqueda.getVuelos(), iD) is not None:
            print("El ID que ingreso ya esta en uso, por favor ingrese uno distinto.")
            iD = int(input())

        print("\nIngrese el precio:")
        precio = int(input())