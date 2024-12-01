#------------------------------------
# Constantes
IVA_PAPELERIA = 0.16
IVA_SUPERMERCADO = 0.04
IVA_FARMACIA = 0.12
# Constantes
#------------------------------------

class Producto:
    def __init__(self, nombre, tipo, valor_unitario, cantidad_bodega, cantidad_minima, cantidad_unidades_vendidas):
        self.nombre = nombre
        self.tipo = tipo
        self.valor_unitario = valor_unitario
        self.cantidad_bodega = cantidad_bodega
        self.cantidad_minima = cantidad_minima
        self.cantidad_unidades_vendidas = cantidad_unidades_vendidas
        
    def __repr__(self):
        return f"{self.nombre} ({self.tipo}) - Valor Unitario: {self.valor_unitario}, En Bodega: {self.cantidad_bodega}, Vendidas: {self.cantidad_unidades_vendidas}"
class Tienda:
    def __init__(self, dinero_en_caja):
        self.dinero_en_caja = dinero_en_caja
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def __repr__(self):
        return f"Tienda con dinero en caja: {self.dinero_en_caja} y {len(self.productos)} productos."
# Crear los productos
producto1 = Producto(nombre="libreta", tipo="PAPELERIA", valor_unitario=5500, cantidad_bodega=44, cantidad_minima=15, cantidad_unidades_vendidas=6)
producto2 = Producto(nombre="leche", tipo="SUPERMERCADO", valor_unitario=2100, cantidad_bodega=25, cantidad_minima=10, cantidad_unidades_vendidas=25)
producto3 = Producto(nombre="jabón", tipo="SUPERMERCADO", valor_unitario=4200, cantidad_bodega=36, cantidad_minima=8, cantidad_unidades_vendidas=14)
producto4 = Producto(nombre="aspirina", tipo="FARMACIA", valor_unitario=400, cantidad_bodega=13, cantidad_minima=11, cantidad_unidades_vendidas=32)

# Crear la tienda
tienda = Tienda(dinero_en_caja=0)  # Inicialmente la caja está vacía

# Agregar los productos a la tienda
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)
tienda.agregar_producto(producto4)

# Ver la tienda y sus productos
print(tienda)
for producto in tienda.productos:
    print(producto)

#----------------------------------------------------------------
# Parte 1 
#----------------------------------------------------------------
print("\n------------------------------------------")
print("Parte 1")
print("------------------------------------------\n")

# Leche: cantidadBodega - cantidadMinima
resta_leche = producto2.cantidad_bodega - producto2.cantidad_minima
print(f"Leche (cantidadBodega - cantidadMinima): {resta_leche}")

# Aspirina: valorUnitario * cantidadBodega
valor_total_aspirina_bodega = producto4.valor_unitario * producto4.cantidad_bodega
print(f"Aspirina (valorUnitario * cantidadBodega): {valor_total_aspirina_bodega}")

# Jabón: (cantidadUnidadesVendidas + cantidadBodega) * (valorUnitario + valorUnitario * IVA_SUPERMERCADO)
total_jabon = (producto3.cantidad_unidades_vendidas + producto3.cantidad_bodega) * (producto3.valor_unitario * (1 + IVA_SUPERMERCADO))
print(f"Jabón: {(producto3.cantidad_unidades_vendidas + producto3.cantidad_bodega)} * ({producto3.valor_unitario} * (1 + {IVA_SUPERMERCADO})) = {total_jabon}")

# Libreta: valorUnitario * cantidadBodega / cantidadUnidadesVendidas * valorUnitario
valor_libreta = (producto1.valor_unitario * producto1.cantidad_bodega) / (producto1.cantidad_unidades_vendidas * producto1.valor_unitario)
print(f"Libreta: {(producto1.valor_unitario * producto1.cantidad_bodega)} / ({producto1.cantidad_unidades_vendidas} * {producto1.valor_unitario}) = {valor_libreta}")

# Leche: valorUnitario * cantidadUnidadesVendidas * IVA_SUPERMERCADO
valor_leche_iva = producto2.valor_unitario * producto2.cantidad_unidades_vendidas * IVA_SUPERMERCADO
print(f"Leche (valorUnitario * cantidadUnidadesVendidas * IVA_SUPERMERCADO): {valor_leche_iva}")

