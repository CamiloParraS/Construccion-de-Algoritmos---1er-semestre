__author__="juan camilo parra"
__license__="GPL"
__version__="1.0.0"
__Email__="juan.parrasan@campusucc.edu.co"

from enum import Enum

class Silla:

    #-------------------------------------------
    # Enumeraciones
    #-------------------------------------------
    
    # Enumeraciones Clase Silla
    class Clase(Enum):
        EJECUTIVA = 1  
        ECONOMICA = 2 

    # Enumeraciones Ubicacion Silla
    class Ubicacion(Enum):
        VENTANA = 1   
        CENTRO = 2    
        PASILLO = 3   

    #-------------------------------------------
    # Atributos
    #-------------------------------------------
    def __init__(self, pNumero, pClase, pUbicacion):
        self.__numero = pNumero
        self.__clase = pClase
        self.__ubicacion = pUbicacion
        self.__pasajero = None

    # Asigna la silla al pasajero 'pPasajero"
    def asignarPasajero(self, pPasajero):
        self.__pasajero = pPasajero

    # Quita al pasajero que se encuentra en la silla, dejandola desocupada
    def desasignarSilla(self):
        self.__pasajero = None
        
    # Informa si la silla esta ocupada
    def sillaAsignada(self):
        return self.__pasajero is not None


#------------------------------------------------------
# SOMETHINGH HELP ME
#-------------------------------------------------------