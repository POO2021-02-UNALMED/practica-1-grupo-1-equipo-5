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
