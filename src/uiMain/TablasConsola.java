//CLASE PARA LA IMPRESION POR PANTALLA DE TABLAS DE DATOS
//AUTORES: JERONIMO SALAZAR, ALVARO GUERRERO, ESTEBAN ACOSTA, KAREN RIVERA
package uiMain;

import java.util.ArrayList;

import gestorAplicacion.alojamiento.Alojamiento;
import gestorAplicacion.adminVuelos.Aerolinea;
import gestorAplicacion.adminVuelos.Tiquete;
import gestorAplicacion.adminVuelos.Vuelo;

//IMPLEMENTA LA INTERFACE GENERADORDETABLAS, PARA IMPRIMIR POR PANTALLA LOS DATOS PASADOS A LOS METODOS EN DETERMINADO FORMATO
//HACIENDO USO DE System.out.printf() (SE DETALLA EN LOS COMENTARIOS DE printEncabezadoAerolinea())
public class TablasConsola implements GeneradorDeTablas {

	//RECIBE UNA LISTA DE AEROLINEAS E IMPRIME POR PANTALLA LOS VUELOS DISPONIBLES (QUE NO ESTEN COMPLETOS) DE CADA AEROLINEA HACIENDO 
	//USO DE LOS METODOS printEncabezadoAerolinea(), printVuelos() Y printSeparador().
	@Override
	public void mostrarTablaDeVuelosDisponiblesPorAerolineas(ArrayList<Aerolinea> aerolineas) 
	{
		for (int i = 0; i < aerolineas.size(); i++)
		{
			Aerolinea aerolinea = aerolineas.get(i);
			printEncabezadoAerolinea(aerolineas.get(i));
			printVuelos(aerolinea.vuelosDisponibles(aerolinea.getVuelos())); 
			printSeparador();
		}	
	}
	
	//RECIBE UNA LISTA DE AEROLINEAS E IMPRIME POR PANTALLA TODOS LOS VUELOS DE CADA AEROLINEA HACIENDO 
	//USO DE LOS METODOS printEncabezadoAerolinea(), printVuelos() Y printSeparador()
	@Override
	public void mostrarTablaDeVuelosPorAerolineas(ArrayList<Aerolinea> aerolineas) 
	{
		for (int i = 0; i < aerolineas.size(); i++)
		{
			Aerolinea aerolinea = aerolineas.get(i);
			printEncabezadoAerolinea(aerolineas.get(i));
			printVuelos(aerolinea.getVuelos()); 
			printSeparador();
		}	
	}
	
	//RECIBE UNA AEROLINEA Y SUS VUELOS, E IMPRIME POR PANTALLA ESTOS VUELOS HACIENDO 
	//USO DE LOS METODOS printEncabezadoAerolinea(), printVuelos() Y printSeparador()
	@Override
	public void mostrarTablaDeVuelos(Aerolinea aerolinea, ArrayList<Vuelo> vuelos) 
	{
		if (vuelos.size() != 0)
		{
			printEncabezadoAerolinea(aerolinea);
			printVuelos(vuelos);
			printSeparador();	
		}
	}
	
	//RECIBE UNA LISTA DE TIQUETES Y SE ENCARGA DE MOSTRAR POR PANTALLA CADA UNO DE LOS PASAJEROS ASOCIADOS A ESA LISTA DE TIQUETES
	@Override
	public void mostrarTablaDePasajeros(ArrayList<Tiquete> tiquetes) 
	{
		System.out.println("---------------------------------------------------------------");
		System.out.printf("%5s %12s %16s %17s","ID", "NOMBRE", "PASAPORTE", "EMAIL"+"\n");
		System.out.println("---------------------------------------------------------------");
		
		for (int i = 0; i < tiquetes.size(); i++){
			System.out.printf("%5s %13s %12s %26s",tiquetes.get(i).getId(), tiquetes.get(i).getPasajero().nombre, tiquetes.get(i).getPasajero().getPasaporte(), tiquetes.get(i).getPasajero().getEmail());
			System.out.println();  
		}
		System.out.println("---------------------------------------------------------------");
		System.out.println();
	}
	
