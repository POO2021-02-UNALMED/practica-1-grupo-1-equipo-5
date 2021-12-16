package baseDatos;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.PrintWriter;

import gestorAplicacion.Alojamiento.Alojamiento;
import gestorAplicacion.adminVuelos.Aerolinea;

public class Serializador {
	private static File rutaArchivosTemp = new File("src"+File.separator+"basedatos"+File.separator+"temp");
	
	// SERIALIZAMOS LAS LISTAS DE VUELO Y AERONAVE QUE ESTAN EN CADA AEROLINEA
	public static void serializar() {
		FileOutputStream rutaArchivo; 
		ObjectOutputStream fichero_objeto; 
		File[] ficheros = rutaArchivosTemp.listFiles(); 
		PrintWriter pw;
		

		// CON PRINTWRITER BORRAMOS EL CONTENIDO PARA EVITAR SOBREESCRITURAS 
		for (File archivo : ficheros) { 
			try {
				//BORRA LO QUE HAY EN EL ARCHIVO QUE LE PASAMOS
				pw = new PrintWriter(archivo);
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			}
		}
		

		
		
		for (File archivo1 : ficheros) {

			if (archivo1.getAbsolutePath().contains("Aerolineas")) { 
				try {
					rutaArchivo = new FileOutputStream(archivo1); 
					fichero_objeto = new ObjectOutputStream(rutaArchivo);
					fichero_objeto.writeObject(Aerolinea.getAerolineas()); 
				} catch (FileNotFoundException e) {
					// TODO Auto-generated catch block
					e.printStackTrace(); 
				} catch (IOException e) {
					// TODO Auto-generated catch block e.printStackTrace();
					e.printStackTrace(); 
				}
			}else if(archivo1.getAbsolutePath().contains("Alojamientos")) { 
				try {
					rutaArchivo = new FileOutputStream(archivo1); 
					fichero_objeto = new ObjectOutputStream(rutaArchivo);
					fichero_objeto.writeObject(Alojamiento.getAlojamientos());
				}catch (FileNotFoundException e) {
					// TODO Auto-generated catch block
					e.printStackTrace(); 
				} catch (IOException e) {
					// TODO Auto-generated catch block e.printStackTrace();
					e.printStackTrace();
			}
		}
	}  
}
}
