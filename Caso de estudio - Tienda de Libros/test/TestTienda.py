__author__="juan camilo parra"
__license__="GPL"
__version__="1.0.0"
__Email__="juan.parrasan@campusucc.edu.co"

from src.TiendadeLibros import TiendaDeLibros
from src.UnLibro import Libro

def testTienda():
    # Crear una instancia de la tienda de libros
    tienda = TiendaDeLibros()


    # Dinero en caja incial
    print(f"Deinero en caja inicial: ${tienda.dardineroCaja()}")
    

    # Registrar algunos libros en la tienda
    tienda.registrarLibro("978-3-16-148410-0", "El Quijote", 50.0, 30.0, "ruta1.jpg")
    tienda.registrarLibro("978-1-43-025750-0", "Cien Años de Soledad", 80.0, 45.0, "ruta2.jpg")
    tienda.registrarLibro("978-0-12-345678-9", "1984", 100.0, 60.0, "ruta3.jpg")
    tienda.registrarLibro("978-0-13-110362-7", "Fahrenheit 451", 70.0, 35.0, "ruta4.jpg")

    # Abastecer libros (para incrementar la cantidad)
    tienda.abastecer("978-3-16-148410-0", 20, "2023-01-01")
    tienda.abastecer("978-1-43-025750-0", 15, "2023-01-02")
    tienda.abastecer("978-0-12-345678-9", 10, "2023-01-03")
    tienda.abastecer("978-0-13-110362-7", 25, "2023-01-04")
    
    # Dinero en caja despues de abastecer
    print(f"Deinero en caja despues de abastecer: ${tienda.dardineroCaja()}")

    # Simular ventas
    tienda.vender("978-3-16-148410-0", 5, "2023-01-05")
    tienda.vender("978-1-43-025750-0", 10, "2023-01-06")
    tienda.vender("978-0-12-345678-9", 8, "2023-01-07")
    tienda.vender("978-0-13-110362-7", 3, "2023-01-08")
    

    # Dinero en caja despues de ventas
    print(f"Deinero en caja despues de ventas: ${tienda.dardineroCaja()}")
    
    # Mostrar todas las transacciones
    print("Transacciones realizadas:")
    for libro in tienda.darCatalogo():
        transacciones = libro.darTransacciones()
        for transaccion in transacciones:
            tipo = transaccion.darTipo().name  # Obtener el nombre del tipo de transacción
            cantidad = transaccion.darCantidad()
            fecha = transaccion.darFecha()
            print(f"{tipo} - Cantidad: {cantidad}, Fecha: {fecha}")

    # Probar el método para encontrar el libro más costoso
    libro_mas_costoso = tienda.darLibroMasCostoso()
    if libro_mas_costoso:
        print(f"Libro más costoso: {libro_mas_costoso.titulo} - ${libro_mas_costoso.precioVenta}")
    else:
        print("No hay libros en el catálogo.")

    # Probar el método para encontrar el libro menos costoso
    libro_menos_costoso = tienda.darLibroMenosCostoso()
    if libro_menos_costoso:
        print(f"Libro menos costoso: {libro_menos_costoso.titulo} - ${libro_menos_costoso.precioVenta}")
    else:
        print("No hay libros en el catálogo.")

    # Probar el método para encontrar el libro más vendido
    libro_mas_vendido = tienda.darLibroMasVendido()
    if libro_mas_vendido:
        print(f"Libro más vendido: {libro_mas_vendido.titulo} - {libro_mas_vendido.cantidadVendida} ventas")
    else:
        print("No hay ventas registradas.")

if __name__ == "__main__":
    testTienda()