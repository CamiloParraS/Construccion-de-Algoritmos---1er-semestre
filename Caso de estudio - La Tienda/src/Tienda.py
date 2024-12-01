__author__="juan camilo parra"
__license__="GPL"
__version__="1.0.0"
__Email__="juan.parrasan@campusucc.edu.co"

import sys
sys.path.append('C:/Users/USUARIO/Camilo/Programacion/Caso-Estudio-LaTienda/src')
from Producto import Producto
from Tipo import Tipo

class Tienda:

#----------------------------------------------------------------
# Constructor
# ----------------------------------------------------------------
    #__method__= 'constructor'
    #__params__ = 'Ninguno'
    #def __init__(self):
    #    self.__producto1 = None
    #    self.__producto2 = None
    #   self.__producto3 = None
    #    self.__producto4 = None 
    #    self.__dineroCaja:float = 0.0
    
    def __init__(self):
        self.__producto1 = Producto("", Tipo.PAPELERIA, 0, 0, 0, False, 'A')  
        self.__producto2 = Producto("", Tipo.FARMACIA, 0, 0, 0, False, 'A')  
        self.__producto3 = Producto("", Tipo.PAPELERIA, 0, 0, 0, False, 'A')
        self.__producto4 = Producto("", Tipo.SUPERMERCADO, 0, 0, 0, False, 'A')
        self.__dineroCaja = 0.0

#----------------------------------------------------------------
# Metodos Modificadores
#----------------------------------------------------------------
    __method__='Producto1'
    __params__='nombre, tipo, nValorUnitario:float, cantidadBodega, nSubsidiado:bool, nCalidad'
    __returns__='Ninguna'
    __descriptions__='Este metodo crea el producto 1'
    pass
#----------------------------------------------------------------
# Metodos
#----------------------------------------------------------------
    __method__='Producto1'
    __params__='nombre, tipo, nValorUnitario:float, cantidadBodega, nSubsidiado:bool, nCalidad'
    __returns__='Ninguna'
    __descriptions__='Este metodo crea el producto 1'
    def CrearProducto1(self, nombre, tipo, nValorUnitario: float, cantidadBodega, cantidadMinima: int, nSubsidiado: bool, ncalidad):
        self.__producto1 = Producto(nombre, tipo, nValorUnitario, cantidadBodega, cantidadMinima, nSubsidiado, ncalidad)
    
    __method__ = "AbastecerTienda"
    __parameter__ = "ninguno"
    __returns__ = "Ninguno"
    __Description__ = "metodo que abastece de cuatro productos la tienda"
    def AbastecerTienda(self):
        self.__producto1 = Producto("lapiz", Tipo.PAPELERIA, 1000, 20, 5, False, 'A')
        self.__producto2 = Producto("Aspirina", Tipo.FARMACIA, 800, 50, 2, True, 'A')
        self.__producto3 = Producto("Borrador", Tipo.PAPELERIA, 700, 80, 10, False, 'A')
        self.__producto4 = Producto("Pan", Tipo.SUPERMERCADO, 300, 50, 4, False, 'A')
    
    __method__='DarProucto1'
    __params__='Ninguno'
    __returns__='Producto1'
    __descriptions__='Este metodo retorna la informacion de producto 1'
    def DarProducto1(self):
        return self.__producto1
        
    __method__='DarProucto2'
    __params__='Ninguno'
    __returns__='Producto2'
    __descriptions__='Este metodo retorna la informacion de producto 2'
    def DarProducto2(self):
        return self.__producto2
        
    __method__='DarProucto3'
    __params__='Ninguno'
    __returns__='Producto3'
    __descriptions__='Este metodo retorna la informacion de producto 3'
    def DarProducto3(self):
        return self.__producto3
        
    __method__='DarProucto4'
    __params__='Ninguno'
    __returns__='Producto4'
    __descriptions__='Este metodo retorna la informacion de producto 4'
    def DarProducto4(self):
        return self.__producto4
                
    __method__='DarDineroCaja'
    __params__='Ninguno'
    __returns__='DineroCaja'
    __descriptions__='Este metodo retorna la informacion de producto 1'
    def darDineroCaja(self):
        return self.__dineroCaja

    __method__ = "VenderDeTodo"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguno"
    __Description__ = "metodo que calcula la cantidad disponible del producto 1 y vende esa cantidad de los demas"
    def VenderDeTodo(self):
        cuanto = self.__producto1.DarCantidadBodega()
        self.__producto2.Vender(cuanto)
        self.__producto3.Vender(cuanto)
        self.__producto4.Vender(cuanto)
        
        
    #---------------------------------------------------------------------------
    # Tarea 05
    #---------------------------------------------------------------------------   
     
    # Vender una cierta candtidad del producto cuyo nombre es igual al recibido como parametro
    # El metodo retorna el numero de unidades efectivamente vendidas. 
    # Suponga que el nombre que se recibe como parametro corresponde a uno de los productos de la tienda
    # Utilice el metodo vender de la clase producto como parte de la solucion
    
    def venderProducto(self, pNombreProducto, pCantidad:int):
        if self.__producto1.DarNombre() == pNombreProducto:
            return self.__producto1.Vender(pCantidad)
        elif self.__producto2.DarNombre() == pNombreProducto:
            return self.__producto2.Vender(pCantidad)
        elif self.__producto3.DarNombre() == pNombreProducto:
            return self.__producto3.Vender(pCantidad)
        elif self.__producto4.DarNombre() == pNombreProducto:
            return self.__producto4.Vender(pCantidad)
        else:
            return 0

    # Calcular el numero de productos de papeleria que se venden en la tienda 
    
    def cuantosPapeleria(self):
        vendidosPapeleria = 0
        if self.__producto1.DarTIpo() == Tipo.PAPELERIA:
            vendidosPapeleria += self.__producto1.DarCantidadUnidadesVendidas()
        if self.__producto2.DarTIpo() == Tipo.PAPELERIA:
            vendidosPapeleria += self.__producto2.DarCantidadUnidadesVendidas()   
        if self.__producto3.DarTIpo() == Tipo.PAPELERIA:
            vendidosPapeleria += self.__producto3.DarCantidadUnidadesVendidas()   
        if self.__producto4.DarTIpo() == Tipo.PAPELERIA:
            vendidosPapeleria += self.__producto4.DarCantidadUnidadesVendidas()  
        return vendidosPapeleria

