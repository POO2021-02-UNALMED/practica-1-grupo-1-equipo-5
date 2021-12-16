package uiMain;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Scanner;
import baseDatos.Deserializador;
import baseDatos.Serializador;
import gestorAplicacion.*;
import gestorAplicacion.alojamiento.Alojamiento;
import gestorAplicacion.adminVuelos.*;
import gestorAplicacion.hangar.*;
import java.lang.Math;

public class Admin {

	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		// CASOS DE PRUEBA !!!

		Deserializador.deserializar();

		int opcion;
		do {
			System.out.println("---- SISTEMA DE RESERVAS DE VUELO ---");
			System.out.println("Que operacion desea realizar?");
			System.out.println("1. Ver todos los vuelos disponibles por Aerolinea");
			System.out.println("2. Comprar tiquete para un vuelo por destino y fecha");
			System.out.println("3. Agregar alojamiento en el destino del vuelo");
			System.out.println("4. Modificar tiquete comprado");
			System.out.println("5. Ver opciones de administrador");
			System.out.println("6. Terminar");
			System.out.println("Por favor escoja una opcion: ");
			opcion = sc.nextInt();

			switch (opcion) {
				case 1:
					;
					mostrarVuelosPorAerolineas();
					break;
				case 2:
					generarTiquete();
					break;
				case 3:
					agregarAlojamiento();
					break;
				case 4:
					modificarTiquete();
					break;
				case 5:
					opcionesAdministrador();
					break;
				case 6:
					salirDelSistema();

					break;
			}
		} while (opcion != 6);
	}

	// CASE 1 MAIN: VER TODOS LOS VUELOS DISPONIBLES POR AEROLINEAS

	// MUESTRA UNA TABLA POR CADA AEROLINEA CON LOS VUELOS QUE SE TIENEN
	// DISPONIBLES, HACIENDO USO DE LOS METODOS PRINTENCABEZADO()
	// PRINTVUELOS() Y PRINTSEPARADOR()
	static void mostrarVuelosPorAerolineas() {
		ArrayList<Aerolinea> aerolineasDisponibles = Aerolinea.getAerolineas();
		generadorDeTablas.mostrarTablaDeVuelosDisponiblesPorAerolineas(aerolineasDisponibles);
	}

	// CASE 2 MAIN: GENERAR TIQUETE DE COMPRA DE VUELO
	static void generarTiquete() {
		System.out.println("Quieres buscar un vuelo por:");
		System.out.println("1. Destino");
		System.out.println("2. Destino y fecha");
		System.out.println("3. Regresar");
		int opcion = sc.nextInt();
		while (opcion != 1 & opcion != 2 & opcion != 3) {
			System.out.println("Por favor ingresa una opcion valida");
			opcion = sc.nextInt();
		}

		if (opcion == 1) {
			System.out.println("Por favor ingrese un destino:");
			String destino_1 = sc.next();
			boolean hayVuelos = consultarVuelosPorDestino(destino_1);
			if (!hayVuelos) {
				return;
			}
		} else if (opcion == 2) {
			System.out.println("Por favor ingrese un destino");
			String destino_2 = sc.next();
			System.out.println("Por favor ingrese una fecha (dd-mm-aaaa):");
			String fecha_2 = sc.next();
			boolean hayVuelos = consultarVuelosPorDestinoYFecha(destino_2, fecha_2);
			if (!hayVuelos) {
				return;
			}
		} else {
			return;
		}

		System.out.println("Por favor ingrese el nombre de la aerolinea con la que desea viajar");
		String nombre_aerolinea = sc.next();
		Aerolinea aerolinea = Aerolinea.buscarAerolineaPorNombre(nombre_aerolinea); // eN ESTE METODO SE CAMBIO EL
																					// equals

		while (aerolinea == null) {
			System.out.println("Por favor ingrese un nombre valido");
			nombre_aerolinea = sc.next();
			aerolinea = Aerolinea.buscarAerolineaPorNombre(nombre_aerolinea);
		}

		System.out.println("Por favor ingrese el ID del vuelo que desea comprar");
		int ID = sc.nextInt();
		Vuelo vuelo = aerolinea.buscarVueloPorID(aerolinea.getVuelos(), ID); // eN ESTE METODO SE CAMBIO EL equals
		while (vuelo == null) {
			System.out.println("Por favor ingrese un ID valido");
			ID = sc.nextInt();
			vuelo = aerolinea.buscarVueloPorID(aerolinea.getVuelos(), ID);
		}

		double ID_tiquete = 100 + Math.random() * 900; // DEVUELVE UN NUMERO ALEATORIO DE 3 CIFRAS
		while (Aerolinea.BuscarTiquete((int) ID_tiquete) != null) {
			ID_tiquete = 100 + Math.random() * 900;
		}

		// ELEGIR SILLA
		System.out.println("Que tipo de silla desea comprar?");
		Silla silla = elegirSilla(vuelo);
		if (silla == null) {
			System.out.println("Lo sentimos no se encuentran sillas disponibles con esas caracteristicas\n");
			return;
		}
		Tiquete tiquete = new Tiquete((int) ID_tiquete, vuelo.getPrecio(), vuelo);
		silla.setEstado(false);
		tiquete.setSilla(silla);

		// TOMAR DATOS DEL PASAJERO
		System.out.println("DATOS DEL PASAJERO:");
		System.out.println("Ingrese el nombre:");
		String nombre = sc.next();
		System.out.println("Ingrese su edad:");
		int edad = sc.nextInt();
		System.out.println("Ingrese el numero de su pasaporte:");
		String pasaporte = sc.next();
		System.out.println("Ingrese un e-mail");
		String correo = sc.next();

		Pasajero pasajero = new Pasajero(pasaporte, nombre, tiquete, edad, correo);
		tiquete.setPasajero(pasajero);

		// IMPRIME RESUMEN DE LA COMPRA
		tiquete.asignarPrecio();
		System.out.println(tiquete);

	}

	// CASE 3 MAIN: AGREGAR ALOJAMIENTO EN EL DESTINO DEL VUELO COMPRADO

	// EL METODO PERMITE AGREGAR UN ALOJAMIENTO A UN TIQUETE COMPRADO PREVIAMENTE
	static void agregarAlojamiento() {
		System.out.println("Deseas agregar un alojamiento a tu compra?");
		System.out.println("Por favor ingresa el ID del tiquete que se genero al comprar su vuelo:");
		int tiqueteID = sc.nextInt();
		Tiquete tiquete_solicitado = Aerolinea.BuscarTiquete(tiqueteID);
		if (tiquete_solicitado == null) {
			System.out.println("Lo sentimos, no tenemos un tiquete identificado con ese ID");
			System.out.println();
		} else {
			String destino = tiquete_solicitado.getVuelo().getDestino();
			boolean hayAlojamientos = mostrarAlojamientosPorUbicacion(destino);
			if (!hayAlojamientos) {
				return;
			}
			System.out.println("Por favor ingresa el nombre del alojamiento que desea anadir a su compra:");
			String alojamiento = sc.next();
			Alojamiento alojamiento_solicitado = Alojamiento.buscarAlojamientoPorNombre(alojamiento);
			if (alojamiento_solicitado == null) {
				System.out.println("Lo sentimos, no tenemos un Alojamiento con ese nombre");
				System.out.println();
			} else {
				System.out.println("Cuantos dias desea quedarse en el alojamiento?");
				int num_dias = sc.nextInt();
				tiquete_solicitado.setAlojamiento(alojamiento_solicitado);
				tiquete_solicitado.asignarPrecio(num_dias);

				System.out.println("Perfecto! el alojamiento " + alojamiento_solicitado.getNombre()
						+ " se ha agregado correctamente a su tiquete de compra.");
				System.out.println();
				System.out.println(tiquete_solicitado);
			}
		}
	}

	// CASE 4 MAIN: MODIFICAR TIQUETE COMPRADO
	// NOS PERMITE MODIFICAR EL ALOJAMIENTO Y LA SILLA DE UN TIQUETE
	static void modificarTiquete() {
		System.out.println("Ingrese el ID del tiquete que desea modificar.");
		int ID = sc.nextInt();
		Tiquete tiquete = Aerolinea.BuscarTiquete(ID);
		if (tiquete == null) {
			System.out.println("El ID ingresado no se encuentra\n");
		} else {
			System.out.println("Que aspectos de su tiquete desea modificar?");
			System.out.println("1: Modificar alojamiento");
			System.out.println("2: Modificar Silla");

			int opcion = sc.nextInt();

			switch (opcion) {

				case 1:
					int dias = modificarAlojamiento(tiquete);
					if (dias > 0) {
						tiquete.asignarPrecio(dias);
						System.out.println(tiquete);
					}
					break;
				case 2:
					modificarSilla(tiquete);
			}
		}
	}

	// METODOS DE MODIFICAR TIQUETE

	// ESTE METODO RECIBE UN TIQUETE AL CUAL SE LE VA A MODIFICAR EL ATRIBUTO SILLA:
	// LO HACE CAMBIANDO EL ATRIBUTO estaDisponible DE SU SILLA ACTUAL A TRUE Y
	// ASIGNANDO OTRA SILLA HACIENDO USO DEL METODO ELEGIR SILLA
	private static void modificarSilla(Tiquete tiquete) {

		System.out.println("A que tipo de silla desea cambiar?");
		Silla silla = elegirSilla(tiquete.getVuelo());
		if (silla == null) {
			System.out.println("Lo sentimos no se encuentran sillas disponibles con esas caracteristicas\n");
			return;
		}
		silla.setEstado(false);
		tiquete.getSilla().setEstado(true);
		tiquete.setSilla(silla);

		System.out.println("*************************************");
		System.out.println("SU SILLA HA SIDO MODIFICADA CON EXITO");
		System.out.println("*************************************\n");
		tiquete.asignarPrecio();
		System.out.println(tiquete);

	}

	private static int modificarAlojamiento(Tiquete tiquete_solicitado) {
		if (tiquete_solicitado.getAlojamiento() == null) {
			System.out.println("Aun no tiene un alojamiento asociado a su tiquete, puede agregar uno en la opcion 3.");
			System.out.println();
			return 0;
		}
		String destino = tiquete_solicitado.getVuelo().getDestino();
		mostrarAlojamientosPorUbicacion(destino);
		System.out.println("Por favor ingresa el nombre del alojamiento al que desea cambiar");
		String alojamiento = sc.next();
		Alojamiento alojamiento_solicitado = Alojamiento.buscarAlojamientoPorNombre(alojamiento);
		if (alojamiento_solicitado == null) {
			System.out.println("Lo sentimos, no tenemos un Alojamiento con ese nombre\n");
			return -1;
		} else {
			System.out.println("Por favor ingrese el numero de dias que se va a quedar en el alojamiento");
			int dias = sc.nextInt();
			tiquete_solicitado.setAlojamiento(alojamiento_solicitado);
			System.out.println("Perfecto! su alojamiento ha sido modificado a " + alojamiento_solicitado.getNombre()
					+ " exitosamente.");
			System.out.println();
			return dias;
		}
	}

	// CASE 5 MAIN: OPCIONES DE ADMINISTRADOR
	static void opcionesAdministrador() {

		int opcion;
		do {

			System.out.println("Que opcion desea realizar como administrador?");
			System.out.println("1. Listar Pasajeros.");
			System.out.println("2. Agregar Vuelo.");
			System.out.println("3. Cancelar vuelo.");
			System.out.println("4. Retirar un avion.");
			System.out.println("5. Agregar Alojamiento.");
			System.out.println("6. Eliminar Alojamiento.");
			System.out.println("7. Salir del administrador.");
			System.out.println("Por favor escoja una opcion: ");

			opcion = sc.nextInt();

			switch (opcion) {
				case 1:
					listarPasajeros();
					break;
				case 2:
					agregarNuevoVuelo();
					break;
				case 3:
					cancelarVuelos();
					break;
				case 4:
					retirarAvion();
					break;
				case 5:
					nuevoAlojamiento();
					break;
				case 6:
					retirarAlojamiento();
					break;
				case 7:
					salirDelAdministrador();
					break;
			}
		} while (opcion != 7);
	}

	// METODOS DE LAS OPCIONES DE ADMINISTRADOR

	// CASE 1: LISTAR PASAJEROS DE UN VUELO
	private static void listarPasajeros() {
		ArrayList<Aerolinea> aerolineas = Aerolinea.getAerolineas();
		generadorDeTablas.mostrarTablaDeVuelosPorAerolineas(aerolineas);

		System.out.println("Ingrese el ID del vuelo: ");
		int IDBusqueda = sc.nextInt();

		ArrayList<Tiquete> tiquetes = new ArrayList<Tiquete>();
		Vuelo vuelo = null;
		for (Aerolinea i : aerolineas) {
			if (i.buscarVueloPorID(i.getVuelos(), IDBusqueda) != null) {
				vuelo = i.buscarVueloPorID(i.getVuelos(), IDBusqueda);
				break;
			}
		}
		if (vuelo == null) {
			System.out.println("No tenemos vuelos con ese ID.\n");
			return;
		}
		tiquetes = vuelo.getTiquetes();
		System.out.println("LISTA DE PASAJEROS PARA EL VUELO " + IDBusqueda);

		if (tiquetes.size() == 0) {
			System.out.println("El vuelo aun no tiene pasajeros asociados \n");
		} else {
			generadorDeTablas.mostrarTablaDePasajeros(tiquetes);
		}
	}

	// CASE 2: AGREGAR NUEVO VUELO A UNA AEROLINEA
	private static void agregarNuevoVuelo() {
		ArrayList<Aerolinea> aerolineas = Aerolinea.getAerolineas();
		System.out.println("AGREGAR NUEVO VUELO \n");
		generadorDeTablas.mostrarTablaDeAerolineas(aerolineas);
		System.out.println("Ingrese el nombre de la aerolinea para agregar vuelo\n");
		String nombreAerolinea = sc.next();

		ArrayList<String> list = new ArrayList<>();
		for (Aerolinea i : aerolineas) {
			list.add(i.getNombre());
		}
		boolean existe = list.contains(nombreAerolinea);

		while (existe == false) {
			System.out.println("\nESA AEROLINEA NO EXISTE");
			System.out.println("Ingrese un nombre del listado anterior\n");
			String nombreAerolinean = sc.next();
			existe = list.contains(nombreAerolinean);
		}
		System.out.println();

		System.out.println("Ingrese el ID del nuevo vuelo (3 cifras):");
		int iD = sc.nextInt();
		Aerolinea aerolinea_busqueda = Aerolinea.buscarAerolineaPorNombre(nombreAerolinea);
		while (Integer.toString(iD).length() != 3) {
			System.out.println("Por favor ingrese un ID de 3 cifras.");
			iD = sc.nextInt();
		}
		while (aerolinea_busqueda.buscarVueloPorID(aerolinea_busqueda.getVuelos(), iD) != null) {
			System.out.println("El ID que ingreso ya esta en uso, por favor ingrese uno distinto.");
			iD = sc.nextInt();
		}

		System.out.println("\nIngrese el precio:");
		int precio = sc.nextInt();
		System.out.println();

		System.out.println("Ingrese el origen:");
		String origen = sc.next();
		System.out.println();

		System.out.println("Ingrese el destino:");
		String destino = sc.next();
		System.out.println();

		System.out.println("Iingrese la distancia (KM):");
		double distancia = sc.nextDouble();
		System.out.println();

		System.out.println("Ingrese fecha de salida (DD-MM-AAAA):");
		String fechaSalida = sc.next();
		System.out.println();

		System.out.println("Ingrese hora de salida (24:00):");
		String horaSalida = sc.next();
		System.out.println();

		System.out.println("Que tipo de aeronave es?");
		System.out.println("Ingrese 1 para avion" + "\n" + "Ingrese 2 para avioneta");
		int aeronave = sc.nextInt();

		if (aeronave == 1) {
			System.out.println("Ingrese el nombre del avion:");
			String nombreAvion = sc.next();
			System.out.println();

			Avion avion = new Avion(nombreAvion, Aerolinea.buscarAerolineaPorNombre(nombreAerolinea));
			Vuelo vuelo = new Vuelo(iD, precio, origen, destino, avion, distancia, fechaSalida, horaSalida);
			System.out.println("***************************************");
			System.out.println("SU VUELO SE HA REGISTRADO CORRECTAMENTE");
			System.out.println("***************************************\n");

		} else if (aeronave == 2) {
			System.out.println("INGRESE EL NOMBRE DE LA AVIONETA:");
			String nombreAvioneta = sc.next();
			System.out.println();
			Avioneta avioneta = new Avioneta(nombreAvioneta, Aerolinea.buscarAerolineaPorNombre(nombreAerolinea));
			Vuelo vuelo = new Vuelo(iD, precio, origen, destino, avioneta, distancia, fechaSalida, horaSalida);
			System.out.println("***************************************");
			System.out.println("SU VUELO SE HA REGISTRADO CORRECTAMENTE");
			System.out.println("***************************************\n");
		} else {
			System.out.println("No manejamos ese tipo de aeronave");

		}
	}

	// CASE 3: CANCELAR VUELO DE UNA AEROLINEA
	public static void cancelarVuelos() {
		System.out.println("Estos son los vuelos que tenemos:\n");
		ArrayList<Aerolinea> aerolineas = Aerolinea.getAerolineas();
		generadorDeTablas.mostrarTablaDeVuelosPorAerolineas(aerolineas);
		System.out.println("Ingrese el ID del vuelo a eliminar:");
		int id = sc.nextInt();

		for (Aerolinea aerolinea : aerolineas) {
			for (int i = 0; i < aerolinea.getVuelos().size(); i++) {
				if (aerolinea.buscarVueloPorID(aerolinea.getVuelos(), id) != null) {
					aerolinea.cancelarVuelo(id);
					System.out.println("El vuelo se ha eliminado correctamente.");
					return;
				}
			}
		}
		System.out.println("No tenemos un vuelo identificado con ese ID \n");
	}

	// CASE 4: RETIRAR AERONAVE
	// SI ENCUENTRA EL NOMBRE DEL AVION, ELIMINA EL VUELO QUE ESTABA ASOCIADO A EL
	// AVION QUE SE DESEA RETIRAR
	public static void retirarAvion() {
		boolean aeronave_encontrada = false;
		System.out.println("Ingrese el nombre de la Aeronave que se desea retirar:");
		String nombre_aeronave = sc.next();
		ArrayList<Aerolinea> aerolineasDisponibles = Aerolinea.getAerolineas();
		for (int i = 0; i < aerolineasDisponibles.size(); i++) {
			Aerolinea aerolinea = aerolineasDisponibles.get(i);
			Vuelo vuelo = aerolinea.buscarVueloPorAeronave(aerolinea.getVuelos(), nombre_aeronave);
			if (vuelo != null) {
				vuelo.getAeronave().setDescompuesto(true);
				aerolinea.cancelarVuelo(vuelo.getID());
				System.out.println("Se ha retirado la aeronave descompuesta y el vuelo asociado a este.");
				System.out.println();
				aeronave_encontrada = true;
				break;
			}
		}
		if (!aeronave_encontrada) {
			System.out.println("Lo sentimos, no encontramos una aeronave asociada al nombre que ingreso.");
			System.out.println();
		}
	}
	//CASE 5: AGREGAR ALOJAMIENTO
	// PERMITE AGREGAR UN ALOJAMIENTO A LA LISTA DE ALOJAMIENTOS DISPONIBLES, ESTO DESDE SU CONSTRUCTOR
	public static void nuevoAlojamiento()
	{
		System.out.println("Ingrese el nombre del alojamiento que desea agregar a nuestra lista:");
		String nombre = sc.next();
		System.out.println();
		
		System.out.println("Ingrese la locacion:");
		String locacion = sc.next();
		System.out.println();
		
		System.out.println("Ingrese el precio por dia:");
		long precio = sc.nextLong();
		System.out.println();
		
		System.out.println("Ingrese el numero de estrellas (1-5):");
		int estrellas = sc.nextInt();
		System.out.println();
		
		Alojamiento nuevoAlojamiento = new Alojamiento(nombre, locacion, precio, estrellas);
		System.out.println("Perfecto! El alojamiento " + nuevoAlojamiento.getNombre() + " se ha agregado a nuestra lista.");
		
	}
	//CASE 7: RETIRAR ALOJAMIENTO
	// MUESTRA LOS ALOJAMIENTOS QUE SE TIENEN DISPONIBLES, PARA POSTERIORMENTE PREGUNTAR POR EL NOMBRE DEL ALOJAMIENTO
	// QUE SE DESEA RETIRAR DE LA LISTA Y ELIMINARLO DE LA LISTA DE ALOJAMIENTOS.
	public static void retirarAlojamiento()
	{
		System.out.println("Estos son los alojamientos que tenemos asociados:");
		generadorDeTablas.mostrarTablaDeAlojamientos(Alojamiento.getAlojamientos());
	
		System.out.println("Ingrese el nombre del alojamiento que desea retirar de nuestra lista:");
		String nombre = sc.next();
		
		if (Alojamiento.buscarAlojamientoPorNombre(nombre) != null)
		{
			for (int i = 0; i < Alojamiento.getAlojamientos().size(); i++ )
			{
				if (Alojamiento.getAlojamientos().get(i).getNombre().equals(nombre))
				{
					Alojamiento.getAlojamientos().remove(i);
					System.out.println("El alojamiento " + nombre + " se ha eliminado correctamente.");
					System.out.println();
				}
			}	
		}
		else
		{
			System.out.println("Lo sentimos, no tenemos un alojamiento con este nombre.");
			System.out.println();
		}
	}
	
	// CASE 9: SALIR DEL ADMINISTRADOR
	private static void salirDelAdministrador() {
		System.out.println("Gracias por usar nuestras opciones de administrador! \n");
	}
	
