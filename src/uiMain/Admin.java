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
					case 1: ;
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
		}while (opcion != 6);
	}
		
	// CASE 1 MAIN: VER TODOS LOS VUELOS DISPONIBLES POR AEROLINEAS	
	
		// MUESTRA UNA TABLA POR CADA AEROLINEA CON LOS VUELOS QUE SE TIENEN DISPONIBLES, HACIENDO USO DE LOS METODOS PRINTENCABEZADO()
		// PRINTVUELOS() Y PRINTSEPARADOR()
		static void mostrarVuelosPorAerolineas()
		{
			ArrayList<Aerolinea> aerolineasDisponibles = Aerolinea.getAerolineas();
			generadorDeTablas.mostrarTablaDeVuelosDisponiblesPorAerolineas(aerolineasDisponibles);
		}
	// CASE 2 MAIN: GENERAR TIQUETE DE COMPRA DE VUELO
		static void generarTiquete()
		{
			System.out.println("Quieres buscar un vuelo por:");
			System.out.println("1. Destino");
			System.out.println("2. Destino y fecha");
			System.out.println("3. Regresar");
			int opcion = sc.nextInt();
			while(opcion != 1 & opcion != 2 & opcion != 3)
			{
				System.out.println("Por favor ingresa una opcion valida");
				opcion = sc.nextInt();
			}
			
			if (opcion == 1) 
			{
				System.out.println("Por favor ingrese un destino:");
				String destino_1 = sc.next();
				boolean hayVuelos = consultarVuelosPorDestino(destino_1);
				if (!hayVuelos)
				{
					return;
				}
			}
			else if (opcion == 2)
			{
				System.out.println("Por favor ingrese un destino");
				String destino_2 = sc.next();
				System.out.println("Por favor ingrese una fecha (dd-mm-aaaa):");
				String fecha_2 = sc.next();
				boolean hayVuelos = consultarVuelosPorDestinoYFecha(destino_2, fecha_2);
				if (!hayVuelos)
				{
					return;
				}
			}
			else
			{
				return;
			}
			
			System.out.println("Por favor ingrese el nombre de la aerolinea con la que desea viajar");
			String nombre_aerolinea = sc.next();
			Aerolinea aerolinea = Aerolinea.buscarAerolineaPorNombre(nombre_aerolinea); // eN ESTE METODO SE CAMBIO EL equals
		
			while(aerolinea == null) {
				System.out.println("Por favor ingrese un nombre valido");
				nombre_aerolinea = sc.next();
				aerolinea = Aerolinea.buscarAerolineaPorNombre(nombre_aerolinea);
			}
			
			System.out.println("Por favor ingrese el ID del vuelo que desea comprar");
			int ID = sc.nextInt();
			Vuelo vuelo = aerolinea.buscarVueloPorID(aerolinea.getVuelos(), ID); // eN ESTE METODO SE CAMBIO EL equals
			while(vuelo == null) {
				System.out.println("Por favor ingrese un ID valido");
				ID = sc.nextInt();
				vuelo = aerolinea.buscarVueloPorID(aerolinea.getVuelos(), ID);
			}
			
			double ID_tiquete = 100 + Math.random() * 900; //DEVUELVE UN NUMERO ALEATORIO DE 3 CIFRAS
			while(Aerolinea.BuscarTiquete((int)ID_tiquete) != null) {
				ID_tiquete = 100 + Math.random() * 900;
			}
			
			
			//ELEGIR SILLA
			System.out.println("Que tipo de silla desea comprar?");
			Silla silla = elegirSilla(vuelo);
			if (silla == null) {
			System.out.println("Lo sentimos no se encuentran sillas disponibles con esas caracteristicas\n");
			return;
			}
			Tiquete tiquete = new Tiquete((int)ID_tiquete, vuelo.getPrecio(), vuelo);			
			silla.setEstado(false);
			tiquete.setSilla(silla);
			
			
			//TOMAR DATOS DEL PASAJERO
			System.out.println("DATOS DEL PASAJERO:");
			System.out.println("Ingrese el nombre:");
			String nombre= sc.next();
			System.out.println("Ingrese su edad:");
			int edad = sc.nextInt();
			System.out.println("Ingrese el numero de su pasaporte:");
			String pasaporte = sc.next();
			System.out.println("Ingrese un e-mail");
			String correo = sc.next();
			
			Pasajero pasajero = new Pasajero(pasaporte,nombre,tiquete,edad,correo);
			tiquete.setPasajero(pasajero);
			
		
			//IMPRIME RESUMEN DE LA COMPRA
			tiquete.asignarPrecio();
			System.out.println(tiquete);
			
		}

}

