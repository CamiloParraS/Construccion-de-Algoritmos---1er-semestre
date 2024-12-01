__author__="juan camilo parra"
__license__="GPL"
__version__="1.0.0"
__Email__="juan.parrasan@campusucc.edu.co"

import Constantes
from Tipo import Tipo
import Tienda
class Producto:

#----------------------------------------------------------------
# Constantes
# ----------------------------------------------------------------

    IVA_PAPELERIA = 0.16
    IVA_SUPERMERCADO = 0.04
    IVA_FARMACIA = 0.12

#----------------------------------------------------------------
# Constructor
# ----------------------------------------------------------------

    def __init__(self, nombre, tipo, valorUnitario:float, cantidad:int, cantidadMinima:int, subsidiado: bool, calidad):
        
#----------------------------------------------------------------
# Atributos
#----------------------------------------------------------------
        self.__nombre=nombre
        self.__tipo=tipo
        self.__valorUnitario = valorUnitario
        self.__cantidadBodega = cantidad
        self.__cantidadMinima = cantidadMinima
        self.__cantidadUnidadesVendidas = 0
        self.__subsidiado = subsidiado
        self.__calidad = calidad

#----------------------------------------------------------------
# self.subsidiado = True 
# self.subsidiado = False
#----------------------------------------------------------------

    def CalcularPrecioSupermercador(self):
        self.__valorUnitario += self.__valorUnitario + (self.__valorUnitario * self.IVA_SUPERMERCADO) 

#----------------------------------------------------------------
# Metodos
#----------------------------------------------------------------

    #------------------------------------------------------------
    #    __method__ = ""
    #   __parameter__ = ""
    #   __returns__= ""
    #   __Description__ = ""
    #-------------------------------------------------------------
    
    
    #-------------------------------------------------------------
    # Metodos Modificadores
    #-------------------------------------------------------------
    __method__ = "DarNombre"
    __parameter__ = "Ninguno"
    __returns__ = "Nombre del producto"
    __Description__ = "metodo que retorna el nombre del producto"
    def CambiarNombre (self, nombre):
        self.__nombre = nombre

    __method__ = "CambiarTipo"
    __parameter__ = "tipo"
    __returns__ = "ninguna"
    __Description__ = "Metodo que cambia el tipo de la clase"
    def CambiarTipo (self, tipo):
        self.__tipo = tipo
        
    __method__ = "CambiarValorUnitario"
    __parameter__ = "ValorUnitario"
    __returns__ = "ninguno"
    __Description__ = "Metodo que cambia el valor  unitario de la clase"
    def CambiarValorUnitario (self, valorunitario):
        self.__valorUnitario = valorunitario
        
    __method__ = "cantidadBodega"
    __parameter__ = "cantidadBodega"
    __returns__ = "ninguno"
    __Description__ = "Metodo que cambia la cantidad en bodega"
    def CambiarCantidadBodega (self, cantidadBodega):
        self.__cantidadBodega = cantidadBodega
        
    __method__ = "CambiarCantidadMinima"
    __parameter__ = "cantidadUnidadesVendidas"
    __returns__= "Ninguna"
    __Description__ = "metodo que cambia la cantidad unidades vendidas de la clase"
    def  CambiarCantidadMinima (self, cantidadMinima):
        self.__cantidadMinima = cantidadMinima

        
