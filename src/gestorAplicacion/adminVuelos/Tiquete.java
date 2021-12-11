package gestorAplicacion.adminVuelos;
import java.io.Serializable;
import gestorAplicacion.hangar.*;


import gestorAplicacion.alojamiento.Alojamiento;

public class Tiquete implements Serializable {
	private static final long serialVersionUID = 1L;
	private int id;
	private int precio;
	private Vuelo vuelo;
	private Silla silla;
	private Pasajero pasajero;
	private Alojamiento alojamiento;

	//CONSTRUCTORES

	public Tiquete(int id, int precio, Vuelo vuelo) {
		this.id = id;
		this.precio = precio;
		this.vuelo = vuelo;
		vuelo.getTiquetes().add(this);
	}

	public Tiquete(int id, int precio, Vuelo vuelo, Silla silla, Pasajero pasajero, Alojamiento alojamiento) {
		this.id = id;
		this.precio = precio;
		this.vuelo = vuelo;
		this.silla = silla;
		this.pasajero = pasajero;
		this.alojamiento = alojamiento;
		vuelo.getTiquetes().add(this);
	}

	// METODOS

	/*Este metodo no tiene parametros de entra o de salida porque el valor resultante
	  es guardado en el atributo precio de cada instancia*/
	public boolean asignarPrecio() {
		boolean hayDescuento = false;
		int precio_total=vuelo.getPrecio() + this.getSilla().getClase().getPrecio();
		if (pasajero.getEdad()<5) {
			hayDescuento = true;
			this.precio = (int) (precio_total - (precio_total*0.25));
		}else if (pasajero.getEdad()>5 && pasajero.getEdad()<=10){
			this.precio = (int) (precio_total - (precio_total*0.15));
			hayDescuento = true;
		}else {
			this.precio = precio_total;
		}
		return hayDescuento;
	}

	/*Este metodo sobreescribe asignarPrecio y tiene parametros de entra numero de dias para el alojamiento porque el valor resultante
	  es guardado en el atributo precio de cada instancia*/
	public void asignarPrecio(int num_dias) {
		int precio_total=vuelo.getPrecio()+ alojamiento.calcularPrecio(num_dias) + this.getSilla().getClase().getPrecio();
		if (pasajero.getEdad()<5) {
			this.precio = (int) (precio_total - (precio_total*0.15));
		}else if (pasajero.getEdad()>5 && pasajero.getEdad()<=10){
			this.precio = (int) (precio_total - (precio_total*0.15));
		}else {
			this.precio = precio_total;
		}
	}

	public void confimarCompra() {
		this.vuelo.getTiquetes().add(this);
	}

	public String toString()
	{
		if (this.alojamiento==null) {
			return  "*************************************\n"+
					"      Su compra ha sido exitosa\n"+
					"    Gracias por confiar en nostros\n"+
					"*************************************\n"+

					"------------------------------------\n"+
					"      Tiquete No."+ this.id + "\n"+
					"------------------------------------\n"+
					"Nombre Pasajero: " + pasajero.nombre + "\n" +
					"Fecha: " + vuelo.getFecha_de_salida() + "\n" +
					"Vuelo: " + vuelo.getID() + "\n" +
					"Num Silla: " + silla.getNumero_de_silla() + " "  + silla.getUbicacion() + "\n" +
					"Origen: " + vuelo.getOrigen() + "\n" +
					"Destino: " + vuelo.getDestino() + "\n" +
					"Precio Total: " + this.getPrecio() + "\n" +
					"------------------------------------\n";


		}else {
			
			return  "*************************************\n"+
					"      Su compra ha sido exitosa\n"+
					"    Gracias por confiar en nostros\n"+
					"*************************************\n"+
					"------------------------------------\n"+
					"      Tiquete No."+ this.id + "\n"+
					"------------------------------------\n"+
					"Nombre Pasajero: " + pasajero.nombre + "\n" +
					"Fecha: " + vuelo.getFecha_de_salida() + "\n" +
					"Vuelo: " + vuelo.getID() + "\n" +
					"Silla: " + silla.getNumero_de_silla() + " - "  + silla.getUbicacion()  + "\n" +
					"Origen: " + vuelo.getOrigen() + "\n" +
					"Destino: " + vuelo.getDestino() + "\n" +
					"Alojamiento: " + alojamiento.getNombre() + "\n" +
					"Precio Total: " + this.getPrecio() + "\n" +
					"------------------------------------\n";

		}
	}

	//GETTERS Y SETTERS

	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public int getPrecio() {
		return precio;
	}
	public void setPrecio(int precio) {
		this.precio = precio;
	}
	public Vuelo getVuelo() {
		return vuelo;
	}
	public void setVuelo(Vuelo vuelo) {
		this.vuelo = vuelo;
	}
	public Silla getSilla() {
		return silla;
	}
	public void setSilla(Silla silla) {
		this.silla = silla;
	}
	public Pasajero getPasajero() {
		return pasajero;
	}
	public void setPasajero(Pasajero pasajero) {
		this.pasajero = pasajero;
	}
	public Alojamiento getAlojamiento() {
		return alojamiento;
	}
	public void setAlojamiento(Alojamiento alojamiento) {
		this.alojamiento = alojamiento;
	}
}
