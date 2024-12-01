__author__="juan camilo parra"
__license__="GPL"
__version__="1.0.0"
__Email__="juan.parrasan@campusucc.edu.co"

from enum import Enum

class Tipo(Enum):
    VENTA = 1
    ABASTECIMIENTO = 2

class Transaccion:
    def __init__(self, tipo: Tipo, cantidad: int, fecha: str):
    #------------------------------------------------------------------
    # Constructor
    #-------------------------------------------------------------------
        self.tipo = tipo
        self.cantidad = cantidad
        self.fecha = fecha

    #--------------------------------------------------------------------
    # Getters
    #--------------------------------------------------------------------
    def darTipo(self):
        return self.tipo

    def darCantidad(self):
        return self.cantidad

    def darFecha(self):
        return self.fecha
    
    #-------------------------------------------------------------------
    # Setters
    #-------------------------------------------------------------------
    def cambiarTipo(self, tipo: Tipo):
        self.tipo = tipo
        
    def cambiarCantidad(self, cantidad):
        self.cantidad = cantidad
        
    def cambiarFecha(self, fecha):
        self.fecha = fecha
