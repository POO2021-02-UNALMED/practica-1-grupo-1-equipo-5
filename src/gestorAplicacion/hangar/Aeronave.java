package gestorAplicacion.hangar;
import gestorAplicacion.adminVuelos.*;
import java.io.Serializable;
public abstract class Aeronave implements Serializable{

	private static final long serialVersionUID = 1L;
	// ATRIBUTOS
	protected final  int GASTO_GASOLINA = 120;
	private String nombre;
	private Aerolinea aerolinea;
	private boolean descompuesto;
	private Silla[] SILLAS_ECONOMICAS;
	private Silla[] SILLAS_EJECUTIVAS;

	// CONTRUCTOR
	protected Aeronave(String nombre, Aerolinea aerolinea) {
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
		return GASTO_GASOLINA;
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
	/*ESTE METODO RECORRAN LOS ARREGLOS DE SILLAS EJECUTIVOS Y ECONOMICAS DE CADA AVION Y AVIONETA 
	PARA VERIFICAR LA CANTIDAD DE SILLAS QUE ESTAN OCUPADAS Y RETORNAR DICHA CANTIDAD*/

	public String Calcular_Sillas_Ocupadas() {
		int cont = 0;
		for (Silla i : this.getSILLASECONOMICAS()) {
			if (i.isEstado()) {
				cont += 1;
			}
		}
		for (Silla j : this.getSILLASEJECUTIVAS()) {
			if (j.isEstado()) {
				cont += 1;
			}
		}
		return "Esta es la cantidad de silla ocupadas:"+cont;
	}

	/*ESTE METODO RECIBE UN TIPO DE DATO DOUBLE DE LA DISTANCIA QUE HAY DESDE EL LUGAR DE ORIGEN AL LUGAR DE DESTINO
	Y RETONARNA EL COSTO TOTAL DE GASOLINA PARA RECORRER EL TRAYECTO*/
	public abstract double Calcular_Consumo_Gasolina(double distancia_en_km);
}
