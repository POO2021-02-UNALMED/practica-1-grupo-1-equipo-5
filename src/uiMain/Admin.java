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
		

}

