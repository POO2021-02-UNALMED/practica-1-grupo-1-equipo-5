class Pasajero:

    def __init__(self, pasaporte, nombre, tiquete, edad, email):
        self._pasaporte = pasaporte
        self.nombre = nombre
        self._tiquete = tiquete
        self._edad = edad
        self._email = email
        tiquete.setPasajero(self)

    #GETTERS Y SETTERS

    def getPasaporte(self):
        return self._pasaporte

    def setPasaporte(self, pasaporte):
        self._pasaporte = pasaporte

    def getTiquete(self):
        return self._tiquete

    def setTiquete(self, tiquete):
        self._tiquete = tiquete

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getEmail(self):
        return self._email
        
    def setEmail(self, email):
        self._email = email