# Aspirina: valorUnitario * (1 + IVA_FARMACIA) * cantidadUnidadesVendidas
valor_aspirina_iva = producto4.valor_unitario * (1 + IVA_FARMACIA) * producto4.cantidad_unidades_vendidas
print(f"Aspirina (valorUnitario * (1 + IVA_FARMACIA) * cantidadUnidadesVendidas): {valor_aspirina_iva}")

# Tienda: Promedio de los valores unitarios de los productos
promedio_valor_productos = (producto1.valor_unitario + producto2.valor_unitario + producto3.valor_unitario + producto4.valor_unitario) / 4
print(f"Tienda (promedio valor unitario productos): {promedio_valor_productos}")

# Tienda: (producto1.cantidadBodega - producto1.cantidadMinima) * (producto1.valorUnitario * (1 + IVA_PAPELERIA))
producto1_iva = (producto1.cantidad_bodega - producto1.cantidad_minima) * producto1.valor_unitario * (1 + IVA_PAPELERIA)
print(f"Tienda (producto1 - libreta): {producto1_iva}")

# Tienda: dineroEnCaja - (producto2.cantidadMinima * producto2.valorUnitario)
dinero_restante = tienda.dinero_en_caja - (producto2.cantidad_minima * producto2.valor_unitario)
print(f"Tienda (dinero en caja menos el valor mínimo de leche): {dinero_restante}")

# Tienda: producto3.cantidadUnidadesVendidas * (1 + IVA_SUPERMERCADO)
valor_jabon_vendido = producto3.cantidad_unidades_vendidas * producto3.valor_unitario * (1 + IVA_SUPERMERCADO)
print(f"Jabón vendido con IVA: {valor_jabon_vendido}")

print("\n------------------------------------------")
print("Parte 1")
print("------------------------------------------\n")

#----------------------------------------------------------------
# Parte 1 
#----------------------------------------------------------------

#----------------------------------------------------------------
# Parte 2 
#----------------------------------------------------------------
print("\n------------------------------------------")
print("Parte 2")
print("------------------------------------------\n")

# Parte II - Evaluación de expresiones relacionales

# Libreta: tipo == Tipo.PAPELERIA
libreta_papeleria = producto1.tipo == "PAPELERIA"
print(f"libreta.tipo == 'PAPELERIA': {libreta_papeleria}")  # True

# Libreta: tipo != Tipo.FARMACIA
libreta_no_farmacia = producto1.tipo != "FARMACIA"
print(f"libreta.tipo != 'FARMACIA': {libreta_no_farmacia}")  # True

# Leche: cantidadMinima >= cantidadBodega
leche_cantidad_minima_mayor = producto2.cantidad_minima >= producto2.cantidad_bodega
print(f"leche.cantidadMinima >= leche.cantidadBodega: {leche_cantidad_minima_mayor}")

# Jabón: valorUnitario <= 10000
jabon_valor_menor = producto3.valor_unitario <= 10000
print(f"jabón.valorUnitario <= 10000: {jabon_valor_menor}")

# Aspirina: cantidadBodega - cantidadMinima != cantidadUnidadesVendidas
aspirina_diferencia_cantidad = (producto4.cantidad_bodega - producto4.cantidad_minima) != producto4.cantidad_unidades_vendidas
print(f"aspirina.cantidadBodega - cantidadMinima != cantidadUnidadesVendidas: {aspirina_diferencia_cantidad}")

# Jabón: cantidadBodega * valorUnitario == cantidadUnidadesVendidas * IVA_PAPELERIA
jabon_comparacion_valor = (producto3.cantidad_bodega * producto3.valor_unitario) == (producto3.cantidad_unidades_vendidas * IVA_PAPELERIA)
print(f"jabón.cantidadBodega * valorUnitario == cantidadUnidadesVendidas * IVA_PAPELERIA: {jabon_comparacion_valor}")

# Tienda: Unidades vendidas de producto1 y producto2 > producto3
tienda_comparacion_ventas = (producto1.cantidad_unidades_vendidas + producto2.cantidad_unidades_vendidas) > producto3.cantidad_unidades_vendidas
print(f"Unidades vendidas (libreta + leche) > jabón: {tienda_comparacion_ventas}")  # True

