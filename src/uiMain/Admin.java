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
