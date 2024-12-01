__author__="juan camilo parra"
__license__="GPL"
__version__="1.0.0"
__Email__="juan.parrasan@campusucc.edu.co"

from silla import Silla
from Pasajero import Pasajero

class Avion:
    #------------------------------------------------------
    # Constructor
    #------------------------------------------------------
    def __init__(self):
        self.sillas = []
        for i in range(0, 50):
            if i <= 8:  
                clase = Silla.Clase.EJECUTIVA
                if i % 2 == 1:
                    ubicacion = Silla.Ubicacion.VENTANA
                else:
                    ubicacion = Silla.Ubicacion.PASILLO
            else:  
                clase = Silla.Clase.ECONOMICA
                if i % 3 == 1:
                    ubicacion = Silla.Ubicacion.VENTANA
                elif i % 3 == 2:
                    ubicacion = Silla.Ubicacion.CENTRO
                else:
                    ubicacion = Silla.Ubicacion.PASILLO
            self.sillas.append(Silla(i, clase, ubicacion))
               
    #------------------------------------
    # Metodos
    #------------------------------------

    # Busca una silla disponible que cumpla con las preferencias
    def asignarSilla(self, pasajero, clase, ubicacion):
        for silla in self.sillas:
            if not silla.sillaAsignada() and silla.darClase() == clase and silla.darUbicacion() == ubicacion:
                silla.asignarPasajero(pasajero) 
                return True
        return False
                   
    #  Elimina la reserva de un pasajero usando la cédula
    def eliminarReserva(self, cedula):
        for silla in self.sillas:
            if silla.sillaAsignada() and silla.darPasajero().darCedula() == cedula:
                silla.desasignarSilla()
                return True
        return False

    # Busca un pasajero por cédula y muestra su información
    def buscarPasajero(self, cedula):
        for silla in self.sillas:
            if silla.sillaAsignada() and silla.darPasajero().darCedula() == cedula:
                pasajero = silla.darPasajero()
                print(f"Pasajero encontrado en silla {silla.darNumero()}: Nombre: {pasajero.darNombre()}, Cédula: {pasajero.darCedula()}.")
                return
        print("Error: No se encontró un pasajero con esa cédula.")
        
    # Calcula el porcentaje de ocupación del avión
    def calcularPorcentajeOcupacion(self):
        total_asignadas = 0
        for silla in self.sillas:
            if silla.sillaAsignada():
                total_asignadas += 1
        porcentajeOcupacion = (total_asignadas / len(self.sillas)) * 100
        return porcentajeOcupacion
    
#------------------------------------------------------------------------------------------------------------------------------------   
    #---------------------------------------------------------------------------------------
    # Tarea 04 - 12/11/24
    # Para cada uno de los problemas que se plantean a continuación, escriba el 
    # método que lo resuelve. No olvide identificar primero el patrón de algoritmo que se 
    # necesita y usar las guías que se dieron en secciones anteriores
    #-----------------------------------------------------------------------------------------
    
    # Calcular el numero de sillas ejecutivas ocupadas en el avion
    def contarSillasEjecutivasOcupadas(self):
        totalOcupadas = 0
        for silla in self.sillas:
            if silla.darClase() == Silla.Clase.EJECUTIVA and silla.sillaAsignada():
                totalOcupadas += 1
        return totalOcupadas
    
    # Localizar la silla en la que se encuentra el pasajero identificado con la cédula que 
    # se entrega como parámetro. Si no hay ningún pasajero en clase ejecutiva con esa 
    # cédula, el método retorna null 
    def buscarPasajeroEjecutivo(self, cedula:str):
        for silla in self.sillas:
            if silla.darClase() == Silla.Clase.EJECUTIVA and silla.sillaAsignada() and silla.darPasajero().darCedula() == cedula:
                return silla  
        return None  
    
    # Localizar una silla económica disponible, en una localización dada (ventana, 
    # centro o pasillo). Si no existe ninguna, el método retorna null :
    def buscarSillaEconomicaLibre (self, ubicacion: Silla.Ubicacion, pasajero: Pasajero):
        for silla in self.sillas:
            if not silla.sillaAsignada() and silla.darClase() == silla.clase.ECONOMICA and silla.darUbicacion() == ubicacion:
                return silla
        return None
    
    # Asignar al pasajero que se recibe como parámetro una silla en clase económica 
    # que esté libre (en la ubicación pedida). Si el proceso tiene éxito, el método retorna 
    # verdadero. En caso contrario, retorna falso:
    def asignarSillaEconomica(self, ubicacion, pasajero):
        for silla in self.sillas:
            if not silla.sillaAsignada() and silla.darClase() == Silla.Clase.ECONOMICA and silla.darUbicacion() == ubicacion:
                silla.asignarPasajero(pasajero)
                return True
        return False  

    # Anular la reserva en clase ejecutiva que tenía el pasajero con la cédula dada.
    # Retorna verdadero si el proceso tiene éxito
    def anularReservaEjecutivo(self, cedula: str) :
         for silla in self.sillas:
             if silla.darClase() == silla.clase.EJECUTIVA and silla.sillaAsignada() and silla.darPasajero().darCedula() == cedula:
                 silla.desasignarsilla
                 return True
             return False
     
    # Contar el número de puestos disponibles en una ventana, en la zona económica
    # del avión:
    def contarVentanasEconomica(self):
        ventanasLibres = 0
        for silla in self.sillas:
            if silla.darClase() == Silla.Clase.ECONOMICA and not silla.sillaAsignada() and silla.darUbicacion() == Silla.Ubicacion.VENTANA:
                ventanasLibres += 1
        return ventanasLibres
    
    # Informar si en la zona económica del avión hay dos personas que se llamen igual.
    # Patrón de doble recorrido: 
    def hayDosHomonimosEconomica(self):
        for i in range(len(self.sillas)):
            if self.sillas[i].sillaAsignada():
                nombreSilla = self.sillas[i].darPasajero().darNombre()
                for j in range(i + 1, len(self.sillas)):
                    if self.sillas[j].sillaAsignada():
                        nombreSilla2 = self.sillas[j].darPasajero().darNombre()
                        if nombreSilla == nombreSilla2:
                            return True
        return False
#-------------------------------------------------------------------------------------------------------------------------------    