	//RECIBE UNA LISTA DE AEROLINEAS Y SE ENCARGA DE MOSTRAR POR PANTALLA LOS NOMBRES DE ESAS AEROLINEAS
	@Override
	public void mostrarTablaDeAerolineas(ArrayList<Aerolinea> aerolineas) 
	{
		System.out.println("AEROLINEAS DISPONIBLES");
		System.out.println("----------------------");

		for(Aerolinea aerolinea:aerolineas) 
		{
			System.out.printf("%14s",aerolinea.getNombre());
			System.out.println();
		}
		System.out.println("----------------------");
	}
	
	//RECIBE UNA LISTA DE ALOJAMIENTOS E IMPRIME UNA TABLA CON LOS ATRIBUTOS DE CADA ALOJAMIENTO.
	public void mostrarTablaDeAlojamientos(ArrayList<Alojamiento> alojamientos)
	{
		System.out.println();
		System.out.println("-------------------------------------------------------------"); 
		System.out.printf("%10s %15s %18s %12s", "NOMBRE", "LOCACION", "PRECIO POR DIA", "ESTRELLAS");  
		System.out.println();  
		System.out.println("-------------------------------------------------------------");
		
		for (int j = 0; j < alojamientos.size(); j++) {
			System.out.format("%13s %11s %16s %11s", alojamientos.get(j).getNombre(), alojamientos.get(j).getLocacion(), alojamientos.get(j).getPrecio_dia(), alojamientos.get(j).getEstrellas());  
			System.out.println(); 
			}
		
		System.out.println("-------------------------------------------------------------");  
		System.out.println();
	}
	
	//IMPRIME POR PANTALLA UN ENCABEZADO CON EL NOMBRE DE LA AEROLINEA Y LOS ATRIBUTOS DE LOS VUELOS QUE POSEE LA AEROLINEA. 
	static void printEncabezadoAerolinea(Aerolinea aerolinea) 
	{
		System.out.println("VUELOS DISPONIBLES DE LA AEROLINEA " + aerolinea.getNombre().toUpperCase());
		System.out.println("--------------------------------------------------------------------------------------------------"); 
		System.out.printf("%4s %13s %12s %14s %12s %22s %12s", "ID", "PRECIO", "ORIGEN", "DESTINO", "FECHA", "HORA DE SALIDA", "AERONAVE");  
		System.out.println();  
		System.out.println("--------------------------------------------------------------------------------------------------");
		
		// System.out.printf() PERMITE DARLE UN FORMATO A LOS DATOS DE SALIDA
		// % INDICA QUE EN ESA POSICION SE VA A ESCRIBIR UN VALOR, SE PUEDEN PONER TANTOS COMO VARIABLES A MOSTRAR
		// ESTAS VARIABLES SE ESCRIBEN A CONTINUACION DE LAS COMMILLAS Y SEPARADAS POR COMAS
		// LA s INDICA QUE SE VA A MOSTRAR UNA CADENA DE CARACTERES, Y EL VALOR NUMERICO INDICA LA ALINEACION A LA DERECHA.
	}
	
	// SE ENCARGA DE RECORRER LOS VUELOS DE UNA AEROLINEA PARA IR IMPRIMIENDO, LINEA POR LINEA, LA INFORMACION PERTINENTE DE CADA UNO.
	static void printVuelos(ArrayList<Vuelo> vuelos) 
	{
		for (int j = 0; j < vuelos.size(); j++) 
		{
			System.out.format("%5s %12s %13s %13s %15s %11s %21s", vuelos.get(j).getID(), vuelos.get(j).getPrecio(), vuelos.get(j).getOrigen(),vuelos.get(j).getDestino(), vuelos.get(j).getFecha_de_salida(), vuelos.get(j).getHora_de_salida(), vuelos.get(j).getAeronave());  
			System.out.println(); 
		}
	}
	
	//IMPRIME POR PANTALLA UN SEPARADOR PARA LA TABLA DE VUELOS
	static void printSeparador() 
	{
		System.out.println("--------------------------------------------------------------------------------------------------");  
		System.out.println();	
	}





	
	

}