# Tienda: dineroEnCaja <= producto4.cantidadUnidadesVendidas * ( ( 1 + IVA_FARMACIA ) * producto4.valorUnitario )
dinero_comparacion_aspirina = tienda.dinero_en_caja <= producto4.cantidad_unidades_vendidas * ((1 + IVA_FARMACIA) * producto4.valor_unitario)
print(f"dineroEnCaja <= (aspirina.unidadesVendidas * (1 + IVA_FARMACIA) * valorUnitario): {dinero_comparacion_aspirina}")

# Tienda: Suma de cantidades en bodega de todos los productos <= 1000
suma_bodega_tienda = (producto1.cantidad_bodega + producto2.cantidad_bodega + producto3.cantidad_bodega + producto4.cantidad_bodega) <= 1000
print(f"Suma de bodega de todos los productos <= 1000: {suma_bodega_tienda}")

# Tienda: dineroEnCaja * IVA_libreta > producto1.cantidadUnidadesVendidas * valorUnitario_libreta
dinero_vs_ventas_libreta = (tienda.dinero_en_caja * IVA_PAPELERIA) > (producto1.cantidad_unidades_vendidas * producto1.valor_unitario)
print(f"dineroEnCaja * IVA_libreta > libreta.unidadesVendidas * valorUnitario: {dinero_vs_ventas_libreta}")

print("\n------------------------------------------")
print("Parte 2")
print("------------------------------------------\n")

#----------------------------------------------------------------
# Parte 2 
#----------------------------------------------------------------

#----------------------------------------------------------------
# Parte 3 
#----------------------------------------------------------------
print("\n------------------------------------------")
print("Parte 3")
print("------------------------------------------\n")

# Parte III - Evaluación de expresiones lógicas

# Leche: !(tipo == Tipo.PAPELERIA || tipo == Tipo.FARMACIA)
leche_no_papeleria_no_farmacia = not (producto2.tipo == "PAPELERIA" or producto2.tipo == "FARMACIA")
print(f"leche no es PAPELERIA ni FARMACIA: {leche_no_papeleria_no_farmacia}")  # True

# Jabón: tipo == Tipo.SUPERMERCADO && valorUnitario <= 10000
jabon_supermercado_y_valor = (producto3.tipo == "SUPERMERCADO") and (producto3.valor_unitario <= 10000)
print(f"jabón es SUPERMERCADO y valorUnitario <= 10000: {jabon_supermercado_y_valor}")

# Aspirina: cantidadBodega > cantidadMinima && cantidadBodega < cantidadUnidadesVendidas
aspirina_rango_cantidad = (producto4.cantidad_bodega > producto4.cantidad_minima) and (producto4.cantidad_bodega < producto4.cantidad_unidades_vendidas)
print(f"aspirina cantidadBodega > cantidadMinima y < cantidadUnidadesVendidas: {aspirina_rango_cantidad}")

# Libreta: valorUnitario >= 1000 && valorUnitario <= 5000
libreta_valor_rango = (producto1.valor_unitario >= 1000) and (producto1.valor_unitario <= 5000)
print(f"libreta valorUnitario entre 1000 y 5000: {libreta_valor_rango}")

# Leche: tipo != Tipo.PAPELERIA && tipo != Tipo.SUPERMERCADO
leche_no_papeleria_no_supermercado = (producto2.tipo != "PAPELERIA") and (producto2.tipo != "SUPERMERCADO")
print(f"leche no es PAPELERIA ni SUPERMERCADO: {leche_no_papeleria_no_supermercado}")

# Aspirina: tipo == Tipo.PAPELERIA && valorUnitario > 50 && !(cantidadMinima < cantidadBodega)
aspirina_condiciones = (producto4.tipo == "PAPELERIA") and (producto4.valor_unitario > 50) and not (producto4.cantidad_minima < producto4.cantidad_bodega)
print(f"aspirina tipo == PAPELERIA y valorUnitario > 50 y no (cantidadMinima < cantidadBodega): {aspirina_condiciones}")

# Tienda: producto1,2,3,4 diferentes tipos, verificar condición
tienda_comparacion_tipos = (producto1.tipo == "PAPELERIA") and (producto2.tipo == "SUPERMERCADO") and (producto3.tipo != "FARMACIA") and (producto4.tipo == "SUPERMERCADO")
print(f"Tienda tipos (papeleria, supermercado, no farmacia, supermercado): {tienda_comparacion_tipos}")  # False

