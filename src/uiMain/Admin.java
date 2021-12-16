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
	//  CASOS DE PRUEBA !!!		
		 
		System.out.println(tiquete);

	}

	// CASE 3 MAIN: AGREGAR ALOJAMIENTO EN EL DESTINO DEL VUELO COMPRADO
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
					tiquete.asignarPrecio();
					System.out.println(tiquete);
					break;
			}
		}
	}

	// METODOS DE MODIFICAR TIQUETE
	private static void modificarSilla(Tiquete tiquete) {
		tiquete.getSilla().setEstado(true);
		System.out.println("A que tipo de silla desea cambiar?");
		elegirSilla(tiquete, tiquete.getVuelo());
		System.out.println("*************************************");
		System.out.println("SU SILLA HA SIDO MODIFICADA CON EXITO");
		System.out.println("*************************************\n");
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

		for (int i = 0; i < aerolineas.size(); i++) {
			Aerolinea aerolinea = aerolineas.get(i);
			System.out.println("VUELOS DISPONIBLES DE LA AEROLINEA " + aerolinea.getNombre().toUpperCase());
			System.out.println("------------------------------------------------------------------------------------");
			System.out.printf("%4s %12s %14s %12s %20s %12s", "ID", "ORIGEN", "DESTINO", "FECHA", "HORA DE SALIDA",
					"AERONAVE");
			System.out.println();
			System.out.println("------------------------------------------------------------------------------------");
			System.out.println();
			ArrayList<Vuelo> vuelos = aerolinea.getVuelos();

			for (int j = 0; j < vuelos.size(); j++) {
				System.out.format("%4s %12s %14s %16s %12s %17s", vuelos.get(j).getID(), vuelos.get(j).getOrigen(),
						vuelos.get(j).getDestino(), vuelos.get(j).getFecha_de_salida(),
						vuelos.get(j).getHora_de_salida(), vuelos.get(j).getAeronave().getNombre());
				System.out.println();
			}
			System.out.println();
		}

		System.out.println("Ingrese el ID del vuelo: ");
		int IDBusqueda = sc.nextInt();

		ArrayList<Tiquete> tiquetes = new ArrayList<Tiquete>();

		for (Aerolinea i : aerolineas) {
			if (i.buscarVueloPorID(i.getVuelos(), IDBusqueda) == null) {
				continue;
			}
			tiquetes = i.buscarVueloPorID(i.getVuelos(), IDBusqueda).getTiquetes();
			if (tiquetes != null) {
				break;
			}
		}
		System.out.println("LISTA DE PASAJEROS PARA EL VUELO " + IDBusqueda);

		if (tiquetes.size() == 0) {
			System.out.println("El vuelo aun no tiene pasajeros asociados \n");
		} else {
			System.out.println("-------------------------------------------");
			System.out.printf("%4s %16s %14s", "NOMBRE", "PASAPORTE", "EMAIL" + "\n");
			System.out.println("-------------------------------------------");

			for (int i = 0; i < tiquetes.size(); i++) {
				System.out.printf("%4s %13s %13s", tiquetes.get(i).getPasajero().nombre,
						tiquetes.get(i).getPasajero().getPasaporte(), tiquetes.get(i).getPasajero().getEmail());
				System.out.println();
			}
			System.out.println();
		}

	}

	// CASE 2: AGREGAR NUEVO VUELO A UNA AEROLINEA
	private static void agregarNuevoVuelo() {
		ArrayList<Aerolinea> aerolinea = Aerolinea.getAerolineas();
		System.out.println("AGREGAR NUEVO VUELO \n");
		System.out.println("ESTAS SON LAS AEROLINEAS DISPONIBLES");
		System.out.println("------------------------------------");

		for (Aerolinea aerolineas : aerolinea) {
			System.out.println(aerolineas.getNombre());
		}

		System.out.println("------------------------------------\n");
		System.out.println("Ingrese el nombre de la aerolinea para agregar vuelo\n");
		String nombreAerolinea = sc.next();

		ArrayList<String> list = new ArrayList<>();
		for (Aerolinea i : aerolinea) {
			list.add(i.getNombre());
		}
		boolean existe = list.contains(nombreAerolinea);

		while (existe == false) {
			System.out.println("ESA AEROLINEA NO EXISTE");
			System.out.println("Ingrese un nombre del listado anterior\n");
			String nombreAerolinean = sc.next();
			existe = list.contains(nombreAerolinean);

		}
		System.out.println();

		System.out.println("Ingrese el ID del nuevo vuelo:");
		int iD = sc.nextInt();
		System.out.println();

		System.out.println("Ingrese el precio:");
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

		System.out.println("Ingrese hora de salida (12:00):");
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
			Vuelo vuelo = new Vuelo(iD, precio, origen, destino, avion, distancia, fechaSalida, horaSalida); // �DISTANCIA?
			System.out.println("***************************************");
			System.out.println("SU VUELO SE HA REGISTRADO CORRECTAMENTE");
			System.out.println("***************************************\n");

		} else if (aeronave == 2) {
			System.out.println("INGRESE EL NOMBRE DE LA AVIONETA:");
			String nombreAvioneta = sc.next();
			System.out.println();
			Avioneta avioneta = new Avioneta(nombreAvioneta, Aerolinea.buscarAerolineaPorNombre(nombreAerolinea));
			Vuelo vuelo = new Vuelo(iD, precio, origen, destino, avioneta, distancia, fechaSalida, horaSalida); // �DISTANCIA?
			System.out.println("***************************************");
			System.out.println("SU VUELO SE HA REGISTRADO CORRECTAMENTE");
			System.out.println("***************************************\n");

		} else {
			System.out.println("No manejamos ese tipo de aeronave");

		}
	}

	// CASE 3: CANCELAR VUELO DE UNA AEROLINEA
	public static void cancelarVuelos() {
		ArrayList<Aerolinea> aerolinea = Aerolinea.getAerolineas();
		System.out.println("Estos son los ID de los vuelos que tenemos:\n");
		System.out.println("***********************************************\n");
		System.out.printf("%4s %13s %12s %16s", "ID", "AEROLINEA", "ORIGEN", "DESTINO \n");

		for (Aerolinea aerolineas : aerolinea) {
			for (int i = 0; i < aerolineas.getVuelos().size(); i++) {
				Vuelo vuelos = aerolineas.getVuelos().get(i);
				System.out.printf("%4s %13s %12s %14s", vuelos.getID(), aerolineas.getNombre(),
						aerolineas.getVuelos().get(i).getOrigen(), aerolineas.getVuelos().get(i).getDestino());
				System.out.println();
			}

		}
		System.out.println();
		System.out.println("***********************************************\n");
		System.out.println("Ingrese el ID del vuelo a eliminar:");
		int id = sc.nextInt();

		for (Aerolinea aerolineas : aerolinea) {
			for (int i = 0; i < aerolineas.getVuelos().size(); i++) {
				if (aerolineas.buscarVueloPorID(aerolineas.getVuelos(), id) != null) {
					aerolineas.cancelarVuelo(id);
					System.out.println("El vuelo se ha eliminado correctamente.");
					return;
				}
			}
		}
		System.out.println("No tenemos un vuelo identificado con ese ID \n");
	}

	// CASE 4: RETIRAR AVION
	// ESTA HECHO PARA ELIMINAR EL VUELO QUE CONTENIA EL AVION, QUE POR CONVENCION,
	// ES SOLO UNO (CONFLICTOS CON LAS SILLAS)
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

	// CASE 5: AGREGAR ALOJAMIENTO
	public static void nuevoAlojamiento() {
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
		System.out.println(
				"Perfecto! El alojamiento " + nuevoAlojamiento.getNombre() + " se ha agregado a nuestra lista.");

	}

	// CASE 7: RETIRAR ALOJAMIENTO
	public static void retirarAlojamiento() {
		System.out.println("Estos son los alojamientos que tenemos asociados:\n");
		System.out.println("************");
		System.out.printf("%9s %19s", "NOMBRE", "UBICACION ");
		System.out.println();

		for (int i = 0; i < Alojamiento.getAlojamientos().size(); i++) {
			Alojamiento alojamiento = Alojamiento.getAlojamientos().get(i);
			System.out.printf("%4s %13s", alojamiento.getNombre(), alojamiento.getLocacion());
			System.out.println();
		}
		System.out.println("************");

		System.out.println("Ingrese el nombre del alojamiento que desea retirar de nuestra lista:");
		String nombre = sc.next();

		if (Alojamiento.buscarAlojamientoPorNombre(nombre) != null) {
			for (int i = 0; i < Alojamiento.getAlojamientos().size(); i++) {
				if (Alojamiento.getAlojamientos().get(i).getNombre().equals(nombre)) {
					Alojamiento.getAlojamientos().remove(i);
					System.out.println("El alojamiento " + nombre + " se ha eliminado correctamente.");
					System.out.println();
				}
			}
		} else {
			System.out.println("Lo sentimos, no tenemos un alojamiento con este nombre.");
			System.out.println();
		}
	}

	// CASE 9: SALIR DEL ADMINISTRADOR
	private static void salirDelAdministrador() {
		System.out.println("Gracias por usar nuestras opciones de administrador! \n");

	}

	// CASE 6 MAIN: FINALIZAR SISTEMA DE ADMINISTRACION DE VUELOS

	private static void salirDelSistema() {
		System.out.println("Gracias por usar nuestro servicio!");
		System.exit(0);

	}

	// METODOS AUXILIARES: TABLAS DE VUELOS
	static void printEncabezado(Aerolinea aerolinea) {
		System.out.println("VUELOS DISPONIBLES DE LA AEROLINEA " + aerolinea.getNombre().toUpperCase());
		System.out.println(
				"--------------------------------------------------------------------------------------------------");
		System.out.printf("%4s %13s %12s %14s %12s %22s %12s", "ID", "PRECIO", "ORIGEN", "DESTINO", "FECHA",
				"HORA DE SALIDA", "AERONAVE");
		System.out.println();
		System.out.println(
				"--------------------------------------------------------------------------------------------------");
	}

	static void printListaAdmin(Aerolinea aerolinea) {
		System.out.println("VUELOS DISPONIBLES DE LA AEROLINEA " + aerolinea.getNombre().toUpperCase());
		System.out.println(
				"------------------------------------------------------------------------------------------------");
		System.out.printf("%4s %13s %12s %14s %12s %22s %12s", "ID", "ORIGEN", "DESTINO", "FECHA", "HORA DE SALIDA",
				"AVION");
		System.out.println();
		System.out.println(
				"--------------------------------------------------------------------------------------------------");
	}

	static void printVuelos(ArrayList<Vuelo> vuelos) {
		for (int j = 0; j < vuelos.size(); j++) {
			System.out.format("%5s %12s %13s %13s %15s %11s %21s", vuelos.get(j).getID(), vuelos.get(j).getPrecio(),
					vuelos.get(j).getOrigen(), vuelos.get(j).getDestino(), vuelos.get(j).getFecha_de_salida(),
					vuelos.get(j).getHora_de_salida(), vuelos.get(j).getAeronave());
			System.out.println();
		}
	}

	static void printiIdVuelos(ArrayList<Vuelo> vuelos) {
		for (int j = 0; j < vuelos.size(); j++) {
			System.out.format("%5s", vuelos.get(j).getID());
			System.out.println();
		}
	}

	static void printSeparador() {
		System.out.println(
				"--------------------------------------------------------------------------------------------------");
		System.out.println();
	}

	// METODOS AUXILIARES - TABLA DE VUELOS POR...

	// OPCION 1: CONSULTAR VUELO POR DESTINO
	static boolean consultarVuelosPorDestino(String destino) {

		System.out.println("Estos son los vuelos disponibles hacia " + destino + " por nuestras aerolineas:");
		System.out.println();
		boolean hayVuelos = false;

		ArrayList<Aerolinea> aerolineasDisponibles = Aerolinea.getAerolineas();
		for (int i = 0; i < aerolineasDisponibles.size(); i++) {
			Aerolinea aerolinea = aerolineasDisponibles.get(i);
			ArrayList<Vuelo> vuelosPorDestino = aerolinea
					.buscarVueloPorDestino(aerolinea.vuelosDisponibles(aerolinea.getVuelos()), destino);
			if (vuelosPorDestino.size() != 0) {
				hayVuelos = true;
				printEncabezado(aerolinea);
				printVuelos(vuelosPorDestino);
				printSeparador();
			}
		}
		if (hayVuelos == false) {
			System.out.println("Lo sentimos, no tenemos vuelos disponibles para ese destino");
			System.out.println();
		}
		return hayVuelos;
	}

	// OPCION 1: CONSULTAR VUELO POR DESTINO Y FECHA
	static boolean consultarVuelosPorDestinoYFecha(String destino, String fecha) {
		System.out.println();
		System.out.println("Estos son los vuelos disponibles hacia " + destino + " en la fecha " + fecha
				+ " por nuestras aerolineas:");
		System.out.println();
		boolean hayVuelos = false;

		ArrayList<Aerolinea> aerolineasDisponibles = Aerolinea.getAerolineas();
		for (int i = 0; i < aerolineasDisponibles.size(); i++) {
			Aerolinea aerolinea = aerolineasDisponibles.get(i);
			ArrayList<Vuelo> vuelosPorDestino = aerolinea
					.buscarVueloPorDestino(aerolinea.vuelosDisponibles(aerolinea.getVuelos()), destino);
			if (vuelosPorDestino.size() != 0) {
				ArrayList<Vuelo> vuelosPorFecha = aerolinea.buscarVueloPorFecha(vuelosPorDestino, fecha);
				if (vuelosPorFecha.size() != 0) {
					printEncabezado(aerolinea);
					printVuelos(vuelosPorFecha);
					printSeparador();
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

	// METODOS AUXILIARES - TABLA ALOJAMIENTOS
	static boolean mostrarAlojamientosPorUbicacion(String ubicacion) {
		System.out.println("Estos son los alojamientos disponibles en " + ubicacion + ":");
		boolean hayAlojamientos = false;
		ArrayList<Alojamiento> alojamientosDisponibles = Alojamiento.buscarAlojamientoPorUbicacion(ubicacion);
		if (alojamientosDisponibles.size() != 0) {
			hayAlojamientos = true;
			System.out.println();
			System.out.println("-------------------------------------------------------------");
			System.out.printf("%10s %15s %18s %12s", "NOMBRE", "LOCACION", "PRECIO POR DIA", "ESTRELLAS");
			System.out.println();
			System.out.println("-------------------------------------------------------------");

			for (int j = 0; j < alojamientosDisponibles.size(); j++) {
				System.out.format("%13s %11s %16s %11s", alojamientosDisponibles.get(j).getNombre(),
						alojamientosDisponibles.get(j).getLocacion(), alojamientosDisponibles.get(j).getPrecio_dia(),
						alojamientosDisponibles.get(j).getEstrellas());
				System.out.println();
			}

			System.out.println("-------------------------------------------------------------");
			System.out.println();

		} else {
			System.out.println("Lo sentimos, no tenemos alojamientos disponibles para ese destino");
			System.out.println();
		}
		return hayAlojamientos;
	}

	// METODOS AUXILIARES - ELEGIR SILLA
	static void elegirSilla(Tiquete tiquete, Vuelo vuelo) {
		System.out.println("1: Ejecutiva");
		System.out.println("2: Economica");

		int nombre_clase = sc.nextInt();
		String clase;
		while (nombre_clase != 1 & nombre_clase != 2) {
			System.out.println("Porfavor ingrese una opcion valida");
			nombre_clase = sc.nextInt();
		}

		System.out.println("Cual de las siguientes ubicaciones prefiere?");
		System.out.println("1: Pasillo");
		System.out.println("2: Ventana");

		if (nombre_clase == 2) {
			clase = "ECONOMICA";
			System.out.println("3: Central");
		} else {
			clase = "EJECUTIVA";
		}

		int num_ubicacion = sc.nextInt();

		while (num_ubicacion != 1 & num_ubicacion != 2 & num_ubicacion != 3) {
			System.out.println("Porfavor ingrese una opcion valida");
			num_ubicacion = sc.nextInt();
		}
		Ubicacion ubicacion;
		if (num_ubicacion == 1) {
			ubicacion = Ubicacion.PASILLO;
		} else if (num_ubicacion == 2) {
			ubicacion = Ubicacion.VENTANA;
		} else {
			ubicacion = Ubicacion.CENTRAL;
		}
		Silla silla = vuelo.getAeronave().buscarSillaPorUbicacionyTipo(ubicacion, clase);
		silla.setEstado(false);
		tiquete.setSilla(silla);
	}
}}
