package gestorAplicacion;
public class Tiquete {
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
		return  "Nombre Pasajero: " + pasajero.nombre + "\n" + 
				"Fecha: " + vuelo.getFecha_de_salida() + "\n" + 
				"Vuelo: " + vuelo.getID() + "\n" + 
				"Origen: " + vuelo.getOrigen() + "\n" + 
				"Destino: " + vuelo.getDestino() + "\n" + 
				"Alojamiento: " + alojamiento.getNombre() + "\n" + 
				"Precio Total: " + this.getPrecio() + "\n" +
				"*************************************\n"+
				"      Su compra ha sido exitosa\n"+
				"    Gracias por confiar en nostros\n"+
				"*************************************\n";
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
