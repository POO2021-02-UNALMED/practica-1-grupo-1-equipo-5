package baseDatos;

import java.io.*;
import java.util.ArrayList;

import gestorAplicacion.alojamiento.Alojamiento;
import gestorAplicacion.adminVuelos.*;
import gestorAplicacion.hangar.*;

public class Deserializador {
		
	private static File rutaTemp = new File("src"+File.separator+"basedatos"+File.separator+"temp");
	
	public static void deserializar() {
		File[] docs = rutaTemp.listFiles();
		FileInputStream archivo;
		ObjectInputStream guardado;
		
		
		for (File file : docs) {
			if (file.getAbsolutePath().contains("Aerolineas")) {
				try {
					archivo = new FileInputStream(file);
					guardado = new ObjectInputStream(archivo); 
					Aerolinea.setAerolineas((ArrayList<Aerolinea>) guardado.readObject());
				}catch(FileNotFoundException e) {
					e.printStackTrace();
				}catch(IOException e) {
					e.printStackTrace();
				}catch(ClassNotFoundException e) {
					e.printStackTrace();;
				}				
			}else if (file.getAbsolutePath().contains("Alojamientos")) {
				try {
				archivo = new FileInputStream(file);
				guardado = new ObjectInputStream(archivo);
				Alojamiento.setAlojamientos((ArrayList<Alojamiento>) guardado.readObject());
				}catch(FileNotFoundException e) {
					e.printStackTrace();
				}catch(IOException e) {
					e.printStackTrace();
				}catch(ClassNotFoundException e) {
					e.printStackTrace();;
				}
			}
		}
	}
}

			
						