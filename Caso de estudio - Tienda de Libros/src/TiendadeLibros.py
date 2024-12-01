__author__="juan camilo parra"
__license__="GPL"
__version__="1.0.0"
__Email__="juan.parrasan@campusucc.edu.co"

from UnLibro import Libro
from UnaTransaccion import Tipo

class TiendaDeLibros:
    #------------------------------------------------------------------
    # Constructor
    #------------------------------------------------------------------
    def __init__(self):
        self.caja = 1000000
        self.catalogo = []  
    #--------------------------------------------------------------------
    # Getters
    #--------------------------------------------------------------------
    def dardineroCaja(self):
        return self.caja

    def darCatalogo(self):
        return self.catalogo
    
    #-------------------------------------------------------------------
    # Setters
    #-------------------------------------------------------------------
    
    def cambiarDineroCaja(self, valor):
     self.caja = valor
    
    #---------------------------------------------------------------------
    # Metodos
    #---------------------------------------------------------------------
    
    # Requerimiento oara registrar un libro en el catalogo
    __method__ = "registrarLibro"
    __parameter__ = "isbn, titulo, precioVenta, precioCompra, rutaImagen"
    __returns__ = "True si el libro fue registrado correctamente"
    __Description__ = "Método que registra un nuevo libro en el catálogo."
    def registrarLibro(self, isbn, titulo, precioVenta, precioCompra, rutaImagen):
        nuevoLibro = Libro(isbn, titulo, precioVenta, precioCompra, rutaImagen)
        self.catalogo.append(nuevoLibro)
        return True
        
    # Requerimiento para eliminar un libro del catalogo
    __method__ = "eliminarLibro"
    __parameter__ = "isbn"
    __returns__ = "True si el libro fue eliminado, False si no se encontró"
    __Description__ = "Método que elimina un libro del catálogo basado en su ISBN."
    def eliminarLibro(self, isbn):
        for libro in self.catalogo:
            if libro.isbn == isbn:
                self.catalogo.remove(libro)
                return True
        return False

    # Requerimiento para buscar un libro por su título
    __method__ = "buscarLibroPorTitulo"
    __parameter__ = "titulo"
    __returns__ = "El libro encontrado o None si no existe"
    __Description__ = "Busca un libro en el catálogo usando su título."
    def buscarLibroPorTitulo(self, titulo):
        for libro in self.catalogo:
            if libro.titulo == titulo:
                return libro
        return None

    # Requerimiento para buscar un libro por su ISBN
    __method__ = "vender"
    __parameter__ = "isbn, cantidad, fecha"
    __returns__ = "True si la venta fue exitosa, False si el libro no está disponible"
    __Description__ = "Método para registrar la venta de un libro."
    def buscarLibroPorISBN(self, isbn):
        for libro in self.catalogo:
            if libro.isbn == isbn:
                return libro
        return None

    # Requerimiento para abastecer un libro
    __method__ = "abastecer"
    __parameter__ = "isbn, cantidad, fecha"
    __returns__ = "True si el libro fue abastecido correctamente, False si el libro no existe"
    __Description__ = "Método que incrementa el stock de un libro en el catálogo y disminuye el dinero en la caja según el precio de compra."
    def abastecer(self, isbn, cantidad, fecha):
        libro = self.buscarLibroPorISBN(isbn)
        if libro:
            libro.abastecer(cantidad,fecha)
            self.caja -= libro.precioCompra * cantidad
            return True
        return False
                

    # Requerimiento para vender un libro 
    __method__ = "vender"
    __parameter__ = "isbn, cantidad, fecha"
    __returns__ = "True si la venta fue exitosa, False si el libro no existe"
    __Description__ = "Método que registra la venta de un libro, actualiza la caja y disminuye la cantidad en el inventario."
    def vender(self, isbn, cantidad, fecha):
        libro = self.buscarLibroPorISBN(isbn)
        if libro:
            libro.vender(cantidad, fecha)
            self.caja += libro.precioVenta * cantidad
            return True
        return False

    # Requerimiento para contar transacciones de abastecimiento
    __method__ = "CantidadTransaccionesAbastecimiento"
    __parameter__ = "isbn"
    __returns__ = "El número de transacciones de tipo abastecimiento para un libro dado, o 0 si el libro no existe"
    __Description__ = "Cuenta el número de transacciones de abastecimiento realizadas para un libro en particular basado en su ISBN."
    def CantidadTransaccionesAbastecimiento(self, isbn):
        libro = self.buscarLibroPorISBN(isbn)
        if libro:
            cantidadTransacciones = 0
            for transaccion in libro.transacciones:
                if transaccion.darTipo() == Tipo.ABASTECIMIENTO:
                    cantidadTransacciones += 1
            return cantidadTransacciones
        return 0
            
    # Requerimiento para buscar el libro más costoso
    __method__ = "darLibroMasCostoso"
    __parameter__ = "Ninguno"
    __returns__ = "El libro con el precio de venta más alto en el catálogo, o None si el catálogo está vacío"
    __Description__ = "Busca y retorna el libro más costoso en el catálogo basado en su precio de venta."
    def darLibroMasCostoso(self):
        if len(self.catalogo) == 0:
            return None
        libro_mas_costoso = self.catalogo[0]
        for i in range(1, len(self.catalogo)):
            if self.catalogo[i].precioVenta > libro_mas_costoso.precioVenta:
                libro_mas_costoso = self.catalogo[i]
        return libro_mas_costoso
    
    # Requerimiento para buscar el libro menos costoso
    __method__ = "darLibroMenosCostoso"
    __parameter__ = "Ninguno"
    __returns__ = "El libro con el precio de venta más bajo en el catálogo, o None si el catálogo está vacío"
    __Description__ = "Busca y retorna el libro menos costoso en el catálogo basado en su precio de venta."
    def darLibroMenosCostoso(self):
        if len(self.catalogo) == 0:
            return None
        libro_menos_costoso = self.catalogo[0]
        for i in range(1, len(self.catalogo)):
            if self.catalogo[i].precioVenta < libro_menos_costoso.precioVenta:
                libro_menos_costoso = self.catalogo[i]
        return libro_menos_costoso


    # Requerimiento para buscar el libro más vendido
    __method__ = "darLibroMasVendido"
    __parameter__ = "Ninguno"
    __returns__ = "El libro con la mayor cantidad de ventas en el catálogo, o None si no hay libros"
    __Description__ = "Busca y retorna el libro que ha registrado la mayor cantidad de ventas."
    def darLibroMasVendido(self):
        if len(self.catalogo) == 0:
            return None
        libro_mas_vendido = self.catalogo[0]
        for i in range(1, len(self.catalogo)):
            if self.catalogo[i].cantidadVendida > libro_mas_vendido.cantidadVendida:
                libro_mas_vendido = self.catalogo[i]
        return libro_mas_vendido
