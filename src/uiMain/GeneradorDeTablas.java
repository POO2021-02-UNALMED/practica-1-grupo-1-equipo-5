package uiMain;
import java.util.ArrayList;
import gestorAplicacion.adminVuelos.*;
import gestorAplicacion.alojamiento.*;

public interface GeneradorDeTablas{
	public abstract void mostrarTablaDeVuelosDisponiblesPorAerolineas(ArrayList<Aerolinea> aerolineas);
	public abstract void mostrarTablaDeVuelosPorAerolineas(ArrayList<Aerolinea> aerolineas);
	public abstract void mostrarTablaDeVuelos(Aerolinea aerolineas, ArrayList<Vuelo> vuelos);
	public abstract void mostrarTablaDePasajeros(ArrayList<Tiquete> tiquetes);
	public abstract void mostrarTablaDeAerolineas(ArrayList<Aerolinea> aerolineas);
	public abstract void mostrarTablaDeAlojamientos(ArrayList<Alojamiento> alojamientos);
}
