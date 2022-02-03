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

