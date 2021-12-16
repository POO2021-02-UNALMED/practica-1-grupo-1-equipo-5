package gestorAplicacion.hangar;
import gestorAplicacion.adminVuelos.*;
import java.io.Serializable;
public abstract class Aeronave implements Serializable{

	private static final long serialVersionUID = 1L;
	// ATRIBUTOS
	protected final int Gasto_gasolina = 120;
	private String nombre;
	private Aerolinea aerolinea;
	private boolean descompuesto;
	private Silla[] SILLAS_ECONOMICAS;
	private Silla[] SILLAS_EJECUTIVAS;

	// CONTRUCTOR
	public Aeronave(String nombre, Aerolinea aerolinea) {
		this.nombre = nombre;
		this.aerolinea = aerolinea;
	}

	// GET AND SET
	public Aerolinea getAerolinea() {
		return aerolinea;
	}

	public void setAerolinea(Aerolinea aerolinea) {
		this.aerolinea = aerolinea;
	}

	public Silla[] getSILLASECONOMICAS() {
		return SILLAS_ECONOMICAS;
	}

	public void setSILLASECONOMICAS(Silla[] sILLAS_ECONOMICAS) {
		SILLAS_ECONOMICAS = sILLAS_ECONOMICAS;
	}

	public Silla[] getSILLASEJECUTIVAS() {
		return SILLAS_EJECUTIVAS;
	}

	public void setSILLASEJECUTIVAS(Silla[] sILLAS_EJECUTIVAS) {
		SILLAS_EJECUTIVAS = sILLAS_EJECUTIVAS;
	}

	public int getGastoGasolina() {
		return Gasto_gasolina;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}



	// METODOS

	public boolean isDescompuesto() {
		return descompuesto;
	}

	public void setDescompuesto(boolean descompuesto) {
		this.descompuesto = descompuesto;
	}

	public String toString() {
		return this.nombre;
	}

	// BUSCAR SILLAS POR UBICACION Y TIPO
//	EN ESTE METODO SE RECIBE UNA UBICACION(UBICACION) Y UN TIPO(STRING), LOS CUALES UTILIZA PARA BUSCAR DENTRO DE
//	LAS LISTAS DE LA AERONAVE QUE LO LLAMA UNA SILLA CON LA UBICACION Y TIPO QUE SE INGRESAN.
	public Silla buscarSillaPorUbicacionyTipo(Ubicacion ubicacion, String tipo) {

		if (tipo.equalsIgnoreCase("ECONOMICA")) {
			for (Silla i : SILLAS_ECONOMICAS) {
				if (i.isEstado() & i.getUbicacion().equals(ubicacion)) {
					return i;
				}
			}
		} else if (tipo.equalsIgnoreCase("EJECUTIVA")) {
			for (Silla i : SILLAS_EJECUTIVAS) {
				if (i.isEstado() & i.getUbicacion().equals(ubicacion)) {
					return i;
				}
			}
		}
		return null;
	}
	/*Este método recorreran los arreglos de sillas ejecutivos y economicas de cada avión y avioneta
	para verificar la cantidad de sillas que estan ocupadas y retornaran dicha cantidad*/
	public abstract int Calcular_Sillas_Ocupadas();

	/*Este método recibe un tipo de dato double de la distancia que hay desde el lugar de origen al lugar de destino
	y retornara el costo total de gasolina por recorrer el trayecto*/
	public abstract double Calcular_Consumo_Gasolina(double distancia_en_km);
}