//	CASE 6 MAIN: FINALIZAR SISTEMA DE ADMINISTRACION DE VUELOS
	private static void salirDelSistema() {
		System.out.println("Gracias por usar nuestro servicio!");
		Serializador.serializar();
		System.exit(0);
	}
	
// METODOS AUXILIARES - TABLA DE VUELOS POR...
	
	// OPCION 1: CONSULTAR VUELO POR DESTINO
	
	// ESTE METODO RECIBE COMO PARAMETRO UN DESTINO (STRING) Y RECORRE CADA AEROLINEA EJECUTANDO EL METODO DE AEROLINEA BUSCARVUELOPORDESTINO()
	// PARA ALMACENAR ESTOS VUELOS EN UNA LISTA Y MOSTRARLOS POR PANTALLA. SI ENCONTRO AL MENOS UN VUELO EN ALGUNA AEROLINEA
	// QUE TUVIERA ASOCIADO ESTE DESTINO RETORNA LA VARIABLE boolean HAYVUELOS CON EL VALOR true, DE LO CONTRARIO RETORNA false.
	static boolean consultarVuelosPorDestino(String destino) 
	{
		System.out.println("Estos son los vuelos disponibles hacia " + destino + " por nuestras aerolineas:" );
		System.out.println();
		boolean hayVuelos = false;
		
		ArrayList<Aerolinea> aerolineasDisponibles = Aerolinea.getAerolineas();
		for (int i = 0; i < aerolineasDisponibles.size(); i++)
		{
			Aerolinea aerolinea = aerolineasDisponibles.get(i);
			ArrayList<Vuelo> vuelosPorDestino = aerolinea.buscarVueloPorDestino(aerolinea.vuelosDisponibles(aerolinea.getVuelos()), destino);
			if (vuelosPorDestino.size() != 0)
			{
				generadorDeTablas.mostrarTablaDeVuelos(aerolinea, vuelosPorDestino);
				hayVuelos = true;	
			}
		}
		if (hayVuelos == false) 
		{
		System.out.println("Lo sentimos, no tenemos vuelos disponibles para ese destino");
		System.out.println();
		}
		return hayVuelos;
	}
	
	// OPCION 2: CONSULTAR VUELO POR DESTINO Y FECHA
	
	// ESTE METODO RECIBE COMO PARAMETRO UN DESTINO (STRING) Y UNA FECHA (STRING) Y RECORRE CADA AEROLINEA EJECUTANDO EL METODO DE AEROLINEA 
	// BUSCARVUELOPORDESTINO() SI LOS ENCUENTRA, EJECUTA EL METODO DE AEROLINEA BUSCARVUELOPORFECHA() PARA ALMACENAR ESTOS VUELOS EN UNA LISTA 
	// Y MOSTRARLOS POR PANTALLA. SI ENCONTRO AL MENOS UN VUELO EN ALGUNA AEROLINEA QUE TUVIERA ASOCIADO ESE DESTINO Y ESA FECHA, 
	// RETORNA LA VARIABLE boolean HAYVUELOS CON EL VALOR true, DE LO CONTRARIO RETORNA false.
	static boolean consultarVuelosPorDestinoYFecha(String destino, String fecha) 
	{
		System.out.println();
		System.out.println("Estos son los vuelos disponibles hacia " + destino + " en la fecha " + fecha + " por nuestras aerolineas:" );
		System.out.println();
		boolean hayVuelos = false;
		
		ArrayList<Aerolinea> aerolineasDisponibles = Aerolinea.getAerolineas();
		for (int i = 0; i < aerolineasDisponibles.size(); i++)
		{
			Aerolinea aerolinea = aerolineasDisponibles.get(i);
			ArrayList<Vuelo> vuelosPorDestino = aerolinea.buscarVueloPorDestino(aerolinea.vuelosDisponibles(aerolinea.getVuelos()), destino);
			if (vuelosPorDestino.size() != 0)
			{
				ArrayList<Vuelo> vuelosPorFecha = aerolinea.buscarVueloPorFecha(vuelosPorDestino, fecha);
				if(vuelosPorFecha.size() != 0 ){
					generadorDeTablas.mostrarTablaDeVuelos(aerolinea, vuelosPorFecha);
					hayVuelos = true;
				}
			}
		}
		if (hayVuelos == false) {
			System.out.println("Lo sentimos, no tenemos vuelos disponibles para ese destino y fecha especificos");
			System.out.println();
		}
		return hayVuelos;
	}

}
