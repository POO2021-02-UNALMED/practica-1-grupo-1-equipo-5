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
	static void mostrarVuelosPorAerolineas()
	{
	
	}
	

// CASE 2 MAIN: GENERAR TIQUETE DE COMPRA DE VUELO
	static void generarTiquete()
	{
		
	}
	
// CASE 3 MAIN:	AGREGAR ALOJAMIENTO EN EL DESTINO DEL VUELO COMPRADO
	static void agregarAlojamiento() 
	{
		
	}
	
	
// CASE 4 MAIN:	MODIFICAR TIQUETE COMPRADO
	static void modificarTiquete()
	{
		
	}

	//METODOS DE MODIFICAR TIQUETE
	private static void modificarSilla (Tiquete tiquete) 
	{
		
	}
	
	private static int modificarAlojamiento(Tiquete tiquete_solicitado) 
	{
		return 0;
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
			}while (opcion != 7);
	}

	// METODOS DE LAS OPCIONES DE ADMINISTRADOR
	
	// CASE 1: LISTAR PASAJEROS DE UN VUELO
	private static void listarPasajeros() 
	{
	
	}
		
	// CASE 2: AGREGAR NUEVO VUELO A UNA AEROLINEA
	private static void agregarNuevoVuelo() 
	{  
		
	}
	
	// CASE 3: CANCELAR VUELO DE UNA AEROLINEA
	public static void cancelarVuelos() 
	{		

	}
	
	//CASE 4: RETIRAR AVION
	//ESTA HECHO PARA ELIMINAR EL VUELO QUE CONTENIA EL AVION, QUE POR CONVENCION, ES SOLO UNO (CONFLICTOS CON LAS SILLAS)
	public static void retirarAvion() 
	{
		
	}
	
	//CASE 5: AGREGAR ALOJAMIENTO
	public static void nuevoAlojamiento()
	{
		
	}
	
	//CASE 6: RETIRAR ALOJAMIENTO
	public static void retirarAlojamiento()
	{
		
	}
	
	// CASE 7: SALIR DEL ADMINISTRADOR
	private static void salirDelAdministrador() {
		System.out.println("Gracias por usar nuestras opciones de administrador! \n");	
	}
	
//	CASE 6 MAIN: FINALIZAR SISTEMA DE ADMINISTRACION DE VUELOS

	private static void salirDelSistema() {
		System.out.println("Gracias por usar nuestro servicio!");
		System.exit(0);
	
	}

// METODOS AUXILIARES: TABLAS DE VUELOS
	static void printEncabezado(Aerolinea aerolinea) 
	{
		
	}

	static void printListaAdmin(Aerolinea aerolinea) 
	{
	
	}
	
	static void printVuelos(ArrayList<Vuelo> vuelos) 
	{
		
	}
	
	static void printiIdVuelos(ArrayList<Vuelo> vuelos) 
	{
		
	}
	
	static void printSeparador() 
	{
		
	}
	
// METODOS AUXILIARES - TABLA DE VUELOS POR...
	
	// OPCION 1: CONSULTAR VUELO POR DESTINO
	static boolean consultarVuelosPorDestino(String destino) 
	{
		return false;
	}
	
	// OPCION 1: CONSULTAR VUELO POR DESTINO Y FECHA
	static boolean consultarVuelosPorDestinoYFecha(String destino, String fecha) 
	{
		return false;
	}	
	
// METODOS AUXILIARES - TABLA ALOJAMIENTOS
	static boolean mostrarAlojamientosPorUbicacion(String ubicacion) 
	{
		return false;
	}
	
//METODOS AUXILIARES - ELEGIR SILLA
	static void elegirSilla(Tiquete tiquete,Vuelo vuelo) 
	{

	}
}	





