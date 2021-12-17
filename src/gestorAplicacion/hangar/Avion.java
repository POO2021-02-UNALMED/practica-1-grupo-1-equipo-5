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

		// LA VARIABLE UBICACION VA CAMBIANDO SU VALOR SEGUN LOS SIGUIENTES PROCESOS, SE
		// USA PARA LA ASIGNACION DEL ATRIBUTO UBICACION DE LAS SILLAS.
		Ubicacion ubicacion = null;

		// EL SIGUIENTE PROCESO CREA Y AGREGA SILLAS A LA LISTA DE SILLAS EJECUTIVAS QUE
		// POSEE LA CLASE AVION("HEREDA LA LISTA DE AERONAVE")
		// NOTA: LAS SILLAS DE TIPO EJECUTIVA SE REPARTEN EN GRUPOS DE 4 EN FILA
		// SEPARADAS POR UN PASILLO.(POR TANTO NO HAY UBICACION CENTRAL)
		for (int numPosicion = 0; numPosicion < NUM_SILLAS_EJECUTIVAS; numPosicion++) {
			if (numPosicion % 4 == 0 || numPosicion % 4 == 3) {
				ubicacion = Ubicacion.VENTANA;
			} else {
				ubicacion = Ubicacion.PASILLO;
			}

			this.getSILLASEJECUTIVAS()[numPosicion] = new Silla(Clase.EJECUTIVA, numPosicion, ubicacion);
		}

		// EL SIGUIENTE PROCESO CREA Y AGREGA SILLAS A LA LISTA DE SILLAS ECONOMICAS QUE
		// POSEE LA CLASE AVION("HEREDA LA LISTA DE AERONAVE")
		// NOTA: LAS SILLAS DE TIPO ECONOMICA SE REPARTEN EN GRUPOS DE 6 EN FILA
		// SEPARADAS POR UN PASILLO
		for (int numPosicion = 0; numPosicion < NUM_SILLAS_ECONOMICAS; numPosicion++) {
			if (numPosicion % 6 == 0 || numPosicion % 6 == 5) {
				ubicacion = Ubicacion.VENTANA;
			} else if (numPosicion % 6 == 1 || numPosicion % 6 == 4) {
				ubicacion = Ubicacion.CENTRAL;
			} else if (numPosicion % 6 == 2 || numPosicion % 6 == 3) {
				ubicacion = Ubicacion.PASILLO;
			}
			this.getSILLASECONOMICAS()[numPosicion] = new Silla(Clase.ECONOMICA, numPosicion, ubicacion);
		}
	}

	@Override
	public String toString() {
		return this.getNombre() + "_A";
	}

	public static int getNumSillasEconomicas() {
		return NUM_SILLAS_ECONOMICAS;
	}

	public static int getNumSillasEjecutivas() {
		return NUM_SILLAS_EJECUTIVAS;
	}

	// METODOS

	/*ESTE METODO RECIBE UN TIPO DE DATO DOUBLE DE LA DISTANCIA QUE HAY DESDE EL LUGAR DE ORIGEN AL LUGAR DE DESTINO
	Y RETONARNA EL COSTO TOTAL DE GASOLINA PARA RECORRER EL TRAYECTO*/
	public double Calcular_Consumo_Gasolina(double distancia_en_km) {
		double consumido;
		consumido = this.getGastoGasolina() * distancia_en_km;
		return consumido;
	}
}