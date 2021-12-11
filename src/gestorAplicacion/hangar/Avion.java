package gestorAplicacion.hangar;
import gestorAplicacion.adminVuelos.*;

public class Avion extends Aeronave {
	private final static int NUM_SILLAS_ECONOMICAS = 24;
	private final static int NUM_SILLAS_EJECUTIVAS = 12;

	// CONSTRUCTOR
	public Avion(String nombre, Aerolinea aerolinea) {
		super(nombre, aerolinea);
		this.setSILLASECONOMICAS(new Silla[NUM_SILLAS_ECONOMICAS]);
		this.setSILLASEJECUTIVAS(new Silla[NUM_SILLAS_EJECUTIVAS]);
	
		Ubicacion ubicacion = null;
		for (int numPosicion =0; numPosicion<NUM_SILLAS_EJECUTIVAS;numPosicion++) {
			if (numPosicion%4 ==0 || numPosicion%4==3) {
				ubicacion = Ubicacion.VENTANA;
			}
			else {
				ubicacion = Ubicacion.PASILLO;
			}
			
			this.getSILLASEJECUTIVAS()[numPosicion]= new Silla(Clase.EJECUTIVA,numPosicion,ubicacion);
		}
		
		for (int numPosicion =0; numPosicion<NUM_SILLAS_ECONOMICAS;numPosicion++) {
			if (numPosicion%6 ==0 || numPosicion%6==5) {
				ubicacion = Ubicacion.VENTANA;
			}
			else if (numPosicion%6 ==1 || numPosicion%6==4) {
				ubicacion = Ubicacion.CENTRAL;
			}
			else if (numPosicion%6==2 || numPosicion%6 ==3){
				ubicacion = Ubicacion.PASILLO;
			}
			this.getSILLASECONOMICAS()[numPosicion]= new Silla(Clase.ECONOMICA,numPosicion,ubicacion);
		}
	}

	@Override
	public String toString() {
		return this.getNombre();
	}

	public static int getNumSillasEconomicas() {
		return NUM_SILLAS_ECONOMICAS;
	}

	public static int getNumSillasEjecutivas() {
		return NUM_SILLAS_EJECUTIVAS;
	}

	// METODOS

	public int Calcular_Sillas_Ocupadas() {
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
		return cont;
	}

	public double Calcular_Consumo_Gasolina(double distancia_en_km) {
		double consumido;
		consumido = this.getGastoGasolina() * distancia_en_km;
		return consumido;
	}
}