#----------------------------------------------------------------
# Hacer estos metodos
# DarNombre
# DarTipo
# DarValorUnitario
# DarCantidadBodega
# DarCantidadMinima
# DarCantidadUnidadesVendidas
#----------------------------------------------------------------

    __method__ = "DarNombre"
    __parameter__ = "Ninguno"
    __returns__ = "Nombre del producto"
    __Description__ = "metodo que retorna el nombre del producto"
    def DarNombre(self):
        return self.__nombre
    
    __method__ = "DarTIpo"
    __parameter__ = "Ninguno"
    __returns__ = "Tipo del producto"
    __Description__ = "Retorna el tipo del producto"
    def DarTIpo(self):
        return self.__tipo
    
    __method__ = "DarValorUnitario"
    __parameter__ = "Ninguno"
    __returns__ = "Valor Unitario"
    __Description__ = "Retorna el Valor Unitario"
    def DarValorUnitario(self):
        return self.__valorUnitario
    
    __method__ = "DarCantidadBodega"
    __parameter__ = "Ninguno"
    __returns__ = "Cantidad Bodega"
    __Description__ = "Retorna la cantidad en bodega"
    def DarCantidadBodega(self):
        return self.__cantidadBodega
    
    __method__ = "DarCantidadMinima"
    __parameter__ = "Ninguno"
    __returns__ = "Cantidad Minima"
    __Description__ = "Retorna la cantidad minima en bodega"
    def DarCantidadMinima(self):
        return self.__cantidadMinima
    
    __method__ = "DarCantidadUnidadesVendidas"
    __parameter__ = "Ninguno"
    __returns__ = "CantidadUnidadesVendidas"
    __Description__ = "Retorna la cantidad de unidades vendidas"
    def DarCantidadUnidadesVendidas(self):
        return self.__cantidadUnidadesVendidas
   
    __method__ = "DarPublicidad"
    __parameter__ = "Ninguno"
    __returns__ = "Mesnaje publicitario de n producto"
    __Description__ = "Metodo que brinda publicidad de un producto"
    def DarPublicidad(self):
        # Metodo facil ------------------------------------------------------------------
        # return 'compre el producto ' + self.__nombre +'por solo $'+self.__valorUnitario
        # Metodo facil ------------------------------------------------------------------ 
        # Metodo Pro --------------------------------------------------------------------
        return f'compre el producto {self.DarNombre} porsolo $ {self.DarValorUnitario}' 
        # Metodo Pro ---------------------------------------------------------------------
    
    __method__ = "EsIgual"
    __parameter__ = "Producto"
    __returns__ = "True o False segun el resultado"
    __Description__ = "Metodo que permite comparar el producto con otro ingresado por el usuario"
    def EsIgual(self,  producto):
        return self.DarNombre() is producto
    
    __method__='Vender'
    __params__='Cantidad de producto a vender'
    __returns__='Ninguno'
    __descriptions__='Metodo que permite vender'
    def Vender(self, cProducto):
        if cProducto > self.DarCantidadBodega():
            self.__cantidadUnidadesVendidas += self.DarCantidadBodega()
            self.__cantidadBodega = 0
        else:
            self.__cantidadUnidadesVendidas += cProducto
            self.__cantidadBodega -= cProducto

    __method__='AgregarNuevaUnidadBodega'
    __params__='Ninguno'
    __returns__='Nada'
    __descriptions__='Este metodo permite Agregar un producto en bodega'
    def AgregarNuevaUnidadBodega(self):
        self.__cantidadBodega+=1
        
    __method__='Pedir'
    __params__='Cantidad pedido'
    __returns__='Nada'
    __descriptions__='Este metodo permite realizar un pedido de un producto'
    def Pedir(self, cantidad):
        self.__cantidadBodega += cantidad
        #self.__cantidadBodega = self.__cantidadBodega+cantidad
        
    def HaySuficiente(self, cProducto):
        # Forma 1
        #suficiente = False
        #
        #if(cProducto <= self.DarCantidadBodega()):
        #   suficiente = True
        #else 
        #   suficiente = False
        #return suficiente

        #Forma 2 
        #suficiente = False
        #if(cProducto <= self.DarCantidadBodega()):
        #   suficiente = True
        #return suficiente
        
        #Forma 3
        #if(cProducto <= self.DarCantidadBodega()):
        #    return True
        #else
        #    return False
        
        #Forma 4 
        return cProducto <= self.DarCantidadBodega()
    
    __method__='DarPrecioPapeleria'
    __params__='conIva'
    __returns__='Precio Final'
    __descriptions__='Metodo que calcula el precio final de papeleria con iva o sin iva'
    def DarPrecioPapeleria(self, coniva:bool):
        preciofinal = self.DarValorUnitario()
        if(coniva):
            preciofinal = preciofinal * (1 + self.IVA_PAPELERIA)
        return preciofinal
    
    __method__='AjustarPrecio'
    __params__='Ninguno'
    __returns__='Ninguno'
    __descriptions__='Metodo que premite ajustar el precio si no se han vendido 100 unidades'
    def AjustarPrecio(self):
        if(self.DarCantidadUnidadesVendidas() < 100):
            self.__valorUnitario = self.__valorUnitario * 0.8
        else:
            self.__valorUnitario = self.__valorUnitario * 1.1
            
    __method__ = "DarIva"
    __parameter__ = "Ninguno"
    __returns__ = "iva"
    __Description__ = "metodo que permite retornar el iva segun su tipo"
    def DarIva(self):
        #forma 1
        # iva = 0
        # if self.DarTIpo() == Tipo.PAPELERIA:
        #     iva = self.IVA_PAPELERIA
        # elif self.DarTIpo() == Tipo.DOGUERIA:
        #     iva = self.IVA_FARMACIA
        # else:
        #     iva = self.IVA_SUPERMERCADO
        
        #Forma 2
        if self.DarTIpo() == Tipo.PAPELERIA:
            return self.IVA_PAPELERIA
        elif self.DarTIpo() == Tipo.FARMACIA:
            return self.IVA_FARMACIA
        else:
            return self.IVA_SUPERMERCADO
       
    #---------------------------------------------------------------------------
    # Tarea 05
    #---------------------------------------------------------------------------   
     
    # Aumentar el valor unitario del producto, utilizando la siguiente politica:
    # Si el producto cuesta menos de $1000, aumentar el 1%. 
    # Si cuesta entre $1000 y $5000, aumenta el 2%
    # Si cuesta mas de $5000 aumentar el 3%

    def subirValorUnitario(self):
        if self.__valorUnitario < 1000:
            self.__valorUnitario *= 1.01
        elif  self.__valorUnitario >= 1000 <= 5000:
            self.__valorUnitario  *= 1.02
        else :
            self.__valorUnitario *= 1.03
            
    # Recibir un pedido, solo si en bodega se tienen menos unidades de las indicadas en el tope minimo
    # en caso contrario el metodo no debe hacer nada

    def hacerPedido(self, pCantidad:int):
        if self.__cantidadBodega >= self.__cantidadMinima:
            self.__cantidadBodega += pCantidad

    # Modificar el precio del producto, utilizando la siguiente politica: 
    # si elproducto es drogueria o papeleri debe disminuir un 10%
    # si es supermercado  debe aumentar un 5%

    def cambiarValorUnitario(self):
        if self.__tipo == Tipo.FARMACIA:
            self.__valorUnitario *=  0.9
        elif self.__tipo == Tipo.PAPELERIA:
            self.__valorUnitario *=  0.9
        elif self.__tipo == Tipo.SUPERMERCADO:
            self.__valorUnitario *= 1.05

    #---------------------------------------------------------------------------
    # Tarea 05
    #---------------------------------------------------------------------------   