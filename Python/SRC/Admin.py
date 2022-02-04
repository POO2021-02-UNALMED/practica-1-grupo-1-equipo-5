# CLASE ADMIN PARA LA INTERACCION DEL USUARIO CON EL SISTEMA
import random
import pickle
from tkinter import *
from excepciones.ErrorAsignacion import ExcepcionAgregarAlojamiento, ExcepcionIdTiquete, ExcepcionIdVuelo, ExcepcionModificarAlojamiento
from excepciones.ErrorAplicacion import ErrorAplicacion
from excepciones.ErrorFormato import ExcepcionEnteroFloat, ExcepcionEnteroString

from gestorAplicacion.hangar.Clase import Clase
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

    # DESERIALIZACION DE DATOS
    picklefile = open('./baseDeDatos/Aerolineas','rb')
    picklefile2 = open('./baseDeDatos/Alojamientos','rb')
    Aerolinea.setAerolineas(pickle.load(picklefile))
    Alojamiento.setAlojamientos(pickle.load(picklefile2))
    picklefile.close()
    picklefile2.close()
    
    #--------------------------------------------------------------------------------------------------------------------------------------
    # MUESTRA UNA TABLA POR CADA AEROLINEA CON LOS VUELOS QUE SE TIENEN DISPONIBLES
    @staticmethod
    def mostrarVuelosPorAerolineas(frame_operaciones):
        aerolineasDisponibles = Aerolinea.getAerolineas()
        return Admin.mostrarTablaDeVuelosDisponiblesPorAerolineas(aerolineasDisponibles,frame_operaciones)

    #--------------------------------------------------------------------------------------------------------------------------------------
    # RETORNA LA LISTA DE ALOJAMIENTOS DISPONIBLES CON SU NOMBRE Y LOCACION    
    @staticmethod
    def obtenerAlojamientos():
        lista_alojamientos= Alojamiento.getAlojamientos()
        valores =[]
        
        for alojamiento in lista_alojamientos:
            valores.append(alojamiento.getNombre()+"---"+alojamiento.getLocacion())

        return valores

    #--------------------------------------------------------------------------------------------------------------------------------------
    # RECIBE UN VUELO COMO PARAMETRO Y SE ENCARGA DE GENERAR UN TIQUETE CON UN iD ALEATORIO, QUE ES RETORNADO AL FINAL DEL METODO
    @staticmethod
    def generarTiquete(vuelo):
    
        ID_tiquete = 100 + random.random() * 900 # DEVUELVE UN NUMERO ALEATORIO DE 3 CIFRAS
        try:
            while Aerolinea.BuscarTiquete(int(ID_tiquete)) is not None:
                ID_tiquete = 100 + random.random() * 900
        except ExcepcionIdTiquete:
            tiquete = Tiquete(int(ID_tiquete), vuelo.getPrecio(), vuelo)
        return tiquete

    
    #--------------------------------------------------------------------------------------------------------------------------------------
    # CREA UN PASAJERO Y SE LO ASIGNA AL TIQUETE, POSTERIORMENTE SE LE ASIGNA EL PRECIO AL TIQUETE
    @staticmethod
    def asignarTiquete(datos,tiquete):

        nombre = datos[0]
        edad = int(datos[1])
        pasaporte = datos[2]
        correo = datos[-1]

        #SE CREA EL OBJETO PASAJERO Y SE LE ASIGNA AL TIQUETE GENERADO EN EL METODO
        pasajero = Pasajero(pasaporte, nombre, tiquete, edad, correo)
        tiquete.setPasajero(pasajero)

    #--------------------------------------------------------------------------------------------------------------------------------------
    # BUSCA UN TIQUETE CON EL ID PASADO Y SE VERIFICA SI EL TIQUETE TIENE YA UN ALOJAMIENTO SELECCIONADO, SEGUN ESTO SE RETORNA UN TIQUETE
    # NONE O 2
    @staticmethod
    def buscarTiqueteYAlojamiento(id,numero):
        tiqueteID = int(id)
        tiquete_solicitado = Aerolinea.BuscarTiquete(tiqueteID)

        if tiquete_solicitado == None:
            raise ExcepcionIdTiquete(tiqueteID) # SI NO EXISTE EL TIQUETE

        elif tiquete_solicitado.getAlojamiento() != None:
            if numero == 1:
                raise ExcepcionAgregarAlojamiento(tiqueteID) # SI EL TIQUETE YA TIENE UN ALOJAMIENTO ASOCIADO
            else:
                return tiquete_solicitado
        else:
            if numero == 1:
                return tiquete_solicitado # SI HAY ALOJAMIENTOS DISPONIBLES EN EL LUGAR DE DESTINO
            else:
                raise ExcepcionModificarAlojamiento(tiqueteID)
 
    #--------------------------------------------------------------------------------------------------------------------------------------
    # RECIBE UN TIQUETE Y UN NOMBRE DE ALOJAMIENTO, PARA OBTENER EL DESTINO DEL TIQUETE Y POSTERIORMENTE BUSCAR EL ALOJAMIENTO
    # SOLICITADO POR SU NOMBRE
    @staticmethod
    def solicitarAlojamiento(tiquete_solicitado,alojamiento_nombre):
        destino = tiquete_solicitado.getVuelo().getDestino()
        alojamiento_solicitado = Alojamiento.buscarAlojamientoPorNombre(alojamiento_nombre)
        
        if alojamiento_solicitado == None:
            return alojamiento_solicitado #SI NO ENCUENTRA UN ALOJAMIENTO CON ESE NOMBRE

        elif  alojamiento_solicitado.getLocacion().lower() != destino.lower():
            alojamiento_solicitado = None #SI LA LOCACION DEL ALOJAMIENTO ES DISTINTA DEL DESTINO DEL TIQUETE
            return alojamiento_solicitado

        else:
            return alojamiento_solicitado 

    #--------------------------------------------------------------------------------------------------------------------------------------
    # SE LE PASA UN TIQUETE, UN ALOJAMIENTO Y UN NUMERO DE DIAS, PARA SETEARLE EL ALOJAMIENTO AL TIQUETE Y POSTERIORMENTE ASIGNARLE SU 
    # PRECIO EN BASE AL NUMERO DE DIAS QUE SE QUEDARA EN EL ALOJAMIENTO
    @staticmethod
    def agregarAlojamiento(tiquete_solicitado,alojamiento_solicitado,num_dias):
        tiquete_solicitado.setAlojamiento(alojamiento_solicitado)
        tiquete_solicitado.asignarPrecio(int(num_dias))

    #--------------------------------------------------------------------------------------------------------------------------------------    
    # RECIBE UN NUMERO QUE INDICA SI SE ESTA AGREGANDO LA SILLA POR PRIMERA VEZ O SE ESTA MODIFICANDO, UN TIQUETE Y UNA SILLA
    # PARA ASIGNARSELA AL TIQUETE
    @staticmethod
    def modificarSilla(numero, tiquete,silla):
        if numero ==1 :
            tiquete.setSilla(silla)
        else:    
            tiquete.getSilla().setEstado(True) #SE DESOCUPA LA SILLA QUE SE TENIA ANTERIORMENTE
            tiquete.setSilla(silla)
        tiquete.asignarPrecio() #SE RECALCULA EL PRECIO EN BASE A LA NUEVA SILLA

    #--------------------------------------------------------------------------------------------------------------------------------------
    #ESTE METODO RECIBE UN LABEL Y RETORNA UN LABEL. SU OBJETIVO ES MOSTRAR LAS LISTAS DE PASAJAEROS ASOCIADOS A UN VUELO. 
    #PARA ESTO ACCEDEMOS A TRAVES DEL ID DEL VUELO E INVOCAMOS EL METODO BUSCAR VUELO POR ID. AL FINAL NOS MOSTRARA SI EL VUELO TIENE PASAJEROS
    # ASOCIADOS O NO, Y LA INFORMACION ASOCIADA AL ID DEL TIQUETE DEL PASAJAERO, SU NOMBRE, SU PASARTE Y SU EMAIL. 
    @staticmethod
    def isFloat(s):
        try:
            float(s)
            raise ExcepcionEnteroFloat(s)
        except ValueError:
            return
    @staticmethod
    def listarPasajeros(valor,label):
        aerolineas = Aerolinea.getAerolineas()
        if not valor.isdigit():
            Admin.isFloat(valor)
            raise ExcepcionEnteroString(valor)

        IDBusqueda = int(valor)

        tiquetes = []
        vuelo = None
        for i in aerolineas:
            if i.buscarVueloPorID(i.getVuelos(), IDBusqueda) != None:
                vuelo = i.buscarVueloPorID(i.getVuelos(), IDBusqueda)
                break
        if vuelo ==None:
            raise ExcepcionIdVuelo(IDBusqueda)

        tiquetes = vuelo.getTiquetes()
        label["text"]+="LISTA DE PASAJEROS PARA EL VUELO " + str(IDBusqueda)

        if len(tiquetes) == 0:
            label["text"]+="\nEl vuelo aun no tiene pasajeros asociados \n"
        else:
            Admin.mostrarTablaDePasajeros(tiquetes,label)

    #--------------------------------------------------------------------------------------------------------------------------------------
    # ESTE METODO RECIBE LA LISTA DE VALORES NECESARIOS PARA LA CREACION DE UN VUELO
    # PARA ESTO SE HARA UNA VERFICACION DE LA EXISTENCIA DE LA AEROLINEA Y POSTERIORMENTE SE INSTANCIARA UN VUELO SE AREGARA AL ARREGLO DE 
    # VUELOS DE LA AEROLINEA
    
    @staticmethod
    def agregarNuevoVuelo(valores):
        nombreAerolinea = valores[0]
        iD = int(valores[1])
        precio= int(valores[2])
        origen = valores[3]
        destino = valores[4]
        distancia = int(valores[5])
        fechaSalida=valores[6]
        horaSalida = valores[7]
        aeronave = valores[8]
        nombreAeronave = valores[9]
        for aerolinea in Aerolinea.getAerolineas():
            existe_vuelo= aerolinea.buscarVueloPorID(aerolinea.getVuelos(),iD)
            if existe_vuelo !=None:
                return True

        if aeronave.lower() == "avion":
            avion = Avion(nombreAeronave, Aerolinea.buscarAerolineaPorNombre(nombreAerolinea))
            vuelo = Vuelo(iD, precio, origen, destino, avion, distancia, fechaSalida, horaSalida)
    
        elif aeronave.lower() == "avioneta":
            avioneta = Avioneta(nombreAeronave, Aerolinea.buscarAerolineaPorNombre(nombreAerolinea))
            vuelo = Vuelo(iD, precio, origen, destino, avioneta, distancia, fechaSalida, horaSalida)
        return False  

    #--------------------------------------------------------------------------------------------------------------------------------------
    # RECIBE UN ID QUE PERMITIRA BUSCAR EL VUELO EN TODAS LAS AEROLINEAS, SI ES ENCONTRADO SE ELIMINA Y SE RETORNA TRUE, DE LO CONTRARIO
    # RETORNA FALSE

    @staticmethod
    def cancelarVuelos(id):
        vuelo_encontrado = False
        aerolineas = Aerolinea.getAerolineas()
        id = id
        for aerolinea in aerolineas:
            i = 0
            while i < len(aerolinea.getVuelos()):
                if aerolinea.buscarVueloPorID(aerolinea.getVuelos(), id) != None:
                    aerolinea.cancelarVuelo(id)
                    vuelo_encontrado = True
                    break 
                i += 1
        return vuelo_encontrado

    #--------------------------------------------------------------------------------------------------------------------------------------
    # SI ENCUENTRA EL NOMBRE DEL AVION QUE SE DESEA RETIRAR RETORNA TRUE, LO MARCA COMO DESCOMPUESTO Y CANCELA EL VUELO QUE TENIA ASOCIADO 
    # ESTA AERONAVE

    @staticmethod
    def retirarAvion(aeronave):
        aeronave_encontrada = False
        nombre_aeronave = aeronave
        aerolineasDisponibles = Aerolinea.getAerolineas()
        i = 0
        while i < len(aerolineasDisponibles):
            aerolinea = aerolineasDisponibles[i]
            
            vuelo = aerolinea.buscarVueloPorAeronave(aerolinea.getVuelos(), nombre_aeronave)
            if vuelo != None:
                vuelo.getAeronave().setDescompuesto(True)
                aerolinea.cancelarVuelo(vuelo.getID())
                aeronave_encontrada = True
                break
            i += 1
        
        return aeronave_encontrada

    #--------------------------------------------------------------------------------------------------------------------------------------
    # PERMITE AGREGAR UN ALOJAMIENTO A LA LISTA DE ALOJAMIENTOS DISPONIBLES, ESTO DESDE SU CONSTRUCTOR
    @staticmethod
    def nuevoAlojamiento(valores):

        nombre = valores[0]
        locacion = valores[1]
        precio = valores[2]
        estrellas = valores[3]

        nuevoAlojamiento = Alojamiento(nombre, locacion, precio, estrellas)

    #--------------------------------------------------------------------------------------------------------------------------------------
    # RECIBE UN NOMBRE DE UN ALOJAMIENTO, BUSCA SI EXISTE UN ALOJAMIENTO CON ESE NOMBRE, SI ES ASÍ LO ELIMINA Y RETORNA TRUE, DE LO 
    # CONTRARIO RETORNA FALSE
    @staticmethod
    def retirarAlojamiento(nombre):
        alojamiento_encontrado = False
        if Alojamiento.buscarAlojamientoPorNombre(nombre) != None:
            i = 0
            while i < len(Alojamiento.getAlojamientos()):
                if Alojamiento.getAlojamientos()[i].getNombre().lower() == nombre.lower():
                    Alojamiento.getAlojamientos().pop(i)
                    alojamiento_encontrado = True
                    break
                i += 1
        return alojamiento_encontrado

    #--------------------------------------------------------------------------------------------------------------------------------------
    #FINALIZA EL SISTEMA DE ADMINISTRACION DE VUELOS Y SERIALIZA LOS OBJETOS
    @staticmethod
    def salirDelSistema():
        picklefile = open('./baseDeDatos/Aerolineas', 'wb')
        picklefile2 = open('./baseDeDatos/Alojamientos','wb')
        pickle.dump(Aerolinea._aerolineas, picklefile)
        pickle.dump(Alojamiento._alojamientos,picklefile2)
        picklefile.close()
        picklefile2.close()
        quit()


    #--------------------------------------------------------------------------------------------------------------------------------------
    # ESTE METODO RECIBE COMO PARAMETRO UN DESTINO (STRING) Y UN FRAME. RECORRE CADA AEROLINEA EJECUTANDO EL METODO DE AEROLINEA buscarVueloPorDestino()
    # PARA ALMACENAR ESTOS VUELOS EN UNA LISTA Y EJECUTAR EL METODO mostrarTablaDeVuelos, DONDE SE LLENARA UN LABEL CON ESTA INFO. 
    # SI ENCONTRO AL MENOS UN VUELO EN ALGUNA AEROLINEA, RETORNA UNA LISTA QUE CONTIENE LA LISTA DE VUELOS Y LA LISTA DE LOS NOMBRES DE LAS
    # AEROLINEAS QUE TIENEN VUELOS HACIA ESE DESTINO

    @staticmethod
    def consultarVuelosPorDestino(destino, frame_operaciones):
        lista_vuelos_nombres = []
        vuelos = []
        nombreAerolineas =[]

        aerolineasDisponibles = Aerolinea.getAerolineas()
        i = 0
        while i < len(aerolineasDisponibles):
            aerolinea = aerolineasDisponibles[i]
            vuelosPorDestino = aerolinea.buscarVueloPorDestino(aerolinea.vuelosDisponibles(aerolinea.getVuelos()), destino)
            if len(vuelosPorDestino) != 0:
                label = Label(frame_operaciones)
                Admin.mostrarTablaDeVuelos(aerolinea, vuelosPorDestino, label)
                vuelos.append(label)
                nombreAerolineas.append(aerolinea.getNombre())
            i += 1

        lista_vuelos_nombres.append(vuelos)
        lista_vuelos_nombres.append(nombreAerolineas)

        return lista_vuelos_nombres

  
    #--------------------------------------------------------------------------------------------------------------------------------------
    # ESTE METODO RECIBE COMO PARAMETRO UN DESTINO (STRING), UNA FECHA (STRING) Y UN FRAME. RECORRE CADA AEROLINEA EJECUTANDO EL METODO DE 
    # AEROLINEA buscarVueloPorDestino() Y LUEGO buscarVueloPorFecha() PARA ALMACENAR ESTOS VUELOS EN UNA LISTA Y EJECUTAR EL METODO 
    # mostrarTablaDeVuelos, DONDE SE LLENARA UN LABEL CON ESTA INFO. SI ENCONTRO AL MENOS UN VUELO EN ALGUNA AEROLINEA, RETORNA UNA LISTA QUE 
    # CONTIENE LA LISTA DE VUELOS Y LA LISTA DE LOS NOMBRES DE LAS AEROLINEAS QUE TIENEN VUELOS HACIA ESE DESTINO

    @staticmethod
    def consultarVuelosPorDestinoYFecha(destino, fecha, frame_operaciones):

        lista_vuelos_nombres = []
        vuelos = []
        nombreAerolineas =[]

        aerolineasDisponibles = Aerolinea.getAerolineas()
        i = 0
        while i < len(aerolineasDisponibles):
            aerolinea = aerolineasDisponibles[i]
            vuelosPorDestino = aerolinea.buscarVueloPorDestino(aerolinea.vuelosDisponibles(aerolinea.getVuelos()), destino)
            if len(vuelosPorDestino) != 0:
                vuelosPorFecha = aerolinea.buscarVueloPorFecha(vuelosPorDestino, fecha)
                if len(vuelosPorFecha) != 0:
                    label = Label(frame_operaciones)
                    Admin.mostrarTablaDeVuelos(aerolinea, vuelosPorFecha, label)
                    vuelos.append(label)
                    nombreAerolineas.append(aerolinea.getNombre())
            i += 1
        
        lista_vuelos_nombres.append(vuelos)
        lista_vuelos_nombres.append(nombreAerolineas)

        return lista_vuelos_nombres


    #--------------------------------------------------------------------------------------------------------------------------------------
    # RECIBE UN TIQUETE Y LOS DATOS DE UNA SILLA, PARA RETORNAR LA SILLA CON ESTAS CARACTERISTICAS
    @staticmethod
    def elegirSilla(tiquete,datos_silla):
        clase =str( datos_silla[0])
        ubicacion = str(datos_silla[1])

        if ubicacion.lower() == "pasillo":
            ubicacion = Ubicacion.PASILLO
        elif ubicacion.lower() == "ventana":
            ubicacion = Ubicacion.VENTANA
        else:
            ubicacion = Ubicacion.CENTRAL

        return tiquete.getVuelo().getAeronave().buscarSillaPorUbicacionyTipo(ubicacion,clase)

    #--------------------------------------------------------------------------------------------------------------------------------------
    #CREA LA TABLA DE PASAJEROS DE UN VUELO LLENANDO UN LABEL CON LOS DATOS DE LOS PASAJEROS ASOCIADOS A LOS TIQUETES DE UN VUELO
    @staticmethod
    def mostrarTablaDePasajeros(tiquetes,label):
        label["text"]+="\n---------------------------------------------------------------"
        label["text"]+="\n"+"{0:>5} {1:>12} {2:>16} {3:>17}".format("ID", "NOMBRE", "PASAPORTE", "EMAIL"+"\n")
        label["text"]+="---------------------------------------------------------------"

        i = 0
        while i < len(tiquetes):
            label["text"]+="\n"+"{0:>5} {1:>13} {2:>12} {3:>26}".format(str(tiquetes[i].getId()), tiquetes[i].getPasajero().nombre, tiquetes[i].getPasajero().getPasaporte(), tiquetes[i].getPasajero().getEmail())
            i += 1
        label["text"]+="\n---------------------------------------------------------------"
        label["text"]+="\n"

    #--------------------------------------------------------------------------------------------------------------------------------------
    #CREA LA TABLA DE ALOJAMIENTOS LLENANDO UN LABEL CON LOS DATOS DE CADA ALOJAMIENTO EN LA LISTA QUE SE LE PASO
    @staticmethod
    def mostrarTablaDeAlojamientos(alojamientos, label):
        label["text"]+="\n"
        label["text"]+="\n"+ "-------------------------------------------------------------"
        label["text"]+="\n"+"{0:>10} {1:>15} {2:>18} {3:>12}".format("NOMBRE", "LOCACION", "PRECIO POR DIA", "ESTRELLAS")
        label["text"]+="\n"
        label["text"]+="\n"+"-------------------------------------------------------------"

        j = 0
        while j < len(alojamientos):
            label["text"]+="\n"+"{0:>13} {1:>11} {2:>16} {3:>11}".format(alojamientos[j].getNombre(), alojamientos[j].getLocacion(), alojamientos[j].getPrecio_dia(), alojamientos[j].getEstrellas())
            label["text"]+="\n"
            j += 1

        label["text"]+="\n"+"-------------------------------------------------------------"
        label["text"]+="\n"

    @staticmethod
    def mostrarTablaDeVuelosDisponiblesPorAerolineas(aerolineas,frame_operaciones):
        i = 0
        lista = []
        while i < len(aerolineas):
            label = Label(frame_operaciones)
            aerolinea = aerolineas[i]
            Admin.printEncabezadoAerolinea(aerolineas[i],label)
            Admin.printVuelos(aerolinea.vuelosDisponibles(aerolinea.getVuelos()),label)
            Admin.printSeparador(label)
            lista.append(label)
            i += 1
        return lista

    #--------------------------------------------------------------------------------------------------------------------------------------
    #RECIBE UNA AEROLINEA Y SUS VUELOS, Y GENERA UN LABEL CON ESTOS VUELOS HACIENDO USO DE LOS METODOS printEncabezadoAerolinea(), printVuelos() Y printSeparador()
    @staticmethod
    def mostrarTablaDeVuelos(aerolinea,vuelos,label):
        if len(vuelos) != 0:
            Admin.printEncabezadoAerolinea(aerolinea,label)
            Admin.printVuelos(vuelos,label)
            Admin.printSeparador(label)
        return label

    #--------------------------------------------------------------------------------------------------------------------------------------
    #ENCABEZADO CON EL NOMBRE DE LA AEROLINEA Y LOS ATRIBUTOS DE LOS VUELOS QUE POSEE LA AEROLINEA.
    @staticmethod
    def printEncabezadoAerolinea(aerolinea,label):
        label["text"]+="\n"+"VUELOS DISPONIBLES DE LA AEROLINEA " + aerolinea.getNombre().upper()
        label["text"]+="\n"+"--------------------------------------------------------------------------------------------------"
        label["text"]+="\n"+"{0:>4} {1:>13} {2:>12} {3:>14} {4:>12} {5:>22} {6:>12}".format("ID", "PRECIO", "ORIGEN", "DESTINO", "FECHA", "HORA DE SALIDA", "AERONAVE")
        label["text"]+="\n"
        label["text"]+="\n"+"--------------------------------------------------------------------------------------------------"

    # System.out.printf() PERMITE DARLE UN FORMATO A LOS DATOS DE SALIDA
    # % INDICA QUE EN ESA POSICION SE VA A ESCRIBIR UN VALOR, SE PUEDEN PONER TANTOS COMO VARIABLES A MOSTRAR
    # ESTAS VARIABLES SE ESCRIBEN A CONTINUACION DE LAS COMMILLAS Y SEPARADAS POR COMAS
    # LA s INDICA QUE SE VA A MOSTRAR UNA CADENA DE CARACTERES, Y EL VALOR NUMERICO INDICA LA ALINEACION A LA DERECHA.

    #--------------------------------------------------------------------------------------------------------------------------------------
    # SE ENCARGA DE RECORRER LOS VUELOS DE UNA AEROLINEA PARA IR AGREGANDO AL LABEL, LINEA POR LINEA, LA INFORMACION PERTINENTE DE CADA UNO.
    @staticmethod
    def printVuelos(vuelos,label):
        j = 0
        while j < len(vuelos):
            label["text"]+="\n"+"{0:>5} {1:>12} {2:>13} {3:>13} {4:>15} {5:>11} {6:>21}".format(vuelos[j].getID(), vuelos[j].getPrecio(), vuelos[j].getOrigen(), vuelos[j].getDestino(), vuelos[j].getFecha_de_salida(), vuelos[j].getHora_de_salida(), vuelos[j].getAeronave().getNombre())
            label["text"]+="\n"
            j += 1

    #--------------------------------------------------------------------------------------------------------------------------------------
    #SEPARADOR PARA LA TABLA DE VUELOS
    @staticmethod
    def printSeparador(label):
        label["text"]+="\n"+"--------------------------------------------------------------------------------------------------"
        label["text"]+="\n"

    





