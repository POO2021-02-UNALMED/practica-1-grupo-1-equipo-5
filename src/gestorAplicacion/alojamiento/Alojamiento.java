package gestorAplicacion.alojamiento;

import java.util.ArrayList;

public class Alojamiento {
	private String nombre;
	private String locacion;
	private long precio_dia;
	private int estrellas;
	private static ArrayList<Alojamiento> alojamientos = new ArrayList<Alojamiento>();

	//CONSTRUCTORES
	public Alojamiento(String nombre, String locacion, long precio_dia, int estrellas) {
		this.nombre = nombre;
		this.locacion = locacion;
		this.precio_dia = precio_dia;
		this.estrellas = estrellas;
		alojamientos.add(this);
	}


	//CALCULAR PRECIO DEL ALOJAMIENTO
	public int calcularPrecio(int dias) {
		return (int)( dias * this.precio_dia);
	}

	// BUSCAR ALOJAMIENTOS POR...

	public static ArrayList<Alojamiento> buscarAlojamientoPorUbicacion (String ubicacion) {
		ArrayList<Alojamiento> alojamientosEnUbicacion = new ArrayList<Alojamiento>();
		for (int i = 0; i < alojamientos.size(); i++)
		{
		  if (alojamientos.get(i).getLocacion().equals(ubicacion))
		  {
			  alojamientosEnUbicacion.add(alojamientos.get(i));
		  }
		}
		return alojamientosEnUbicacion;
	}

	public static Alojamiento buscarAlojamientoPorNombre(String nombre) {
		for (int i = 0; i < alojamientos.size(); i++)
		{
		  if (alojamientos.get(i).getNombre().equals(nombre))
		  {
			  return alojamientos.get(i);
		  }
		}
		return null;
	}

	//GETTERS Y SETTERS

		public void setLocacion(String locacion) {
			this.locacion = locacion;
		}

		public void setPrecio_dias(long precio_dias) {
			this.precio_dia = precio_dias;
		}

		public static ArrayList<Alojamiento> getAlojamientos() {
			return alojamientos;
		}

		public static void setAlojamientos(ArrayList<Alojamiento> alojamientos) {
			Alojamiento.alojamientos = alojamientos;
		}

		public long getPrecio_dia() {
			return precio_dia;
		}

		public void setPrecio_dia(long precio_dia) {
			this.precio_dia = precio_dia;
		}

		public String getLocacion() {
			return locacion;
		}

		public int getEstrellas() {
			return estrellas;
		}

		public void setEstrellas(int estrellas) {
			this.estrellas = estrellas;
		}

		public String getNombre() {
			return nombre;
		}

		public void setNombre(String nombre) {
			this.nombre = nombre;
		}

	}

