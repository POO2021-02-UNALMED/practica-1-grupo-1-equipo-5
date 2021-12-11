package gestorAplicacion.adminVuelos;
import java.io.Serializable;
import java.util.ArrayList;
import gestorAplicacion.hangar.*;

public class Aerolinea implements Serializable{

	private static final long serialVersionUID = 1L;
	private String nombre;
	private ArrayList<Aeronave> aeronaves = new ArrayList<Aeronave>();
	private ArrayList<Vuelo> vuelos = new ArrayList<Vuelo>();
	private static ArrayList<Aerolinea> aerolineas = new ArrayList<Aerolinea>();

	public Aerolinea(String nombre) {
		this.nombre = nombre;
		aerolineas.add(this);
	}

	// AGREGAR AEROLINEA
	public static void agregarAerolinea(String nombre,ArrayList<Aeronave> aeronaves,ArrayList<Vuelo> vuelos) {
		Aerolinea nueva_aerolinea = new Aerolinea(nombre);
		nueva_aerolinea.setAviones(aeronaves);
		nueva_aerolinea.setVuelos(vuelos);
	}


	//BUSCAR AEROLINEA
	public static Aerolinea buscarAerolineaPorNombre(String nombre2)
	{
		Aerolinea retorno = null;
		for (int i = 0; i < Aerolinea.getAerolineas().size(); i++)
		{
			if( Aerolinea.getAerolineas().get(i).getNombre().equalsIgnoreCase(nombre2))
			{

				retorno=  Aerolinea.getAerolineas().get(i);
			}
		}
		return retorno;
	}

	//BUSCAR VUELO POR...
	public Vuelo buscarVueloPorID (ArrayList<Vuelo> vuelos, int ID)
	{
		for (int i = 0; i < vuelos.size(); i++)
		{
		  if (vuelos.get(i).getID() == ID )
		  {
			  return vuelos.get(i);
		  }
		}
		return null;
	}

	public Vuelo buscarVueloPorAeronave (ArrayList<Vuelo> vuelos, String nombre_Aeronave)
	{
		for (int i = 0; i < vuelos.size(); i++)
		{
		  if (vuelos.get(i).getAeronave().getNombre().equals(nombre_Aeronave) )
		  {
			  return vuelos.get(i);
		  }
		}
		return null;
	}

	public ArrayList<Vuelo> buscarVueloPorDestino (ArrayList<Vuelo> vuelos, String destino)
	{
		ArrayList<Vuelo> vuelosPorDestino = new ArrayList<Vuelo>();
		for (int i = 0; i < vuelos.size(); i++)
		{
		  if (vuelos.get(i).getDestino().equalsIgnoreCase(destino)) // cambio del equals
		  {
			  vuelosPorDestino.add(vuelos.get(i));
		  }
		}
		return vuelosPorDestino;
	}



	public ArrayList<Vuelo> buscarVueloPorFecha (ArrayList<Vuelo> vuelos, String fecha)
	{
		ArrayList<Vuelo> vuelosPorFecha = new ArrayList<Vuelo>();
		for (int i = 0; i < vuelos.size(); i++)
		{
		  if (vuelos.get(i).getFecha_de_salida().equals(fecha))
		  {
			  vuelosPorFecha.add(vuelos.get(i));
		  }
		}
		return vuelosPorFecha;
	}

	// BUSCAR TIQUETE POR ID
	public static Tiquete BuscarTiquete(int ID)
	{
		ArrayList<Aerolinea> aerolineasDisponibles = Aerolinea.getAerolineas();
		for (int i = 0; i < aerolineasDisponibles.size(); i++)
		{
			Aerolinea aerolinea = aerolineasDisponibles.get(i);
			for (int j = 0; j < aerolinea.getVuelos().size(); j++)
			{

				Vuelo vuelo = aerolinea.getVuelos().get(j);
				Tiquete tiquete_buscado = vuelo.buscarTiquetePorID(vuelo.getTiquetes(), ID);
				if (tiquete_buscado != null)
				{
					return tiquete_buscado;
				}
			}
		}
		return null;
	}

	//VUELOS DISPONIBLES
	public ArrayList<Vuelo> vuelosDisponibles(ArrayList<Vuelo> vuelos)
	{
		ArrayList<Vuelo> vuelosDisponibles = new ArrayList<Vuelo>();
		for (int i = 0; i < vuelos.size(); i++)
		{
			if (!vuelos.get(i).isEstaCompleto())
			{
				vuelosDisponibles.add(vuelos.get(i));
			}
		}
		return vuelosDisponibles;
	}

	// AGREGAR O CANCELAR UN VUELO
	public void agregarVuelo(Vuelo vuelo)
	{
		vuelos.add(vuelo);
	}

	public Boolean cancelarVuelo(int vuelo_a_eliminar)
	{
		for (int i = 0; i < vuelos.size(); i++)
		{
		  if (vuelos.get(i).getID() == vuelo_a_eliminar )
		  {
			  vuelos.remove(i);
			  return true;
		  }
		}
		return false;
	}

	// SETTERS Y GETTERS

	public String getNombre() {
		return nombre;
	}


	public void setNombre(String nombre) {
		this.nombre = nombre;
	}


	public ArrayList<Vuelo> getVuelos() {
		return vuelos;
	}


	public void setVuelos(ArrayList<Vuelo> vuelos) {
		this.vuelos = vuelos;
	}

	public ArrayList<Aeronave> getAeronaves() {
		return aeronaves;
	}

	public void setAviones(ArrayList<Aeronave> aviones) {
		this.aeronaves = aviones;
	}

	public static ArrayList<Aerolinea> getAerolineas() {
		return aerolineas;
	}

	public static void setAerolineas(ArrayList<Aerolinea> aerolineas) {
		Aerolinea.aerolineas = aerolineas;
	}

}
