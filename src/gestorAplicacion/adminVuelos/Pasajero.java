package gestorAplicacion.adminVuelos;
import java.io.Serializable;
public class Pasajero implements Serializable {
	
	private static final long serialVersionUID = 1L;
	private String pasaporte;
	public String nombre;
	private Tiquete tiquete;
	private int edad;
	private String email;

	public Pasajero(String pasaporte, String nombre, Tiquete tiquete, int edad, String email) {
		this.pasaporte = pasaporte;
		this.nombre = nombre;
		this.tiquete = tiquete;
		this.edad = edad;
		this.email = email;
		tiquete.setPasajero(this);
	}

	//GETTERS Y SETTERS

	public String getPasaporte() {
		return pasaporte;
	}
	public void setPasaporte(String pasaporte) {
		this.pasaporte = pasaporte;
	}
	public Tiquete getTiquete() {
		return tiquete;
	}
	public void setTiquete(Tiquete tiquete) {
		this.tiquete = tiquete;
	}
	public int getEdad() {
		return edad;
	}
	public void setEdad(int edad) {
		this.edad = edad;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}



}
