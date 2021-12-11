package gestorAplicacion.hangar;
import gestorAplicacion.adminVuelos.*;

public abstract class Aeronave {
	// ATRIBUTOS
	public final int Gasto_gasolina = 120;
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

	public void ToString() {
		System.out.println("FALTA DEFINIR");
	}

	// BUSCAR SILLAS POR UBICACION Y TIPO
	public Silla buscarSillaPorUbicacionyTipo(Ubicacion ubicacion, String tipo) {

		if (tipo.equalsIgnoreCase("ECONOMICA")) {
			for (Silla i : SILLAS_ECONOMICAS) {
				if (i.isEstado() & i.getUbicacion().equals(ubicacion)) {
					// System.out.println("Su numero de silla es: "+i.getNumero_de_silla());
					return i;
				}
			}
		} else if (tipo.equalsIgnoreCase("EJECUTIVA")) {
			for (Silla i : SILLAS_EJECUTIVAS) {
				if (i.isEstado() & i.getUbicacion().equals(ubicacion)) {
					// System.out.println("Su numero de silla es: "+i.getNumero_de_silla());
					return i;
				}
			}
		}
		// System.out.println("Lo sentimos no tenemos disponible una silla con esas
		// caracter�stica, por favor vuelva a escoger ");
		return null;
	}

	public abstract int Calcular_Sillas_Ocupadas();

	public abstract double Calcular_Consumo_Gasolina(double distancia_en_km);
}
