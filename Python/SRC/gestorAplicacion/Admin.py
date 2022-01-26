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
        print("Ingrese el origen:")
        origen = input()
        print()

        print("Ingrese el destino:")
        destino = input()
        print()

        print("Ingrese la distancia (KM):")
        distancia = int(input())
        print()

        print("Ingrese fecha de salida (DD-MM-AAAA):")
        fechaSalida = input()
        print()

        print("Ingrese hora de salida (24:00):")
        horaSalida = input()
        print()

        print("Que tipo de aeronave es?")
        print("Ingrese 1 para avion" + "\n" + "Ingrese 2 para avioneta")
        aeronave = int(input())

        while aeronave != 1 and aeronave != 2:
            print("Por favor ingrese una opcion valida")
            aeronave = int(input())

        if aeronave == 1:
            print("Ingrese el nombre del avion:")
            nombreAvion = input()
            print()

            avion = Avion(nombreAvion, Aerolinea.buscarAerolineaPorNombre(nombreAerolinea))
            vuelo = Vuelo(iD, precio, origen, destino, avion, distancia, fechaSalida, horaSalida)
            print("***************************************")
            print("SU VUELO SE HA REGISTRADO CORRECTAMENTE")
            print("***************************************\n")

        elif aeronave == 2:
            print("INGRESE EL NOMBRE DE LA AVIONETA:")
            nombreAvioneta = input()
            print()
            avioneta = Avioneta(nombreAvioneta, Aerolinea.buscarAerolineaPorNombre(nombreAerolinea))
            vuelo = Vuelo(iD, precio, origen, destino, avioneta, distancia, fechaSalida, horaSalida)
            print("***************************************")
            print("SU VUELO SE HA REGISTRADO CORRECTAMENTE")
            print("***************************************\n")

    # CASE 3: CANCELAR VUELO DE UNA AEROLINEA
    #	 ESTE METODO NO RECIBE PARAMETRO DE ENTRADA Y OFRECE LA FUNCIONALIDAD DE CANCELAR VUELOS ASOCIADOS A UNA AEROLINEA
    #	   SE INVOCAR A LOS METODOS BUSCAR VUELO POR ID Y CANCELAR VUELOS QUE ESTAN IMPLEMENTADO EN AEROLINEA
    #
    @staticmethod
    def cancelarVuelos():
        print("Estos son los vuelos que tenemos:\n")
        aerolineas = Aerolinea.getAerolineas()
        Admin.mostrarTablaDeVuelosPorAerolineas(aerolineas)
        print("Ingrese el ID del vuelo a eliminar:")
        id = int(input())

        for aerolinea in aerolineas:
            i = 0
            while i < len(aerolinea.getVuelos()):
                if aerolinea.buscarVueloPorID(aerolinea.getVuelos(), id) is not None:
                    aerolinea.cancelarVuelo(id)
                    print("El vuelo se ha eliminado correctamente.")
                    return
                i += 1
        print("No tenemos un vuelo identificado con ese ID \n")

    # CASE 4: RETIRAR AERONAVE
    # SI ENCUENTRA EL NOMBRE DEL AVION QUE SE DESEA RETIRAR, LO MARCA COMO DESCOMPUESTO Y CANCELA EL VUELO QUE TENIA ASOCIADO ESTA AERONAVE
    @staticmethod
    def retirarAvion():
        aeronave_encontrada = False
        print("Ingrese el nombre de la Aeronave que se desea retirar:")
        nombre_aeronave = input()
        aerolineasDisponibles = Aerolinea.getAerolineas()
        i = 0
        while i < len(aerolineasDisponibles):
            aerolinea = aerolineasDisponibles[i]

            vuelo = aerolinea.buscarVueloPorAeronave(aerolinea.getVuelos(), nombre_aeronave)
            if vuelo != None:
                vuelo.getAeronave().setDescompuesto(True)
                aerolinea.cancelarVuelo(vuelo.getID())
                print("Se ha retirado la aeronave descompuesta y el vuelo asociado a este.")
                print()
                aeronave_encontrada = True
                break
            i += 1
        if not aeronave_encontrada:
            print("Lo sentimos, no encontramos una aeronave asociada al nombre que ingreso.")
            print()

    #CASE 5: AGREGAR ALOJAMIENTO
    # PERMITE AGREGAR UN ALOJAMIENTO A LA LISTA DE ALOJAMIENTOS DISPONIBLES, ESTO DESDE SU CONSTRUCTOR
    @staticmethod
    def nuevoAlojamiento():
        print("Ingrese el nombre del alojamiento que desea agregar a nuestra lista:")
        nombre = input()
        print()

        print("Ingrese la locacion:")
        locacion = input()
        print()

        print("Ingrese el precio por dia:")
        precio = int(input())
        print()

        print("Ingrese el numero de estrellas (1-5):")
        estrellas = int(input())
        print()

        nuevoAlojamiento = Alojamiento(nombre, locacion, precio, estrellas)
        print("Perfecto! El alojamiento " + nuevoAlojamiento.getNombre() + " se ha agregado a nuestra lista.")

    #CASE 7: RETIRAR ALOJAMIENTO
    # MUESTRA LOS ALOJAMIENTOS QUE SE TIENEN DISPONIBLES HACIENDO USO DEL generadorDeTablas, PARA POSTERIORMENTE PREGUNTAR POR EL NOMBRE DEL
    # ALOJAMIENTO QUE SE DESEA RETIRAR DE LA LISTA Y ELIMINARLO DE LA LISTA DE ALOJAMIENTOS.
    @staticmethod
    def retirarAlojamiento():
        print("Estos son los alojamientos que tenemos asociados:")
        Admin.mostrarTablaDeAlojamientos(Alojamiento.getAlojamientos())

        print("Ingrese el nombre del alojamiento que desea retirar de nuestra lista:")
        nombre = input()

        if Alojamiento.buscarAlojamientoPorNombre(nombre) != None:
            i = 0
            while i < len(Alojamiento.getAlojamientos()):
                if Alojamiento.getAlojamientos()[i].getNombre().lower() == nombre.lower():
                    Alojamiento.getAlojamientos().pop(i)
                    print("El alojamiento " + nombre + " se ha eliminado correctamente.")
                    print()
                i += 1
        else:
            print("Lo sentimos, no tenemos un alojamiento con este nombre.")
            print()

    # CASE 9: SALIR DEL ADMINISTRADOR
    @staticmethod
    def salirDelAdministrador():
        print("Gracias por usar nuestras opciones de administrador! \n")

    #	CASE 6 MAIN: FINALIZAR SISTEMA DE ADMINISTRACION DE VUELOS
    @staticmethod
    def salirDelSistema():
        print("Gracias por usar nuestro servicio!")

        picklefile = open('Aerolineas', 'wb')
        picklefile2 = open('Alojamientos','wb')
        pickle.dump(Aerolinea._aerolineas, picklefile)
        pickle.dump(Alojamiento._alojamientos,picklefile2)
        picklefile.close()
        picklefile2.close()

