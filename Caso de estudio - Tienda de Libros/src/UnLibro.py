__author__="juan camilo parra"
__license__="GPL"
__version__="1.0.0"
__Email__="juan.parrasan@campusucc.edu.co"

from UnaTransaccion import Transaccion
from UnaTransaccion import Tipo

class Libro:
    #------------------------------------------------------------------
    # Constructor
    #-------------------------------------------------------------------
    def __init__(self, isbn, titulo, precioVenta, precioCompra, rutaImagen):
        self.isbn = isbn
        self.titulo = titulo
        self.precioVenta = precioVenta
        self.precioCompra = precioCompra
        self.rutaImagen = rutaImagen
        self.cantidadActual = 0
        self.cantidadVendida = 0
        self.transacciones = []

    #--------------------------------------------------------------------
    # Getters
    #--------------------------------------------------------------------
    def darISBN(self):
        return self.isbn

    def darTitulo(self):
        return self.titulo

    def darPrecioVenta(self):
        return self.precioVenta

    def darPrecioCompra(self):
        return self.precioCompra

    def darCantidadActual(self):
        return self.cantidadActual

    def darRutaImagen(self):
        return self.rutaImagen

    def darTransacciones(self):
        return self.transacciones
    
    #-------------------------------------------------------------------
    # Setters
    #-------------------------------------------------------------------
    def cambiarTitulo(self, nuevoTitulo):
        self.titulo = nuevoTitulo
        
    def cambiarPrecioVenta(self, nuevoPrecioVenta):
        self.precioVenta = nuevoPrecioVenta
        
    def cambiarPrecioCompra(self, nuevoPrecioCompra):
        self.precioCompra = nuevoPrecioCompra
        
    def cambiarRutaImagen(self, nuevaRutaImagen):
        self.rutaImagen = nuevaRutaImagen
        
    def cambiarCantidadActual(self, nuevaCantidad):
        self.cantidadActual = nuevaCantidad
        
    def cambiarCantidadVendida(self, nuevaCantidadVen):
        self.cambiarCantidadVendida = nuevaCantidadVen
    
    #---------------------------------------------------------------------
    # Metodos
    #---------------------------------------------------------------------
    
    # Incrementar la cantidad actual del libro
    __method__ = "abastecer"
    __parameter__ = "cantidad, fecha"
    __returns__ = "Ninguno"
    __Description__ = "Método que incrementa la cantidad actual de un libro en el inventario y registra una transacción de tipo ABASTECIMIENTO."
    def abastecer(self, cantidad, fecha):
        self.cantidadActual += cantidad
        self.registrarTransaccion(Tipo.ASBASTECIMIENTO, cantidad, fecha)

    # Decrementar la cantidad actual del libro
    __method__ = "vender"
    __parameter__ = "cantidad, fecha"
    __returns__ = "True si la venta se realizó correctamente, False si no hay suficiente stock"
    __Description__ = "Método que decrementa la cantidad actual de un libro en el inventario, registra una transacción de tipo VENTA y actualiza la cantidad total vendida."
    def vender(self, cantidad, fecha):
        if cantidad > self.cantidadActual:
            return False
        self.cantidadActual -= cantidad
        self.cantidadVendida += cantidad
        self.registrarTransaccion(Tipo.VENTA, cantidad, fecha)
        return True
        
    # Registrar una nueva transacción
    __method__ = "registrarTransaccion"
    __parameter__ = "Tipo, cantidad, fecha"
    __returns__ = "Ninguno"
    __Description__ = "Método que crea y registra una nueva transacción en la lista de transacciones para un libro."
    def registrarTransaccion(self, Tipo, cantidad, fecha):
        transaccion = Transaccion(Tipo, cantidad, fecha)
        self.transacciones.append(transaccion)
    

    