__author__="juan camilo parra"
__license__="GPL"
__version__="1.0.0"
__Email__="juan.parrasan@campusucc.edu.co"

class Pasajero: 
    #----------------------------------- 
    # Atributos 
    #----------------------------------- 
    #-----------------------------------
    # Constructor
    #-----------------------------------
    def __init__(self, pCedula, pNombre): 
        self.cedula = pCedula  
        self.nombre = pNombre   
    
    #----------------------------------- 
    # Métodos 
    #----------------------------------- 
    
    def darCedula(self):
        return self.cedula  
 
    def darNombre(self): 
        return self.nombre  