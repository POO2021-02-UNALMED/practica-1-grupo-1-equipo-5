// INTERFACE PARA LA GENERACION DE TABLAS
// AUTORES: JERONIMO SALAZAR, ALVARO GUERRERO, ESTEBAN ACOSTA, KAREN RIVERA
package uiMain;
import java.util.ArrayList;
import gestorAplicacion.adminVuelos.*;
import gestorAplicacion.alojamiento.*;

// SU PROPOSITO ES HACER QUE LAS CLASES QUE IMPLEMENTEN LA INTERFACE, MUESTREN TABLAS DE DATOS EN EL FORMATO QUE SE LE QUIERA DAR A LA TABLA
public interface GeneradorDeTablas{
	// METODOS DE LA INTERFACE
	public abstract void mostrarTablaDeVuelosDisponiblesPorAerolineas(ArrayList<Aerolinea> aerolineas);
	public abstract void mostrarTablaDeVuelosPorAerolineas(ArrayList<Aerolinea> aerolineas);
	public abstract void mostrarTablaDeVuelos(Aerolinea aerolineas, ArrayList<Vuelo> vuelos);
	public abstract void mostrarTablaDePasajeros(ArrayList<Tiquete> tiquetes);
	public abstract void mostrarTablaDeAerolineas(ArrayList<Aerolinea> aerolineas);
	public abstract void mostrarTablaDeAlojamientos(ArrayList<Alojamiento> alojamientos);
}
