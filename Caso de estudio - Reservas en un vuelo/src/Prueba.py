

# Suponiendo que las clases Pasajero y Silla están definidas adecuadamente
from silla import Silla
from Pasajero import Pasajero
from Avion import Avion

# Crear una instancia del avión
avion = Avion()

# Crear algunos pasajeros
pasajero1 = Pasajero("Juan Pérez", "123456789")
pasajero2 = Pasajero("Ana Gómez", "987654321")
pasajero3 = Pasajero("Carlos López", "456789123")

# Asignar sillas a los pasajeros con diferentes preferencias
print("Asignando sillas a los pasajeros...")
exito1 = avion.asignarSilla(pasajero1, Silla.Clase.EJECUTIVA, Silla.Ubicacion.VENTANA)
exito2 = avion.asignarSilla(pasajero2, Silla.Clase.ECONOMICA, Silla.Ubicacion.PASILLO)
exito3 = avion.asignarSilla(pasajero3, Silla.Clase.ECONOMICA, Silla.Ubicacion.CENTRO)

print(f"Asignación pasajero1 exitosa: {exito1}")
print(f"Asignación pasajero2 exitosa: {exito2}")
print(f"Asignación pasajero3 exitosa: {exito3}")

# Buscar un pasajero por su cédula
print("\nBuscando pasajeros por cédula...")
avion.buscarPasajero("123456789")  # Debe encontrar a Juan Pérez
avion.buscarPasajero("987654321")  # Debe encontrar a Ana Gómez
avion.buscarPasajero("000000000")  # No debe encontrar nada

# Calcular y mostrar el porcentaje de ocupación del avión
print("\nCalculando el porcentaje de ocupación del avión...")
porcentaje_ocupacion = avion.calcularPorcentajeOcupacion()
print(f"Porcentaje de ocupación del avión: {porcentaje_ocupacion:.2f}%")

# Eliminar la reserva de un pasajero
print("\nEliminando reserva de un pasajero...")
eliminacion_exitosa = avion.eliminarReserva("123456789")
print(f"Eliminación de reserva exitosa: {eliminacion_exitosa}")

# Verificar el porcentaje de ocupación después de eliminar una reserva
porcentaje_ocupacion_despues = avion.calcularPorcentajeOcupacion()
print(f"Porcentaje de ocupación del avión después de eliminar una reserva: {porcentaje_ocupacion_despues:.2f}%")
