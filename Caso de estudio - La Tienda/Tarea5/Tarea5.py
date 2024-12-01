#----------------------------------------------------------------------------
# Nombre: Juan Camilo Parra Sanchez
# ID:  917079
#----------------------------------------------------------------------------

__author__="juan camilo parra"
__license__="GPL"
__version__="1.0.0"
__Email__="juan.parrasan@campusucc.edu.co"

#---------------------------------------------------------------------------
# Tarea 05
#--------------------------------------------------------------------------- 
from src.Producto import Producto
from src.Tienda import Tienda
from src.Tipo import Tipo
      
#---------------------------------------------------------------------------
# Clase Producto
#---------------------------------------------------------------------------
    
# Aumentar el valor unitario del producto, utilizando la siguiente politica:
# Si el producto cuesta menos de $1000, aumentar el 1%. 
# Si cuesta entre $1000 y $5000, aumenta el 2%
# Si cuesta mas de $5000 aumentar el 3%
__method__ = "subirValorUnitario"
__params__ = "Ninguno"
__returns__ = "Ninguno"
__descriptions__ = "Método que aumenta el valor unitario del producto según la politica de los precios"
def subirValorUnitario(self):
    if self.__valorUnitario < 1000:
        self.__valorUnitario *= 1.01
    elif 1000 <= self.__valorUnitario <= 5000:
        self.__valorUnitario  *= 1.02
    else:
        self.__valorUnitario *= 1.03
            
# Recibir un pedido, solo si en bodega se tienen menos unidades de las indicadas en el tope minimo
# en caso contrario el metodo no debe hacer nada
__method__ = 'hacerPedido'
__params__ = 'Cantidad del pedido'
__returns__ = 'Ninguno'
__descriptions__ = 'Método que realiza un pedido si la cantidad en bodega es menor al tope mínimo.'
def hacerPedido(self, pCantidad:int):
    if self.__cantidadBodega < self.__cantidadMinima:
        self.__cantidadBodega += pCantidad

# Modificar el precio del producto, utilizando la siguiente politica: 
# si elproducto es drogueria o papeleria debe disminuir un 10%
# si es supermercado  debe aumentar un 5%
__method__ = 'cambiarValorUnitario'
__params__ = 'Ninguno'
__returns__ = 'Ninguno'
__descriptions__ = 'Método que modifica el precio del preducto segun la politica.'
def cambiarValorUnitario(self):
    if self.__tipo == Tipo.FARMACIA:
        self.__valorUnitario *=  0.9
    elif self.__tipo == Tipo.PAPELERIA:
        self.__valorUnitario *=  0.9
    elif self.__tipo == Tipo.SUPERMERCADO:
        self.__valorUnitario *= 1.05

#---------------------------------------------------------------------------
# Clase Tienda
#---------------------------------------------------------------------------
    
# Vender una cierta candtidad del producto cuyo nombre es igual al recibido como parametro.
# El metodo retorna el numero de unidades efectivamente vendidas. 
# Suponga que el nombre que se recibe como parametro corresponde a uno de los productos de la tienda.
# Utilice el metodo vender de la clase producto como parte de la solucion.
__method__ = "venderProducto"
__params__ = "pNombreProducto, pCantidad: int"
__returns__ = "Número de unidades vendidas"
__descriptions__ = "Vende una cierta cantidad del producto cuyo nombre es igual al recibido como parámetro." 
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
__method__ = "cuantosPapeleria"
__params__ = "Ninguno"
__returns__ = "Número de unidades vendidas del tipo papelería"
__descriptions__ = "Calcula el número de productos de papelería que se venden en la tienda."  
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