# Tienda: (dineroEnCaja / producto1.valorUnitario) >= producto1.cantidadMinima
dinero_vs_minimo_libreta = (tienda.dinero_en_caja / producto1.valor_unitario) >= producto1.cantidad_minima
print(f"dineroEnCaja / valorUnitario_libreta >= cantidadMinima_libreta: {dinero_vs_minimo_libreta}")

# Tienda: Promedio de bodega de producto 2 dentro de un rango
promedio_bodega_leche = (((producto2.cantidad_bodega + producto2.cantidad_bodega) / 10) < 100) and (((producto2.cantidad_bodega + producto2.cantidad_bodega) / 10) >= 50)
print(f"promedio bodega leche dentro de 50 y 100: {promedio_bodega_leche}")

# Tienda: dineroEnCaja * 0.1 <= jabón.valorUnitario * ( 1 + IVA_SUPERMERCADO )
dinero_vs_valor_jabon = (tienda.dinero_en_caja * 0.1) <= (producto3.valor_unitario * (1 + IVA_SUPERMERCADO))
print(f"dineroEnCaja * 0.1 <= valorUnitario_jabon * (1 + IVA_SUPERMERCADO): {dinero_vs_valor_jabon}")

print("\n------------------------------------------")
print("Parte 3")
print("------------------------------------------\n")

#----------------------------------------------------------------
# Parte 3
#----------------------------------------------------------------

#----------------------------------------------------------------
# Parte 4 
#----------------------------------------------------------------
print("\n------------------------------------------")
print("Parte 4")
print("------------------------------------------\n")

# Parte IV - Operadores aritméticos

# Producto: Valor de venta de un producto con IVA del 16% (papeleria)
valor_venta_libreta_iva = producto1.valor_unitario * (1 + IVA_PAPELERIA)
print(f"Valor de venta libreta con IVA del 16%: {valor_venta_libreta_iva}")

# Producto: Número de unidades que se deben vender para alcanzar la cantidad mínima
unidades_para_minimo = producto1.cantidad_minima - producto1.cantidad_unidades_vendidas
print(f"Unidades para alcanzar cantidad mínima (libreta): {unidades_para_minimo}")

# Producto: Número de veces que se ha vendido la cantidad mínima del producto
veces_vendidas_minimo = producto1.cantidad_unidades_vendidas // producto1.cantidad_minima
print(f"Veces que se ha vendido la cantidad mínima (libreta): {veces_vendidas_minimo}")

# Producto: Unidades sobrantes si se arman paquetes de 10
sobrantes_paquetes = producto1.cantidad_bodega % 10
print(f"Unidades sobrantes (libreta) si se arman paquetes de 10: {sobrantes_paquetes}")

# Tienda: Dinero en caja incrementado en 25%
dinero_incrementado = tienda.dinero_en_caja * 1.25
print(f"Dinero en caja incrementado en 25%: {dinero_incrementado}")

# Tienda: Total del IVA a pagar por las unidades vendidas de todos los productos
iva_total = (producto1.cantidad_unidades_vendidas * IVA_PAPELERIA * producto1.valor_unitario) + \
            (producto2.cantidad_unidades_vendidas * IVA_SUPERMERCADO * producto2.valor_unitario) + \
            (producto3.cantidad_unidades_vendidas * IVA_SUPERMERCADO * producto3.valor_unitario) + \
            (producto4.cantidad_unidades_vendidas * IVA_FARMACIA * producto4.valor_unitario)
print(f"Total del IVA a pagar por las unidades vendidas: {iva_total}")

# Tienda: Número de unidades del producto 3 que se pueden pagar con el dinero en caja
unidades_jabon_con_dinero = tienda.dinero_en_caja // producto3.valor_unitario
print(f"Unidades de jabón que se pueden pagar con el dinero en caja: {unidades_jabon_con_dinero}")

# Tienda: Número de estantes de 50 posiciones que se requieren para almacenar todas las unidades en bodega
total_estantes = (producto1.cantidad_bodega + producto2.cantidad_bodega + producto3.cantidad_bodega + producto4.cantidad_bodega) // 50
print(f"Estantes de 50 posiciones necesarios para almacenar todos los productos: {total_estantes}")


print("\n------------------------------------------")
print("Parte 4")
print("------------------------------------------\n")
#----------------------------------------------------------------
# Parte 4
#----------------------------------------------------------------
