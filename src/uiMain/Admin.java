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
		 
				Aerolinea capiFly = new Aerolinea("Capifly");
				Avion avion1 = new Avion("boeing787", capiFly);
				Vuelo vuelo1 = new Vuelo(111, 150000, "Rionegro", "Bogota", avion1, 214.88, "12-10-2011", "14:00");
				Vuelo vuelo2 = new Vuelo(112, 190000, "Rionegro", "Bogota", avion1, 214.88, "13-10-2011", "16:00");
			
				Aerolinea capiFly2 = new Aerolinea("Capifly2");
				Avioneta avioneta1 = new Avioneta("Avioneta787", capiFly2);
				Vuelo vuelo3 = new Vuelo(113, 200000, "Rionegro", "Cartagena", avioneta1, 473.22, "15-10-2011", "15:00");
				Vuelo vuelo4 = new Vuelo(114, 1600000, "Bogota", "Espana",  avioneta1, 8033.74, "31-10-2011", "17:00");
				Vuelo vuelo5 = new Vuelo(115, 230000, "Rionegro", "Bogota", avioneta1, 214.88, "17-10-2011", "16:00");

				Alojamiento alojamiento1 = new Alojamiento("alojamiento1", "Bogota", 55000, 3);
				Alojamiento alojamiento2 = new Alojamiento("alojamiento2", "Bogota", 95000, 4);
				Alojamiento alojamiento3 = new Alojamiento("alojamiento3", "Espana", 105000, 4);

				Tiquete tiquete1 = new Tiquete(1, 12000, vuelo1);
				Pasajero pasajero1 = new Pasajero( "AS1234", "Capibara", tiquete1, 20, "@");
				

				Tiquete tiquete2 = new Tiquete(2, 13000, vuelo1);
				Pasajero pasajero2 = new Pasajero( "AS1111", "Milonesa", tiquete2, 5, "@");
				
				Tiquete tiquete3 = new Tiquete(3, 13000, vuelo3);
				Pasajero pasajero3 = new Pasajero( "AS1256", "Jeronimo", tiquete3, 15, "@");

				tiquete2.setAlojamiento(alojamiento1);

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
		ArrayList<Aerolinea> aerolineasDisponibles = Aerolinea.getAerolineas();
		for (int i = 0; i < aerolineasDisponibles.size(); i++)
		{
			Aerolinea aerolinea = aerolineasDisponibles.get(i);
			printEncabezado(aerolinea);
			printVuelos(aerolinea.vuelosDisponibles(aerolinea.getVuelos())); //SE MUESTRAN LOS VUELOS QUE NO EST�N COMPLETOS
			printSeparador();
			}
	
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