# METODOS AUXILIARES

    # OPCION 1: CONSULTAR VUELO POR DESTINO

    # ESTE METODO RECIBE COMO PARAMETRO UN DESTINO (STRING) Y RECORRE CADA AEROLINEA EJECUTANDO EL METODO DE AEROLINEA buscarVueloPorDestino()
    # PARA ALMACENAR ESTOS VUELOS EN UNA LISTA Y MOSTRARLOS POR PANTALLA CON generadorDeTablas.mostrarTablaDeVuelos(). SI ENCONTRO AL MENOS
    # UN VUELO EN ALGUNA AEROLINEA QUE TUVIERA ASOCIADO ESTE DESTINO RETORNA LA VARIABLE boolean HAYVUELOS CON EL VALOR true, DE LO CONTRARIO RETORNA false.
    @staticmethod
    def consultarVuelosPorDestino(destino):
        print("Estos son los vuelos disponibles hacia " + destino + " por nuestras aerolineas:")
        print()
        hayVuelos = False

        aerolineasDisponibles = Aerolinea.getAerolineas()
        i = 0
        while i < len(aerolineasDisponibles):
            aerolinea = aerolineasDisponibles[i]
            vuelosPorDestino = aerolinea.buscarVueloPorDestino(aerolinea.vuelosDisponibles(aerolinea.getVuelos()), destino)
            if len(vuelosPorDestino) != 0:
                Admin.mostrarTablaDeVuelos(aerolinea, vuelosPorDestino)
                hayVuelos = True
            i += 1
        if hayVuelos == False:
            print("Lo sentimos, no tenemos vuelos disponibles para ese destino")
            print()
        return hayVuelos

    # OPCION 2: CONSULTAR VUELO POR DESTINO Y FECHA

    # ESTE METODO RECIBE COMO PARAMETRO UN DESTINO (STRING) Y UNA FECHA (STRING) Y RECORRE CADA AEROLINEA EJECUTANDO EL METODO DE AEROLINEA
    # buscarVueloPorDestino() SI LOS ENCUENTRA, EJECUTA EL METODO DE AEROLINEA buscarVueloPorFecha() PARA ALMACENAR ESTOS VUELOS EN UNA LISTA
    # Y MOSTRARLOS POR PANTALLA CON generadorDeTablas.mostrarTablaDeVuelos(). SI ENCONTRO AL MENOS UN VUELO EN ALGUNA AEROLINEA QUE TUVIERA
    # ASOCIADO ESE DESTINO Y ESA FECHA, RETORNA LA VARIABLE boolean HAYVUELOS CON EL VALOR true, DE LO CONTRARIO RETORNA false.
    @staticmethod
    def consultarVuelosPorDestinoYFecha(destino, fecha):
        print()
        print("Estos son los vuelos disponibles hacia " + destino + " en la fecha " + fecha + " por nuestras aerolineas:")
        print()
        hayVuelos = False

        aerolineasDisponibles = Aerolinea.getAerolineas()
        i = 0
        while i < len(aerolineasDisponibles):
            aerolinea = aerolineasDisponibles[i]
            vuelosPorDestino = aerolinea.buscarVueloPorDestino(aerolinea.vuelosDisponibles(aerolinea.getVuelos()), destino)
            if len(vuelosPorDestino) != 0:
                vuelosPorFecha = aerolinea.buscarVueloPorFecha(vuelosPorDestino, fecha)
                if len(vuelosPorFecha) != 0:
                    Admin.mostrarTablaDeVuelos(aerolinea, vuelosPorFecha)
                    hayVuelos = True
            i += 1
        if hayVuelos == False:
            print("Lo sentimos, no tenemos vuelos disponibles para ese destino y fecha especificos")
            print()
        return hayVuelos

    # METODOS AUXILIARES - TABLA ALOJAMIENTOS

    # ESTE METODO RECIBE COMO PARAMETRO UNA UBICACION (STRING) Y SE ENCARGA DE BUSCAR LOS ALOJAMIENTOS QUE TIENEN ASOCIADA ESTA UBICACION
    # PARA POSTERIORMENTE MOSTRARLOS EN UNA TABLA POR PANTALLA CON generadorDeTablas.mostrarTablaDeAlojamientos(). SI ENCONTRO AL MENOS UN
    # ALOJAMIENTO QUE TUVIERA ESA UBICACION, RETORNA LA VARIABLE boolean HAYVUELOS CON EL VALOR true, DE LO CONTRARIO RETORNA false.
    @staticmethod
    def mostrarAlojamientosPorUbicacion(ubicacion):
        print("Estos son los alojamientos disponibles en " + ubicacion + ":")
        hayAlojamientos = False
        alojamientosDisponibles = Alojamiento.buscarAlojamientoPorUbicacion(ubicacion)
        if len(alojamientosDisponibles) != 0:
            hayAlojamientos = True
            Admin.mostrarTablaDeAlojamientos(alojamientosDisponibles)
        else:
            print("Lo sentimos, no tenemos alojamientos disponibles para ese destino")
            print()
        return hayAlojamientos

    #METODOS AUXILIARES - ELEGIR SILLA

    #ESTE METODO RECIBE UN TIQUETE Y UN VUELO, ESTE ULTIMO LO UTILIZARA PARA ACCEDER A LAS SILLAS DEL AVION QUE REALIZARA EL VUELO.
    #LUEGO SOLICITA QUE TIPO DE SILLA Y UBICACION PREFIERE, VALORES LOS CUALES USARA PARA BUSCAR  DENTRO DEL AVION SI SE ENCUENTRA UNA SILLA DISPONIBLE
    #CON ESAS CARACTERISTICAS	Y ASIGANARLA AL ATRIBUTO SILLA DE TIQUETE.
    @staticmethod
    def elegirSilla(vuelo):
        print("1: Ejecutiva")
        print("2: Economica")

        nombre_clase = int(input())
        num_ubicacion = None
        clase = None
        while nombre_clase != 1 and nombre_clase!=2:
            print("Porfavor ingrese una opcion valida")
            nombre_clase = input()

        print("Cual de las siguientes ubicaciones prefiere?")
        print("1: Pasillo")
        print("2: Ventana")

        if nombre_clase == 2:
            clase = "ECONOMICA"
            print("3: Central")
            num_ubicacion = int(input())
            while num_ubicacion!=1 and num_ubicacion!=2 and num_ubicacion!=3:
                print("Porfavor ingrese una opcion valida")
                num_ubicacion = int(input())
        else:
            clase = "EJECUTIVA"
            num_ubicacion = int(input())
            while num_ubicacion!=1 and num_ubicacion!=2:
                print("Porfavor ingrese una opcion valida")
                num_ubicacion = int(input())

        ubicacion = None
        if num_ubicacion == 1:
            ubicacion = Ubicacion.PASILLO
        elif num_ubicacion == 2:
            ubicacion = Ubicacion.VENTANA
        else:
            ubicacion = Ubicacion.CENTRAL

        return vuelo.getAeronave().buscarSillaPorUbicacionyTipo(ubicacion,clase)

    @staticmethod
    def mostrarTablaDePasajeros(tiquetes):
        print("---------------------------------------------------------------")
        print("{0:>5} {1:>12} {2:>16} {3:>17}".format("ID", "NOMBRE", "PASAPORTE", "EMAIL"+"\n"), end = '')
        print("---------------------------------------------------------------")

        i = 0
        while i < len(tiquetes):
            print("{0:>5} {1:>13} {2:>12} {3:>26}".format(str(tiquetes[i].getId()), tiquetes[i].getPasajero().nombre, tiquetes[i].getPasajero().getPasaporte(), tiquetes[i].getPasajero().getEmail()), end = '')
            print()
            i += 1
        print("---------------------------------------------------------------")
        print()

    @staticmethod
    def mostrarTablaDeAlojamientos( alojamientos):
        print()
        print("-------------------------------------------------------------")
        print("{0:>10} {1:>15} {2:>18} {3:>12}".format("NOMBRE", "LOCACION", "PRECIO POR DIA", "ESTRELLAS"), end = '')
        print()
        print("-------------------------------------------------------------")

        j = 0
        while j < len(alojamientos):
            print("{0:>13} {1:>11} {2:>16} {3:>11}".format(alojamientos[j].getNombre(), alojamientos[j].getLocacion(), alojamientos[j].getPrecio_dia(), alojamientos[j].getEstrellas()), end = '')
            print()
            j += 1

        print("-------------------------------------------------------------")
        print()

    @staticmethod
    def mostrarTablaDeAerolineas(aerolineas):
        print("AEROLINEAS DISPONIBLES")
        print("----------------------")

        for aerolinea in aerolineas:
            print("{0:>14}".format(aerolinea.getNombre()), end = '')
            print()
        print("----------------------")

    #RECIBE UNA LISTA DE AEROLINEAS E IMPRIME POR PANTALLA LOS VUELOS DISPONIBLES (QUE NO ESTEN COMPLETOS) DE CADA AEROLINEA HACIENDO
    #USO DE LOS METODOS printEncabezadoAerolinea(), printVuelos() Y printSeparador().
    @staticmethod
    def mostrarTablaDeVuelosDisponiblesPorAerolineas(aerolineas):
        i = 0
        while i < len(aerolineas):
            aerolinea = aerolineas[i]
            Admin.printEncabezadoAerolinea(aerolineas[i])
            Admin.printVuelos(aerolinea.vuelosDisponibles(aerolinea.getVuelos()))
            Admin.printSeparador()
            i += 1

    #RECIBE UNA LISTA DE AEROLINEAS E IMPRIME POR PANTALLA TODOS LOS VUELOS DE CADA AEROLINEA HACIENDO
    #USO DE LOS METODOS printEncabezadoAerolinea(), printVuelos() Y printSeparador()
    @staticmethod
    def mostrarTablaDeVuelosPorAerolineas( aerolineas):
        i = 0
        while i < len(aerolineas):
            aerolinea = aerolineas[i]
            Admin.printEncabezadoAerolinea(aerolineas[i])
            Admin.printVuelos(aerolinea.getVuelos())
            Admin.printSeparador()
            i += 1

    #RECIBE UNA AEROLINEA Y SUS VUELOS, E IMPRIME POR PANTALLA ESTOS VUELOS HACIENDO
    #USO DE LOS METODOS printEncabezadoAerolinea(), printVuelos() Y printSeparador()
    @staticmethod
    def mostrarTablaDeVuelos( aerolinea, vuelos):
        if len(vuelos) != 0:
            Admin.printEncabezadoAerolinea(aerolinea)
            Admin.printVuelos(vuelos)
            Admin.printSeparador()



    #IMPRIME POR PANTALLA UN ENCABEZADO CON EL NOMBRE DE LA AEROLINEA Y LOS ATRIBUTOS DE LOS VUELOS QUE POSEE LA AEROLINEA.
    @staticmethod
    def printEncabezadoAerolinea(aerolinea):
        print("VUELOS DISPONIBLES DE LA AEROLINEA " + aerolinea.getNombre().upper())
        print("--------------------------------------------------------------------------------------------------")
        print("{0:>4} {1:>13} {2:>12} {3:>14} {4:>12} {5:>22} {6:>12}".format("ID", "PRECIO", "ORIGEN", "DESTINO", "FECHA", "HORA DE SALIDA", "AERONAVE"), end = '')
        print()
        print("--------------------------------------------------------------------------------------------------")

    # System.out.printf() PERMITE DARLE UN FORMATO A LOS DATOS DE SALIDA
    # % INDICA QUE EN ESA POSICION SE VA A ESCRIBIR UN VALOR, SE PUEDEN PONER TANTOS COMO VARIABLES A MOSTRAR
    # ESTAS VARIABLES SE ESCRIBEN A CONTINUACION DE LAS COMMILLAS Y SEPARADAS POR COMAS
    # LA s INDICA QUE SE VA A MOSTRAR UNA CADENA DE CARACTERES, Y EL VALOR NUMERICO INDICA LA ALINEACION A LA DERECHA.

    # SE ENCARGA DE RECORRER LOS VUELOS DE UNA AEROLINEA PARA IR IMPRIMIENDO, LINEA POR LINEA, LA INFORMACION PERTINENTE DE CADA UNO.
    @staticmethod
    def printVuelos(vuelos):
        j = 0
        while j < len(vuelos):
            print("{0:>5} {1:>12} {2:>13} {3:>13} {4:>15} {5:>11} {6:>21}".format(vuelos[j].getID(), vuelos[j].getPrecio(), vuelos[j].getOrigen(), vuelos[j].getDestino(), vuelos[j].getFecha_de_salida(), vuelos[j].getHora_de_salida(), vuelos[j].getAeronave().getNombre()), end = '')
            print()
            j += 1

    #IMPRIME POR PANTALLA UN SEPARADOR PARA LA TABLA DE VUELOS
    @staticmethod
    def printSeparador():
        print("--------------------------------------------------------------------------------------------------")
        print()

if __name__ == "__main__":
    Admin.main()

